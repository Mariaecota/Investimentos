import comandos as cm
import textos as tx

#Inicio do codigo
codigo = "-1"
while codigo !="5":
    cm.limpar_console()
    codigo = input(tx.menu_inicial)
    if codigo == "1":
        cm.limpar_console()
        input("EM CONSTRUÇÂO, precione ENTER para continuar")
    elif codigo == "2":
        cm.limpar_console()
        input("EM CONSTRUÇÂO, precione ENTER para continuar")
    elif codigo == "3":
        cm.limpar_console()
        input("EM CONSTRUÇÂO, precione ENTER para continuar")
    elif codigo == "4":
        cm.limpar_console()
        input("EM CONSTRUÇÂO, precione ENTER para continuar")
    elif codigo == "5":
        cm.limpar_console()
        print("Fechando...")

    else:
        cm.limpar_console()
        input(f"'{codigo}' - Não é um comando valido, precione ENTER para continuar")