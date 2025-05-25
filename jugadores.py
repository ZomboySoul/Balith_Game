# =====================================
# 🧑‍💻 GESTIÓN DE JUGADORES - BLACKJACK 🧑‍💻
# =====================================

import os
import sys
import json
import hashlib
import time
from utils import limpiar_consola
from colorama import init, Fore, Style
init(autoreset=True)




# ========================
# 🔐 FUNCIONES DE SEGURIDAD
# ========================

# Función para hashear la contraseña
def hashear_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Funcion para obtener la ruta del recurso compatible con PyInstaller
def obtener_ruta_recurso(nombre_archivo):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, nombre_archivo)
    return os.path.join(os.path.abspath("."), nombre_archivo)

archivo_datos = obtener_ruta_recurso("jugadores.json")

# ================================
# 📝 FUNCIONES DE REGISTRO Y LOGIN
# ================================

# Función para manejar el registro de un nuevo jugador
def registrar_jugador():
    limpiar_consola()

    print(Fore.CYAN + "═" * 50)
    print(Fore.MAGENTA + Style.BRIGHT + "📝  REGISTRO DE JUGADOR  📝".center(50))
    print(Fore.CYAN + "═" * 50 + "\n")

    print(Fore.RED + "👉 Escribe 'volver' en cualquier momento para regresar al menú anterior.\n")

    nombre_usuario = input(Fore.YELLOW + Style.BRIGHT + "👤 Ingrese su nombre de usuario: " + Fore.RESET)
    if nombre_usuario.lower() == "volver":
        return  # Sale de la función y vuelve al menú anterior

    contraseña = input(Fore.YELLOW + Style.BRIGHT + "🔑 Ingrese su contraseña: " + Fore.RESET)
    if contraseña.lower() == "volver":
        return

    saldo_inicial = 100  # Saldo inicial
    deuda = 0  # Deuda inicial
    guardar_datos_jugador(nombre_usuario, contraseña, saldo_inicial, deuda)

    print("\n" + Fore.GREEN + Style.BRIGHT + "✅ Registro exitoso.")
    print(Fore.CYAN + f"Bienvenido, {Fore.MAGENTA + nombre_usuario + Fore.CYAN}! Tienes ${saldo_inicial} para jugar.\n")

    time.sleep(1)  # Espera 1 segundo antes de salir

# Función para manejar el inicio de sesión del jugador
def iniciar_sesion():
    limpiar_consola()

    print(Fore.CYAN + "═" * 50)
    print(Fore.MAGENTA + Style.BRIGHT + "🔐  INICIAR SESIÓN  🔐".center(50))
    print(Fore.CYAN + "═" * 50 + "\n")

    print(Fore.RED + "👉 Escribe 'volver' en cualquier momento para regresar al menú anterior.\n")

    nombre_usuario = input(Fore.YELLOW + Style.BRIGHT + "👤 Ingrese su nombre de usuario: " + Fore.RESET)
    if nombre_usuario.lower() == "volver":
        return None, None, None

    contraseña = input(Fore.YELLOW + Style.BRIGHT + "🔑 Ingrese su contraseña: " + Fore.RESET)
    if contraseña.lower() == "volver":
        return None, None, None

    jugador = cargar_jugador_completo(nombre_usuario)

    if jugador:
        hash_guardado = jugador["clave"]
        if hashear_contraseña(contraseña) == hash_guardado:
            print("\n" + Fore.GREEN + Style.BRIGHT + "✅ Inicio de sesión exitoso.")
            time.sleep(1)  # Espera 1 segundo antes de salir
            return nombre_usuario, jugador["saldo"], jugador.get("deuda", 0)
        else:
            print("\n" + Fore.RED + Style.BRIGHT + "❌ Contraseña incorrecta.")
    else:
        print("\n" + Fore.RED + Style.BRIGHT + "❌ Usuario no encontrado.")

    input(Fore.YELLOW + Style.BRIGHT + "👉 Presiona Enter para intentar de nuevo...")
    return None, None, None

# =============================
# 📂 FUNCIONES DE ARCHIVO / JSON
# =============================

# Función para guardar los datos del jugador en el archivo JSON
def guardar_datos_jugador(nombre_usuario, contraseña, saldo_inicial, deuda):
    jugadores = {}
    if os.path.exists(archivo_datos):
        with open(archivo_datos, 'r') as f:
            try:
                jugadores = json.load(f)
            except json.JSONDecodeError:
                jugadores = {}

    jugadores[nombre_usuario] = {
        "clave": hashear_contraseña(contraseña),
        "saldo": saldo_inicial,
        "deuda": deuda
    }

    with open(archivo_datos, 'w') as f:
        json.dump(jugadores, f, indent=4)


# Función para cargar un jugador completo
def cargar_jugador_completo(nombre_usuario):
    if os.path.exists(archivo_datos):
        with open(archivo_datos, 'r') as f:
            jugadores = json.load(f)
        return jugadores.get(nombre_usuario)
    return None


