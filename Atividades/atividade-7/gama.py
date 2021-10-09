import cv2
import numpy as np

def main():
    image = cv2.imread('/home/pedro/Cloud/github/IFPI-visao-computacional/assets/perfil.jpeg', 1)
    gamma = 0.5

    invGamma = 1.0 / gamma
    table = np.array(
        [((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]
    ).astype("uint8")
    result = cv2.LUT(image, table)

    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-7/results/gama.jpg', result)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
