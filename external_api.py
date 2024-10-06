import httpx
from fastapi import APIRouter
import requests

router = APIRouter()


@router.get("/external-api")
async def get_data_from_external_api():
    url = "https://demogdg.free.beeceptor.com/"
    response = requests.get(url)
    return response.text


@router.get("/external-api-async")
async def get_data_from_external_api():
    url = "https://demogdg.free.beeceptor.com/"
    response = await httpx.AsyncClient().get(url, timeout=10)
    return response.text