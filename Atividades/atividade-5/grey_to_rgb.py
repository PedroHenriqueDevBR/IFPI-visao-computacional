import numpy as np
import cv2

def main():
    image = cv2.imread('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-5/results/test.jpg', 1)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-5/results/test.jpg', image)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
