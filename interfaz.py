# =====================================
# 🎰 INTERFAZ DEL JUEGO - BLACKJACK 🎰
# =====================================
import time
import sys
from utils import limpiar_consola,obtener_estadisticas
from jugadores import iniciar_sesion, registrar_jugador, mostrar_ranking
from colorama import init, Fore, Style

# =====================================
# 🎨 INICIALIZACIÓN DE COLORAMA
# =====================================
init(autoreset=True)

# =====================================
# 📖 FUNCIONES DE INTERFAZ: REGLAS
# =====================================
def mostrar_reglas():
    limpiar_consola()
    print(Fore.CYAN + "═" * 50)
    print(Fore.MAGENTA + Style.BRIGHT + "📜  REGLAS DEL BLACKJACK 📜".center(50))
    print(Fore.CYAN + "═" * 50 + "\n")

    reglas = [
        (Fore.YELLOW + "🎯 El objetivo:", "Sumar 21 puntos o acercarse lo más posible sin pasarse."),
        (Fore.YELLOW + "🃏 Valor de las cartas:", "• J, Q, K valen 10.\n  • El As vale 11 o 1, según convenga."),
        (Fore.YELLOW + "📌 Reglas básicas:", "• Si te pasás de 21, perdés.\n  • El crupier pide cartas hasta llegar a 17 o más.")
    ]

    for titulo, descripcion in reglas:
        print(titulo)
        print(descripcion + "\n")
        time.sleep(0.4)

    print(Fore.CYAN + "═" * 50)
    input(Fore.YELLOW + "Presiona Enter para volver al menú...")

# =====================================
# 🎮 FUNCIONES DE INTERFAZ: MENÚ PRINCIPAL
# =====================================
def menu_principal():
    nombre_usuario, saldo, deuda = None, None, 0
    while True:
        limpiar_consola()

        print(Fore.CYAN + "═" * 50)
        print(Fore.MAGENTA + Style.BRIGHT + "🎰  MENÚ PRINCIPAL  🎰".center(50))
        print(Fore.CYAN + "═" * 50 + "\n")

        print(Fore.YELLOW + "📌 Opciones disponibles:\n")
        print(Fore.GREEN + "  1." + Fore.WHITE + " Registrarse 📝")
        print(Fore.GREEN + "  2." + Fore.WHITE + " Iniciar sesión 🔐")
        print(Fore.GREEN + "  3." + Fore.WHITE + " Salir 🚪\n")

        print(Fore.CYAN + "═" * 15)
        opcion = input(Fore.YELLOW + Style.BRIGHT + "\n👉 Elige una opción: ")

        if opcion == '1':
            registrar_jugador()

        elif opcion == '2':
            nombre_usuario, saldo, deuda= iniciar_sesion()
            if nombre_usuario and saldo is not None:
                break
        
        elif opcion == '3':
            limpiar_consola()
            print(Fore.MAGENTA + Style.BRIGHT + "\nGracias por jugar 😎♠️")
            sys.exit()
        
        else:
            input(Fore.RED + Style.BRIGHT + "\n🚫 Opción inválida. Presioná Enter para intentar de nuevo...")

    # Una vez que se ha iniciado sesión correctamente, jugamos
    if nombre_usuario and saldo is not None:
        menu_juego(nombre_usuario, saldo, deuda)

# =====================================
# 🃏 FUNCIONES DE INTERFAZ: MENÚ DE JUEGO
# =====================================
def menu_juego(nombre_usuario, saldo, deuda):
    from juego import jugar_blackjack

    while True:
        limpiar_consola()

         # Obtener las victorias y derrotas actuales
        victorias, derrotas = obtener_estadisticas(nombre_usuario)
        print(Fore.CYAN + "═" * 45)
        print(Fore.MAGENTA + Style.BRIGHT + f"🎰  MENÚ DEL JUEGO - {nombre_usuario} 🎰".center(45))
        print(Fore.CYAN + "═" * 45 + "\n")

        print(Fore.LIGHTWHITE_EX + "-" * 50)
        print(Fore.YELLOW + Style.BRIGHT +
            f"💰 Saldo:      {Fore.GREEN}${saldo:<5}   " +
            f"{Fore.RED}💸 Deuda:     ${deuda:<5}")
        print(Fore.GREEN +
            f"🏆 Victorias:  {victorias:<5}   " +
            f"{Fore.RED}❌ Derrotas:  {derrotas:<5}")
        print(Fore.LIGHTWHITE_EX + "-" * 50 + "\n")

        print(Fore.MAGENTA + "1  Jugar Blackjack")
        print("2  Reglas de Juego")
        print("3  Ranking de jugadores")
        print(Fore.RED + "4  Salir\n")

        opcion = input(Fore.YELLOW + Style.BRIGHT + "👉 Elige una opción: " + Fore.RESET)

        if opcion == '1':
            saldo, deuda = jugar_blackjack(saldo, nombre_usuario, deuda)
            if saldo <= 0:
                print("\n" + Fore.RED + Style.BRIGHT + "❌ Te quedaste sin dinero. Fin del juego.")
                input(Fore.YELLOW + "👉 Presiona Enter para salir...")
                break
        
        elif opcion == '2':
            mostrar_reglas()
        
        elif opcion == '3':
            limpiar_consola()
            mostrar_ranking()
        
        elif opcion == '4':
            print("\n" + Fore.MAGENTA + Style.BRIGHT + f"🎲 Gracias por jugar, {nombre_usuario}. ¡Hasta la próxima! ♠️♥️")
            
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.5)
            
            print("\n")
            time.sleep(1)
            limpiar_consola()
            sys.exit()
        
        else:
            input("\n" + Fore.RED + Style.BRIGHT + "⚠️  Opción inválida. Presioná Enter para intentar de nuevo...")
