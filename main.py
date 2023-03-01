from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def read_root(request: Request):
    return RedirectResponse(url=request.url._url + "docs")
