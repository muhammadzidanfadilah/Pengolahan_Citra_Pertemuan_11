import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data, img_as_float
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from skimage.morphology import convex_hull_image, skeletonize
from skimage.util import invert

st.title("Pengolahan Citra")

# Sidebar for selecting the process
process = st.sidebar.selectbox("Select Image Processing Task", 
                               ["Convex Hull", "Skeletonization", "Active Contour"])

# Function to display the convex hull transformation
def show_convex_hull():
    fig, axes = plt.subplots(4, 5, figsize=(20, 20))
    ax = axes.ravel()
    lfw_images = data.lfw_subset()
    for i in range(20):
        ax[i].imshow(lfw_images[90 + i], cmap=plt.cm.gray)
        ax[i].axis("off")
    fig.tight_layout()
    plt.show()

    plt.tight_layout()
    st.pyplot(fig)

# Function to display the skeletonization
def show_skeletonization():
    image = invert(data.horse())
    skeleton = skeletonize(image)
    
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4), sharex=True, sharey=True)
    axes = axes.ravel()
    
    axes[0].imshow(image, cmap=plt.cm.gray)
    axes[0].axis('off')
    axes[0].set_title('Original', fontsize=20)
    
    axes[1].imshow(skeleton, cmap=plt.cm.gray)
    axes[1].axis('off')
    axes[1].set_title('Skeleton', fontsize=20)
    
    fig.tight_layout()
    st.pyplot(fig)

# Function to display the active contour segmentation
def show_active_contour():
    img = data.astronaut()
    img_gray = rgb2gray(img)

    s = np.linspace(0, 2 * np.pi, 400)
    x = 220 + 100 * np.cos(s)
    y = 100 + 100 * np.sin(s)
    init = np.array([x, y]).T

    contour = active_contour(gaussian(img_gray, 3), init, alpha=0.015, beta=10, gamma=0.001)
    
    fig, ax = plt.subplots(1, 2, figsize=(7, 7))

    ax[0].imshow(img)
    ax[0].set_title("Original Image")

    ax[1].imshow(img)
    ax[1].plot(init[:, 0], init[:, 1], '--r', lw=3)
    ax[1].plot(contour[:, 0], contour[:, 1], '-b', lw=3)
    ax[1].set_title("Active Contour Image")

    plt.show()
    st.pyplot(fig)

# Display the selected process
if process == "Convex Hull":
    show_convex_hull()
elif process == "Skeletonization":
    show_skeletonization()
elif process == "Active Contour":
    show_active_contour()