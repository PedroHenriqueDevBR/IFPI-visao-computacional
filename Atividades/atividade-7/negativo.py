import cv2

def main():
    image = cv2.imread('/home/pedro/Cloud/github/IFPI-visao-computacional/assets/perfil.jpeg', 1)
    result = (255-image)
    cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-7/results/invert.jpg', result)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
