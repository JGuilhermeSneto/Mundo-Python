largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))

area = largura * altura
tinta = area / 2
print('A área da sua parede é de {}x{} igual a {}m²'.format(largura, altura, area))
print('Você precisa de {} litros de tinta para pinta sua parede' .format(tinta))

if area > tinta:
    print('Compre mais {} litros de tinta' .format(area - tinta))
elif tinta > area:
    print('Você tem {} sobrando' .format(tinta - area))
else:
    print('Quantidade correta de tinta!')