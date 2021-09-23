import numpy as np
import cv2

def main():
    image = cv2.imread('/home/pedro/Cloud/github/IFPI-visao-computacional/assets/perfil.jpeg', 1)
    result_3x3 = cv2.GaussianBlur(image, (3,3), 0)
    result_5x5 = cv2.GaussianBlur(image, (5,5), 0)
    result_11x11 = cv2.GaussianBlur(image, (11,11), 0)
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-6/results/GaussianBlur-3x3.jpg', result_3x3)
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-6/results/GaussianBlur-5x5.jpg', result_5x5)
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-6/results/GaussianBlur-11x11.jpg', result_11x11)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
