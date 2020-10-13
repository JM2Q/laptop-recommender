# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:34:24 2020

@author: 77433
"""
from transfer import *
import pandas as pd

filename = 'ZOLlaptop30.csv'
raw_data = pd.read_csv(filename,encoding = 'gbk')
rows ,cols = raw_data.shape
raw_data = raw_data.fillna(0)  # 用0 值填充 空白避免出错
'''
插入新列 cpu_rank , keyboard_haslight,battery_life,weight_type,
is_rtx,game_type,business_type, thin_type,video_type更换以下几列的数据 gpu_memory,screen_size
'''
cols_name = raw_data.columns.tolist()
cols_name.insert(14,'is_apple')
cols_name.insert(14,'game_type')
cols_name.insert(14,'business_type')
cols_name.insert(14,'thin_type')
cols_name.insert(14,'video_type')
cols_name.insert(13,'keyboard_haslight')
cols_name.insert(11,'battery_life')
cols_name.insert(10,'weight_type')
cols_name.insert(5,'is_rtx')
cols_name.insert(2,'cpu_rank')
cols_name.insert(0,'id')
data = raw_data.reindex(columns = cols_name)
data['id']= range(0,rows)

#data.loc[1,'cpu_rank'] = cpu_rank(data.loc[1,'cpu'])
for i in range(rows):
    try:
        data.loc[i,'id'] = int(i)
        data.loc[i,'cpu_rank'] = cpu_rank(data.loc[i,'cpu'])
        data.loc[i,'weight_type'] = weight(data.loc[i,'weight'])
        data.loc[i,'battery_life'] = battery(data.loc[i,'battery'])
        data.loc[i,'keyboard_haslight'] = keyboardhaslight(data.loc[i,'keyboard'])
        data.loc[i,'is_rtx'] = is_rtx(data.loc[i,'gpu'])
        data.loc[i,'video_type'] = video_type(data.loc[i,'description'])
        data.loc[i,'thin_type'] = thin_type(data.loc[i,'description'])
        data.loc[i,'business_type'] = business_type(data.loc[i,'description'])
        data.loc[i,'game_type'] = game_type(data.loc[i,'description'])
        data.loc[i,'screen_size'] = screen_size(data.loc[i,'screen_size'])
        data.loc[i,'gpu_memory'] = gpu_memory(data.loc[i,'gpu_memory'])
        data.loc[i,'ram'] = ram(data.loc[i,'ram'])
        data.loc[i,'is_apple'] = is_apple(data.loc[i,'name'])
    except :
        print(i)
    #print("fixing...",i)
    
newfile = filename.split('.')[0]+'fixed.csv'
data.to_csv(newfile)
print('fix completed!')
    