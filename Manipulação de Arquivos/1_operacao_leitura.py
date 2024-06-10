arquivo = open("Manipulação de Arquivos\lorem.txt", "r")
print(arquivo.read())
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

#tip
#for line in arquivo.readline():
#   print(line)
#for line in arquivo.readlines():
#   print(line)
#while len(linha := arquivo.readline()):
#    print(linha)
arquivo.close()