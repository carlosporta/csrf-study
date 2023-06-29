from secrets import token_urlsafe

from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")
SESSIONS = {}


def gen_session_id():
    return token_urlsafe(32)

def gen_token():
    return token_urlsafe(32)


@app.get("/change-username")
async def change_username(request: Request):
    session_id = gen_session_id()
    token = gen_token()
    response = templates.TemplateResponse(
        "change-username.html",
        {
            "request": request,
        },
    )
    response.set_cookie(key="csrftoken", value=token, secure=True, httponly=True)
    response.set_cookie(key="sessionid", value=session_id, secure=True, httponly=True)
    SESSIONS[session_id] = token
    return response


@app.get("/change-username-submit")
async def change_username_submit(request: Request, old: str, new: str):
    token = request.cookies.get("csrftoken")
    session_id = request.cookies.get("sessionid")

    if session_id not in SESSIONS or token != SESSIONS[session_id]:
        raise HTTPException(status_code=403, detail="Invalid CSRF token")

    response = templates.TemplateResponse(
        "change-username-submit.html",
        {
            "request": request,
            "old": old,
            "new": new,
        },
    )

    response.delete_cookie(key="csrftoken")
    return response
