# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

# Parameters:
n = 200 #number of points
attempts_max = 10 # max number of attempts

y = []
w = np.array([0,0]) # weights vector

# Defining random vector X.
a = np.random.rand(n)
b = np.random.rand(n)
X = np.array(list(zip(a,b)))

# Defining answer vector y
for i in range(n):
  if X[i][0] > X[i][1]: 
      y.append(1) 
  else: 
      y.append(-1)

def plot(X, y, w): # function that plots the points and the boundary line

  rotation_matrix = np.array([[0,-1],[1,0]]) # 270 degrees clockwise rotation matrix
  w_r = np.dot(rotation_matrix, w)*10 # rotated vector w multiplied by 10
  
  plt.figure(figsize = (11,6))
  for i in range(n):
      if y[i] == 1:
          plt.scatter(X[i][0], X[i][1], c = 'b' ) # blue if the point is above the line
      if y[i] == -1:
          plt.scatter(X[i][0], X[i][1], c = 'r') # red if the point is below the line
  plt.xlim(0,1)
  plt.ylim(0,1)
  plt.plot([0,1], [0,1])
  plt.plot([0,w_r[0]],[0,w_r[1]]) # plots rotated w
  plt.show()

# plot the points using vector y and initial w as parameters.
plot(X, y, w)

attempt, errors = 0, []

while attempt < attempts_max: # execute the iteration until the max number of attempts.
  h = []
  errors_count = 0
  for i in range(n):
      h.append(np.sign(np.dot(w.T, X[i])))
      if h[i] != y[i]:
          w = w + X[i]*y[i] # PLA
          errors_count += 1

  errors.append(errors_count)
  attempt += 1

# plot the points using vector h and new w as parameters.
# orange line means the rotated vector w, the boundary line.
plot(X, h, w)

plt.figure(figsize = (11,6))
plt.plot(np.arange((len(errors))),errors)
plt.xlabel('Attempts')
plt.ylabel('Errors')
plt.title('Number of erros by attempt')
plt.show()

# new sample, using the same weights vector w

a2 = np.random.rand(n)
b2 = np.random.rand(n)
X2 = np.array(list(zip(a2,b2)))
h2 = []
for i in range(n):
    h2.append(np.sign(np.dot(w.T, X2[i])))

plot(X2, h2, w)

