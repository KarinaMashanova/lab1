import pickle
from typing import Union
from pandas import DataFrame
from pandas.core.indexes.base import Index as PandasIndex


def save_as_pickle(obj: Union[DataFrame, PandasIndex], path: str) -> None:
    if isinstance(obj, DataFrame):
        obj.to_pickle(path)
    elif isinstance(obj, PandasIndex):
        with open('path', 'wb') as f:
            pickle.dump(obj, f)
    else: 
        pickle.dump(obj, open(path, 'wb'))
        
def load_model(path: str):
    return pickle.load(open(path, 'rb'))
