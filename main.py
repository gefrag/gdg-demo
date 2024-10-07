from fastapi import FastAPI

import external_api
import prime_numbers
import random_country

app = FastAPI()


app.include_router(random_country.router)
app.include_router(prime_numbers.router)
app.include_router(external_api.router)


@app.get("/count")
def count():
    import threading

    return {
        "count": threading.active_count(),
        "names": [str(t) for t in threading.enumerate()],
    }
