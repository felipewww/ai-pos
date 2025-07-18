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

# Resultado:
# O gráfico mostrará os pontos reais e a reta vermelha da regressão linear.
#
# A bolinha verde mostra a previsão para 85m².
#
# O console exibirá algo como:
#
# bash
# Copiar
# Editar
# Preço previsto para 85m²: R$230,00 mil

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dados fictícios
# Tamanho da casa em m²
X = np.array([50, 60, 70, 80, 90, 100]).reshape(-1, 1)
# Preço da casa em milhares
y = np.array([150, 180, 200, 220, 240, 265])

# Criar e treinar o modelo
model = LinearRegression()
model.fit(X, y)

# Fazer uma previsão
tamanho_novo = np.array([[85]])  # 85m²
previsao = model.predict(tamanho_novo)
print(f"Preço previsto para 85m²: R${previsao[0]:,.2f} mil")

# Plotar gráfico
plt.scatter(X, y, color='blue', label='Casas (dados reais)')
plt.plot(X, model.predict(X), color='red', label='Reta da regressão')
plt.scatter(tamanho_novo, previsao, color='green', label='Nova previsão (85m²)')
plt.xlabel('Tamanho da casa (m²)')
plt.ylabel('Preço (mil R$)')
plt.title('Regressão Linear: Tamanho da Casa x Preço')
plt.legend()
plt.grid(True)
plt.show()