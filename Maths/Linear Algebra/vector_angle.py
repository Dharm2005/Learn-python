import numpy as np

# Use rating
a = np.array([5, 4, 1])
b = np.array([4, 5, 2])
c = np.array([1, 2, 5])

# Finding angle between A and C
dot_product_ab = np.dot(a, b)
cos_theta_ab = dot_product_ab / (np.linalg.norm(a) * np.linalg.norm(b))
angle_ab = np.degrees(np.arccos(cos_theta_ab))

# same for A and C
dot_product_ac = np.dot(a, c)
cos_theta_ac = dot_product_ac / (np.linalg.norm(a) * np.linalg.norm(c))
angle_ac = np.degrees(np.arccos(cos_theta_ac))

print(f"Angle between A and B : {angle_ab:.1f} degrees")
print(f"Angle between A and C : {angle_ac:.1f} degrees")