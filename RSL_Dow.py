# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:47:22 2023

@author: U332001
"""

from yahoo_fin.stock_info import get_data
import numpy as np
import pandas as pd
from yahoo_fin import stock_info as si

tickers=set(si.tickers_dow()+si.tickers_sp500())
#si.tickers_sp500()+si.tickers_nasdaq()+si.tickers_dow()+si.tickers_other()
def RSI(array, lag, duration):
    la=array[-duration:]
    lu=array[-(duration+lag):-lag]
    up=la-lu
    up[up<0]=0
    up=sum(up)/duration
    down=lu-la
    down[down<0]=0
    down=sum(down)/duration
    return up/(up+down)
dicto={}

for tikr in tickers:
  data= get_data(tikr, start_date="03/01/2023", end_date="05/10/2023", index_as_date = True, interval="1d")
  data=np.array(data['adjclose'])
  if len(data)>32:
   if RSI(data,1,30)<0.4:
      dicto[tikr]=RSI(data,1,30)
     




