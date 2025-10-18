import numpy as np

array = np.array([
  [['A','B','C'], ['D','E','F'], ['G','H','I']],
  [['J','K','L'], ['M','N','O'], ['P','Q','R']],
  [['S','T','U'], ['V','W','X'], ['Y','Z','_']]
])

word1 = array[0,0,0] + array[0,0,1] + array[2,0,0]
word2 = array[0,0,2] + array[0,0,0] + array[2,0,1]
word3 = array[0,1,2] + array[1,1,2] + array[2,1,2]

print(word1)
print(word2)
print(word3)