import numpy as np


def extract(dataset):
    keywords = ['"', "sql", "statement", "select", "insert", "delete", "update", "drop", "execute"]
    result = []
    for x in dataset["contents"].astype('str'):
        result.append(np.array([1 if keyword in x else 0 for keyword in keywords]))

    return result
