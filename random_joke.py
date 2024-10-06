from fastapi import APIRouter
import httpx

router = APIRouter()



@router.get("/random-joke")
async def get_chuck_norris_joke():
    return await call_jokes_api()


async def call_jokes_api():
    url = "https://api.chucknorris.io/jokes/random"
    response = await httpx.AsyncClient().get(url)
    return response.json()["value"]