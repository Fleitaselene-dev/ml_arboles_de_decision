from pydantic import BaseModel
from fastapi import FastAPI
from routes.routes import router
from fastapi.middleware.cors import CORSMiddleware

import joblib

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)