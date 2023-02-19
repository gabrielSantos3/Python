'''
Desafio 044

Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço
normal e as condições de pagamento:

-> À vista dinheiro / cheque: 10% de desconto
-> À vista no cartão: 5% de desconto
-> Em até 2x no cartão: preço normal
-> 3x ou mais no cartão: 20% de juros
'''

def printOptions():
    print('\nEscolha a sua condição de pagamento: \n[1] À vista dinheiro / cheque: 10% de desconto \n[2] À vista no cartão: 5% de desconto \n[3] Em até 2x no cartão: preço normal \n[4] 3x ou mais no cartão: 20% de juros')


def printValue(value):
    print(f'O novo valor do produto será: R${value :.2f}')
   

value = float(input('\nDigite o valor do produto: R$'))

printOptions()

pay = int(input('\nSua opção: '))

if(pay < 1 or pay > 4):
    print('\nOpção Inválida!')

match pay:
    case 1:
        printValue(value * 0.9)
        
    case 2:
        printValue(value * 0.95)
        
    case 3:
        printValue(value)
        
    case 4:
        printValue(value * 1.2)
        
    
        