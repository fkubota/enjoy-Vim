import yaml
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import time
import func


def main():
    print(f'start {time.ctime()}')
    # config

    with open('config.yml') as file:
        config = yaml.safe_load(file)

    data, target = func.load_dataset()

    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.33, random_state=42)

    # model
    model = DecisionTreeClassifier(**config['model']['params'])
    model.fit(X_train, y_train)

    # pred
    y_test_pred = model.predict(X_test)

    # eval
    acc_test = accuracy_score(y_test, y_test_pred)

    print(f'acc_test: {acc_test}')
    print(f'end {time.ctime()}')


if __name__ == '__main__':
    main()
