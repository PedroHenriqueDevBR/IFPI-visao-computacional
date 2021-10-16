import numpy as np
import matplotlib.pyplot as plt 
import cv2


class EqualizarHistograma:

    def __init__(self):
        self.imagem = cv2.imread("/home/pedro/Cloud/github/IFPI-visao-computacional/assets/perfil.jpeg", 0)

    def calcular_histograma(self):
        self.histograma = self._criar_histograma()
        self.histograma = self._contar_valores(self.histograma, self.imagem)

    def aplicar_equalizacao(self):
        self.numero_pixels = self.imagem.shape[0] * self.imagem.shape[1]
        self.probabilidade = self._calcular_probabilidade_do_histograma(self.histograma, self.numero_pixels)
        self.valor_acumulado = self._calcular_probabilidade_acumulada(self.probabilidade)
        self.valores_de_cinza = self._calcular_novos_valores_de_cinza(self.valor_acumulado)
        self.imagem = self._equalizar_histograma(self.imagem, self.valores_de_cinza)

    def _criar_histograma(self):
        result = {}
        for i in range(0,256):
            result[str(i)] = 0
        return result

    def _contar_valores(self, histograma, imagem):
        for pos_linha in range(len(imagem)):
            for pos_coluna in range(len(imagem[pos_linha])):
                histograma[str(imagem[pos_linha][pos_coluna])] += 1
        return histograma

    def _calcular_probabilidade_do_histograma(self, histograma, numero_pixels):
        probabilidade = {}
        for i in range(0, 256):
            probabilidade[str(i)] = histograma[str(i)] / numero_pixels
        return probabilidade

    def _calcular_probabilidade_acumulada(self, probabilidade):
        soma_probabilidade = 0
        valor_acumulado = {}
        for i in range(0, 256):
            if i == 0:
                pass
            else:
                soma_probabilidade += probabilidade[str(i - 1)]
            valor_acumulado[str(i)] = probabilidade[str(i)] + soma_probabilidade
        return valor_acumulado

    def _calcular_novos_valores_de_cinza(self, valor_acumulado):
        valores_de_cinza = {}
        for i in range(0, 256):
            valores_de_cinza[str(i)] = np.ceil(valor_acumulado[str(i)] * 255)
        return valores_de_cinza

    def _equalizar_histograma(self, imagem, valores_de_cinza):
        for row in range(imagem.shape[0]):
            for column in range(imagem.shape[1]):
                imagem[row][column] = valores_de_cinza[str(int(imagem[row] [column]))]
        return imagem

    def mostrar_histograma_atual(self, dados):
        plt.bar(dados.keys(), dados.values())
        plt.xlabel("Níveis intensidade")
        ax = plt.gca()
        ax.axes.xaxis.set_ticks([])
        plt.grid(True)
        plt.show()

    def salvar_imagem_atual(self, nome_do_arquivo):
        cv2.namedWindow('window')
        cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-9/results/{}.jpg'.format(nome_do_arquivo), self.imagem)
        cv2.waitKey()
        cv2.destroyWindow('window')


def main():
    histograma = EqualizarHistograma()
    histograma.calcular_histograma()
    histograma.aplicar_equalizacao()
    histograma.salvar_imagem_atual('normalizar')


if __name__ == '__main__':
    main()