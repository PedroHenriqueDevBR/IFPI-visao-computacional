import numpy as np
import cv2

def main():
    image = cv2.imread('/home/pedro/Cloud/github/IFPI-visao-computacional/assets/rgb.jpg', 1)
    chanels = cv2.split(image)
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-5/results/ch-blue.jpg', chanels[0])
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-5/results/ch-green.jpg', chanels[1])
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-5/results/ch-red.jpg', chanels[2])
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
