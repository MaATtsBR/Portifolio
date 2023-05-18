nome = input('Digite o seu nome? ')
print('Olá ' + nome)

print('| 1 + | 2 - | 3 * | 4 / |')
escolha = input('Escolha sua operação:')
# Conversão de input (Sting para Int)
int_escolha = int(escolha)

if int_escolha > 4:
    print('Opção invalida!')
else:
    n1 = input('Digite o primeiro número :')
    n2 = input('Digite o segundo número :')
# Conversão de input (Sting para Int)
int_n1 = int(n1)
int_n2 = int(n2)
# Calculos
soma = int_n1 + int_n2
subtracao = int_n1 - int_n2
multiplicacao = int_n1 * int_n2
divisao = int_n1 / int_n2

# Escolhas Menu

if int_escolha == 1:
 print(f'O Resultado é :{soma}')
elif int_escolha == 2:
 print(f'O Resultado é :{subtracao}')
elif int_escolha == 3:
 print(f'O Resultado é :{multiplicacao}')
elif int_escolha == 4:
 print(f'O Resultado é :{divisao}')
