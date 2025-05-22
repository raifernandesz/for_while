numero = int(input("Digite seu numero"))
comeco = int(input("Digite o comeco"))
fim = int(input("Digite o fim"))


for i in (comeco,fim):
    print(f"{i} x {numero} = {i * numero}")
