# Tipos de aprendizado

## Supervisionado

> Naive Bayes, KNN, Regressão Linear, Regressão Logística, SVM (Support Vectors Machine), Árvores de decisão, Arvores Aleatórias, Redes Neurais

Basicamente, precisamos sempre treiná-los inicialmente com um conjunto de dados já classificados 
e avaliar o resultado "predict" com bases de teste/treino

## Não Supervisionado

> K-Means. DBSCAN. Cluster hierárquico. Análise de componentes principais (PCA). T-distributed Stochastic Neighbor Embedding (T-SNE).

- não há rótulos ou categorias pré-definidas. O algoritmo não sabe o que está tentando prever, ele apenas descobre padrões nos dados por conta própria- 
- Usa técnicas matemáticas (como distância Euclidiana para K-Means e DBScan, mas também outras métricas e algoritmos mais complexos) para encontrar padrões, estruturas ou similaridades inerentes nos dados- 
- O objetivo principal é criar clusters (agrupamentos) ou identificar anomalias, ou reduzir a dimensionalidade dos dados. Esses clusters são, de fato, os agrupamentos ou "classes" que o próprio algoritmo define com base na similaridade dos dados- 
- Pré-processamento para Aprendizado Supervisionado: Este é um uso muito comum e poderoso! Os clusters criados por um algoritmo não supervisionado podem ser usados como novos rótulos para os dados. Com esses dados agora "rotulados" (mesmo que os rótulos tenham sido gerados automaticamente), você pode então alimentar um algoritmo de aprendizagem supervisionada. Isso é especialmente útil quando você tem muitos dados, mas poucos ou nenhum rótulo manual, tornando a rotulagem manual inviável.

> #### Exemplo:
> Imagine que você tem milhões de fotos de animais, mas nenhuma delas está rotulada (você não sabe se é um gato, cachorro, pássaro, etc.).
> 
> - Você pode usar um algoritmo de aprendizado não supervisionado (como K-Means) para agrupar as fotos com base em suas similaridades visuais. O algoritmo pode criar, por exemplo, 10 clusters.
> - Ao inspecionar esses clusters, você pode descobrir que o Cluster 1 tem principalmente gatos, o Cluster 2 tem cachorros, o Cluster 3 tem pássaros, e assim por diante.
> - Agora, você pode usar esses clusters como rótulos para as fotos. Por exemplo, todas as fotos no Cluster 1 são "gatos", no Cluster 2 são "cachorros", etc.
> - Com esses rótulos gerados automaticamente, você pode então treinar um algoritmo de aprendizagem supervisionada (como um classificador Naive Bayes ou uma Rede Neural) para classificar novas fotos de animais com base nesses rótulos aprendidos.
> - Então, sim, o aprendizado não supervisionado é uma ferramenta valiosa para entender a estrutura dos dados e, muitas vezes, serve como uma etapa fundamental para preparar dados para tarefas de aprendizado supervisionado.

#### Redução de dimensionalidade

É comum pensar que eles fazem uma seleção de colunas, como: “essa é boa, essa é ruim, vou descartar”.
Mas não é isso que eles fazem — pelo menos, não na maioria dos casos.

Na verdade, a maioria dos algoritmos de redução de dimensionalidade cria novas variáveis a partir das antigas. Ou seja:

Eles combinam as colunas originais de forma matemática para criar novas dimensões que carregam a maior parte da informação útil.

> Supondo um dataset gigante de 130 colunas e pesado para treinar ou clusterizar, 
> O PCA vai calcular combinações lineares dessas colunas (chamadas componentes principais).
> Ele ordena essas componentes pela quantidade de variância explicada (isto é, o quanto da informação original elas conseguem manter).
> Você pode então ficar com, por exemplo, as 10 primeiras componentes que explicam 95% da variância, e descartar o resto.
> ⚠️ Essas novas colunas não são colunas originais do seu dataset, mas misturas matemáticas delas.

## Por Reforço

- todo