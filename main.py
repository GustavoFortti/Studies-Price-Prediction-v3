import pandas as pd
from math import log2

if __name__ == '__main__':
    df = pd.read_csv('./EURUSD60.csv', sep='\t', 
    names=['time' ,'open', 'x', 'close', 'y', 'volume'])

    # df = df['close']

    _win_h = 0
    _los_h = 0
    _win_l = 0
    _los_l = 0

    for i in range(len(df.iloc[10000:, :]['close'])):
        if (i < len(df['close']) - 1):
            x = log2(df.iloc[i:i+1, 3:4].values[0][0] / df.iloc[i+1:i+2, 3:4].values[0][0])
            if (df.iloc[i+1:i+2, 3:4].values[0][0] > df.iloc[i+2:i+3, 3:4].values[0][0]):
                if (x < 0):
                    _win_l = _win_l + 1
                else:
                    _los_l = _los_l + 1
            else:
                if (x < 0):
                    _win_h = _win_h + 1
                else:
                    _los_h = _los_h + 1

    
    # print(sum(_win_h  + _los_h + _win_l + _los_l))
    print('_win_h = ' + str(_win_h))
    print('_los_h = ' + str(_los_h))
    print('t = ' + str(_win_h / (_win_h + _los_h)))

    print('_win_l = ' + str(_win_l))
    print('_los_l = ' + str(_los_l))
    print('t = ' + str(_win_l / (_win_l + _los_l)))