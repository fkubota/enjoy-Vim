import pandas as pd
from ipdb import set_trace as st
from sklearn.datasets import load_iris


def get_datasets():
    iris = load_iris()
    data = iris.data
    feat_name = iris.feature_names
    target = iris.target
    df = pd.DataFrame(data, columns=feat_name)
    return df, target
