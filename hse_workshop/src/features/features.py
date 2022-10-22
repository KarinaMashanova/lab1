import pandas as pd
import numpy as np


def add_early_wakeup(df: pd.DataFrame) -> pd.DataFrame:
    pass
    return df

def passive_smoking(data: pd.DataFrame) -> pd.DataFrame:
    param = {np.NaN: 0,
             '1-2 раза в неделю': 2,
             '3-6 раз в неделю': 4,
             'не менее 1 раза в день': 10,
             '4 и более раз в день': 35,
             '2-3 раза в день': 25}
    new_data = np.array([param[val] for val in data['Частота пасс кур']])
    data['Пасс кур в неделю'] = new_data
    for idx in range(data.shape[0]):
        if data.iloc[idx]['Пассивное курение'] == 0 and data.iloc[idx]['Пасс кур в неделю'] != 0:
            data.loc[idx, 'Пасс кур в неделю'] = 0
    return data

class FeaturesTransformer:
    def __init__(self):
        self.train_data = None
        self.test_data = None

    def fit(self, x_train, x_test):
        self.train_data = x_train
        self.test_data = x_test
        return self

    def transform(self):

        self.train_data = passive_smoking(self.train_data)
        self.test_data = passive_smoking(self.test_data)
        return self.train_data, self.test_data