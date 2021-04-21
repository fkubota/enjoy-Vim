from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from ipdb import set_trace as st
from func import load_dataset
import pandas as pd
import time


def main():
    print(f'start {time.ctime()}')
    data, target = load_dataset()

    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.33, random_state=42)


    # model
    model = DecisionTreeClassifier(max_depth=2)
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)

    # eval
    acc_test = accuracy_score(y_test, y_test_pred)

    print(f'acc_test = {acc_test}')





if __name__ == '__main__':
    main()
