import math

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/calculate", response_class=HTMLResponse)
async def calculate_sum(request: Request, b: float = Form(...), h: float = Form(...)):
    result_rad = math.atan(b / h)
    result_deg = result_rad * (180 / math.pi)
    cuts_pr_90 = 90 / result_deg
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result_deg": f"{result_deg:.2f}",
            "result_rad": f"{result_rad:.2f}",
            "cuts_pr_90": f"{cuts_pr_90:.2f}",
        },
    )
