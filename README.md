# ML_Fraud_Detection

***SUMMARY:***
In this project, we are posing as a startup AI company. We will be pitching our training model to possible investors in the vehicle insurance industry. We will be investigating vehicle insurance claim fraud and further training our model to predict future cases of vehicle insurance fraud.

***OUR OBJECTIVES:***

_For this project, our objective is to perform / create a model that performs a test with an accuracy of >75%-80%. In doing this, we would also like to see our model predictions perform with >95% accuracy._

***OUR APPROACH:***

_In beginning our project, we started with creating a Jupyter notebook of our data, cleansed the data, then exported it as a CSV for the model. With this, our Python script initializes, trains, and evaluates the model._

_Our approach consisted of gathering the data from kaggle, cleaning the data through the filling missing data with "0"; creating our encoders, concatenanting our data, then training the model. _

***OUR DATA:***
_We imported our Data from Kaggle: https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection_

_At first glance of our data, there are 14,997 non-fraudulent rows and 923 fraudulent rows._

_***DISCREPANCIES:***_

_Initially, with our original dataset, we ran the multiple test before deciding on the KNeighbors Test. 
Our discrepancy is with the balanced_accuracy_score of the test, resulting in a value <75%.
With this in mind, we utilized the "SMOTETomek" function to balance the data at 10,722 non-fradulent rows and 10,722 fraudulent rows; essentially balancing the data to assist the model in making accurate predictions. With this in mind, we learned that our dataset size was not large enough through evaluating our F1 Score._

_***AFTER ADDRESSING OUR DISCREPANCIES***_

_After evaluating and deliberating our dataset size issues, we split our data into training and testing sets, applied the appropriate encoding, and tested different balancing techniques. Using the GradientBoostingClassifier and SMOTE Oversampling resulted in the best results._

***OUR LEARNINGS:***

_In performing our analysis, we found that despite our relatively large dataset, the type of model we were hoping to run required more data. Each time we ran a test our balanced accuracy score, train score, and test score proved good numbers. The issue that led us to the conclusion of necessisitating more data was our macro avg score remaining below >60%._

_Another learning of ours includes understanding what data from our dataset was considered "necessary" data, opposed to "noise". By noise, we mean data that the model was implicating into its predictions, leading to the skewing / inaccuracies in our models performance._

***CONCLUSION:***

_In conclusion to our project, we can start by taking away the importance of balancing our data, or using "balanced_accuracy_score" if the data is imbalanced but the values being tested are relatively close to each other._

_Another conclusion we came to was in regard to what is considered "noise" to the model and what is considered key information to the model._

_Finally, we also concluded that since this project is being posed as a real life example, we as an AI startup company would simply request more data from the insurance companies providing the information._

***MISC NOTES:***

_Once again, we initially utilized SMOTETomek to balance our data with the goal of assisting the model in making accurate predictions. After much deliberation, we found our dataset to not be large enough to fully train the model._

_Programming Language Used: Python._

_Packages Used: Anaconda, Pandas, NumPy, sklearn.model_selection: train_test_split, sklearn.metrics: balanced_accuracy_score, sklearn.preprocessing: OneHotEncoder, OrdinalEncoder, and StandardScaler. Sklearn.svm: SVC, sklearn.neighbors: KNeighborsClassifier, sklearn.tree: DecisionTreeClassifier, sklearn.ensemble: RandomForestClassifier, sklearn.ensemble: ExtraTreesClassifier, sklearn.ensemble: GradientBoostingClassifier, sklearn.ensemble: AdaBoostClassifier, imblearn.over_sampling: SMOTE, imblearn.under_sampling: TomekLinks, imblearn.combine: SMOTETomek, sklearn.metrics: classification_report

_Tools Used: Jupyter Notebook (IPython)._

_Credit & Contributors: ballen614, Ozkazanc1991, and 2Hail_
