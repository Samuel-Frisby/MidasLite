from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Query
from app.services.yahoo import get_stock_summary, get_stock_history

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("", response_class=HTMLResponse)
async def get_stock(request: Request, ticker: str = Query(...)):
    stock_data = get_stock_summary(ticker)
    history_data = get_stock_history(ticker)
    
    return templates.TemplateResponse("partials/stock_card.html", {
        "request": request,
        "ticker": ticker.upper(),
        "stock": stock_data,
        "history": history_data
    })

