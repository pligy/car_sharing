from fastapi import FastAPI, APIRouter, Query, HTTPException, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
import database

app = FastAPI()
templates = Jinja2Templates(directory="htmldirectory")
api_router = APIRouter()
'''
@app.route('/')
def something():
    return FileResponse("htmldirectory/index.html", my_list=database.result)
'''
@api_router.get("/", status_code=200)
def change():
    """
    Root GET
    """
    return templates.TemplateResponse(
        "htmldirectory/index.html",
        {"my_list": 12},
    )

@app.get("/")
async def root():
    return FileResponse("htmldirectory/index.html")
