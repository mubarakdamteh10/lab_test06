import json
from fastapi import APIRouter
import datetime

year_api_router = APIRouter()

@year_api_router.get("/service/getage")
async def getyear_test(year : int):
    cerrent_year = 2565
    age = cerrent_year - year
    return {"age": age}
    
    