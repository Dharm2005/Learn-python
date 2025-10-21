import numpy as np

rng = np.random.default_rng()

all_faces = np.array(['🐺','🐨','🦊','🐯','🦁','🦝','🐹','🐼','🐻','🦄'])

faces = rng.choice(all_faces,size=(3,3))

print(faces)