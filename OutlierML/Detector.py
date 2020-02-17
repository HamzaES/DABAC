# importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from sklearn.ensemble import IsolationForest

# splitting test and training sets and removing the "attack_cat" column.
X_train, X_test, y_train, y_test = train_test_split(df.drop([target, 'attack_cat'], axis=1),
                                                                df['attack_cat'],
                                                    test_size=0.33, random_state=11)
# setting up the classifiers clIF = IsolationForest, LOF = LocalOutlierFactor
clIF = IsolationForest(max_samples=0.25, random_state=11, contamination=0.15, n_estimators=100, n_jobs=-1)
clLOF = LocalOutlierFactor(n_neighbors=15, metric='euclidean', algorithm='auto', contamination=0.15, n_jobs=-1)
# fitting the training data to the models
clIF.fit(X_train,y_train)
y_pred_train = clIF.predict(X_train)
y_pred_train_lof = clLOF.fit_predict(X_train_nd, y_train_nd)
# testing on the test set
clIF.fit(X_train,y_train)
y_pred_test = clIF.predict(X_test)
y_pred_test_lof = clLOF.fit_predict(X_train_nd, y_train_nd)
# creating a score to use in GridSearchCV
score = {'AUC': 'roc_auc', 'Recall': make_scorer(recall_score, pos_label=-1)}
# Using GridSearchCV to find  the optimal number of estimators
grid = GridSearchCV(IsolationForest(max_samples=0.25, random_state=11, contamination = 0.15, n_jobs=-1),
                  param_grid={'n_estimators': range(20, 230, 30)},
                  scoring=scoring, refit='Recall')
grid.fit(X_train, y_train)
results = grid.cv_results_ # Storing the result
# Using GridSearchCV to find  the optimal max_samples value
grid_ms = GridSearchCV(IsolationForest(random_state=11, contamination = 0.15, n_estimators=150, n_jobs=-1),
                  param_grid={'max_samples': np.arange(0.1, 1.0, 0.1)},
                  scoring=scoring, refit='Recall')
grid_ms.fit(X_train, y_train)
results = grid_ms.cv_results_ # Storing the result
# Using GridSearchCV to find  the optimal contamination value
grid_cont = GridSearchCV(IsolationForest(random_state=11, max_samples=0.10, n_estimators=150, n_jobs=-1),
                  param_grid={'contamination': np.arange(0.01, 0.25, 0.05)},
                  scoring=scoring, refit='Recall')
grid_cont.fit(X_train_sf, y_train_sf)
results = grid_cont.cv_results_ # Storing the result

# functions that evaluates the "anomaliness" of a request, using IsolationForest and LocalOutlierFactor
def detectOutlierIF(request):
    return clIF.predict(request)
def detectOutlierLOF(request):
    return clLOF.predict(request)
