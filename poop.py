import tensorflow as tf
import numpy as np

A = tf.constant([[0,0,0],[0,0,0], [0,0,0]]) # A is now [[1,2], [3,4]]

print(A.get_shape())

matrix = np.array([[1, 2, 3], [4, 5, 6]])
tf.tensor(matrix)

tf.constant(matrix)


