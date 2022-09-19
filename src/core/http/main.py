from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.http.router.currency_trades import currencyTradesRouter
from src.core.http.router.report import reportRouter
from src.core.http.router.interest_rates import interestRatesRouter
from src.core.http.router.cpi import cpiRouter
from src.core.http.router.eai import eaiRouter
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(currencyTradesRouter)
app.include_router(reportRouter)
app.include_router(interestRatesRouter)
app.include_router(cpiRouter)
app.include_router(eaiRouter)