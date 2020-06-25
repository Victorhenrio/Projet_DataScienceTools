# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:51:11 2020

@author: Alex le BOSS du Game
"""

import fonction_traitement as trait
import actors_labelisation as act
import pandas as pd
import statistics 
import API as api
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn import preprocessing
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.linear_model import LinearRegression,LogisticRegression


movie_ratings = pd.read_csv(r'Data_csv\movie_ratings_full.csv')

movie_ratings = trait.clean_dataframe(movie_ratings)

movie_ratings = movie_ratings.drop(["stars1"],axis=1)
movie_ratings = movie_ratings.drop(["stars2"],axis=1)
movie_ratings = movie_ratings.drop(["stars3"],axis=1)
movie_ratings = movie_ratings.drop(["metascore"],axis=1)
movie_ratings = movie_ratings.drop(["win"],axis=1)
movie_ratings = movie_ratings.drop(["nom"],axis=1)

print(movie_ratings.info())


#%%

#model = KNeighborsClassifier()
#model = LinearSVC(random_state=0, max_iter=500)
model = LinearRegression()

X = movie_ratings.drop(["imdb_ratings"],axis=1)
y = movie_ratings['imdb_ratings']

lab_enc = preprocessing.LabelEncoder()
y_enc = lab_enc.fit_transform(y)

model.fit(X, y_enc) # entrainement du modele
print(model.score(X, y_enc)) # évaluation

"""
Add algo qui sélectionne les features qui influent le +
"""

def deter(model,votes=305000, genre1=0,genre2=1,genre3=2,
           nb_oscar=0,runtime=123,budget=125000000,gross=546000000):
  x = np.array([votes, genre1, genre2,genre3,nb_oscar,
                runtime,budget,gross]).reshape(1, 8)
  print("Prédiction : ")
  print(model.predict(x))
  #print(model.predict_proba(x))

deter(model)

#%%

#model = KNeighborsClassifier()
#model = LinearSVC(random_state=0, max_iter=500)
model = LinearRegression()

X = movie_ratings.drop(["runtime"],axis=1)
y = movie_ratings['runtime']

lab_enc = preprocessing.LabelEncoder()
y_enc = lab_enc.fit_transform(y)

model.fit(X, y_enc) # entrainement du modele
print(model.score(X, y_enc)) # évaluation

"""
Add algo qui sélectionne les features qui influent le +
"""

def deter(model,imdb_ratings=8,votes=305000, genre1=0,genre2=1,genre3=2,
           nb_oscar=0,budget=125000000,gross=546000000):
  x = np.array([imdb_ratings,votes, genre1, genre2,genre3,nb_oscar,
             budget,gross]).reshape(1, 8)
  print("Prédiction : ")
  print(model.predict(x))
  #print(model.predict_proba(x))


deter(model)

#%%

chi2(X, y_enc)

selector = SelectKBest(f_classif, k=4)
print(selector.fit(X, y_enc))
print(selector.scores_)

print(np.array(movie_ratings.feature_names)[selector.get_support()])

#%%

budgets = []
"""
genre = "Drama"
filter = movie_ratings["genres1"] == genre
moy_genre = movie_ratings['budget'].where(filter, inplace = True) 
"""
i = 0 
ref = 'Drama'
for c in movie_ratings["genres1"]:
    genre = c
    if genre == ref:
        budgets.append(movie_ratings['budget'][i])
    i += 1
    
print(budgets_propre)
moy_genre = statistics.mean(budgets_propre)
print(moy_genre)

#print(movie_ratings.info())