# TareaSemana3: Sistema de Gestión de Mascotas

## Objetivo General
Desarrollar un sistema de gestión de mascotas utilizando **dos enfoques diferentes** para comparar y comprender las diferencias entre la **Programación Tradicional** y la **Programación Orientada a Objetos (POO)**.

---

## Datos Manejados por Cada Mascota

Cada mascota en ambos programas contiene la siguiente información:

| Dato | Tipo | Descripción |
|------|------|-------------|
| **Nombre** | String | Nombre único de la mascota |
| **Especie** | String | Tipo de animal (perro, gato, pájaro, etc.) |
| **Edad** | Entero | Edad en años (≥ 0) |
| **Peso** | Decimal | Peso en kilogramos (> 0) |
| **Color** | String | Color o combinación de colores |

---

## PROGRAMA 1: PROGRAMACIÓN TRADICIONAL

### 📁 Ubicación
```
programacion_tradicional/
└── tradicional.py
```

### 🎯 Concepto

La **Programación Tradicional (procedural)** se basa en:
- **Variables**: almacenan datos de forma global o local
- **Funciones**: bloques de código reutilizables que realizan tareas específicas
- **Estructuras de datos**: diccionarios/tuplas para agrupar información relacionada
- **NO utiliza clases ni objetos**

### 🛠️ Funciones Principales

#### 1. `solicitar_datos()`
```python
def solicitar_datos():
    """Pide al usuario los datos de una mascota y los devuelve como diccionario."""
```

**Propósito**: 
- Solicita los datos de una nueva mascota por teclado
- Valida cada entrada (no vacío, tipo correcto, valores válidos)
- Devuelve un diccionario con la información

**Validaciones**:
- Nombre y color no pueden estar vacíos
- Edad debe ser un entero no negativo
- Peso debe ser un número positivo (decimal)

**Retorna**: `dict` con claves: `nombre`, `especie`, `edad`, `peso`, `color`

---

#### 2. `mostrar_informacion(mascota)`
```python
def mostrar_informacion(mascota):
    """Recibe un diccionario con la información de la mascota y la muestra formateada."""
```

**Propósito**:
- Recibe un diccionario (mascota)
- Imprime la información de forma legible y organizada

**Entrada**: diccionario con datos de la mascota

**Salida**: impresión formateada en consola

---

#### 3. `mostrar_todas_mascotas(mascotas)`
```python
def mostrar_todas_mascotas(mascotas):
    """Muestra la información de todas las mascotas registradas."""
```

**Propósito**:
- Itera sobre la lista de mascotas
- Muestra la información de cada una
- Maneja el caso cuando la lista está vacía

**Entrada**: lista de diccionarios (mascotas)

**Salida**: impresión en consola

---

#### 4. `mostrar_menu()`
```python
def mostrar_menu():
    """Muestra el menú de opciones."""
```

**Propósito**:
- Imprime un menú interactivo con opciones
- Facilita la navegación del usuario

---

#### 5. `main()`
```python
def main():
    """Controla el flujo principal del programa."""
```

**Propósito**:
- **Punto de entrada** del programa
- Crea una lista vacía para almacenar mascotas
- Implementa un **bucle infinito** que:
  1. Muestra el menú
  2. Lee la opción del usuario
  3. Ejecuta la acción correspondiente
  4. Termina cuando el usuario selecciona "Salir"

**Lógica del menú**:
- **Opción 1**: Llamar a `solicitar_datos()` y agregar el resultado a la lista
- **Opción 2**: Llamar a `mostrar_todas_mascotas()`
- **Opción 3**: Salir del programa

---

### 📊 Flujo de Ejecución (Diagrama Conceptual)

```
Inicio
  ↓
[Inicializar lista vacía de mascotas]
  ↓
┌─ Mostrar Menú
│  ├─ Opción 1 (Registrar)
│  │  ├─ Llamar solicitar_datos()
│  │  ├─ Validar entrada
│  │  └─ Agregar diccionario a lista
│  │
│  ├─ Opción 2 (Mostrar)
│  │  └─ Iterar lista y mostrar cada mascota
│  │
│  └─ Opción 3 (Salir)
│     └─ Romper bucle → Fin
└─ Repetir (mientras opción ≠ 3)
```

---

### 💾 Estructura de Datos

