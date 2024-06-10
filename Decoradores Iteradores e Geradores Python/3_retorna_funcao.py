def calculadora(operacao):
    def soma(a, b):
        return a+b
    def subtracao(a, b):
        return a-b
    def multiplicacao(a, b):
        return a*b
    def divisao(a, b):
        return a/b
    match operacao:
        case '+':
            return soma
        case '-':
            return subtracao
        case '/':
            return divisao
        case '*':
            return multiplicacao
op = calculadora('+')
print(op(2, 2))
op = calculadora('-')
print(op(2, 2))
op = calculadora('/')
print(op(2, 2))
op = calculadora('*')
print(op(2, 2))