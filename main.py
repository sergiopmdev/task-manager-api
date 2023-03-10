from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from routes.users import users


app = FastAPI()

origins = ["http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users)


@app.get("/")
def read_root(request: Request):
    return RedirectResponse(url=request.url._url + "docs")