```python
# Datos en memoria usando diccionarios:
mascotas = [
    {
        "nombre": "Luna",
        "especie": "Gato",
        "edad": 2,
        "peso": 15.5,
        "color": "Negro"
    },
    {
        "nombre": "Max",
        "especie": "Perro",
        "edad": 5,
        "peso": 25.0,
        "color": "Marrón"
    }
]
```

---

### ⚙️ Ventajas y Desventajas

| Ventajas | Desventajas |
|----------|------------|
| ✓ Simple de entender para principiantes | ✗ Difícil de mantener con datos complejos |
| ✓ Flexible con funciones reutilizables | ✗ No hay encapsulación de datos |
| ✓ Rápido para prototipos pequeños | ✗ Propenso a errores si se modifica la estructura |
| | ✗ No ofrece organización clara para datos relacionados |

---

---

## PROGRAMA 2: PROGRAMACIÓN ORIENTADA A OBJETOS

### 📁 Ubicación
```
programacion_poo/
├── main.py      (punto de entrada del programa)
└── mascota.py   (definición de la clase Mascota)
```

### 🎯 Concepto

La **Programación Orientada a Objetos (POO)** se basa en:
- **Clases**: plantillas o "moldes" que definen objetos
- **Objetos**: instancias de una clase con **atributos** y **métodos**
- **Encapsulación**: agrupar datos y funciones relacionadas
- **Reutilización y mantenimiento** mejorados

---

### 📦 Archivo: `mascota.py`

Define la **clase Mascota** que modela una mascota.

#### Definición de la Clase

```python
class Mascota:
    """Clase que representa una mascota con nombre, especie, edad, peso y color."""
```

---

#### 🔹 Constructor: `__init__(self, nombre, especie, edad, peso, color)`

```python
def __init__(self, nombre: str, especie: str, edad: int, peso: float, color: str):
    self.nombre = nombre
    self.especie = especie
    self.edad = edad
    self.peso = peso
    self.color = color
```

**Propósito**:
- Se ejecuta automáticamente cuando se crea un objeto de la clase
- Inicializa los **atributos** (características) del objeto

**Parámetros**:
- `self`: referencia al objeto actual
- `nombre`, `especie`, `edad`, `peso`, `color`: datos de la mascota

**Atributos creados**:
- `self.nombre`: almacena el nombre
- `self.especie`: almacena la especie
- `self.edad`: almacena la edad
- `self.peso`: almacena el peso
- `self.color`: almacena el color

**Ejemplo de uso**:
```python
# Crear un objeto Mascota
luna = Mascota("Luna", "Gato", 2, 15.5, "Negro")
# Ahora luna.nombre = "Luna", luna.edad = 2, etc.
```

---

#### 🔹 Método: `mostrar_informacion(self)`

```python
def mostrar_informacion(self):
    """Muestra la información de la mascota de forma organizada."""
    print('----- Información de la mascota -----')
    print(f"Nombre : {self.nombre}")
    print(f"Especie: {self.especie}")
    print(f"Edad   : {self.edad} años")
    print(f"Peso   : {self.peso} kg")
    print(f"Color  : {self.color}")
    print('------------------------------------')
```

**Propósito**:
- Muestra los datos del objeto de forma formateada
- Accede a los atributos usando `self.atributo`

**Diferencia con la versión tradicional**:
- En tradicional: recibe un diccionario como parámetro
- En POO: accede a sus propios datos (self)

**Ejemplo de uso**:
```python
luna.mostrar_informacion()
# Salida:
# ----- Información de la mascota -----
# Nombre : Luna
# Especie: Gato
# Edad   : 2 años
# Peso   : 15.5 kg
# Color  : Negro
# ------------------------------------
```

---

#### 🔹 Método: `hacer_sonido(self)`

```python
def hacer_sonido(self):
    """Devuelve (y muestra) un sonido representativo según la especie."""
    especie_lower = self.especie.strip().lower()
    if 'perro' in especie_lower:
        sonido = '¡Guau!'
    elif 'gato' in especie_lower:
        sonido = '¡Miau!'
    elif 'paj' in especie_lower or 'ave' in especie_lower or 'pájaro' in especie_lower:
        sonido = '¡Pío!'
    else:
        sonido = '¡...!'
    
    print(f"{self.nombre} hace: {sonido}")
    return sonido
```

**Propósito**:
- Implementa un comportamiento específico según la especie
- Demuestra que los **métodos pueden tener lógica** (no solo mostrar datos)

