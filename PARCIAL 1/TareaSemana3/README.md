# Sistema de Gestión de Mascotas - TareaSemana3

Este proyecto contiene dos programas Python que resuelven el mismo problema (registrar y gestionar mascotas) utilizando dos enfoques diferentes: **Programación Tradicional** y **Programación Orientada a Objetos**.

## Descripción

Ambos programas permiten:
- **Registrar infinitas mascotas** con los siguientes datos:
  - Nombre
  - Especie
  - Edad (en años)
  - Peso (en kg)
  - Color
- **Almacenar mascotas** sin mostrarlas de inmediato
- **Visualizar todas las mascotas registradas** bajo demanda
- **Menú interactivo** para navegar entre opciones

---

## Estructura del Proyecto

```
TareaSemana3/
├── programacion_tradicional/
│   └── tradicional.py          # Programa con enfoque procedural
└── programacion_poo/
    ├── main.py                 # Punto de entrada del programa POO
    └── mascota.py              # Definición de la clase Mascota
```

---

## 1. Programa 1: Programación Tradicional

### Ubicación
```
programacion_tradicional/tradicional.py
```

### Características
- **Sin clases ni objetos**: utiliza solo funciones y diccionarios
- **Funciones principales**:
  - `solicitar_datos()`: recibe datos de teclado y devuelve un diccionario
  - `mostrar_informacion(mascota)`: muestra la información de una mascota
  - `mostrar_todas_mascotas(mascotas)`: muestra todas las mascotas registradas
  - `mostrar_menu()`: imprime el menú de opciones
  - `main()`: controla el flujo principal del programa

### Cómo ejecutar

```bash
python "C:\Users\Dayvis\OneDrive - Universidad Estatal Amazónica\UEA-REPOSITORY-2626\2626-POO-CalderonDayvis\PARCIAL 1\TareaSemana3\programacion_tradicional\tradicional.py"
```

### Ejemplo de uso

```
Sistema de registro de mascotas (Programación tradicional)
Permite registrar infinitas mascotas y visualizarlas bajo demanda.

----- MENÚ -----
1. Registrar nueva mascota
2. Mostrar todas las mascotas
3. Salir
----------------
Seleccione una opción (1-3): 1

Creando mascota #1 (ingrese los datos):
Nombre: Fido
Especie: Perro
Edad (años): 3
Peso (kg): 25.5
Color: Marrón
✓ Mascota registrada exitosamente. Total: 1
```

---

## 2. Programa 2: Programación Orientada a Objetos

### Ubicación
```
programacion_poo/
├── main.py
└── mascota.py
```

### Características

#### Archivo: `mascota.py`
Define la **clase Mascota** con:
- **Atributos**:
  - `nombre`: str
  - `especie`: str
  - `edad`: int
  - `peso`: float
  - `color`: str
- **Métodos**:
  - `__init__(nombre, especie, edad, peso, color)`: constructor
  - `mostrar_informacion()`: muestra los datos de forma organizada
  - `hacer_sonido()`: imprime un sonido representativo según la especie

#### Archivo: `main.py`
Punto de entrada del programa que:
- Crea múltiples objetos de la clase Mascota
- Proporciona un menú interactivo
- Permite registrar infinitas mascotas
- Muestra todas las mascotas bajo demanda

### Cómo ejecutar

```bash
python "C:\Users\Dayvis\OneDrive - Universidad Estatal Amazónica\UEA-REPOSITORY-2626\2626-POO-CalderonDayvis\PARCIAL 1\TareaSemana3\programacion_poo\main.py"
```

### Ejemplo de uso

```
Sistema de gestión de mascotas (Programación Orientada a Objetos)
Permite registrar infinitas mascotas y visualizarlas bajo demanda.

----- MENÚ -----
1. Registrar nueva mascota
2. Mostrar todas las mascotas
3. Salir
----------------
Seleccione una opción (1-3): 1

Creando mascota #1 (ingrese los datos):
Nombre: Luna
Especie: Gato
Edad (años): 2
Peso (kg): 15.5
Color: Negro
✓ Mascota registrada exitosamente. Total: 1

----- MENÚ -----
1. Registrar nueva mascota
2. Mostrar todas las mascotas
3. Salir
----------------
Seleccione una opción (1-3): 2

===== MASCOTAS REGISTRADAS (1) =====

--- Mascota #1 ---

----- Información de la mascota -----
Nombre : Luna
Especie: Gato
Edad   : 2 años
Peso   : 15.5 kg
Color  : Negro
------------------------------------

Luna hace: ¡Miau!

========================================
```

---

## Diferencias Clave

| Aspecto | Tradicional | POO |
|---------|-------------|-----|
| **Estructura de datos** | Diccionarios | Objetos (instancias de clase) |
| **Organización** | Funciones | Métodos en clases |
| **Encapsulación** | No | Sí (atributos privados) |
| **Reutilización** | Limitada | Alta |
| **Mantenimiento** | Más difícil con escalado | Más fácil y modular |
| **Complejidad** | Simple | Intermedia |

---

## Validaciones Implementadas

Ambos programas incluyen:
- ✓ Validación de campos vacíos (nombre, especie, color)
- ✓ Validación de edad (entero no negativo)
- ✓ Validación de peso (número positivo)
- ✓ Manejo de opciones inválidas del menú
- ✓ Mensaje cuando no hay mascotas registradas

---

## Notas Importantes

1. **Entrada de teclado**: ambos programas solicitan datos interactivamente
2. **Persistencia**: los datos se almacenan en memoria durante la ejecución (no se guardan en archivos)
3. **Extensiones posibles**:
   - Guardar datos en archivo (JSON, CSV)
   - Buscar mascota por nombre
   - Editar información de mascota existente
   - Eliminar mascota del registro
   - Calcular edad en meses/años de mascota

---

## Ejecución desde PowerShell

Para facilitar el uso desde PowerShell:

```powershell
# Programa tradicional
cd "C:\Users\Dayvis\OneDrive - Universidad Estatal Amazónica\UEA-REPOSITORY-2626\2626-POO-CalderonDayvis\PARCIAL 1\TareaSemana3\programacion_tradicional"
python tradicional.py

# Programa POO
cd "..\programacion_poo"
python main.py
```

---

**Autor**: Dayvis Calderón  
**Fecha**: Junio 2026  
**Asignatura**: Programación Orientada a Objetos  
**Universidad**: Universidad Estatal Amazónica

