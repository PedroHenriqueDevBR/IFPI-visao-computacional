import numpy as np
import cv2

def main():
    image = cv2.imread('/home/pedro/Dev/PythonProjects/VisaoComputacional/assets/perfil.jpeg')
    resize = cv2.resize(image, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_CUBIC)

    cv2.imwrite('/home/pedro/Dev/PythonProjects/VisaoComputacional/Atividades/atividade-4/results/escala.jpg', resize)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
