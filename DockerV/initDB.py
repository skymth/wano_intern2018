# -*- coding: utf-8 -*-
import random
import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy import create_engine

num = 1000 #num of data
start = datetime(2018, 1, 1)

df = pd.DataFrame({
    'id' : random.sample(range(1,10000),num),
    'create_time' : [start + timedelta(hours=x) for x in range(num)],
    'update_time' : [start + timedelta(hours=x) for x in range(num)],
    'report_date' : [start + timedelta(days=x) for x in range(num)],
    'store_id' : [random.randint(0,3) for i in range(num)],
    'country_id' : [random.randint(0,5) for i in range(num)],
    'artist_id' : [random.randrange(100,600,100) for i in range(num)],
    'release_id' : [0 for i in range(num)],
    'song_id' : [0 for i in range(num)],
    'distribution_type' : [random.randint(0,1) for i in range(num)],
    'total_quantity' : [random.randint(1,10) for i in range(num)],
    'jpy_unit_price' : [0.0 for i in range(num)],
    'jpy_total_price' : [0.0 for i in range(num)],
    })

df['release_id'] = [df['artist_id'][i] + random.randrange(10,60,10) for i in range(num)]
df['song_id'] = [df['release_id'][i] + random.randrange(1,6) for i in range(num)]
df['jpy_unit_price'] = [df['song_id'][i]%10*100 for i in range(num)]
df['jpy_total_price'] = [df['jpy_unit_price'][i]*df['total_quantity'][i] for i in range(num)]


table_name = "wano_intern"
db_settings = {
    "host": 'localhost',
    "database": 'skymth_db',
    "user": 'skymth_user',
    "password": 'skymth_pass',
    "port": 3306
}

engine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(**db_settings))
df.to_sql(table_name, engine,if_exists = 'append',  index=False)
