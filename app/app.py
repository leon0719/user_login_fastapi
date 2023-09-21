from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from database import create_db

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await create_db()


app.mount("/static", StaticFiles(directory="../static/css"), name="static")
templates = Jinja2Templates(directory="../static/templates")


@app.get("/")
async def render_example_template(request: Request):
    context = {"title": "Login Page"}
    return templates.TemplateResponse("index.html", {"request": request, **context})
