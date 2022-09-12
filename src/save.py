from src.core.db.connect_db import db
from src.cpi.regions import regions
import json

def saveUseCase():
  database = db()

  for region in regions:
    region_name = region['db_id']

    collection = database[f'cpi-{region_name}']

    file = open(f'cpi/cpi-{region_name}.json', 'rb')
    products = json.loads(file.read())

    index = 0
    for product in products:

      if index == 0:
        id = '631a471d5d359b88a2bfb5a9'
        product['_id'] = id
        collection.insert_one(product)
      
      if index >= 1:
        name = product['name']

        if name == 'Alimentos e Bebidas não Alcoólicas':
          id = '631a471d5d359b88a2bfb5aa'
          product['_id'] = id
          collection.insert_one(product)

        if name == 'Bebidas Alcoólicas, Tabaco e Narcóticos':
          id = '631a471d5d359b88a2bfb5ab'
          product['_id'] = id
          collection.insert_one(product)

        if name == 'Vestuários e Calçados':
          id = '631a471d5d359b88a2bfb5ac'
          product['_id'] = id
          collection.insert_one(product)

        if name == 'Habitação, Água, Electricidade, Gás e Outros Combustíveis':
          id = '631a471d5d359b88a2bfb5ad'
          product['_id'] = id
          collection.insert_one(product)
        
        if name == 'Mobiliário, Artigos de Decoração, Equipamento Doméstico e Manutenção da Habitação':
          id = '631a471d5d359b88a2bfb5ae'
          product['_id'] = id
          collection.insert_one(product)
        
        if name == 'Saúde':
          id = '631a471d5d359b88a2bfb5af'
          product['_id'] = id
          collection.insert_one(product)

        if name == 'Transportes':
          id = '631a471d5d359b88a2bfb5b0'
          product['_id'] = id
          collection.insert_one(product)

        if name == 'Comunicações':
          id = '631a471d5d359b88a2bfb5b1'
          product['_id'] = id
          collection.insert_one(product)
        
        if name == 'Lazer, Recreação e Cultura':
          id = '631a471d5d359b88a2bfb5b2'
          product['_id'] = id
          collection.insert_one(product)

        if name == 'Educação':
          id = '631a471d5d359b88a2bfb5b3'
          product['_id'] = id
          collection.insert_one(product)

        if name == 'Restaurantes, Hotéis, Cafés e Similares':
          id = '631a471d5d359b88a2bfb5b4'
          product['_id'] = id
          collection.insert_one(product)

        if name == 'Bens e Serviços Diversos':
          id = '631a471d5d359b88a2bfb5b5'
          product['_id'] = id
          collection.insert_one(product)

       
      index += 1





    file.close()







