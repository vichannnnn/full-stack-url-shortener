import asyncpg
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from Database import Database, init_db
from url_handler import URL, url_cache, reverse_cache

templates = Jinja2Templates(directory="templates")


def init_app():
    app = FastAPI()
    db = Database()
    origins = ['http://localhost:3000']
    app.add_middleware(CORSMiddleware,
                       allow_origins=origins,
                       allow_credentials=True,
                       allow_methods=['*'],
                       allow_headers=['*'],
                       )

    @app.middleware("http")
    async def db_session_middleware(request: Request, call_next):
        request.state.pool = db.pool
        response = await call_next(request)
        return response

    @app.on_event("shutdown")
    async def shut_down_event():
        print("Shutting down app..")
        await db.pool.close()
        print("Pool closed successfully.")

    @app.on_event("startup")
    async def start_up_event():
        print("Starting up..")
        print("Connected to Postgres.")
        await db.create_pool()
        print("Pool successfully created.")
        await init_db(db.pool)
        for id, url, key in await db.pool.fetch(''' SELECT * FROM url_keys '''):
            url_cache[key] = url
            reverse_cache[url] = key
        print("Cache loaded.")

    @app.get("/")
    async def main(request: Request):
        resp = {
            "request": request,
        }
        return templates.TemplateResponse("index.html", resp)

    @app.get("/{key}")
    async def redirect_to_url(request: Request, key: str):
        target_url = url_cache[key]
        return RedirectResponse(target_url, 302)

    @app.post("/create")
    async def create_url(request: Request, body: dict):

        url_obj = URL(body["url"])
        await url_obj.generate_short_url(request.state.pool)
        return url_obj.data

    return app


app = init_app()
