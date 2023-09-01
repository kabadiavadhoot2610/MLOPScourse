from sklearn.model_selection import train_test_split
from sklearn import svm,datasets
#We will put all utils here

def read_digits():
    digits = datasets.load_digits()
    X = digits.images
    y = digits.target
    return X,y

def preprocess_data(data):
    # flatten the images
    n_samples = len(data)
    data = data.reshape((n_samples, -1))
    return data

#Splitting the data
def split_data(x,y,test_size,random_state = 1):
    X_train , X_test, y_train ,y_test = train_test_split(x,y,test_size=0.3,shuffle=False,random_state=random_state)
    return X_train,X_test,y_train,y_test

#Model training
def train_model(x,y,model_params,model_type="svm"):
    if model_type == "svm":
        clf = svm.SVC
    model = clf(**model_params)
    model.fit(x,y)
    return model

def train_test_dev_split(x,y,test_size,random_state=1):
    X_main,X_test,y_main,y_test = train_test_split(x,y,test_size=100,stratify=y) 
    X_train,x_dev,y_train, y_dev = train_test_split(X_main,y_main,test_size=100)
    return X_train,X_test,y_train,y_test,x_dev,y_dev


    