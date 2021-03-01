import yaml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from ipdb import set_trace as st
import pandas as pd
import time
import func


def main():
    print(f'sart: {time.ctime()}')
    with open('config.yml') as file:
        config = yaml.safe_load(file)

    model_params = config['model']['params']

    df, target = func.get_datasets()
    train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
            df, target, test_size=0.33, random_state=42)

    model = RandomForestClassifier(**model_params)
    model.fit(X_train, y_train)

    y_test_pred = model.predict(X_test)

    acc_test = accuracy_score(y_test, y_test_pred)

    print(f'acc_test: {acc_test}')


if __name__ == '__main__':
    main()
