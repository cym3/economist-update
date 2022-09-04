from src.report.domain.requiredFields.report import Report

async def reportService(tasks: list[Report]):
    r_tasks = []
    
    for task in tasks:
        task.pop('_id')
        
        if task['isDone'] == True:
            task['isDone'] = 'Yes'
        if task['isDone'] == False:
            task['isDone'] = 'No'

        values = task.values()

        values = [v for v in values]
        
        r_tasks.append(values)

    return r_tasks
