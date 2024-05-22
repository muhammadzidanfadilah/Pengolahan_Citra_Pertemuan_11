# Tugas Pengolahan Citra Pertemuan 11

```
Nama  : Muhammad Zidan Fadillah
Nim   : 312210277
Kelas : TI.22.A.2
Mata Kuliah : Pengolahan Citra
```

# Convex hull
# input
```
import matplotlib.pyplot as plt

from skimage.morphology import convex_hull_image
from skimage import data, img_as_float
from skimage.util import invert

image = invert(data.lfw_subset())

chull = convex_hull_image(image)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
ax = axes.ravel()

ax[1].set_title('Transformed picture')
ax[1].imshow(chull, cmap=plt.cm.gray)
ax[1].set_axis_off()

plt.tight_layout()
plt.show()
```

# Output
![convex](https://github.com/muhammadzidanfadilah/Pengolahan_Citra_Pertemuan_11/assets/115553474/2e3c1d90-b6f0-4b4a-a67a-bebabc787de0)

# Menggunakan Skeletonize(image)

# Horse

# Input 
```
from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert

image = invert(data.horse())

skeleton = skeletonize(image)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
                         sharex=True, sharey=True)

ax = axes.ravel()
ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].axis('off')
ax[0].set_title('original', fontsize=20)

ax[1].imshow(skeleton, cmap=plt.cm.gray)
ax[1].axis('off')
ax[1].set_title('skeleton', fontsize=20)

fig.tight_layout()
```
# Output
![Kuda](https://github.com/muhammadzidanfadilah/Pengolahan_Citra_Pertemuan_11/assets/115553474/92aec015-f52f-45c7-96e3-515931a5b4bb)


# Moon
# Input
```
from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert

image = invert(data.moon())

skeleton = skeletonize(image)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
                         sharex=True, sharey=True)

ax = axes.ravel()
ax[0].imshow(image, cmap=pit.cm.gray)
ax[0].axis('off')
ax[0].set_title('original', fontsize=20)

ax[1].imshow(skeleton, cmap=pit.cm.gray)
ax[1].axis('off')
ax[1].set_title('skeleton', fontsize=20)

fig.tight_layout()
```
# Output
![bulan](https://github.com/muhammadzidanfadilah/Pengolahan_Citra_Pertemuan_11/assets/115553474/91987510-01d9-4d07-b5a6-618922c35de1)




# Menggunakan Activate Contour
# Astronaut
# Input

```
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour

img = data.astronaut()

s = np.linspace(0, 2*np.pi, 400)
x = 220 + 100*np.cos(s)
y = 100 + 100*np.sin(s)
init = np.array([x, y]).T

cntr = active_contour(gaussian(img, 3),init,alpha=0.015, beta=10, gamma=0.001)
fig, ax = plt.subplots(1, 2, figsize=(7, 7))
ax[0].imshow(img, cmap=pit.cm.gray)
ax[0].set_title("Original Image")

ax[1].imshow(img, cmap=pit.cm.gray)
ax[1].plot(init[:, 0], init[:, 1], '--r', lw=3)
ax[1].plot(cntr[:, 0], cntr[:, 1], '-b', lw=3)
ax[1].set_title("Active Contour Image")
```

# Output
![astronaut](https://github.com/muhammadzidanfadilah/Pengolahan_Citra_Pertemuan_11/assets/115553474/379c64b5-0c75-4be8-974c-618127fdf1b8)

# Cat
# Input
```
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour

img = data.cat()

s = np.linspace(0, 2*np.pi, 400)
x = 220 + 100*np.cos(s)
y = 100 + 100*np.sin(s)
init = np.array([x, y]).T

cntr = active_contour(gaussian(img, 3),init,alpha=0.015, beta=10, gamma=0.001)
fig, ax = plt.subplots(1, 2, figsize=(7, 7))
ax[0].imshow(img, cmap=pit.cm.gray)
ax[0].set_title("Original Image")

ax[1].imshow(img, cmap=pit.cm.gray)
ax[1].plot(init[:, 0], init[:, 1], '--r', lw=3)
ax[1].plot(cntr[:, 0], cntr[:, 1], '-b', lw=3)
ax[1].set_title("Active Contour Image")
```

# Output
![kucing](https://github.com/muhammadzidanfadilah/Pengolahan_Citra_Pertemuan_11/assets/115553474/0dd52a2d-6221-411f-923b-e6616055d586)
