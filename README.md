# perceptron-learning-algorithm
A simple demonstration of how the PLA works.

Packages used: Numpy, Matplotlib.

In this demonstration a 'X' vector is generated randomly. X lenght is n and each element of the vector is a (a,b) tuple. a and b are between 0 and 1.

All (a,b) dots and a 'y = x' boundary line are represented in a 2D plot. The dots above the line are blue colored, the others are red.

![screenshot1](https://github.com/matheuscoradini/perceptron-learning-algorithm/blob/master/images/screenshot1.PNG)

The inputs of the algorithm are the vectors X and y(X), y(X) is the target. The outputs are a weight vector w and the hypothesis h(X), where h(x) = sign(wTx). The PLA compare vector h(X) and y(X) iteratively, and everytime y[i] != h[i] the algorithm tries to improve w, adding the Xy vector: w = w + Xy. In this demonstration, one of the parameters is the attempts_max, that sets the maximum number of iterations. 

After that, our w vector is rotated by 270 degrees, and it represents the new boundary line.

n = 20, attempts_max = 10:
![screenshot2](https://github.com/matheuscoradini/perceptron-learning-algorithm/blob/master/images/screenshot2.PNG)

The more dots we have, more accurate is our w. n = 200, attempts_max = 10:
![screenshot2](https://github.com/matheuscoradini/perceptron-learning-algorithm/blob/master/images/screenshot3.PNG)

