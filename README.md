# 🃏 Balith: Blackjack en Consola (CMD) con Python

**Balith** es un juego de **Blackjack** (también conocido como 21) desarrollado en Python para ejecutarse en consola (CMD). El proyecto está organizado utilizando **modularización**, separando la lógica en distintos archivos para una mejor estructura, mantenimiento y escalabilidad.

---

## 📜 Descripción del Juego

Balith es una versión clásica del Blackjack donde el jugador compite contra el crupier (la banca) para alcanzar 21 puntos sin pasarse. El juego permite apostar, llevar registro de partidas ganadas, y ofrece una experiencia visual mejorada para consola gracias a módulos como `colorama`.
Además, cuenta con un sistema de usuarios que se guarda en un archivo **JSON** a modo de base de datos local.

---

## 📂 Estructura del Proyecto

```bash
balith/
├── interzas.py
├── juego.py
├── jugadores.py
├── jugadores.json
├── main.py
└── utils.py
```

---

## 📄 Descripción de Archivos

| Archivo                  | Descripción                                                                                                                                                                                      |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **main.py**        | Archivo principal que inicia y controla el flujo general del juego. Desde aquí se cargan los usuarios, se inicializan las partidas y se manejan los menús principales.                          |
| **juego.py**       | Contiene la lógica central del juego: reparto de cartas, control de turnos, verificación de ganadores y cálculo de puntajes.                                                                   |
| **jugadores.py**   | Maneja todo lo relacionado a los jugadores: crear nuevos usuarios, actualizar información, consultar saldo, registrar estadísticas. Interactúa directamente con el archivo `jugadores.json`. |
| **jugadores.json** | Actúa como base de datos local. Aquí se almacenan los datos de los usuarios: nombre, saldo, estadísticas de partidas, y demás información persistente.                                       |
| **interzas.py**    | Encargado de las interfaces visuales en consola. Desde menús, mensajes decorados hasta animaciones de inicio o resultados.                                                                       |
| **utils.py**       | Funciones auxiliares y utilitarias que asisten a los demás módulos, como validaciones, generación de cartas, formateo de texto y colores para consola.                                         |

---

## ⚙️ Tecnologías Utilizadas

- **Python 3.13+**
- **Colorama** (para color en consola)
- **JSON** (para almacenamiento local)
- Librerías estándar de Python (`random`, `os`, `time`, etc.)

---

## 🚀 Cómo Ejecutarlo

1. Cloná o descargá este repositorio.
2. Asegurate de tener Python 3.13 o superior instalado.
3. Instalá las dependencias necesarias:

```bash
pip install colorama
```

4. Ejecutá el juego desde consola:

```bash
python main.py
```

---

## 🎮 Características

- Blackjack clásico contra la banca.
- Sistema de usuarios con almacenamiento persistente.
- Estadísticas personales por jugador.
- Animaciones y texto decorado en consola.
- Modularización completa del código para mayor limpieza y escalabilidad.
- Funcionlidad de prestamos a la banca
- Posibilidad de expandir con nuevas funcionalidades (logros, torneos,etc.).

---

## 📌 Notas

- El archivo `jugadores.json` se genera automáticamente si no existe, y guarda todos los datos de los usuarios de forma local.
- Diseñado para ejecutarse en **consola CMD** o **Terminal**.

---

## 🤝 Créditos

Desarrollado por **Agustin Lezcano - ZomboySoul - Bytech Technology**
Si te gustó o querés aportar ideas, ¡no dudes en colaborar!
