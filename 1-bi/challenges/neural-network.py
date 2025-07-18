import tensorflow as tf #para criar e treinar a rede neural.
import numpy as np

# Cada linha representa uma casa | Colunas: [tamanho_m2, quartos, idade_anos]
# X: matriz com 100 amostras e 3 características
# X = np.random.random((100, 3))
X = np.array([
    [70, 2, 10],
    [50, 1, 20],
    [120, 3, 5],
    [100, 3, 15],
    [60, 2, 30],
    [80, 2, 8],
    [90, 3, 12],
    [40, 1, 35],
    [110, 4, 7],
    [55, 2, 25]
])

# Preços em milhares de reais (R$)
# y: vetor de saída com 100 valores
# y = np.random.random((100, 1))
y = np.array([
    [350],
    [250],
    [600],
    [520],
    [300],
    [400],
    [480],
    [220],
    [620],
    [270]
])

# Definindo o modelo usando Input
inputs = tf.keras.Input(shape=(3,))
x = tf.keras.layers.Dense(10, activation='relu')(inputs)
outputs = tf.keras.layers.Dense(1)(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Compilando o modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Treinando o modelo
model.fit(X, y, epochs=5)