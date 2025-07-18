# Tanto lambda quanto def criam funções. Por exemplo:

# ❗ Diferenças principais:
# Aspecto           |	def                             |   lambda
# Nome obrigatório? |	Sim                             |	Não (pode ser anônima)
# Várias linhas?    |	Sim                             |	Não, apenas uma única expressão
# Legibilidade	    |   Melhor para funções complexas   |	Melhor para funções simples e rápidas
# Retorno           |	Usa return	Sempre retorna o valor da expressão

# Mais comum em...	Funções normais	map, filter, sorted, callbacks

dobro = lambda x: x * 2
print(dobro(5))  # 10

# Dobrar todos os números da lista
nums = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, nums))
print(dobrados)  # [2, 4, 6, 8]