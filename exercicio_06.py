frequencia_populacional = float(input("Qual a frequência populacional (%)? "))
gene = input ("Qual é o gene? ")
impacto = input("Qual o impacto? Alto ou Baixo? ")
reads = int(input("Qual o número de reads? "))
freq_alelica = float(input("Qual a frequencia alelica (%)? "))
if (reads < 10) or (freq_alelica < 20):
    print("Não será relevante.")
elif impacto != "Alto":
    print("Não será relevante.")
elif frequencia_populacional > 5:
    print("Não será relevante.")
elif not((gene == "HFE") or (gene == "MEFV") or (gene == "GJB2")):
    print("Será relevante, pois exceção de Gene.")
else:
    print("Não será relevante.")