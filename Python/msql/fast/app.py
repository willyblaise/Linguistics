from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import aiomysql
from pydantic import BaseModel, validator
from datetime import date, datetime
from typing import List

# FastAPI app instance
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

    class Config:
        json_encoders = {
            date: lambda v: v.isoformat() if v else None,
            datetime: lambda v: v.isoformat() if v else None,
        }
        
 #   @validator('start_date', 'payoff_date', 'created_at', 'updated_at', pre=True)
 #   def parse_dates(cls, value):
 #       if isinstance(value, (date, datetime)):
 #           return value.isoformat()
 #       return value

class TransactionBase(BaseModel):
    loan_id: int
    payment_amount: float
    payment_date: date

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    transaction_id: int
    created_at: datetime

    @validator('payment_date', 'created_at', pre=True)
    def parse_dates(cls, value):
        if isinstance(value, (date, datetime)):
            return value.isoformat()
        return value

# FastAPI endpoints
@app.post("/loans/", response_model=LoanResponse)
async def create_loan(loan: LoanCreate, db: aiomysql.Connection = Depends(get_db)):
    async with db.cursor() as cursor:
        # Insert into 'loans' table
        await cursor.execute(
            "INSERT INTO loans (borrower_name, loan_amount, interest_rate, start_date, payoff_date) VALUES (%s, %s, %s, %s, %s)",
            (loan.borrower_name, loan.loan_amount, loan.interest_rate, loan.start_date, loan.payoff_date)
        )
        loan_id = cursor.lastrowid
        await db.commit()

    # Retrieve created loan
    return LoanResponse.parse_obj({**loan.dict(), "loan_id": loan_id, "status": "active"})

@app.get("/loans/{loan_id}", response_model=LoanResponse)
async def get_loan(loan_id: int, db: aiomysql.Connection = Depends(get_db)):
    async with db.cursor() as cursor:
        # Retrieve loan by ID
        await cursor.execute("SELECT * FROM loans WHERE loan_id = %s", (loan_id,))
        result = await cursor.fetchone()

        if result:
            columns = [desc[0] for desc in cursor.description]
            loan_dict = dict(zip(columns, result))
            return LoanResponse.parse_obj(loan_dict)

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Loan not found")

@app.post("/transactions/", response_model=TransactionResponse)
async def create_transaction(transaction: TransactionCreate, db: aiomysql.Connection = Depends(get_db)):
    async with db.cursor() as cursor:
        # Insert into 'transactions' table
        await cursor.execute(
            "INSERT INTO transactions (loan_id, payment_amount, payment_date) VALUES (%s, %s, %s)",
            (transaction.loan_id, transaction.payment_amount, transaction.payment_date)
        )
        transaction_id = cursor.lastrowid
        await db.commit()

    # Retrieve created transaction
    return TransactionResponse.parse_obj({**transaction.dict(), "transaction_id": transaction_id})

@app.get("/transactions/{transaction_id}", response_model=TransactionResponse)
async def get_transaction(transaction_id: int, db: aiomysql.Connection = Depends(get_db)):
    async with db.cursor() as cursor:
        # Retrieve transaction by ID
        await cursor.execute("SELECT * FROM transactions WHERE transaction_id = %s", (transaction_id,))
        result = await cursor.fetchone()

        if result:
            columns = [desc[0] for desc in cursor.description]
            transaction_dict = dict(zip(columns, result))
            return TransactionResponse.parse_obj(transaction_dict)

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
