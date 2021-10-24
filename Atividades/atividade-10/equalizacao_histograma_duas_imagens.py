import numpy as np
import matplotlib.pyplot as plt 
import cv2


class EqualizarHistogramaDuasImagens:

    def criar_histograma(self, imagem):
        self.imagem = cv2.imread("/home/pedro/Cloud/github/IFPI-visao-computacional/assets/{}".format(imagem), 0)
        self.histograma = self._criar_histograma()
        self.histograma = self._contar_valores(self.histograma, self.imagem)
        self.numero_pixels = self.imagem.shape[0] * self.imagem.shape[1]
        self.probabilidade = self._calcular_probabilidade_do_histograma(self.histograma, self.numero_pixels)
        self.valor_acumulado = self._calcular_probabilidade_acumulada(self.probabilidade)
        self.valores_de_cinza = self._calcular_novos_valores_de_cinza(self.valor_acumulado)
        return self.valores_de_cinza

    def aplicar_equalizacao(self, imagem, valores_de_cinza):
        self.imagem = cv2.imread("/home/pedro/Cloud/github/IFPI-visao-computacional/assets/{}".format(imagem), 0)
        return self._equalizar_histograma(self.imagem, valores_de_cinza)

    def compara_os_histogramas(self, hist_01, hist_02):
        resultado = {}
        for pos_1 in range(len(hist_01.values())):
            posicao_menor_valor = 0
            menor_valor = hist_02['0']
            for pos_2 in range(len(hist_02.values())):
                if abs(hist_01[str(pos_1)] - hist_02[str(pos_2)]) < menor_valor:
                    posicao_menor_valor = pos_2
                    menor_valor = abs(hist_01[str(pos_1)] - hist_02[str(pos_2)])
            resultado[str(pos_1)] = hist_02[str(posicao_menor_valor)] - 1
        return resultado

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
        valor_acumulado = {}
        soma_probabilidade = 0
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

    def salvar_imagem(self, nome_do_arquivo, imagem):
        cv2.namedWindow('window')
        cv2.imwrite('/home/pedro/Cloud/github/IFPI-visao-computacional/Atividades/atividade-10/results/{}.jpg'.format(nome_do_arquivo), imagem)
        cv2.waitKey()
        cv2.destroyWindow('window')


def main():
    equalizador = EqualizarHistogramaDuasImagens()

    histograma_entrada = equalizador.criar_histograma('teste.jpg')
    histograma_referencia = equalizador.criar_histograma('keyboard.jpg')

    resultado = equalizador.compara_os_histogramas(histograma_entrada, histograma_referencia)
    imagem_equalizada = equalizador.aplicar_equalizacao('teste.jpg', resultado)
    equalizador.salvar_imagem('test', imagem_equalizada)

    # equalizador.mostrar_histograma_atual(resultado)


if __name__ == '__main__':
    main()