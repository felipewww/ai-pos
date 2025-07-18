# Regressão linear é um modelo estatístico simples usado para prever um valor numérico com base em outro.
#
# 📈 Definição simples:
# A regressão linear busca encontrar uma reta que melhor represente a relação entre uma variável independente (X) e uma variável dependente (Y).
#
# 🔍 Exemplo prático:
# Imagine que você quer prever o preço de uma casa com base no seu tamanho em m².
#
# Entrada (X): tamanho da casa
#
# Saída (Y): preço da casa
#
# A regressão linear tenta ajustar uma equação do tipo:
#
# ini
# Copiar
# Editar
# Y = aX + b
# Onde:
#
# a é o coeficiente angular (inclinação da reta),
#
# b é o coeficiente linear (intercepto com o eixo Y),
#
# Y é o valor que queremos prever (preço),
#
# X é a variável usada como entrada (tamanho da casa).
#
# 📊 Visualmente:
# Se você colocar os dados em um gráfico, a regressão linear desenha uma linha reta que passa o mais próximo possível dos pontos.
#
# 🧠 Para que serve?
# Prever preços, vendas, notas, salários etc.
#
# Entender se há relação entre duas variáveis.
#
# É base para modelos mais complexos (como regressão polinomial ou redes neurais).
#
# ✅ Vantagens:
# Fácil de entender e implementar.
#
# Bom desempenho em problemas simples.
#
# ⚠️ Limitações:
# Só funciona bem quando a relação entre X e Y é aproximadamente linear.
#
# Sensível a outliers (valores fora do padrão).

from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

model = LinearRegression().fit(X, y)
print(model.coef_)