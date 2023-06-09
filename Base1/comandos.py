import os

# Comando para limpar console
def limpar_console():
    if os.name == 'nt':  # Verifica se o sistema operacional é o Windows
        os.system('cls')  # Comando para limpar o console no Windows
    else:
        os.system('clear')  # Comando para limpar o console em sistemas Unix-like

limpar_console()

