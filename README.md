# Proyecto Game - Independence Day

Juego estilo Space Invaders hecho con Pygame.

## Requisitos

- macOS (probado en macOS 13.x)
- Python 3.12
- pip

## Estructura

- `game.py`: archivo principal del juego.
- `assets/images`: imagenes del juego (jugador, enemigos, fondo, icono, bala).
- `assets/audios`: musica/sonidos.
- `assets/fonts`: fuentes para score y game over.

## Preparar entorno (recomendado)

Este proyecto ya tiene un entorno recomendado: `.venv312` con Python 3.12.

1. Activar entorno:

```bash
source .venv312/bin/activate
```

2. Verificar version:

```bash
python -V
```

Deberia mostrar algo como `Python 3.12.x`.

3. Si necesitas reinstalar dependencias:

```bash
python -m pip install --upgrade pip
python -m pip install pygame
```

## Ejecutar el juego

Con el entorno activado:

```bash
python game.py
```

## Controles

- Flecha izquierda: mover jugador a la izquierda.
- Flecha derecha: mover jugador a la derecha.
- Espacio: disparar.
- Cerrar ventana: salir del juego.

## Solucion de problemas

- Error `no such file or directory` al ejecutar Python por ruta absoluta:
  usa comillas si hay espacios en el path, o ejecuta desde la carpeta del proyecto.
- Si `pygame` falla en Python 3.14, usa el entorno `.venv312` (Python 3.12), donde este proyecto ya fue probado.

## Notas

- Existe otro entorno `.venv` con Python 3.14, pero para este proyecto se recomienda `.venv312`.

## Proximas mejoras

1. Agregar pantalla de inicio con boton de jugar y salir.
2. Implementar niveles con aumento progresivo de velocidad y cantidad de enemigos.
3. Incorporar efectos de sonido para disparo, impacto y game over.
4. Mostrar barra de vida o sistema de vidas del jugador.
5. Crear sistema de pausa y reanudacion con tecla P.
6. Guardar el mejor puntaje en un archivo local.
7. Refactorizar `game.py` en modulos (`player`, `enemy`, `ui`, `audio`) para facilitar mantenimiento.
