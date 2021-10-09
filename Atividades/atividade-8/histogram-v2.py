import numpy as np
import cv2
import matplotlib.pyplot as plt

def main():
    image = cv2.imread("/home/pedro/Cloud/github/IFPI-visao-computacional/assets/perfil.jpeg")
    vals = image.mean(axis=2).flatten()
    counts, bins = np.histogram(vals, range(257))
    plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
    plt.xlim([-0.5, 255.5])
    plt.show()


if __name__ == '__main__':
    main()
