import asyncpg
import yaml

with open("authentication.yaml", "r", encoding="utf8") as stream:
    yaml_data = yaml.safe_load(stream)


async def init_db(pool: asyncpg.Pool):
    await pool.execute(
        '''CREATE TABLE IF NOT EXISTS url_keys (
           ID SERIAL PRIMARY KEY,
           url TEXT,
           shortened_url TEXT,
           UNIQUE(url),
           UNIQUE(shortened_url)
           )'''
    )
    print("Table successfully created.")
    return


class Database:
    def __init__(self):
        self.pool = None

    async def create_pool(self):
        self.pool = await asyncpg.create_pool(host=yaml_data['host'], database=yaml_data['database'],
                                              user=yaml_data['user'],
                                              password=yaml_data['password'])
