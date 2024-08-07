import math as m

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
# resultado = num1 + num2
# print(f"O resultado da soma é: {resultado}")
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# num1 = int(input("Digite um número inteiro: "))
# num2 = 5
# resultado = num1 % num2
# print(f"O resto da divisão é: {resultado}")
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
# resultado = num1 * num2
# print(f"O resutlado da multiplicação é: {resultado}")
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
# resultado = num1 // num2
# print(f"O resutlado inteiro da divisão é: {resultado}")
# # 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# num1 = int(input("Digite um número inteiro: "))
# resultado = num1 ** 2
# print(f"O resutlado do quadrado é: {resultado}")


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# num1 = float(input("Digite o primeiro número com decimais: "))
# num2 = float(input("Digite o segundo número com decimais: "))
# resultado = num1 + num2
# print(f"O resultado da soma é: {resultado}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.~
# num1 = float(input("Digite o primeiro número com decimais: "))
# num2 = float(input("Digite o segundo número com decimais: "))
# resultado = (num1 + num2) / 2
# print(f"O média é: {resultado}")
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# num1 = float(input("Digite um número para a base: "))
# num2 = float(input("Digite um número para a potencia: "))
# resultado = num1 ** num2
# print(f"O resultado é: {resultado}")
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# num1 = float(input("Digite a temperatura em Celsius: "))
# resultado = num1 * 1.8 + 32
# print(f"A temperatura em Fahrenheit é: {resultado}")
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input("Digite o raio de um círculo: "))
# resultado = m.pi * raio ** 2
# print(f"A área do círculo de raio {raio} é: {resultado}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# text = input("Introduza o texto que pretende colocar em maiúsculas: ")
# resultado = text.upper()
# print(resultado)
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# text = input("Introduza o seu nome completo: ")
# resultado = text.lower()
# print(resultado)
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# text = input("Introduza uma frase: ")
# resultado = text.strip()
# print(resultado)
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Digite uma data com o seguinte formato dd/mm/yyyy: ")
# date_list = data.split("/")
# print(f"Dia:  {date_list[0]}")
# print(f"Mês:  {date_list[1]}")
# print(f"Ano:  {date_list[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# text1 = input("Introduza a primeira palavra: ")
# text2 = input("Introduza a primeira palavra: ")
# resultado = text1 + text2
# print(f"Texto contactenado: {resultado}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    resultado = celsius * 1.8 + 32
    print(f"A temperatura em Fahrenheit é: {resultado}")
except ValueError:
    print("Por favor, digite uma temperatura correcta.")

# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