# ==========================================
# 💰 FUNCIONES DE ACTUALIZACIÓN DE SALDO Y DEUDA
# ==========================================

# Función para actualizar solo el saldo y deuda
def actualizar_saldo(nombre_usuario, nuevo_saldo, deuda):
    if os.path.exists(archivo_datos):
        with open(archivo_datos, 'r') as f:
            try:
                jugadores = json.load(f)
            except json.JSONDecodeError:
                jugadores = {}

        if nombre_usuario in jugadores:
            jugadores[nombre_usuario]["saldo"] = nuevo_saldo
            jugadores[nombre_usuario]["deuda"] = deuda

            with open(archivo_datos, 'w') as f:
                json.dump(jugadores, f, indent=4)


# ====================================
# 📊 FUNCIONES DE ESTADÍSTICAS Y LOGROS
# ====================================

# Función para actualizar estadísticas después de una partida
def actualizar_estadisticas(nombre_usuario, resultado):
    if os.path.exists(archivo_datos):
        with open(archivo_datos, 'r') as f:
            try:
                jugadores = json.load(f)
            except json.JSONDecodeError:
                jugadores = {}
        
        if nombre_usuario in jugadores:
            jugador = jugadores[nombre_usuario]

            # Inicializar estadísticas si no existen
            jugador.setdefault("victorias", 0)
            jugador.setdefault("derrotas", 0)
            jugador.setdefault("empates", 0)
            jugador.setdefault("racha_ganadas", 0)
            jugador.setdefault("racha_perdidas", 0)

            if resultado == "victoria":
                jugador["victorias"] += 1
                jugador["racha_ganadas"] += 1
                jugador["racha_perdidas"] = 0
            elif resultado == "derrota":
                jugador["derrotas"] += 1
                jugador["racha_perdidas"] += 1
                jugador["racha_ganadas"] = 0
            elif resultado == "empate":
                jugador["empates"] += 1
                # Las rachas no cambian en empate

            with open(archivo_datos, 'w') as f:
                json.dump(jugadores, f, indent=4)


# ================================
# 💵 FUNCIONES DE PRÉSTAMO Y CRÉDITO
# ================================

# Función para ofrecer préstamo
def ofrecer_prestamo(saldo, deuda):
    if saldo <= 0:
        print(Fore.RED + "Te has quedado sin dinero.")
        while True:
            prestamo = input(Fore.YELLOW + "¿Te gustaría pedir un préstamo del casino? (25/100 o 0 para rechazar): ")
            if prestamo.isdigit():
                prestamo = int(prestamo)
                if prestamo in [25, 100]:
                    saldo += prestamo
                    print(Fore.GREEN + f"Préstamo de ${prestamo} otorgado. Ahora tienes ${saldo}.")
                    deuda += prestamo
                    return saldo, deuda
                elif prestamo == 0:
                    print(Fore.RED + "No aceptaste préstamo. Fin del juego.")
                    exit()
                else:
                    print(Fore.RED + "Monto no válido. Solo se permite 25 o 100.")
            else:
                print(Fore.RED + "Entrada no válida. Por favor, ingresa un número.")
    return saldo, deuda


# ===========================
# 🏆 FUNCIONES DE VISUALIZACIÓN
# ===========================

# Función para mostrar ranking
def mostrar_ranking():
    try:
        with open(archivo_datos, "r") as archivo:
            jugadores = json.load(archivo)
    except FileNotFoundError:
        print(Fore.RED + "No hay jugadores registrados aún.")
        return

    sin_deuda = {nombre: datos for nombre, datos in jugadores.items() if datos.get('deuda', 0) == 0}

    if not sin_deuda:
        print(Fore.RED + "No hay jugadores sin deudas en este momento.")
        input(Fore.YELLOW + "\n👉 Presiona Enter para volver al menú...")
        return

    ranking = sorted(sin_deuda.items(), key=lambda x: x[1]['saldo'], reverse=True)

    print(Fore.CYAN + "═" * 50)
    print(Fore.MAGENTA + "🏆 RANKING DE JUGADORES 🏆".center(50))
    print(Fore.CYAN + "═" * 50 + "\n")

    nombre_ancho = 20
    saldo_ancho = 10

    def color_rgb(r, g, b, texto):
        return f"\033[38;2;{r};{g};{b}m{texto}\033[0m"

    for i, (nombre, datos) in enumerate(ranking[:10], 1):
        puesto = f"{i}".ljust(3)
        nombre_formato = nombre.ljust(nombre_ancho)
        saldo_formato = f"${datos['saldo']}".rjust(saldo_ancho)
        linea = f"{puesto}{nombre_formato}{saldo_formato}"

        if i == 1:
            color = color_rgb(255, 215, 0, linea)
        elif i == 2:
            color = color_rgb(192, 192, 192, linea)
        elif i == 3:
            color = color_rgb(205, 127, 50, linea)
        else:
            color = linea

        print(color)

    input(Fore.YELLOW + "\n👉 Presiona Enter para volver al menú...")
    