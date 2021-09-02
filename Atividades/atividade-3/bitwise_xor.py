import cv2
import numpy as np

class BitwiseXor:

    def __init__(self, path_01, path_02):
        self.image_01 = cv2.imread(path_01)
        self.image_02 = cv2.imread(path_02)

    def hard_code(self):
        print('hard')

    def easy_mode(self):
        result = cv2.bitwise_xor(self.image_01, self.image_02)
        cv2.imwrite('/home/pedro/Dev/PythonProjects/VisaoComputacional/Atividades/atividade-3/results/xor.jpg', result)
        cv2.destroyAllWindows()


def main():
    path_01 = '/home/pedro/Dev/PythonProjects/VisaoComputacional/assets/flower_2.jpg'
    path_02 = '/home/pedro/Dev/PythonProjects/VisaoComputacional/assets/barcode_2.jpg'
    bitwise = BitwiseXor(path_01=path_01, path_02=path_02)
    bitwise.easy_mode()


if __name__ == '__main__':
    main()
