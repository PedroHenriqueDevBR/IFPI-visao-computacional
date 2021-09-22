import numpy as np
import cv2

def main():
    image = cv2.imread('/home/pedro/Cloud/github/IFPI-visao-computacional/assets/perfil.jpeg', 1)
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-5/results/colorida.jpg', image)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
