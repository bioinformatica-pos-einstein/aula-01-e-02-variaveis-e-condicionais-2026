base = input("Escolha uma das seguintes bases nitrogenadas A, C, T ou G: ")
match(base):
    case "A":
        print("A base complementar é T")
    case "T":
        print("A base complementar é A")
    case "C":
        print("A base complementar é G")
    case "G":
        print("A base complementar é C")
    case _:
        print("Base inválida. Comece novamente")