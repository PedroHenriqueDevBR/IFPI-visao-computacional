import cv2
import numpy as np

class AddImage:

    def __init__(self, path_01, path_02):
        self.image_01 = cv2.imread(path_01)
        self.image_02 = cv2.imread(path_02)

    def easy_mode(self):
        result = cv2.add(self.image_01, self.image_02)
        cv2.imwrite('/home/pedro/Dev/PythonProjects/VisaoComputacional/Atividades/atividade-3/results/add.jpg', result)
        cv2.destroyAllWindows()


def main():
    path_01 = '/home/pedro/Dev/PythonProjects/VisaoComputacional/assets/perfil.jpeg'
    path_02 = '/home/pedro/Dev/PythonProjects/VisaoComputacional/assets/perfil-2.jpeg'
    bitwise = AddImage(path_01=path_01, path_02=path_02)
    bitwise.easy_mode()


if __name__ == '__main__':
    main()
