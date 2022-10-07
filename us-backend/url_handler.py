import random
import string
import asyncpg
import validators
from fastapi import HTTPException

all_chars = string.ascii_letters + string.digits
url_cache = {}
reverse_cache = {}

class URL:
    def __init__(self, address: str):
        self.address: str = self.validate_address(address)
        self.short_url = None
        self.data = None

    def validate_address(self, address: str):
        if not validators.url(address):
            raise HTTPException(status_code=400, detail="Bad URL")
        return address

    async def generate_short_url(self, pool: asyncpg.Pool):
        if not self.short_url:
            key = "".join(random.choice(all_chars) for _ in range(7))

            try:
                self.short_url = reverse_cache[self.address]
                self.data = {
                    'url': self.address,
                    'short_url': self.short_url

                }
                return self.data
            except KeyError:
                pass

            retry_counter = 0
            while retry_counter < 20:
                try:
                    await pool.execute(''' INSERT INTO url_keys (url, shortened_url) VALUES ($1, $2) ''', self.address, key)
                    url_cache[key] = self.address
                    self.short_url = key
                    reverse_cache[self.address] = key
                    break
                except asyncpg.UniqueViolationError:
                    key = "".join(random.choice(all_chars) for _ in range(7))
                    retry_counter += 1

            else:
                raise HTTPException(status_code=400, detail="Something went wrong!")

            self.data = {
                'url': self.address,
                'short_url': self.short_url

            }
        return self.data
