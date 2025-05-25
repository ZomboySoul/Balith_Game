# =======================================
# 🔧 FUNCIONES AUXILIARES - BLACKJACK 🔧
# =======================================

import os
import json
from colorama import init, Fore, Style
init(autoreset=True)
archivo_datos = "jugadores.json"

# ============================
# 🧹 FUNCIONES DE LIMPIEZA
# ============================

# Función para limpiar la consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')


# ===============================
# 📋 FUNCIONES DE VISUALIZACIÓN
# ===============================

# Función para mostrar el menú de inicio
def mostrar_inicio():
    limpiar_consola()
    print(Fore.GREEN + Style.BRIGHT + "═" * 46)
    print(Fore.MAGENTA + Style.BRIGHT + "        ♠️♦️   BLACKJACK EN PYTHON  ♣️♥️        ")
    print(Fore.GREEN + Style.BRIGHT + "═" * 46 + "\n")

# Función para mostrar la mano del jugador o del crupier
def mostrar_mano(mano, ocultar_primera=False):
    simbolos = {
        'Corazones': '♥️',
        'Diamantes': '♦️',  
        'Tréboles': '♣️',
        'Picas': '♠️'
    }

    if ocultar_primera:
        print(Fore.YELLOW + "[Carta oculta]" + Style.RESET_ALL)
        cartas_a_mostrar = mano[1:]
    else:
        cartas_a_mostrar = mano

    # Mostramos todas las cartas en una sola línea
    for carta in cartas_a_mostrar:
        simbolo = simbolos[carta[1]]
        color = Fore.RED if carta[1] in ['Corazones', 'Diamantes'] else Fore.WHITE
        valor = carta[0]

        # Mostrar la carta con marco
        print(color + "┌──────┐", end="  ")
    print()  # Espacio después de las primeras líneas

    for carta in cartas_a_mostrar:
        simbolo = simbolos[carta[1]]
        color = Fore.RED if carta[1] in ['Corazones', 'Diamantes'] else Fore.WHITE
        valor = carta[0]

        # Ajuste para que el símbolo ocupe dos espacios
        print(f"{color}│ {Fore.RESET}{valor:<2} {color}{simbolo:<2}│", end="  ")
    print()  # Espacio después de la segunda línea

    for carta in cartas_a_mostrar:
        simbolo = simbolos[carta[1]]
        color = Fore.RED if carta[1] in ['Corazones', 'Diamantes'] else Fore.WHITE
        valor = carta[0]

        print(color + "│      │", end="  ")
    print()  # Espacio después de la tercera línea

    for carta in cartas_a_mostrar:
        simbolo = simbolos[carta[1]]
        color = Fore.RED if carta[1] in ['Corazones', 'Diamantes'] else Fore.WHITE
        valor = carta[0]

        # Ajuste para que el símbolo ocupe dos espacios
        print(f"{color}│ {simbolo:<2}{Fore.RESET}{valor:>2}{color} │", end="  ")
    print()  # Espacio después de la cuarta línea

    for carta in cartas_a_mostrar:
        simbolo = simbolos[carta[1]]
        color = Fore.RED if carta[1] in ['Corazones', 'Diamantes'] else Fore.WHITE
        valor = carta[0]

        print(color + "└──────┘", end="  ")
    print()  # Espacio al final para separar las cartas



# Función para obtener las estadísticas del jugador
def obtener_estadisticas(nombre_usuario):
    if os.path.exists(archivo_datos):
        with open(archivo_datos, 'r') as f:
            jugadores = json.load(f)
        jugador = jugadores.get(nombre_usuario)
        if jugador:
            return jugador.get("victorias", 0), jugador.get("derrotas", 0)
    return 0, 0