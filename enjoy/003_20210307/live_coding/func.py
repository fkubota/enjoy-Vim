from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


def load_dataset():
    iris = load_iris()

    return iris.data, iris.target