**Lógica**:
- Convierte la especie a minúsculas para comparación
- Verifica si contiene palabras clave
- Retorna un sonido representativo

**Ejemplo de uso**:
```python
luna.hacer_sonido()  # Salida: Luna hace: ¡Miau!
max_obj.hacer_sonido()  # Salida: Max hace: ¡Guau!
```

---

### 📲 Archivo: `main.py`

Punto de entrada del programa que utiliza la clase Mascota.

#### Función: `solicitar_mascota_por_usuario(indice=1)`

```python
def solicitar_mascota_por_usuario(indice=1):
    """Solicita datos al usuario y crea un objeto Mascota."""
    # Solicita datos y valida...
    return Mascota(nombre, especie, edad, peso, color)
```

**Propósito**:
- Solicita datos interactivamente
- Valida cada entrada
- **Crea y devuelve un objeto Mascota**

**Diferencia con tradicional**:
- Devuelve un objeto (instancia de clase)
- No un diccionario

---

#### Función: `mostrar_todas_mascotas(mascotas)`

```python
def mostrar_todas_mascotas(mascotas):
    """Muestra la información de todas las mascotas registradas."""
    if not mascotas:
        print("\n¡No hay mascotas registradas aún!\n")
        return

    print(f"\n===== MASCOTAS REGISTRADAS ({len(mascotas)}) =====")
    for i, m in enumerate(mascotas, 1):
        print(f"\n--- Mascota #{i} ---")
        m.mostrar_informacion()      # Llama al método del objeto
        m.hacer_sonido()              # Llama al método del objeto
    print("=" * 40 + "\n")
```

**Propósito**:
- Recorre la lista de objetos Mascota
- Llama a los métodos de cada objeto

**Diferencia con tradicional**:
- Llama `m.mostrar_informacion()` (método del objeto)
- En lugar de `mostrar_informacion(m)` (función con parámetro)

---

#### Función: `main()`

```python
def main():
    """Controla el flujo principal del programa."""
    mascotas = []
    contador = 1

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            m = solicitar_mascota_por_usuario(contador)
            mascotas.append(m)
            contador += 1

        elif opcion == "2":
            mostrar_todas_mascotas(mascotas)

        elif opcion == "3":
            print("\n¡Hasta luego!")
            break

        else:
            print("\n✗ Opción inválida.")
```

**Propósito**:
- **Punto de entrada** del programa
- Maneja la lógica de menú
- Almacena **objetos** en lugar de diccionarios

---

### 📊 Flujo de Ejecución (Diagrama Conceptual)

```
Inicio
  ↓
[Inicializar lista vacía de mascotas]
  ↓
┌─ Mostrar Menú
│  ├─ Opción 1 (Registrar)
│  │  ├─ Solicitar datos
│  │  ├─ CREAR OBJETO: m = Mascota(...)
│  │  └─ mascotas.append(m)
│  │
│  ├─ Opción 2 (Mostrar)
│  │  └─ Para cada objeto m en mascotas:
│  │     ├─ m.mostrar_informacion()  (llamar método)
│  │     └─ m.hacer_sonido()         (llamar método)
│  │
│  └─ Opción 3 (Salir)
│     └─ break → Fin
└─ Repetir (mientras opción ≠ 3)
```

---

### 💾 Estructura de Datos con POO

```python
# Los datos se almacenan como objetos:
mascotas = [
    Mascota("Luna", "Gato", 2, 15.5, "Negro"),
    Mascota("Max", "Perro", 5, 25.0, "Marrón")
]

# Cada objeto tiene su propia copia de atributos:
# mascotas[0].nombre = "Luna"
# mascotas[0].edad = 2
# mascotas[1].nombre = "Max"
# mascotas[1].edad = 5
```

---

### ⚙️ Ventajas y Desventajas

| Ventajas | Desventajas |
|----------|------------|
| ✓ Datos y métodos organizados en objetos | ✗ Requiere más código inicial |
| ✓ Cada mascota es un objeto independiente | ✗ Curva de aprendizaje más pronunciada |
| ✓ Encapsulación: datos + comportamiento | ✗ Overhead de memoria por objetos |
| ✓ Fácil de extender y mantener | |
| ✓ Reutilización clara de código | |
| ✓ Mejor para sistemas grandes | |

---

---

## COMPARACIÓN: TRADICIONAL vs POO

### 1️⃣ Creación de Datos

