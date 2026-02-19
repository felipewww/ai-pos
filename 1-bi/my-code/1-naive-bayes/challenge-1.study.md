# vectorizer = CountVectorizer()

- Não é um algorítimo, é só um pré-processador de texto → transforma em números
- Ideal para modelos simples ou para quem está começando
- Interpreta só a frequência de palavras, não contexto
- Mas ele sozinho não classifica — ele transforma o texto em números para que um modelo (como Naive Bayes, SVM, etc.) possa aprender padrões.

### Geralmente você:

> - Coleta exemplos reais de spam e não-spam 
> - Usa CountVectorizer para transformar os textos 
> - Treina um modelo de classificação (ex: MultinomialNB, LogisticRegression)
> - Esse modelo aprende quais padrões de palavras são comuns em spam 
> - Depois, você usa o modelo para prever se um novo texto é spam
 
### Exemplo
```
from sklearn.feature_extraction.text import CountVectorizer

textos = ["gosto de sorvete", "sorvete é bom"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(textos)

vectorizer.get_feature_names_out()
# ['bom', 'de', 'gosto', 'sorvete', 'é']
```

### Matriz gerada
|                                 | bom | de | gosto | sorvete | é |
| ------------------------------- | --- | -- | ----- | ------- | - |
| **Texto 1**: "gosto de sorvete" | 0   | 1  | 1     | 1       | 0 |
| **Texto 2**: "sorvete é bom"    | 1   | 0  | 0     | 1       | 1 |

### ⚠️ Limitações
Ele não considera contexto ou ordem das palavras

Trata palavras diferentes com o mesmo peso, mesmo que algumas sejam mais importantes

Frases com mesmo vocabulário em ordens diferentes terão o mesmo vetor

Para resolver essas limitações, usa-se técnicas mais avançadas como TfidfVectorizer, word2vec, BERT, etc.

Se quiser, posso mostrar a diferença entre o CountVectorizer e o TfidfVectorizer.

# MultinomialNB - Naive Bayes

É um algoritimo de aprendizagem supervisionada que aprende conforme a classificação
É uma variante específica do algoritmo Naive Bayes, feita para lidar com dados discretos — como contagens de palavras, que é exatamente o tipo de dado que o CountVectorizer gera.

📚 Tipos de Naive Bayes (em sklearn):

| Classe          | Quando usar                                      | Exemplo típico                  |
| --------------- | ------------------------------------------------ | ------------------------------- |
| `MultinomialNB` | Para dados de **contagem** (como palavras)       | Classificação de texto, spam    |
| `GaussianNB`    | Para dados **contínuos** com distribuição normal | Dados numéricos (ex: sensores)  |
| `BernoulliNB`   | Para **valores binários** (0 ou 1)               | Presença ou ausência de palavra |



> Naive Bayes é um método de machine learning que usa a frequência das ocorrências nos dados para prever uma variável de interesse. Ele se baseia no pensamento bayesiano, que propõe que nossas crenças devem ser ajustadas conforme novas evidências surgem. Por exemplo, se você acredita que todos os gansos são brancos porque sempre viu gansos brancos ou porque alguém lhe disse isso, essa crença muda ao encontrar um ganso preto. Com mais gansos pretos, sua crença se atualiza novamente. Isso ilustra como o conhecimento evolui com a experiência. O modelo é chamado de "naive" (ingênuo) porque parte da suposição de que as variáveis são independentes entre si e não considera conhecimento prévio; ele constrói as probabilidades a partir dos próprios dados disponíveis.

