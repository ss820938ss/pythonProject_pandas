import time
import pandas as pd

ts = pd.date_range(start='2021-07-01',
                   end=None,
                   periods=12,
                   freq='3W',
                   tz='Asia/Seoul')

print(ts)

print('---------------------------------------------------------')

ts = pd.period_range(start='2021-07-01',
                     end=None,
                     periods=12,
                     freq='3M') #3개월 단위로 기간을 정하겠다.
print(ts)

print('---------------------------------------------------------')

ts = pd.date_range(start='2021-01-01',
                   end=None,
                   periods=12,
                   freq='M')
data = ['3% 상승','1% 상승','3% 하락','4% 상승','2% 상승','6% 상승',
        '3% 상승','3% 상승','3% 하락','7% 하락','1% 상승','2% 하락']
sr = pd.Series(data=data, index=ts)

print(sr)

print('---------------------------------------------------------')
