num = int(input("Informe um numero para ser fatorado, maior que 0: "))

valor_fatoracao = 1
for i in range(1, num + 1):
	valor_fatoracao *= i

print(valor_fatoracao)
