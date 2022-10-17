from src.currentCurrencyTrades.infra.main import tradesInfra
from src.currentCurrencyTrades.aws.parse.tables import tablesParser
from src.currentCurrencyTrades.aws.extract.tables import extractTable
from src.currentCurrencyTrades.domain.requiredFields.page_validator import fileValidator
from src.currentCurrencyTrades.services.current_trades import currencyTradesService
from src.currentCurrencyTrades.domain.entities.save_current_trades import saveCurrentTradesDB
from src.currentCurrencyTrades.domain.entities.get_all_currencies import getAllCurrenciesDB

name: str = 'exchange-rates'

def currentCurrencyTradesUseCase():
    file_path = tradesInfra(name=name)

    if file_path:
        response = extractTable(documentPath=file_path)

        is_valid_page = fileValidator(response, name)

        if is_valid_page:
            tables = tablesParser(response)

            currencies = getAllCurrenciesDB()
            
            currenciesTrades = currencyTradesService(currencies, tables)

            saveCurrentTradesDB(currenciesTrades)

    return currenciesTrades
