#import external files

#import feature_extraction as fe
#import feature_extraction_static as fe

import static_feature as st
import dynamic.dynamic_feature as dy

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
"""

Appln_Path = "/home/venkatesh/fyp/Testing/"
APK_name = "2a3de2b348c02fdb96a11af33ff9fcb932a47b7d.apk"
permissions_path = "/home/venkatesh/fyp/github/final_year_project/"
permissions_file = "list_of_permissions.txt"
total_syscall_path = "/home/venkatesh/fyp/github/final_year_project/"    
total_syscall_file = "list_of_syscalls.txt"

#converting text permission to list
with open(permissions_path + permissions_file) as f:
    permissions_list = f.read().splitlines()


#number of permissions in permission list
permissions_list_length = len(permissions_list)

#converting text extracted_syscall to list
with open(total_syscall_path + total_syscall_file) as f:
    total_syscall_list = f.read().splitlines()

#number of extracted_syscall in extracted_syscall list
total_syscall_list_length = len(total_syscall_list)


current_APK = Appln_Path + APK_name

current_static_vector = st.static_feature_vector(permissions_list,permissions_list_length,current_APK)
current_dynamic_vector = dy.dynamic_feature_vector(total_syscall_list,total_syscall_list_length,current_APK,Appln_Path,APK_name)
#current_dynamic_vector = current_static_vector
print("Current Static vector : ")
print(current_static_vector[0])
print("Current Dynamic vector : ")
print(current_dynamic_vector[0])

current_total_vector = np.append(current_static_vector,current_dynamic_vector)

print("Current total vector : ")
print(current_total_vector)
"""

# Split-out validation dataset
#X = fe.final_perm_vector
X = np.loadtxt('permission_vector.csv')
print(X)
#Y = fe.final_binary_class_vector
Y = np.loadtxt('binary_class_vector.csv')
print(Y)


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

#1 evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=2, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring,error_score=np.nan)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
	model.fit(X,Y)




# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()


# Make predictions on validation dataset
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)


print(" \n\n\n\n0 = benignware \n1 = malware")
print("Predicated :" + str(predictions))
print("Expected   :" + str(Y_validation))
print("Accuracy")
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))




