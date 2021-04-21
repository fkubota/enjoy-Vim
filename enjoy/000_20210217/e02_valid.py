'''
test を valid にして

* :%s などの置換コマンドは禁止！
'''

from sklearn.model_selection import KFold
kf = KFold(n_splits=5, shuffle=True)
for fold_i, (train_idx, test_idx) in enumerate(kf.split(X)):
    X_train, X_test = X.values[train_idx, :], X.values[test_idx, :]
    y_train, y_test = y[train_idx], y[test_idx]
