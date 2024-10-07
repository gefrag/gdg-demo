import httpx
import requests
from fastapi import APIRouter

router = APIRouter()

url = "https://demogdg2.free.beeceptor.com/"

@router.get("/external-api")
async def get_data_from_external_api():
    response = requests.get(url)
    return response.text


@router.get("/external-api-async")
async def get_data_from_external_api():
    response = await httpx.AsyncClient().get(url, timeout=10)
    return response.text