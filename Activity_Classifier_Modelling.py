import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import confusion_matrix


# loading already pickled data
def load_data():
    file=open('har_data.pkl','rb')
    data=pickle.load(file)
    file.close()
    return data

# color legend and activity set
def legend():
    d={}
    d[1]='cyan'
    d[2]='red'
    d[3]='yellow'
    d[4]='blue'
    d[5]='green'
    d[6]='purple'
    
    k={}
    file='UCI HAR Dataset/activity_labels.txt'
    a=pd.read_csv(file,header=None)
    for i in range(a.shape[0]):
        t=a.iloc[i]
        t=t[0]
        t=t.split()
        x,y=t
        x=int(x)
        k[x]=y
        
    return d,k

# function to normalise data
def standardise(X_train,X_test):
    ss=StandardScaler().fit(X_train)
    X_train=ss.transform(X_train)
    X_test=ss.transform(X_test)
    return X_train,X_test

# function to reduce dimensions of data
def reduce_pca(X_train,X_test,comp):
    X_train,X_test=standardise(X_train,X_test)
    model=PCA(n_components=comp,whiten=True)
    X_train=model.fit_transform(X_train)
    X_test=model.transform(X_test)
    return X_train,X_test

# function to plot data 
def visualize(X_train,y_train):
    key,activity=legend()
    
    label_list=[]
    for i in range(1,7):
        x=mpatches.Patch(color=key[i], label=activity[i])
        label_list.append(x)
    
    for i in range(X_train.shape[0]):
        plt.scatter(X_train[i][1], X_train[i][0] , color=key[y_train[i]])
        
    plt.legend(handles=label_list)
    plt.show()

# function to create training set and development set
def train_dev_set(X_train,y_train):
    return train_test_split(X_train,y_train,test_size=0.3,random_state=0)

# function to create classifier
def svm_fit(X,y,classification_type):
    model = svm.SVC(decision_function_shape= classification_type,kernel='linear')
    model.fit(X,y)
    e=model.score(X,y)
    return model,e

# function to computer mis-classification error
def error(model,X,y):
    e=model.score(X,y)
    return e
    
# function to assemble pipeline
def run_model(X_train,y_train,X_test,y_test,features):
    # normalising data
    X_train,X_test=standardise(X_train,X_test)
    # dimension reduction
    X_train,X_test=reduce_pca(X_train,X_test,features)
    # splitting into training  and development set
    X_train,X_dev,y_train,y_dev=train_dev_set(X_train,y_train)
    # building model
    model,e_train=svm_fit(X_train,y_train,'ovo')
    e_dev=error(model,X_dev,y_dev)
    e_test=error(model,X_test,y_test)
    
    print('Training accuracy=',e_train)
    print('Development accuracy=',e_dev)
    print('Testing accuracy=',e_test)
    
    cm=confusion_matrix(y_test,model.predict(X_test))
    return model,cm


if __name__=='__main__':

    data=load_data()
    
    X_train=data['X_train']
    X_test=data['X_test']
    y_train=data['y_train']
    y_test=data['y_test']
    y_train=np.ravel(y_train)
    y_test=np.ravel(y_test)
    
    X_tr,X_t=reduce_pca(X_train,X_test,2)
    visualize(X_tr,y_train)
    
    model,cm=run_model(X_train,y_train,X_test,y_test,220)
    
