# ==========================================================
# ARQUIVO DE ESTUDO PYTHON - SARAH
# Conceitos: variáveis, entrada de dados, estruturas de repetição,
# funções, manipulação de arquivos e gráficos (turtle)
# ==========================================================

# -------------------------------
# VARIÁVEIS E TIPOS DE DADOS
# -------------------------------

codigo = 10
salario = 1500.00
nome = 'Sarah'
situacao = True

tipo = type(salario)
print("Salário:", salario)
print("Tipo da variável salário:", tipo)
print()

# -------------------------------
# ENTRADA DE DADOS E CONDICIONAL
# -------------------------------

notaA = float(input("Digite sua nota A: "))
notaB = float(input("Digite sua nota B: "))

media = (notaA + notaB) / 2

if media >= 7:
    print("A média: %.1f - Aprovado" % media)
else:
    print("A média: %.1f - Reprovado" % media)

print()

# -------------------------------
# ESTRUTURA DE REPETIÇÃO (WHILE)
# -------------------------------

qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor (negativo para parar): "))

while valor > 0:
    soma += valor
    qtd += 1
    valor = float(input("Digite outro valor: "))

if qtd > 0:
    media = soma / qtd
    print("\nTotal da soma:", soma)
    print("Quantidade de valores:", qtd)
    print("Média da soma:", media)
else:
    print("\nNenhum valor positivo foi informado.")

print()

# -------------------------------
# FUNÇÕES
# -------------------------------

def lerNotas():
    n = float(input("Digite uma nota para o aluno: "))
    return n

def result(n1, n2):
    media = (n1 + n2) / 2
    print("Nota 1:", n1)
    print("Nota 2:", n2)
    print("Média:", media, "Resultado:", end=" ")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = lerNotas()
b = lerNotas()
result(a, b)

print()

# -------------------------------
# MANIPULAÇÃO DE ARQUIVOS
# -------------------------------

arquivo = open("arquivo.txt", "w")
arquivo.write('Curso Python \n')
arquivo.write('Aula Prática')
arquivo.close()

lerArquivo = open("arquivo.txt", "r")
print("Conteúdo do arquivo:")
print(lerArquivo.read())
lerArquivo.close()

print()

# -------------------------------
# DESENHO COM TURTLE
# -------------------------------

import turtle
import math

bob = turtle.Turtle()

def polyline(t, n, length, angle):
    """Desenha uma sequência de segmentos."""
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    """Desenha n segmentos de reta com ângulo igual."""
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """Desenha um arco de círculo."""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    """Desenha um círculo completo."""
    arc(t, r, 360)

circle(bob, 100)

turtle.mainloop()
