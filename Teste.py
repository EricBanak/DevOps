# ex 1: Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Hello World")

# ex 2:Faça um Programa que peça dois números e imprima a soma.
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
soma = valor1 + valor2
print(valor1, "+", valor2, "=", soma)

# ex 3: Faça um Programa que peça as 4 notas bimestrais e mostre a média...

nota1 = float(input("Nota do primeiro bimestre: "))
nota2 = float(input("Nota do segundo bimestre: "))
nota3 = float(input("Nota do terceiro bimestre: "))
nota4 = float(input("Nota do quarto bimestre: "))
print("A sua media foi: ", (nota1+nota2+nota3+nota4)/4)

    
# ex 4: Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Insira o Raio do circulo: "))

resultado = (3.14*raio**2)
print(resultado)

# ex 5: Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

lado = float(input("Insira a medida de um lado do quadrado: "))

resultado = (lado*lado)
resultado2 = (resultado*2)
print("O dobro da area do quadrado eh: ", resultado2)

# ex 6: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

hora = float(input("Quanto voce ganha por hora? "))
horames = float(input("Quantas horas vc trabalha por mes? "))
salario = (hora*horames)
print("Seu salario no referido mes foi de ", salario, "reais")

# ex 7: Faça um programa para cadastrar a escalação do seu time no Cartola FC.
# -*- coding: utf-8 -*-
print("========= CARTOLA FC =========")
time = str(input("Insira o nome do seu time: "))
padrao = str(input("Insira o padrao que sera usado em sua escalacao: "))

if padrao == "3-4-3":
    zagueiros = str(input("Insira o nome dos 3 zagueiros da sua escalacao: "))
    arq = open(r"D:\Programação\Repositorio\Tutoriais Python\Escalacoes\3-4-3.txt", "w")
    arq.write("TIME: "+time+"\n"+"\n")
    arq.write("Zagueiros: "+zagueiros+"\n")
    meias = str(input("Insira o nome dos 4 meias de sua escalacao: "))
    arq.write("Meias: "+meias+"\n")
    atacantes = str(input("Insira o nome dos 3 atacantes de sua escalacao: "))
    arq.write("Atacantes: "+atacantes+"\n")
    arq.close()
    print("Sua escalacao foi salva no arquivo 3-4-3.txt")

elif padrao == "3-5-2":
    zagueiros = str(input("Insira o nome dos 3 zagueiros da sua escalacao: "))
    arq = open(r"D:\Programação\Repositorio\Tutoriais Python\Escalacoes\3-5-2.txt", "w")
    arq.write("TIME: "+time+"\n"+"\n")
    arq.write("Zagueiros: "+zagueiros+"\n")
    meias = str(input("Insira o nome dos 5 meias de sua escalacao: "))
    arq.write("Meias: "+meias+"\n")
    atacantes = str(input("Insira o nome dos 2 atacantes de sua escalacao: "))
    arq.write("Atacantes: "+atacantes+"\n")
    arq.close()
    print("Sua escalacao foi salva no arquivo 3-5-2.txt")

elif padrao == "4-3-3":
    zagueiros = str(input("Insira o nome dos 4 zagueiros da sua escalacao: "))
    arq = open(r"D:\Programação\Repositorio\Tutoriais Python\Escalacoes\4-3-3.txt", "w")
    arq.write("TIME: "+time+"\n"+"\n")
    arq.write("Zagueiros: "+zagueiros+"\n")
    meias = str(input("Insira o nome dos 3 meias de sua escalacao: "))
    arq.write("Meias: "+meias+"\n")
    atacantes = str(input("Insira o nome dos 3 atacantes de sua escalacao: "))
    arq.write("Atacantes: "+atacantes+"\n")
    arq.close()
    print("Sua escalacao foi salva no arquivo 4-3-3.txt")

elif padrao == "4-4-2":
    zagueiros = str(input("Insira o nome dos 4 zagueiros da sua escalacao: "))
    arq = open(r"D:\Programação\Repositorio\Tutoriais Python\Escalacoes\4-4-2.txt", "w")
    arq.write("TIME: "+time+"\n"+"\n")
    arq.write("Zagueiros: "+zagueiros+"\n")
    meias = str(input("Insira o nome dos 4 meias de sua escalacao: "))
    arq.write("Meias: "+meias+"\n")
    atacantes = str(input("Insira o nome dos 2 atacantes de sua escalacao: "))
    arq.write("Atacantes: "+atacantes+"\n")
    arq.close()
    print("Sua escalacao foi salva no arquivo 4-4-2.txt")

elif padrao == "4-5-1":
    zagueiros = str(input("Insira o nome dos 4 zagueiros da sua escalacao: "))
    arq = open(r"D:\Programação\Repositorio\Tutoriais Python\Escalacoes\4-5-1.txt", "w")
    arq.write("TIME: "+time+"\n"+"\n")
    arq.write("Zagueiros: "+zagueiros+"\n")
    meias = str(input("Insira o nome dos 5 meias de sua escalacao: "))
    arq.write("Meias: "+meias+"\n")
    atacantes = str(input("Insira o nome dos 1 atacantes de sua escalacao: "))
    arq.write("Atacantes: "+atacantes+"\n")
    arq.close()
    print("Sua escalacao foi salva no arquivo 4-5-1.txt")

elif padrao == "5-3-2":
    zagueiros = str(input("Insira o nome dos 5 zagueiros da sua escalacao: "))
    arq = open(r"D:\Programação\Repositorio\Tutoriais Python\Escalacoes\5-3-2.txt", "w")
    arq.write("TIME: "+time+"\n"+"\n")
    arq.write("Zagueiros: "+zagueiros+"\n")
    meias = str(input("Insira o nome dos 3 meias de sua escalacao: "))
    arq.write("Meias: "+meias+"\n")
    atacantes = str(input("Insira o nome dos 2 atacantes de sua escalacao: "))
    arq.write("Atacantes: "+atacantes+"\n")
    arq.close()
    print("Sua escalacao foi salva no arquivo 5-3-2.txt")

elif padrao == "5-4-1":
    zagueiros = str(input("Insira o nome dos 5 zagueiros da sua escalacao: "))
    arq = open(r"D:\Programação\Repositorio\Tutoriais Python\Escalacoes\5-4-1.txt", "w")
    arq.write("TIME: "+time+"\n"+"\n")
    arq.write("Zagueiros: "+zagueiros+"\n")
    meias = str(input("Insira o nome dos 4 meias de sua escalacao: "))
    arq.write("Meias: "+meias+"\n")
    atacantes = str(input("Insira o nome dos 1 atacantes de sua escalacao: "))
    arq.write("Atacantes: "+atacantes+"\n")
    arq.close()
    print("Sua escalacao foi salva no arquivo 5-4-1.txt")

else:
    print("O padrao selecionado eh invalido.")


print("commit três")
print("commit quatro")
print("commit quinto")
print("commit sexto")
print("commit 7")