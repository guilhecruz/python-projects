altura = float(input("Qual a altura da sua parede?"))
largura = float(input("Qual a largura da sua parede?"))

m2 = altura*largura

tinta = m2/2

print("Você precisará de {}l de tinta para pintar sua parede de {}m²".format(tinta, m2))