**Tradicional**:
```python
mascota = solicitar_datos()  # devuelve dict
# mascota = {"nombre": "Luna", "especie": "Gato", ...}
```

**POO**:
```python
mascota = solicitar_mascota_por_usuario(1)  # devuelve Mascota
# mascota es un objeto con atributos: mascota.nombre, mascota.edad, ...
```

---

### 2️⃣ Acceso a Datos

**Tradicional**:
```python
print(mascota['nombre'])  # acceso con clave de diccionario
```

**POO**:
```python
print(mascota.nombre)  # acceso con atributo del objeto
```

---

### 3️⃣ Mostrar Información

**Tradicional**:
```python
mostrar_informacion(mascota)  # función recibe diccionario
```

**POO**:
```python
mascota.mostrar_informacion()  # método del objeto
```

---

### 4️⃣ Comportamiento (Sonidos)

**Tradicional**: 
- No implementado (solo muestra datos)

**POO**:
```python
mascota.hacer_sonido()  # método específico del objeto
```

---

### 5️⃣ Escalabilidad

| Aspecto | Tradicional | POO |
|--------|-------------|-----|
| Agregar nueva acción | Crear nueva función | Agregar nuevo método a clase |
| Múltiples mascotas | Lista de diccionarios | Lista de objetos independientes |
| Validación de dato | Dentro de la función | Dentro del constructor (__init__) |

---

## FLUJO DE USUARIO

### Interacción Común

```
1. Programa inicia → Muestra menú
2. Usuario selecciona "1" → Registra mascota
3. Programa solicita: Nombre, Especie, Edad, Peso, Color
4. Mascota se almacena (sin mostrar)
5. Menú vuelve a aparecer
6. Usuario vuelve a opción "1" → Registra otra mascota
7. Usuario selecciona "2" → Se muestran todas las mascotas
   - Información de cada mascota
   - Sonido que hace cada mascota
8. Usuario selecciona "3" → Programa termina
```

---

## VALIDACIONES IMPLEMENTADAS

### En ambos programas:

✅ **Nombre y Color**:
- No pueden estar vacíos
- Se solicita repetidamente si son inválidos

✅ **Edad**:
- Debe ser entero
- No puede ser negativo
- Se pide de nuevo si falla

✅ **Peso**:
- Debe ser número decimal (float)
- Debe ser positivo (> 0)
- Se pide de nuevo si falla

✅ **Opción del menú**:
- Solo acepta 1, 2 o 3
- Muestra error si es inválida

---

## PUNTOS CLAVE DE APRENDIZAJE

### Programación Tradicional
- 📌 Las funciones son bloques independientes
- 📌 Los datos se pasan como parámetros
- 📌 Las responsabilidades están dispersas
- 📌 Útil para programas pequeños y simples

### Programación Orientada a Objetos
- 📌 Una clase agrupa datos (atributos) y comportamiento (métodos)
- 📌 Cada objeto es independiente con su propia copia de datos
- 📌 Los métodos pueden acceder a los atributos del objeto (self)
- 📌 Mejor para mantener y extender programas grandes

---

## POSIBLES EXTENSIONES

### Agregar a la clase Mascota:

```python
# Método: cumplir años
def cumplir_anios(self):
    self.edad += 1
    print(f"¡{self.nombre} ha cumplido {self.edad} años!")

# Método: verificar si es adulto
def es_adulto(self):
    return self.edad >= 3

# Método: cambiar peso
def cambiar_peso(self, nuevo_peso):
    if nuevo_peso > 0:
        self.peso = nuevo_peso
    else:
        print("El peso debe ser positivo")
```

### Agregar al menú:

```python
4. Buscar mascota por nombre
5. Editar información de mascota
6. Eliminar mascota
7. Guardar datos en archivo
8. Cargar datos desde archivo
```

---

## CONCLUSIÓN

Ambos programas **resuelven el mismo problema**, pero de maneras fundamentalmente diferentes:

- **Tradicional**: enfoque procedural, simple pero limitado
- **POO**: enfoque organizado, escalable y mantenible

Para este ejercicio académico, la **POO demuestra conceptos clave** como:
- Encapsulación
- Abstracción
- Modularidad
- Reutilización

Conforme los proyectos crecen en complejidad, los beneficios de POO se hacen más evidentes.

---

**Creado**: Junio 2026  
**Asignatura**: Programación Orientada a Objetos  
**Universidad**: Universidad Estatal Amazónica  
**Alumno**: Dayvis Calderón

