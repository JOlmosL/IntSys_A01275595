import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import csv

#####Gobal Variables
Path = "../ds/"
#####

def main():
    columns = col_names()
    print("Available columns are: \n[ID][Column Name]")
    for i in range(len(columns)):
        print("[", i , "][" + columns[i]+"]")
    df = pd.read_csv(Path + 'SkillCraft_Ds.csv', usecols=columns)

    idX = int(input("Column to be Xs (Use IDs): "))     #Assigning specific IDs for specific columns
    idY = int(input("Column to be Ys (Use IDs): "))

    colNameX = columns[idX]     #Assigning column names based on IDs
    colNameY = columns[idY]

    X = df[colNameX]    #Assigning Xs and Ys datas
    Y = df[colNameY]
    
    print(X.shape)  #See size or # of elements
    print(Y.shape)

    test_per = float(input(" % of Data to be used in testing: "))
    test_per = test_per / 100
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = test_per) #The remaining of the test_per will go towards training set
    
    print(X_train.shape)  #See size of training elements
    print(Y_train.shape)
    print(X_test.shape)  #See size of testing elements
    print(Y_test.shape)

    model = linear_model.LinearRegression()
    model.fit(X_train, X_test)  #Defining the input for the model building

    #Y_pred = model.predict(X_test)
#
    ##Seing how the model performance 8:12
    #print("Coefficients: ", model.coef_)
    #print("Intercept: ", model.intercept_)
    #print("Mean Squared Error (MSE): %.2f" % mean_squared_error(Y_test, Y_pred))
    #print("Coefficient of Determination (R^2): %.2f" % r2_score(Y_test, Y_pred))    

    
def col_names():
    with open(Path + 'SkillCraft_Ds.csv') as raw_data:   #Getting Column names
        csv_reader = csv.reader(raw_data, delimiter = ',')
        headers = []
        for row in csv_reader:
            headers.append(row)
            break
    return headers[0]

if __name__ == "__main__":
    main()