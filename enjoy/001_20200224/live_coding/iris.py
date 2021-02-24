from ipdb import set_trace as st
import pandas as pd
import yaml
import time
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import func as F


def main():
    print(f'start at {time.ctime()}')
    with open('config.yml') as file:
        config = yaml.safe_load(file)
    model_params = config['model']['params']

    df, target = F.get_datasets()
    X_train, X_test, y_train, y_test = train_test_split(df, target, test_size=0.33, random_state=42)

    # model
    model = DecisionTreeClassifier(**model_params)
    model.fit(X_train, y_train)

    # pred
    y_test_pred = model.predict(X_test)

    # eval
    acc_test = accuracy_score(y_test, y_test_pred)

    print(f'acc_test: {acc_test}')
    print(f'end at {time.ctime()}')


if __name__ == '__main__':
    main()
