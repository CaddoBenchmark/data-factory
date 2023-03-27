import numpy as np
import pandas as pd

def extract(dataset):
    keywords = ['"', "sql", "statement", "select", "insert", "delete", "update", "drop", "execute"]
    # columns = ['x__"', "x__sql", "x__statement", "x__select", "x__insert", "x__delete", "x__update",
    #            "x__drop", "x__execute"]
    columns = ['x__contents', "y__G0"]
    result = []
    indexes = []
    index = 0
    for x in dataset["contents"].astype('str'):
        # result.append(np.array([x]))
        indexes.append(index)
        index += 1

    data_frame = pd.DataFrame(data=result, columns=columns)
    data_frame["y__G0"] = dataset["G0"]
    data_frame["x__contents"] = dataset["contents"]
    data_frame["idx"] = indexes
    return data_frame
