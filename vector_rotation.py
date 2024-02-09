""" Calculate the rotation of the vector in 2D using the multiplication operator given angle alpha and the vector"""

def calculate_rotation_vector(vector, alpha):
  rotation = [vector[0] * np.cos(alpha) - vector[1] * np.sin(alpha),
            vector[0] * np.sin(alpha) + vector[1] * np.cos(alpha)]
  return rotation

calculate_rotation_vector(np.array([2, 3]), np.pi / 5)