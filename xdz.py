import random
import pandas as pd
import numpy as np
import asyncio
from time import sleep
import os
import logging
import pytz
from datetime import datetime, timedelta





def updateXDZ(sender, receiver, num):
  df = pd.read_csv('./inkbot/xdz.csv')

  last = 678
  
  condition = ((df['client1'] == int(sender)) & (df['client2'] == int(receiver))) | ((df['client1'] == int(receiver)) &(df['client2'] == int(sender)))
  # If such row exists

  desired_timezone = pytz.timezone('America/New_York')
  current_time = datetime.now(desired_timezone)

  
  if condition.any():
    lastTime = df.loc[condition, 'time'].values[0]
    
    ts1 = datetime.strptime(lastTime, "%Y-%m-%d %H:%M:%S.%f%z")
    # ts2 = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S.%f%z")
    if current_time - ts1 <= timedelta(days=30):
      df.loc[condition, 'value1'] += float(num)
      
    else:
      df.loc[condition, 'value1'] = float(num)
      
    df.loc[condition, 'time'] = current_time
    last = df.loc[condition, 'value1'].values[0]
    
  else:  # If no such row exists
    # print('no matching row, creating... printing types\n')
    # print("type of input:")
    # print(type(sender))
    # print(type(receiver))
    # print("\n type of data init: ")
    # print(df.dtypes)
    new_row = pd.DataFrame({'client1': [sender], 'client2': [receiver], 'value1': [num], 'time': [current_time]})
    df = pd.concat([df, new_row], ignore_index=True)

    df['client1'] = df['client1'].astype('int64')
    df['client2'] = df['client2'].astype('int64')
    last = num
  df.to_csv("./inkbot/xdz.csv", index=False)
  return last







