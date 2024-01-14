from fastapi import FastAPI, HTTPException, Form, Request, Depends, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, DateTime, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class MyForm(BaseModel):
    units: Optional[int] = None
    meal: Optional[str] = None

class Record(BaseModel):
    id: int
    units: str
    meal: str
    created_at: str

# SQLAlchemy model
Base = declarative_base()

class MealRecord(Base):
    __tablename__ = 'inject'

    id = Column(Integer, primary_key=True)
    units = Column(String(255))
    meal = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

# SQLAlchemy database connection
DATABASE_URL = "sqlite:///./cool.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# SQLAlchemy session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, search: str = '', date: str = '', id: str = ''):
    db = SessionLocal()
    query = db.query(MealRecord)

    if search:
        query = query.filter(MealRecord.meal.ilike(f'%{search}%'))

    if date:
        query = query.filter(MealRecord.created_at.ilike(f'%{date}%'))

    if id:
        query = query.filter(MealRecord.id.ilike(f'%{id}%'))

    meal_data = query.all()

    db.close()

    return templates.TemplateResponse("index.html", {"request": request, "inject": meal_data})


@app.get("/get-meal-records", response_class=HTMLResponse)
async def get_meal_records(request: Request, db: Session = Depends(get_db)):
    meal_records = db.query(MealRecord).all()

    # Convert the query result to a list of dictionaries
    records_list = []
    for record in meal_records:
        records_list.append({
            'id': record.id,
            'units': record.units,
            'meal': record.meal,
            'created_at': record.created_at.strftime('%Y-%m-%d')  # Convert date to string for JSON serialization
        })

    return templates.TemplateResponse("meals.html", {"request": request, "meals": records_list})


@app.get('/add-meal', response_class=HTMLResponse)
async def get_add_meal_form(request: Request):
    return templates.TemplateResponse('add_meal.html', {'request': request, 'form': MyForm()})



@app.post('/add-meal', response_class=HTMLResponse)
async def add_meal(
    request: Request,
    units: int = Form(...),
    meal: str = Form(...),
    db: Session = Depends(get_db)
):

   # Process the form data
    new_entry = MealRecord(units=units, meal=meal)
    db.add(new_entry)
    try:
        db.commit()
    except Exception as e:
        print(f"Database commit error: {e}")
        raise HTTPException(status_code=505, detail="Internal Server Error")

    redirect_path =  app.url_path_for("get_meal_records_desc")
    return RedirectResponse(url=redirect_path, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/get-meal-records-desc", response_class=HTMLResponse)
async def get_meal_records_desc(request: Request, db: Session = Depends(get_db)):
    meal_records = db.query(MealRecord).order_by(desc(MealRecord.created_at)).all()

    # Convert the query result to a list of dictionaries
    records_list = []
    for record in meal_records:
        record_dict = {
            'id': record.id,
            'units': record.units,
            'meal': record.meal,
            'created_at': record.created_at.strftime('%Y-%m-%d')  # Convert date to string for JSON serialization
        }
        records_list.append(record_dict)

    return templates.TemplateResponse("meals_desc.html", {"request": request, "meals": records_list})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8008)
