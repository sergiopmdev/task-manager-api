from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from exceptions.handlers import exception_409_handler
from exceptions.users import UserAlreadyExists
from routes.users import users


app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "https://task-manager-50u4.onrender.com",
    "3.75.158.163",
    "3.125.183.140",
    "35.157.117.28",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users)

app.add_exception_handler(UserAlreadyExists, exception_409_handler)


@app.get("/")
def read_root(request: Request):
    return RedirectResponse(url=request.url._url + "docs")
