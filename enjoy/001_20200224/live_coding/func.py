import pandas as pd
from sklearn.datasets import load_iris


def get_datasets():
    iris = load_iris()
    data = iris.data
    feature_names = iris.feature_names
    target = iris.target
    df = pd.DataFrame(data, columns=feature_names)

    return df, target
