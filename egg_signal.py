import numpy as np
def EGG_SIGNAL(matriz):
 signal  = matriz - np.mean(matriz)
 return signal

#  para efeitos de teste
matriz_original = np.random.randn(2,2)
print(matriz_original,"matriz\n")
media_matriz_original = np.mean(matriz_original)
print(media_matriz_original,"média\n")
matriz_EGG = EGG_SIGNAL(matriz_original)
print(matriz_EGG,"resultado final")