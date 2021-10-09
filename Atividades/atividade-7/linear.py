import cv2
import numpy as np

def main():
    image = cv2.imread('/home/pedro/Cloud/github/IFPI-visao-computacional/assets/perfil.jpeg', 1)
    gamma = 0.5

    normalizedImg = np.zeros((800, 800))
    result = cv2.normalize(image,  normalizedImg, 0, 255, cv2.NORM_MINMAX)

    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-7/results/normalizar.jpg', result)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()