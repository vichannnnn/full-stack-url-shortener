# URL Shortener

Foobar is a Python library for dealing with word pluralization.

## Prerequisites

Please make sure that you have Docker installed. 

Please also make sure that this application is only hosted locally, as the short link generated on the website can only be copy pasted with `localhost`.

Please note that the set-up instruction is also specifically tailored for **MacOS**.

## Installation

First, clone this repository:

```bash
git init
git clone https://github.com/vichannnnn/full-stack-url-shortener.git
```

The entire application then can be started with just docker-compose after entering the root directory of the application:

```bash
cd full-stack-url-shortener
docker-compose up -d --build
```

## Usage

The link provided should be a full link rather than just a part of it. For example, `https://www.google.com` instead of `www.google.com`

The output should be in the format, for example, `http://localhost:8000/NNijfbs`

Repeatedly giving the same address input should also return the same shortened link.

<img width="391" alt="image" src="https://user-images.githubusercontent.com/54580948/194596838-e69446d3-65a2-4d43-8deb-6ce7154181c2.png">


## Information

The application tech stack are as follow:

Frontend - JS & React 

Backend - Python & FastAPI

Database - Postgres

Dev Ops - Docker & Caddy



## Notes
For simplicity's sake, I did not implement any `.gitignore`, hence you will see files like `.env` being imported in the repo as well, this is under the assumption this application is an MVP and POC and for the ease of setting up on locally on another system without having to do additional configuration.
