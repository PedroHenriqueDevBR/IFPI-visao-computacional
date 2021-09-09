import numpy as np
import cv2

def main():
    image = cv2.imread('/home/pedro/Dev/PythonProjects/VisaoComputacional/assets/perfil.jpeg')
    rows, cols = image.shape[:2] # Importante para definir os eixos da rotação 
 
    transformacao_matriz_ = np.float32([[1,0,100] , [0,1,50]]) # Transformação da matriz para ser aplicada no warpAffine
    dst = cv2.warpAffine(image, transformacao_matriz_, (cols,rows))

    cv2.imwrite('/home/pedro/Dev/PythonProjects/VisaoComputacional/Atividades/atividade-4/results/translacao.jpg', dst)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
