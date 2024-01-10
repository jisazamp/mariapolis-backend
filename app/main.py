from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.billing_controller import router as billing_router

app = FastAPI(title="Mariapolis API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(billing_router)
