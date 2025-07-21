from fastapi import FastAPI
from .database import engine
from .routes import manager_routes, student_routes
from . import models


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(manager_routes.router, tags=['Manager Routes'])
app.include_router(student_routes.router, tags=['Student Routes'])

