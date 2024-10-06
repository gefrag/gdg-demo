from fastapi import FastAPI

import external_api
import prime_numbers
import random_joke

app = FastAPI()


app.include_router(random_joke.router)
app.include_router(prime_numbers.router)
app.include_router(external_api.router)