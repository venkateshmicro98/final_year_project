#import external files

import feature_extraction as fe


# Load libraries
import numpy as np
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)




# Split-out validation dataset
X = fe.final_perm_vector
print(X)
Y = fe.final_binary_class_vector
print(Y)

#Import Library
from sklearn import svm
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create SVM classification object 
#model = svm.SVC(kernel='linear', C=1, gamma=1) 
model = KNeighborsClassifier(n_neighbors=2)
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.55)  

print("KNN X_train")
print(X_train)


print("KNN X_test")
print(X_test)

print("KNN y_train")
print(y_train)

print("KNN y_test")
print(y_test)


# there is various option associated with it, like changing kernel, gamma and C value. Will discuss more # about it in next section.Train the model using the training sets and check score
model.fit(X, Y)
model.score(X, Y)
#Predict Output
predicted= model.predict(X_test)
print("KNN Predicted")
print(predicted)
print("KNN Accuracy : ")
print(accuracy_score(y_test, predicted))
#target_names = ["Benign","Malware"]
print(classification_report(y_test, predicted))

print("KNN Not Used : ")
set(y_test) - set(predicted)


model = svm.SVC(kernel='linear', C=1, gamma=1) 

 
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.55)  

print("SVM X_train")
print(X_train)


print("SVM X_test")
print(X_test)

print("SVM y_train")
print(y_train)

print("SVM y_test")
print(y_test)


# there is various option associated with it, like changing kernel, gamma and C value. Will discuss more # about it in next section.Train the model using the training sets and check score
model.fit(X, Y)
model.score(X, Y)
#Predict Output
predicted= model.predict(X_test)
print("SVM Predicted")
print(predicted)
print("SVM Accuracy : ")
print(accuracy_score(y_test, predicted))
#target_names = ["Benign","Malware"]
print(classification_report(y_test, predicted))

print("SVM Not Used : ")
set(y_test) - set(predicted)



"""
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'


# Spot Check Algorithms
models = []
#models.append(('LR', LogisticRegression(solver='lbfgs', multi_class='ovr')))
#models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier(n_neighbors=2)))
#models.append(('CART', DecisionTreeClassifier()))
#models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=2, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring,error_score=np.nan)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)



# Make predictions on validation dataset
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

"""