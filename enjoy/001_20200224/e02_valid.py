'''
test を valid にして

* :%s などの置換コマンドは禁止！
'''

from sklearn.model_selection import KFold
kf = KFold(n_splits=5, shuffle=True)
for fold_i, (train_idx, valid_idx) in enumerate(kf.split(X)):
    X_train, X_valid = X.values[train_idx, :], X.values[valid_idx, :]
    y_train, y_valid = y[train_idx], y[valid_idx]


df_test
