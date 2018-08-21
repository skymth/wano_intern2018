# -*- coding: utf-8 -*-
import random
import pandas as pd
from datetime import datetime, timedelta

num = 100 #num of data
start = datetime(2018, 1, 1, 00, 00, 00)

df = pd.DataFrame({
    'id' : random.sample(range(1,10000),num),
    'create_time' : [start + timedelta(hours=x) for x in range(num)],
    'update_time' : [start + timedelta(hours=x) for x in range(num)],
    'report_date' : [None for i in range(num)],
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

