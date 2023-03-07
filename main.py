from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from routes.users import users


app = FastAPI()
app.include_router(users)


@app.get("/")
def read_root(request: Request):
    return RedirectResponse(url=request.url._url + "docs")
