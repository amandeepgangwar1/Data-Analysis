import numpy as np

a = np.array([1, 3, 4])
print(type(a))

b = np.zeros(5)
c = np.ones(3)
d = np.arange(1, 6)

print(b)
print(c)
print(d)


# Vectorized operations

print(a + 10)
print(a * 10)
print(a < 1)