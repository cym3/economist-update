from src.cpi.services.cpi import cpiService
from src.cpi.domain.entities.save_cpi import saveCpiDB
from src.cpi.domain.entities.get_all_cpi import getAllCpiDB

async def cpiUseCase():
    # all = await getAllCpiDB()
    
    CPI = await cpiService()

    # await saveCpiDB(CPI)

    return CPI
