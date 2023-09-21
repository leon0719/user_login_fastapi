from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from database import create_db
from schemas import UserCreate, UserRead, UserUpdate
from oauth2 import auth_backend, active_user, fastapi_users
from fastapi import Depends


app = FastAPI()
app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(), prefix="/auth", tags=["auth"]
)
app.include_router(
    fastapi_users.get_verify_router(UserRead), prefix="/auth", tags=["auth"]
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserCreate, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: UserRead = Depends(active_user)):
    return {"message": f"Hello {user.username} and {user.email}"}


@app.on_event("startup")
async def on_startup():
    await create_db()


app.mount("/static", StaticFiles(directory="../static/css"), name="static")
templates = Jinja2Templates(directory="../static/templates")


@app.get("/")
async def render_example_template(request: Request):
    context = {"title": "Login Page"}
    return templates.TemplateResponse("index.html", {"request": request, **context})
