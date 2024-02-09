"""Calculate the vector projection give A projected on to B"""

import numpy as np

def calculate_vector_projection(A, B):
  vector_a = np.array(A)
  vector_b = np.array(B)
  scalar_product = np.dot(vector_a, vector_b)
  module = np.linalg.norm(vector_b)
  return scalar_product / module ** 2 * vector_b

calculate_vector_projection([2, 3], [4,1])
print(f"Proyección del vector {[2,3]} en {[4,1]}: {calculate_vector_projection([2, 3], [4, 1])}")