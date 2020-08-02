'''
from sklearn.datasets import load_boston
boston = load_boston()
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(boston.data,boston.target,random_state = 22, train_size=0.7)
lr = LinearRegression().fit(X_train,y_train)
print("training Accuracy: {:.2f}".format(lr.score(X_train,y_train)))
print("test accuracy: {:.2f}".format(lr.score(X_test,y_test)))

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
print(lr)
print(lr.coef_)
print(lr.intercept_)
y_pred = lr.predict(X_test)
print(y_pred)
print()


print((y_test==y_pred).sum()/len(y_test))
print(boston["data"])

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
myData = pd.read_csv('C:/Users/madhu/PycharmProjects/Test/salary.csv')
print(myData)
X_train, X_test, y_train, y_test = train_test_split(myData[['Age', 'Experience']], myData['Salaryy'], random_state=22, train_size=0.5)
lr = LinearRegression().fit(X_train, y_train)
print("training accuracy : {:.2f}".format(lr.score(X_train, y_train)))
print("test accuracy : {:.2f}".format(lr.score(X_test, y_test)))
'''
import math

import pandas as pd
temp_d = {'X1':[4,2,11,3,7], 'X2':[3,5,4,2,4], 'X3':[8,9,7,8,5], 'X4':[7,3,6,1,2], 'X5':[6,1,5,9,6], 'Y':[1,0,0,1,1]}
temp_d = [[4,2,11,3,7],[3,5,4,2,4],[8,9,7,8,5],[7,3,6,1,2],[6,1,5,9,6],[1,0,0,1,1]]
df = pd.DataFrame(temp_d, columns = ['X1','X2','X3','X4','X5','Y'])
df = pd.DataFrame(temp_d)
def euclidean_Distance(r1,r2):
    d = 0.0
    for i in range(0,len(r1) -1): # I don't want to consider the value for Column Y
        d += math.pow(r1[i] - r2[i],2) # d = d + (X1-x1)^2 +(X2-x2)^2 + (X3-x3)^2...+(X5-x4)^2
    return math.sqrt(d)

def nearest_neighbors(train_data, test_row, k):
    dist = list()

    for tr in train_data:
        d = euclidean_Distance(tr,test_row)
        dist.append((tr,d))

    dist.sort(key = lambda t: t[1]) #sorting the list on the basis of distance. (<row>,dist)
    neighbors = list()
    for i in range(k):
        neighbors.append(dist[i][0])
    return neighbors


test_row = [3,10,5,9,6]
nearest_neighbors(df,test_row,3)


from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify=cancer.target, random_state= 21 , train_size= 0.7)

training_accuracy = []
test_accuracy = []
# try n_neighbors from 1 to 10
neighbors_settings = range(1, 11)

for n in neighbors_settings:
    # build the model
    clf = KNeighborsClassifier(n_neighbors=n)
    clf.fit(X_train, y_train)
    # record training set accuracy
    training_accuracy.append(clf.score(X_train, y_train))
    # record generalization accuracy
    test_accuracy.append(clf.score(X_test, y_test))

plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.show()
