## Regressão linear (simples / múltipla)

É uma ferramenta para ***testar hipóteses e verificar tendências*** que achamos com base na experiência ou intuição.
Você tem uma suspeita empírica:

> - Simples: testa “X influencia Y?”
> - Múltipla: testa “X₁, X₂, X₃... influenciam Y?”

> "Acho que quanto mais eu invisto em anúncios, mais eu vendo."

A regressão linear vai verificar essa relação nos dados e dizer, por exemplo:

- Se existe uma tendência clara (positiva ou negativa)
- Se a relação é forte ou fraca
- Qual é o “peso” (impacto) da variável explicativa (investimento) sobre a variável resposta (vendas)

### Um exemplo fora do marketing

> "Acho que quem dorme mais tem melhor desempenho nas provas."

Você pode usar regressão linear para testar essa hipótese com dados de alunos.

Ela não diz que dormir mais causa notas melhores, mas mostra se há uma tendência nos dados que indica isso.


## 📌 Métricas

| **Métrica**          | **O que mede**                                     | **Interpretação**                                                                                             | **Bom quando...**                        |
| -------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **R²**               | Proporção da variação de Y explicada por X         | Varia de 0 a 1. Quanto mais próximo de 1, melhor.                                                             | Está perto de 1                          |
| **R² ajustado**      | Igual ao R², mas penaliza excesso de variáveis     | Ideal em regressão múltipla. Se R² aumenta mas ajustado cai, a nova variável não ajuda.                       | É alto e próximo do R²                   |
| **p-valor**          | Significância estatística dos coeficientes         | Se < 0.05, a variável é relevante. Se > 0.05, pode ser ruído.                                                 | Está abaixo de 0.05                      |
| **Coeficientes (β)** | Impacto de cada variável sobre o resultado         | Mostra quanto Y varia quando X varia 1 unidade. Ex: β = 2 → a cada 1 real investido, vendas sobem 2 unidades. | Têm valor significativo e p-valor < 0.05 |
| **MAE**              | Erro médio absoluto                                | Média das diferenças absolutas entre previsão e real. Menos sensível a outliers.                              | É baixo                                  |
| **MSE**              | Erro quadrático médio                              | Erro médio, mas penaliza mais erros grandes (por elevar ao quadrado).                                         | É baixo                                  |
| **RMSE**             | Raiz quadrada do MSE (mesma unidade da variável Y) | Mais fácil de interpretar que o MSE.                                                                          | É baixo                                  |


## Como avaliar MAE, MSE e RMSE

Após treinar um modelo e executá-lo, é necessário extrair informações das métricas para
verificar o quanto o modelo está bom

```
# Fazendo previsões no conjunto de teste
previsoes = modelo.predict(X_test)

erro_medio_quadratico = mean_squared_error(y_test, previsoes)
erro_absoluto_medio = mean_absolute_error(y_test, previsoes)
r_quadrado = r2_score(y_test, previsoes)
```

| Métrica                         | O que significa ser "baixo"?                                                                                                                                                                                                                                          |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MAE** (erro absoluto médio)   | A média dos erros está **próxima de zero**. Ex: se você está prevendo vendas em R\$, um MAE de 5 significa que, em média, erra R\$5. Se suas vendas giram em torno de R\$10, isso é **muito alto**. Se suas vendas giram em torno de R\$5.000, isso é **baixíssimo**. |
| **MSE** (erro quadrático médio) | Como ele eleva os erros ao quadrado, **penaliza mais erros grandes**. Um MSE baixo (próximo de zero) significa que poucos erros são grandes demais. Mas como ele está na escala quadrática, seu valor não é fácil de interpretar diretamente.                         |
| **RMSE** (raiz do MSE)          | Tem **a mesma unidade da variável alvo** (por isso é mais interpretável). Novamente: baixo em relação à escala da variável prevista. Se você prevê temperatura em °C, um RMSE de 1°C pode ser bom. Se for previsão de lucro em milhões, 1 milhão pode ser péssimo.    |

Um técnica seria comparar a **média** dos valores reais com o **MAE (Erro Absoluto Médio)** é uma **forma simples e bastante intuitiva** de avaliar se o erro do seu modelo está alto ou baixo.

---

### ✅ Como interpretar:

* Se o **MAE for muito menor que a média**, o modelo está indo bem.
* Se o **MAE for próximo da média**, o modelo está praticamente chutando (não está aprendendo nada útil).
* Se o **MAE for maior que a média**, o modelo está pior que um chute (muito ruim).

---

### 📊 Exemplo prático:

Você está prevendo o valor de compras dos clientes:

* **Média dos valores reais (target)**: R\$ 500
* **MAE**: R\$ 40
  → O modelo **erra em média R\$ 40**, o que é **só 8% da média** → ótimo resultado!

Agora:

* **Média dos valores reais**: R\$ 500
* **MAE**: R\$ 450
  → O modelo **erra quase tudo** → resultado muito ruim.

---

### 📌 Dica extra:

Você pode transformar essa comparação em **porcentagem de erro**:

```math
Erro relativo (%) = (MAE / Média dos valores reais) × 100
```

E avaliar:

| Erro Relativo (%) | Interpretação    |
| ----------------- | ---------------- |
| 0% a 10%          | Excelente        |
| 10% a 20%         | Bom              |
| 20% a 40%         | Aceitável        |
| > 40%             | Ruim ou ineficaz |

---

## 🔹 O que é o **R² (R-quadrado)**?

> **R² mede quanto do comportamento da variável Y é explicado pelas variáveis X.**

* **Varia de 0 a 1** (ou 0% a 100%)
* **R² = 0,80 (ou 80%)** → quer dizer que 80% da variação em `vendas`, por exemplo, pode ser explicada pelo modelo (como `investimento em anúncios`).

## Interpretação:

* `R² = 1`: predição perfeita.
* `R² = 0`: o modelo não explica nada além da média.
* `R² < 0`: o modelo é pior que simplesmente prever a média.

### ✅ Bom para:

* Saber **se o modelo está explicando bem os dados**
* **Comparar modelos** (quanto maior o R², melhor — com cautela)

---

## 🔹 O que é o **p-valor**?

> Mede-se a relação entre uma variável X e Y é estatisticamente significativa.**

* O **p-valor vai de 0 a 1**
* Se **p-valor < 0.05**, geralmente consideramos que a variável **tem efeito real**
* Se **p-valor > 0.05**, o modelo sugere que pode ter sido **sorte ou ruído**

> Um p-valor alto não “prova” que não há relação — só diz que **não temos evidência forte o suficiente** com aqueles dados.

---

## 🎯 Em conjunto:

* O **R²** diz **“quão bem o modelo inteiro explica Y”**
* O **p-valor** diz **“qual variável X é realmente útil dentro desse modelo”**

---

## 🧪 Exemplo prático:

> Você fez uma regressão:
> `vendas = investimento_em_ads + seguidores + quantidade_de_posts`

* R² = 0.78 → ótimo, seu modelo explica 78% das vendas.
* Mas...
    * investimento\_em\_ads: p-valor = 0.01 ✅
    * seguidores: p-valor = 0.30 ⚠️
    * quantidade\_de\_posts: p-valor = 0.85 ❌

🧾 Resultado: Só o investimento parece ter uma relação confiável com as vendas, os outros podem estar só "de carona".

---

