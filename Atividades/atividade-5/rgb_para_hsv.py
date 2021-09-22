import numpy as np
import cv2

def main():
    image = cv2.imread('/home/pedro/Cloud/github/IFPI-visao-computacional/assets/perfil.jpeg', 1)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-5/results/rgb_hsv.jpg', image)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
