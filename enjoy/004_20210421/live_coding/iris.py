import yaml
from ipdb import set_trace as st
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def get_datasets():
    iris = load_iris()
    data = iris.data
    target = iris.target
    feature_names = iris.feature_names

    df = pd.DataFrame(data, columns=feature_names)

    return df, target


def get_config():
    with open('config.yml') as file:
        config = yaml.safe_load(file)
    return config


def main():
    print('hello vim')
    config = get_config()
    seed = config['globals']['seed']
    test_size = config['globals']['test_size']
    df, target = get_datasets()

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(
            df, target, test_size=test_size, random_state=seed)
    # model
    model = DecisionTreeClassifier(random_state=seed)
    model.fit(X_train, y_train)

    # eval
    y_test_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_test_pred)

    print(f'accuracy_test: {acc:.4f}')


if __name__ == '__main__':
    main()
