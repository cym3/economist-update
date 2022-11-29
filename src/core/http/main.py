from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.http.router.money import MoneyRouter
from src.core.http.router.currency_trades import currencyTradesRouter
from src.core.http.router.report import reportRouter
from src.core.http.router.interest_rates import interestRatesRouter
from src.core.http.router.cpi import cpiRouter
from src.core.http.router.economic_activity import economicActivityRouter
from src.core.http.router.business_confidence import businessConfidenceRouter
from src.core.http.router.credit import creditRouter
from src.core.http.router.crypto_trades import cryptoTradesRouter
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
app.include_router(creditRouter)
app.include_router(economicActivityRouter)
app.include_router(businessConfidenceRouter)
app.include_router(MoneyRouter)
app.include_router(cryptoTradesRouter)
