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


@app.post("/", response_class=HTMLResponse)
async def calculate_sum(
    request: Request,
    cut_width: float = Form(...),
    cut_depth: float = Form(...),
    radius: float = Form(...),
    total_deg: float = Form(...),
):
    result_rad = math.atan(cut_width / cut_depth)
    result_deg = result_rad * (180 / math.pi)
    cuts_pr_90 = 90 / result_deg
    curve_ratio = 360 / total_deg
    print(curve_ratio)
    curve_len = (radius * 2 * math.pi) / curve_ratio
    num_cuts = total_deg / result_deg
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result_deg": f"{result_deg:.2f}",
            "result_rad": f"{result_rad:.2f}",
            "cuts_pr_90": f"{cuts_pr_90:.2f}",
            "curve_len": f"{curve_len:.2f}",
            "num_cuts": f"{num_cuts:.2f}",
        },
    )
