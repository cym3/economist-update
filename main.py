import schedule
import time
from src.cpi.main import cpiUseCase
from src.currentCurrencyTrades.main import currentCurrencyTradesUseCase
from src.interestRates.main import interestRatesUseCase
from src.report.main import reportUseCase
from src.core.mail.my_mail import sandMyMail

schedule.every().day.at("00:00").do(cpiUseCase)
schedule.every().day.at("04:00").do(sandMyMail)
schedule.every().day.at("04:00").do(reportUseCase)
schedule.every().day.at("08:00").do(interestRatesUseCase)

schedule.every().day.at("08:00").do(currentCurrencyTradesUseCase)
schedule.every().day.at("16:00").do(currentCurrencyTradesUseCase)


while True:
    schedule.run_pending()
    time.sleep(1)
     