"""
Following replaces DecisionTree Classifier() with my own custom one.
MyCLF is a child class of the BaseEstimator.

"""

import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.tree import DecisionTreeClassifier

class MyCLF(BaseEstimator, ClassifierMixin): #Child class

        def __init__(self, mode=0, learning_rate = 0.01): #Constructor - sets some initial values
            self.mode = mode # specific feature of the class, MyCLF

            self.learning_rate = learning_rate # specific feature of the class, MyCLF

            self.clf =  DecisionTreeClassifier(max_depth = 5) #Type of classifier
            if self.mode == 1:
                print("MyCLF() = %s" %(self.clf))

        def fit(self, X, y): #METHOD 1 - like training
            self.clf.fit(X,y)

        def predict(self, X): #METHOD 2 
            return self.clf.predict(X)
        
        def score(self, X, y): #METHOD 3
            return self.clf.score(X,y)
    
"""
Creating an object, the object is -  Classifier

    my_classifier = MyCLF(mode=1)    # Creates a specific classifier, called an instance of the object

Attributes of the Classifier
    my_classifier.mode           # The classifier's mode, kind of like a characteristic of the instance
   my_classifier.learning_rate  # The classifier's learning rate, 

Methods of the Classifier - Method's are like actions the objects can perform
       my_classifier.fit()    # Train the classifier
    my_classifier.predict()  # Make predictions
    
"""