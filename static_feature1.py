import numpy as np
from androguard.core.bytecodes.apk import APK

def static_feature_vector(permissions_list,permissions_list_length,current_APK_path):
    #initialising permission vector
    permissions_vector = np.zeros((1,permissions_list_length),dtype = int)
    current_apk = APK( current_APK_path )
    #extraction current application permissions
    current_apk_permissions = current_apk.get_permissions()
    print (current_apk_permissions)
    
    #generating vector
    for permission in current_apk_permissions:
        print (permission)
        for index,current_permission in enumerate(permissions_list):
            if(current_permission == permission):
                print(index,current_permission)
                permissions_vector[0,index] = 1

    #print(permissions_vector)
    return permissions_vector