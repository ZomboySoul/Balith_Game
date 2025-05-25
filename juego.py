# =====================================
# 🃏 JUEGO DE BLACKJACK 🃏
# =====================================

import time
import random
from utils import mostrar_inicio, mostrar_mano, limpiar_consola
from jugadores import actualizar_saldo, actualizar_estadisticas
from colorama import init, Fore, Style
from jugadores import ofrecer_prestamo

# =====================================
# 🎨 INICIALIZACIÓN DE COLORAMA
# =====================================
init(autoreset=True)

# =====================================
# 🃏 FUNCIONES DEL JUEGO
# =====================================

# Función para calcular el valor de una carta
def valor_carta(carta):
    valor = carta[0]
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11
    else:
        return int(valor)

# Función para crear un mazo de cartas
def crear_mazo():
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    mazo = [(valor, palo) for palo in palos for valor in valores]
    random.shuffle(mazo)
    return mazo

# Función para calcular el puntaje total de la mano
def calcular_puntaje(mano):
    puntaje = sum(valor_carta(carta) for carta in mano)
    num_as = sum(1 for carta in mano if carta[0] == 'A')
    while puntaje > 21 and num_as:
        puntaje -= 10
        num_as -= 1
    return puntaje

# =====================================
# 🎮 FUNCIONES DE JUEGO PRINCIPALES
# =====================================

# Función para jugar blackjack con préstamo y pago de deuda
def jugar_blackjack(saldo, nombre_usuario, deuda):
    from interfaz import menu_juego

    mostrar_inicio()

    while True:
        print(Fore.YELLOW + Style.BRIGHT + f"💰 Saldo: {Fore.GREEN}${saldo}   " +
              f"{Fore.RED}Deuda: ${deuda}\n")

        if saldo <= 0:
            saldo, deuda = ofrecer_prestamo(saldo, deuda)
            if deuda > 0:
                print(Fore.GREEN + f"Te hemos otorgado un préstamo. Ahora debes ${deuda}.")

        apuesta = input(Fore.YELLOW + "💸 Ingresa tu apuesta (o escribe 'salir' si querés dejar la mesa): ")
        if apuesta.lower() == 'salir':
            actualizar_saldo(nombre_usuario, saldo, deuda)
            return menu_juego(nombre_usuario, saldo, deuda)

        if apuesta.isdigit() and int(apuesta) <= saldo and int(apuesta) > 0:
            apuesta = int(apuesta)
            break
        else:
            print(Fore.RED + "Apuesta no válida. Asegúrate de tener suficiente dinero.")

    limpiar_consola()
    print(Fore.MAGENTA + "🃏 Barajando cartas...")
    time.sleep(2)
    limpiar_consola()

    mazo = crear_mazo()
    mano_jugador = [mazo.pop(), mazo.pop()]
    mano_crupier = [mazo.pop(), mazo.pop()]

    while True:
        print(Fore.BLUE + "Tu mano:")
        mostrar_mano(mano_jugador)
        print(Fore.BLUE + "\nMano del crupier:")
        mostrar_mano(mano_crupier, ocultar_primera=True)

        while calcular_puntaje(mano_jugador) < 21:
            accion = input(Fore.YELLOW + "\n¿Querés pedir otra carta? (s/n): ")
            if accion.lower() == 's':
                limpiar_consola()
                mano_jugador.append(mazo.pop())
                print(Fore.BLUE + "\nTu mano:")
                mostrar_mano(mano_jugador)
            elif accion.lower() == 'n':
                break
            else:
                print(Fore.RED + "Opción inválida. Escribe 's' para pedir otra carta o 'n' para plantarte.")

        puntaje_jugador = calcular_puntaje(mano_jugador)

        resultado = None  # Variable para guardar el resultado

        if puntaje_jugador > 21:
            print(Fore.RED + f"\n¡Te pasaste con {puntaje_jugador} puntos! Perdiste.")
            print(Fore.BLUE + "\nMano final del crupier:")
            mostrar_mano(mano_crupier)
            print(Fore.GREEN + f"\nEl crupier tenía {calcular_puntaje(mano_crupier)} puntos.")
            saldo -= apuesta
            resultado = "derrota"

        else:
            while calcular_puntaje(mano_crupier) < 17:
                mano_crupier.append(mazo.pop())

            puntaje_crupier = calcular_puntaje(mano_crupier)

            print(Fore.BLUE + "\nMano final del crupier:")
            mostrar_mano(mano_crupier)
            print(Fore.CYAN + f"\nTu puntaje: {puntaje_jugador} | Puntaje del crupier: {puntaje_crupier}")

            if puntaje_crupier > 21 or puntaje_jugador > puntaje_crupier:
                print(Fore.GREEN + "\n¡Ganaste!")
                saldo += apuesta
                resultado = "victoria"

            elif puntaje_jugador == puntaje_crupier:
                print(Fore.YELLOW + "\nEmpate.")
                resultado = "empate"

            else:
                print(Fore.RED + f"\nPerdiste por {puntaje_crupier - puntaje_jugador} puntos.")
                saldo -= apuesta
                resultado = "derrota"

        # Pago de deuda si ganó
        if resultado == "victoria" and deuda > 0:
            pago_deuda = round(saldo * 0.50)
            if pago_deuda > deuda:
                pago_deuda = deuda
            deuda -= pago_deuda
            saldo -= pago_deuda
            print(Fore.YELLOW + f"\nPagaste ${pago_deuda} de la deuda. Te queda una deuda de ${deuda}.")

        # Si se quedó sin saldo, ofrecer préstamo
        if saldo <= 0:
            print(Fore.RED + f"\nDebes devolver la deuda de ${deuda} en la próxima ronda.")
            saldo, deuda = ofrecer_prestamo(saldo, deuda)

        # Actualizar estadísticas y saldo antes de volver al menú
        actualizar_estadisticas(nombre_usuario, resultado)
        actualizar_saldo(nombre_usuario, saldo, deuda)

        print(Fore.YELLOW + f"\nTu saldo actual es: ${saldo}")
        time.sleep(8)
        return saldo, deuda
