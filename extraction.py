import numpy as np
import pandas as pd

def extract(dataset):
    keywords = ['"', "sql", "statement", "select", "insert", "delete", "update", "drop", "execute"]
    columns = ['x__"', "x__sql", "x__statement", "x__select", "x__insert", "x__delete", "x__update",
               "x__drop", "x__execute"]
    result = []
    indexes = []
    index = 0
    for x in dataset["contents"].astype('str'):
        result.append(np.array([1 if keyword in x else 0 for keyword in keywords]))
        indexes.append(index)
        index += 1

    data_frame = pd.DataFrame(data=result, columns=columns)
    data_frame["y__class_value"] = dataset["class_value"]
    data_frame["idx"] = indexes
    return data_frame
