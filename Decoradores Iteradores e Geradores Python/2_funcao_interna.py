def principal():
    print("Executando a função principal")

    def funcao_interna():
        print("Ececutando a função interna")
    def funcao_2():
        print("Executando função 2")
    funcao_interna()
    funcao_2()
principal()