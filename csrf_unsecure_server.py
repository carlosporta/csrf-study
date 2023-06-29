from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/change-username")
async def change_username(request: Request):
    return templates.TemplateResponse("change-username.html", {"request": request})


@app.get("/change-username-submit")
async def change_username_submit(request: Request, old: str, new: str):
    return templates.TemplateResponse(
        "change-username-submit.html",
        {
            "request": request,
            "old": old,
            "new": new,
        },
    )
