O `.corr()` é só uma das muitas funções úteis que o **Pandas DataFrame** oferece para análise de dados.

Aqui vai uma lista organizada com **as funções mais úteis**, divididas por tipo de operação:

---

### 📊 **Análise Estatística Rápida**

| Função          | Descrição                                     |
| --------------- | --------------------------------------------- |
| `df.describe()` | Estatísticas gerais (média, desvio, min, etc) |
| `df.mean()`     | Média por coluna numérica                     |
| `df.median()`   | Mediana                                       |
| `df.mode()`     | Moda                                          |
| `df.std()`      | Desvio padrão                                 |
| `df.var()`      | Variância                                     |
| `df.min()`      | Mínimo                                        |
| `df.max()`      | Máximo                                        |
| `df.sum()`      | Soma                                          |
| `df.count()`    | Quantidade de valores não nulos               |
| `df.corr()`     | Correlação                                    |
| `df.cov()`      | Covariância                                   |
| `df.quantile()` | Quantil                                       |

---

### 🔁 **Agrupamento e Agregação**

| Função             | Descrição                                    |
| ------------------ | -------------------------------------------- |
| `df.groupby()`     | Agrupa dados por categoria                   |
| `df.agg()`         | Agregações customizadas                      |
| `df.pivot_table()` | Cria tabelas dinâmicas                       |
| `df.resample()`    | Agrupa por data (útil para séries temporais) |

---

### 🧼 **Limpeza e Manipulação**

| Função                 | Descrição                       |
| ---------------------- | ------------------------------- |
| `df.dropna()`          | Remove linhas com valores nulos |
| `df.fillna(valor)`     | Preenche valores nulos          |
| `df.drop(columns=[])`  | Remove colunas                  |
| `df.rename()`          | Renomeia colunas                |
| `df.replace()`         | Substitui valores               |
| `df.astype()`          | Converte tipos de dados         |
| `df.duplicated()`      | Verifica duplicatas             |
| `df.drop_duplicates()` | Remove duplicatas               |

---

### 🔍 **Filtros e Seleção**

| Função                 | Descrição                              |
| ---------------------- | -------------------------------------- |
| `df.loc[]`             | Seleção por rótulo (label)             |
| `df.iloc[]`            | Seleção por posição (index)            |
| `df.query()`           | Filtra usando uma string com condições |
| `df[df["coluna"] > x]` | Filtro com condição lógica             |

---

### 🔧 **Outras úteis**

| Função              | Descrição                                      |
| ------------------- | ---------------------------------------------- |
| `df.info()`         | Estrutura geral do DataFrame                   |
| `df.shape`          | Tamanho (linhas, colunas)                      |
| `df.columns`        | Nomes das colunas                              |
| `df.index`          | Índices das linhas                             |
| `df.sort_values()`  | Ordena os dados                                |
| `df.apply()`        | Aplica uma função linha/coluna                 |
| `df.map()`          | Aplica função a uma coluna                     |
| `df.value_counts()` | Frequência de valores (ideal para categóricos) |

---

Se quiser, posso montar uma tabela interativa ou uma cheatsheet PDF com os principais comandos. Deseja isso?
