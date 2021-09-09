import numpy as np
import cv2

def main():
    image = cv2.imread('/home/pedro/Dev/PythonProjects/VisaoComputacional/assets/perfil.jpeg')
    rows, cols = image.shape[:2] # Importante para definir os eixos da rotação 
 
    eixos_de_entrada = np.float32([[0,0], [cols-1,0], [0,rows-1]])
    eixos_de_saida = np.float32([[cols-1,0], [0,0], [cols-1,rows-1]])
    
    transformacao_matriz_ = cv2.getAffineTransform(eixos_de_entrada , eixos_de_saida) # Transformação da matriz para ser aplicada no warpAffine
    dst = cv2.warpAffine(image, transformacao_matriz_, (cols,rows))
    
    out = cv2.hconcat([image, dst])
    cv2.imwrite('/home/pedro/Dev/PythonProjects/VisaoComputacional/Atividades/atividade-4/results/espelhamento.jpg', out)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
