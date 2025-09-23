try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    s = n1 + n2
    if s > 20:
        print(False, "maior que 20")
    else:
        print("Soma dos valores é:", s)
        print(True)
except ValueError:
    print("Por favor, digite apenas números válidos.")