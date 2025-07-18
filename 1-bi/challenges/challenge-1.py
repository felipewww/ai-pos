from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Desenvolver um script em Python que seja capaz de classificar textos curtos em categorias pré-definidas
# pelo usuário (por exemplo, "tecnologia", "esportes" ou "política"). Esta atividade enfatiza o entendimento de como
# os dados podem ser transformados e utilizados para treinar um modelo simples de Machine Learning.

# Dados de exemplo
textos = [
    "O novo lançamento da Apple",
    "Resultado do jogo de ontem",
    "Eleições presidenciais",
    "Atualização no mundo da tecnologia",
    "Campeonato de futebol",
    "Política internacional"
]
categorias = ["tecnologia", "esportes", "política", "tecnologia", "esportes", "política"]

# Convertendo textos em uma matriz de contagens de tokens
# Ele transforma textos em vetores numéricos, onde cada posição representa a frequência de uma palavra no texto.
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(textos)

# print(X.toarray())
# print(vectorizer.get_feature_names_out())
# print('\nFEAT NAMES')
# print(vectorizer.get_feature_names_out())

# Dividindo os dados em conjuntos de treinamento e teste
# test_size = percentual de dados que serão separados para o treino
# random_state = garante que a separação seja a mesma sempre que rodar o código
X_train, X_test, y_train, y_test = train_test_split(X, categorias, test_size=0.5, random_state=42)

print(X_test)
# Treinando o classificador Naive Bayes
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Predição e Avaliação
# Qual categoria (Y_test) o texto (X_test) seria categorizado...
y_pred = clf.predict(X_test)

# comparamos o PREDICT (y_pred) com a categoria
print(f"Acurácia: {accuracy_score(y_test, y_pred)}")


#################