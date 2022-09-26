import schedule
import time
from src.economicActivityAggregate.check_update import checkEconomicActivityUpdateUseCase
from src.cpi.main import cpiUseCase
from src.currentCurrencyTrades.main import currentCurrencyTradesUseCase
from src.interestRates.main import interestRatesUseCase
from src.report.main import reportUseCase
from src.core.mail.my_mail import sandMyMail
from dotenv import load_dotenv

load_dotenv()

# Check updates 
schedule.every().day.at("02:00").do(checkEconomicActivityUpdateUseCase)

schedule.every().day.at("03:00").do(cpiUseCase)
schedule.every().day.at("04:00").do(sandMyMail)
schedule.every().day.at("04:00").do(reportUseCase)
schedule.every().day.at("08:00").do(interestRatesUseCase)

schedule.every().day.at("08:00").do(currentCurrencyTradesUseCase)
schedule.every().day.at("16:00").do(currentCurrencyTradesUseCase)



# schedule.every(5).seconds.do(reportUseCase)

while True:
    schedule.run_pending()
    time.sleep(1)
     