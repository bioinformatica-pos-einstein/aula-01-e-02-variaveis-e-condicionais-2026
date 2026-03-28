"""
Você está analisando uma variante genética e precisa saber se ela é relevante para análise ou não.

Obs: Esse exercício é uma simplificação! Depois vocês vão saber avaliar de verdade!

Você vai receber 5 parametros:

Frequência Populacional: Frequencia da variante na população em porcentagem.

Gene: Gene da variante.

Impacto: Se ela está numa posição de impacto ALTO ou BAIXO.

Reads: Quantidade de reads da variante.

Vaf: Frequencia alélica da variante.

A primeira coisa é tomar cuidado com a qualidade da leitura. Se a variante tiver menos de 10 reads OU uma frequência alélica abaixo de 20% a gente vai dizer que ela não é relevante, pois deve ser um artefato.

Se ela não for um artefato temos que avaliar as seguintes coisas:

- Ela só vai ser relevante se o impacto for ALTO.
- Ela não vai ser relevante se a frequência dela for maior que 5%, a não ser que esteja nos seguintes genes de exceção: 'HFE', 'MEFV' ou 'GJB2'.
"""

frequencia_populacional = int(input("Digite a frequencia: "))
gene = input("Digite o gene: ")
impacto = input("Digite o impacto (ALTO ou BAIXO): ")
reads = int(input("Digite os reads: "))
vaf = int(input("Digite o VAF: "))

genes_de_excecao = (gene == 'HFE') or (gene == 'MEFV') or (gene == 'GJB2')

if (reads < 10) or (vaf < 20):
    print("Não é relevante, deve ser artefato.")
elif impacto != "ALTO":
    print("Não é relevante.")
elif (frequencia_populacional > 5) and not genes_de_excecao:
    print("Não é relevante.")
else:
    print("É relevante.")