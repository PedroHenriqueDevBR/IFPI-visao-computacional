import numpy as np
import cv2
import matplotlib.pyplot as plt

def main():
    image = cv2.imread("/home/pedro/Cloud/github/IFPI-visao-computacional/assets/perfil.jpeg")
    bits = np.zeros(256, np.int32)
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            intensity = 0
            for k in range(0, len(image[i][j])):
                intensity += image[i][j][k]
            bits[intensity/3] += 1

    counts, bins = np.histogram(bits, range(257))
    plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
    plt.xlim([-0.5, 255.5])
    plt.show()


if __name__ == '__main__':
    main()
