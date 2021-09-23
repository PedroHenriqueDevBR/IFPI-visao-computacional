import numpy as np
import cv2

def main():
    image = cv2.imread('/home/pedro/Cloud/github/IFPI-visao-computacional/assets/perfil.jpeg', 1)
    result_3x3 = cv2.medianBlur(image, 3)
    result_5x5 = cv2.medianBlur(image, 5)
    result_11x11 = cv2.medianBlur(image, 11)
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-6/results/medianBlur-3x3.jpg', result_3x3)
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-6/results/medianBlur-5x5.jpg', result_5x5)
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-6/results/medianBlur-11x11.jpg', result_11x11)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
