import os
import numpy as np
from androguard.core.bytecodes.apk import APK

#paths and filenames
benignware_path  = "/home/venkatesh/fyp/Dataset/Malware/ADRD/"
permissions_path = "/home/venkatesh/fyp/github/final_year_project/"
permissions_file = "list_of_permissions.txt"

#converting text permission to list
with open(permissions_path + permissions_file) as f:
    permissions_list = f.read().splitlines()

#number of permissions in permission list
permissions_list_length = len(permissions_list)

#print("Permission List : " + str(permissions_list))
print("Length of permission list : " + str(permissions_list_length))

#sorting list to optimise the matching 
permissions_list.sort()

#number of application in benignware
files_count = len(os.listdir(benignware_path))
print ("Total no. of benignware files : " + str(files_count))

#print("Permission List : " + str(permissions_list))

#initialising permission vector
permissions_vector = np.zeros((files_count,permissions_list_length),dtype = int)
#print(permissions_vector)

# read the entries
with os.scandir(benignware_path) as listOfEntries:  
    for appln_num,entry in enumerate(listOfEntries):
        # Application Number
        print (appln_num)
        if entry.is_file():
            #application file name
            print(entry.name)
            current_apk = APK( benignware_path + entry.name)
            #extraction current application permissions
            current_apk_permissions = current_apk.get_permissions()
            print (current_apk_permissions)
            
            #generating vector
            for permission in current_apk_permissions:
                print (permission)
                for index,current_permission in enumerate(permissions_list):
                    if(current_permission == permission):
                        print(index,current_permission)
                        permissions_vector[appln_num,index] = 1


#finalised vector
print (permissions_vector)


# Check the versions of libraries

# Python version
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

# Load libraries
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
X = permissions_vector
print(X)
np.unique(X)
Y = [0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1]
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
models.append(('KNN', KNeighborsClassifier()))
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
knn = LogisticRegression()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

