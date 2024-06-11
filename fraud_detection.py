import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report

print()
print("Reading in data... ")
X_train  = pd.read_csv('challenges/ML_Fraud_Detection/data/encoded_training_data.csv', header=None)
y_train  = pd.read_csv('challenges/ML_Fraud_Detection/data/encoded_training_fraud_scoring.csv', header=None)
X_test   = pd.read_csv('challenges/ML_Fraud_Detection/data/encoded_test_data.csv', header=None)
y_test   = pd.read_csv('challenges/ML_Fraud_Detection/data/encoded_test_fraud_scoring.csv', header=None)

# Need to flatten the y data out to quiet down some warnings.
y_train = np.ravel(y_train)
y_test = np.ravel(y_test)

print(f"There are {len(X_train)} rows of training data.")

# Applying SMOTE to balance the data by adding more fraud cases
smote = SMOTE()
X_smote, y_smote = smote.fit_resample(X_train, y_train)

# Print out some confirmations that SMOTE worked.
v, fraud_counts_before = np.unique(y_train, return_counts=True)
v, fraud_counts_after = np.unique(y_smote, return_counts=True)

print()
print(f"Before SMOTE oversampling, there were {fraud_counts_before[1]} fraud rows.")
print(f"After SMOTE oversampling, there are {fraud_counts_after[1]} fraud rows.")
print()

model = GradientBoostingClassifier().fit(X_smote,y_smote)
y_predict = model.predict(X_test)

print("\nGradientBoostingClassifier with SMOTE Oversampling\n",
      "====================================================\n",
      classification_report(y_test, y_predict, labels=[0,1]))

print("Writing predictions to file: challenges/ML_Fraud_Detection/data/fraud_predictions.csv\n")
pd.DataFrame(y_predict).to_csv('challenges/ML_Fraud_Detection/data/fraud_predictions.csv', index=False, header=False)
