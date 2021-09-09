import numpy as np
import cv2

def main():
    image = cv2.imread('/home/pedro/Dev/PythonProjects/VisaoComputacional/assets/perfil.jpeg')
    rows, cols = image.shape[:2] # Importante para definir os eixos da rotação 
 
    transformacao_matriz_ = cv2.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 45, 0.70)
    dst = cv2.warpAffine(image, transformacao_matriz_, (cols,rows))

    cv2.imwrite('/home/pedro/Dev/PythonProjects/VisaoComputacional/Atividades/atividade-4/results/rotacao.jpg', dst)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
