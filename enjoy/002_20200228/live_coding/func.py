from ipdb import set_trace as st
from sklearn.datasets import load_iris


def load_dataset():
    iris = load_iris()
    return iris.data, iris.target
