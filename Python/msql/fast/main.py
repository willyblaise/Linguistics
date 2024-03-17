from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import aiomysql
from pydantic import BaseModel
from datetime import date, datetime
from typing import List

app = FastAPI()

# Database configuration
database_config = {
    "host": "localhost",
    "port": 3306,
    "user": "champ",
    "password": "loga",
    "db": "family_loans",
}

# Dependency to get a database connection pool
async def get_db():
    pool = await aiomysql.create_pool(**database_config)
    db = await pool.acquire()
    yield db
    await pool.release(db)

# Pydantic models for request and response
class LoanBase(BaseModel):
    borrower_name: str
    loan_amount: float
    interest_rate: float = 0.00
    start_date: date
#    payoff_date: date = None

class LoanCreate(LoanBase):
    pass

class LoanResponse(LoanBase):
    loan_id: int
    status: str
    created_at: datetime
    updated_at: datetime

# Jinja2 templates configuration
templates = Jinja2Templates(directory="templates")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# FastAPI endpoints
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/loans", response_class=HTMLResponse)
async def view_loans(request: Request, db: aiomysql.Connection = Depends(get_db)):
    async with db.cursor() as cursor:
        # Retrieve outstanding loans
        await cursor.execute("SELECT * FROM loans WHERE status = 'active'")
        results = await cursor.fetchall()

        loans = [LoanResponse.parse_obj(dict(zip([desc[0] for desc in cursor.description], result))) for result in results]

        return templates.TemplateResponse("loans.html", {"request": request, "loans": loans})

if __name__ == "__main__":
    import uvicorn
    from starlette.requests import Request

    uvicorn.run(app, host="127.0.0.1", port=8000)
