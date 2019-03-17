#import external files

#import feature_extraction as fe
#import feature_extraction_static as fe


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
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)




# Split-out validation dataset
#X = fe.final_perm_vector
X = np.loadtxt('permission_vector.csv')
print(X)
#Y = fe.final_binary_class_vector
Y = np.loadtxt('binary_class_vector.csv')
print(Y)

"""
#Import Library
from sklearn import svm
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create SVM classification object 
#model = svm.SVC(kernel='linear', C=1, gamma=1) 
model = KNeighborsClassifier(n_neighbors=2)
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.30)  

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

#print("KNN Not Used : ")
#set(y_test) - set(predicted)


model = KNeighborsClassifier(n_neighbors=2)
from sklearn.model_selection import train_test_split 
print("Dimension before PCA")
print(X.shape)
pca = PCA(n_components=16)
X_p = pca.fit_transform(X,Y)
print("Dimension after PCA")
print(X_p.shape)
X_train, X_test, y_train, y_test = train_test_split(X_p, Y, test_size = 0.30)  

print("KNN X_train with PCA")
print(X_train)


print("KNN X_test with PCA")
print(X_test)

print("KNN y_train with PCA")
print(y_train)

print("KNN y_test with PCA")
print(y_test)


# there is various option associated with it, like changing kernel, gamma and C value. Will discuss more # about it in next section.Train the model using the training sets and check score
model.fit(X_p, Y)
model.score(X_p, Y)
#Predict Output
predicted= model.predict(X_test)
print("KNN Predicted with PCA")
print(predicted)
print("KNN Accuracy with PCA: ")
print(accuracy_score(y_test, predicted))
#target_names = ["Benign","Malware"]
print(classification_report(y_test, predicted))

#print("KNN Not Used with PCA: ")
#set(y_test) - set(predicted)



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
#print(classification_report(y_test, predicted))

#print("SVM Not Used : ")
#set(y_test) - set(predicted)

"""


validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'


# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='lbfgs', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier(n_neighbors=2)))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
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

