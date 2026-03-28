velocidade = float(input("Digite sua velocidade: "))
print("Bom dia, cliente.")
if velocidade <= 80:
    print(f"Voce foi multado em R${velocidade*7}")
else:
    print("Voce nao foi multado")