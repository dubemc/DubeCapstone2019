

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #Data Visualization Libraries
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

dimensions = ['Glucose Level', 'Minutes passed', 
                'Carbohydrate Intake', 'Insulin Injected', 
                'Sick?', 'Menstrual Cycle?'
            ]

#Function Defs
def train(model,x,y):
    '''Calls the fit function'''
    model.fit(X_train, y_train)
    return model

def get_input():
    '''This gets user inputs and puts them in a dictionary.  If the user does
    not respond to some of the prompts, there will be an empty string in that
    spot which we will exclude later
    '''
    
    print('''Please respond to the following prompts as best as you can.  If you
          do not know the answer to a question, simply leave it blank''')
    inputs = {}
    #for each possible dimension, we will get input and store it in a dict
    for dim in dimensions:
        inputs[dim] = input(f'Enter your input value for {dim}:')

    return inputs

def make_training_data(inputs, train_data):
    '''loop through dimensions and if there is a value in the inputs dict for 
    that dimension, add it to the list of dimensions we want in our training
    set.
    '''
    #make list to contain dimensions we want to train on
    train_dims = []
    #loop through all possible dimensions
    for dim in dimensions:
        #If the value of the dimension is not an empty string, add it to the list
        if inputs[dim]:
            train_dims.append(dim)
    #extract the relevant columns from the training data
    X = train_data[train_dims]
    Y = train_data['Insulin Injected']
    return train_test_split(X, Y, test_size=0.4, random_state=0)

def evaluate_model(model,test_x, test_y):
    '''Uses the test data to determine the mean squared error for the model'''
    pred = model.predict(test_x)
    return mean_squared_error(test_y, pred)

def make_input_df(inputs):
    '''Makes a dataframe of the input data containing only the columns that the
    user actually entered
    '''
    inputs_no_empties = {}
    #make a dictionary that has all the same vals as the inputs dict but removes
    #and empty keys
    for key in inputs:
        if inputs[key]:
            inputs_no_empties[key] = inputs[key]
    
    return pd.DataFrame([inputs_no_empties])
    
dd = pd.read_csv("~/desktop/DSCData.csv")
dd.head()
dd.info()
dd.describe()
dd['Glucose Level'][0]
#sns.pairplot(dd)
dd.corr()

#------------------------------------------Set data frame size---------------------------------------------------
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.width', None)

#get user input
inputs = get_input()
#split up the training data into a test and training set
X_train, X_test, y_train, y_test = make_training_data(inputs,dd)
#initialize and train the model
n = MLPRegressor(solver='lbfgs', learning_rate='adaptive', max_iter=10000000)
n = train(n,X_train, y_train)
#get the error of the model
error = evaluate_model(n, X_test, y_test)
print(f'model error: {error}')
#predict using the user entered values
input_df = make_input_df(inputs)
prediction = n.predict(input_df)