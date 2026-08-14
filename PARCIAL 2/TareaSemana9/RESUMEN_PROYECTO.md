# Resumen del Proyecto - TareaSemana9

## 🎯 Objetivo del Proyecto

Clonar el software de **TareaSemana8** (Sistema de Restaurante) e implementar **persistencia de datos en archivos JSON** utilizando una estructura tipo **diccionario**.

## ✅ Objetivos Cumplidos

### 1. Clonación de TareaSemana8
- ✅ Se replicó la estructura de clases (Producto, Cliente)
- ✅ Se mantuvieron los servicios base (Restaurante)
- ✅ Se preservó la lógica de validación

### 2. Implementación de Persistencia JSON
- ✅ Método `a_diccionario()` en modelos
- ✅ Método `desde_diccionario()` en modelos
- ✅ Módulo GestorDatos para I/O
- ✅ Conversión bidireccional de datos

### 3. Estructura de Diccionarios
- ✅ Productos como diccionarios con 5 campos
- ✅ Clientes como diccionarios con 3 campos
- ✅ Formato JSON legible y estructurado

### 4. Mejoras Adicionales
- ✅ Menú expandido (8 opciones)
- ✅ Validación robusta
- ✅ Sistema de pruebas
- ✅ Documentación completa

## 📦 Componentes del Sistema

### Capa de Datos (Modelos)
```
Producto
├── código (str)
├── nombre (str)
├── categoría (str)
├── precio (float)
└── Métodos JSON: a_diccionario(), desde_diccionario()

Cliente
├── identificación (str)
├── nombre (str)
├── correo (str)
└── Métodos JSON: a_diccionario(), desde_diccionario()
```

### Capa de Lógica (Servicios)
```
Restaurante
├── Gestión de productos
├── Gestión de clientes
└── Validaciones

GestorDatos (NUEVO)
├── Guardar en JSON
├── Cargar desde JSON
└── Gestionar archivos
```

### Capa de Presentación (Interfaz)
```
main.py
├── Menú interactivo
├── Entrada de usuario
├── Validación de datos
└── Orquestación de servicios
```

## 🗂️ Estructura de Archivos JSON

### Formato de Productos
```json
{
    "codigo": "P001",
    "nombre": "Pizza Margarita",
    "categoria": "Platos Principales",
    "precio": 12.5,
    "tipo": "Producto"
}
```

### Formato de Clientes
```json
{
    "identificacion": "1234567890",
    "nombre": "Juan Pérez",
    "correo": "juan@example.com"
}
```

## 🔄 Flujo de Serialización

### Guardar Datos (Objeto → JSON)
```
1. Crear objeto Producto/Cliente
2. Llamar a_diccionario()
3. Convertir lista a diccionarios
4. Serializar con json.dump()
5. Guardar en archivo .json
```

### Cargar Datos (JSON → Objeto)
```
1. Leer archivo .json
2. Parsear con json.load()
3. Convertir diccionarios
4. Llamar desde_diccionario()
5. Crear objetos en memoria
```

## 📊 Estadísticas del Proyecto

| Métrica | Valor |
|---------|-------|
| Archivos Python creados | 8 |
| Líneas de código | ~800 |
| Métodos implementados | 30+ |
| Pruebas automatizadas | 5 |
| Opciones de menú | 8 |
| Principios SOLID | 4 |

## 🚀 Funcionalidades

### Gestión de Productos
- ✅ Registrar nuevo producto
- ✅ Listar todos los productos
- ✅ Validar códigos duplicados
- ✅ Guardar en JSON
- ✅ Cargar desde JSON

### Gestión de Clientes
- ✅ Registrar nuevo cliente
- ✅ Listar todos los clientes
- ✅ Validar IDs duplicados
- ✅ Guardar en JSON
- ✅ Cargar desde JSON

### Persistencia de Datos
- ✅ Crear archivos JSON automáticamente
- ✅ Convertir objetos a diccionarios
- ✅ Convertir diccionarios a objetos
- ✅ Recuperar datos entre sesiones
- ✅ Validar integridad de datos

## 🧪 Pruebas Realizadas

### Prueba 1: Creación de Modelos ✅
- Verificar creación de objetos
- Verificar conversión a diccionarios
- Verificar recuperación desde diccionarios

### Prueba 2: Persistencia JSON ✅
- Guardar datos en archivos
- Verificar integridad de archivos
- Validar estructura JSON

### Prueba 3: Carga desde JSON ✅
- Cargar datos desde archivos
- Recrear objetos correctamente
- Verificar cantidad de datos

### Prueba 4: Validación de Duplicados ✅
- Prevenir códigos duplicados
- Prevenir IDs duplicadas
- Mostrar mensajes de error

### Prueba 5: Estructura JSON ✅
- Verificar formato correcto
- Validar campos requeridos
- Confirmar codificación UTF-8

## 📈 Comparativa: TareaSemana8 vs TareaSemana9

### TareaSemana8 (Base)
- ❌ Solo en memoria
- ❌ Datos se pierden al cerrar
- ❌ Sin serialización
- ✅ Validación básica
- ✅ Estructura OOP

### TareaSemana9 (Mejorado)
- ✅ Memoria + Persistencia JSON
- ✅ Datos recuperables entre sesiones
- ✅ Serialización completa
- ✅ Validación robusta
- ✅ Estructura OOP mejorada
- ✅ Gestor de datos específico

## 🎓 Conceptos de Programación Aplicados

### Programación Orientada a Objetos (POO)
- ✅ Encapsulación
- ✅ Herencia (si aplicable)
- ✅ Polimorfismo
- ✅ Abstracción

### Principios SOLID
- ✅ Single Responsibility Principle
- ✅ Open/Closed Principle
- ✅ Dependency Inversion
- ✅ Interface Segregation

### Estructuras de Datos
- ✅ Listas (List[Producto], List[Cliente])
- ✅ Diccionarios (JSON)
- ✅ Tuplas (return values)
- ✅ Tipos genéricos

### Gestión de Archivos
- ✅ Lectura/Escritura
- ✅ Codificación UTF-8
- ✅ Manejo de excepciones
- ✅ Creación de directorios

## 📝 Documentación Generada

1. **README.md** (restaurante_app/) - Guía de usuario
2. **DOCUMENTACION_TECNICA.md** - Detalles técnicos
3. **GUIA_RAPIDA.md** - Inicio rápido
4. **RESUMEN_PROYECTO.md** - Este archivo
5. **Docstrings** en cada método
6. **pruebas.py** - Ejemplos de uso

## 🎯 Caso de Uso Principal

**Escenario**: Un restaurante necesita guardar información de productos y clientes.

1. **Usuario registra datos** (opciones 1-2)
2. **Sistema valida** (sin duplicados)
3. **Usuario guarda** (opción 5)
4. **Datos se escriben en JSON** (persistencia)
5. **Usuario cierra programa**
6. **Próxima sesión, usuario carga** (opción 6)
7. **Datos recuperados** (intactos)

## 🔧 Configuración

### Rutas por defecto
```
datos/productos.json    # Archivo de productos
datos/clientes.json     # Archivo de clientes
```

### Personalización
```python
gestor = GestorDatos(
    ruta_productos="mi_ruta/productos.json",
    ruta_clientes="mi_ruta/clientes.json"
)
```

## 💡 Patrones de Diseño Utilizados

1. **Data Transfer Object (DTO)**
   - Los diccionarios actúan como DTOs
   - Facilita serialización

2. **Service Locator**
   - GestorDatos centraliza I/O

3. **Factory Pattern**
   - `desde_diccionario()` crea objetos

4. **Repository Pattern**
   - GestorDatos actúa como repositorio

## 📚 Estructura de Carpetas Final

```
TareaSemana9/
├── GUIA_RAPIDA.md
├── DOCUMENTACION_TECNICA.md
├── RESUMEN_PROYECTO.md
└── restaurante_app/
    ├── __init__.py
    ├── main.py
    ├── pruebas.py
    ├── README.md
    ├── datos/
    │   ├── productos.json
    │   └── clientes.json
    ├── modelos/
    │   ├── __init__.py
    │   ├── producto.py
    │   └── cliente.py
    └── servicios/
        ├── __init__.py
        ├── restaurante.py
        └── gestor_datos.py
```

## ✨ Características Destacadas

### 1. Serialización Bidireccional
- Convertir objetos a JSON en ambas direcciones
- Preservar datos intactos

### 2. Validación Robusta
- Prevención de duplicados
- Validación de entrada

### 3. Gestión Automática
- Crear directorios automáticamente
- Manejar archivos elegantemente

### 4. Interfaz Amigable
- Menú claro y fácil de usar
- Mensajes informativos

### 5. Código Limpio
- Nombres descriptivos
- Documentación completa
- Principios SOLID

## 🎯 Resultados de Pruebas

```
✓ PRUEBA 1: Creación de modelos        [ÉXITO]
✓ PRUEBA 2: Persistencia en JSON       [ÉXITO]
✓ PRUEBA 3: Carga desde JSON           [ÉXITO]
✓ PRUEBA 4: Validación de duplicados   [ÉXITO]
✓ PRUEBA 5: Estructura JSON            [ÉXITO]

RESULTADO FINAL: ✅ TODAS LAS PRUEBAS PASADAS
```

## 🚀 Cómo Ejecutar

### Ejecución Interactiva
```bash
cd restaurante_app
python main.py
```

### Ejecución de Pruebas
```bash
cd restaurante_app
python pruebas.py
```

## 📖 Próximas Mejoras Sugeridas

1. **Búsqueda avanzada** - Filtrar datos
2. **CRUD completo** - Actualizar/Eliminar
3. **Interfaz gráfica** - GUI con tkinter
4. **Base de datos** - Migrar a SQLite
5. **API REST** - Exponer como servicio
6. **Exportación CSV** - Formato adicional
7. **Autenticación** - Control de acceso

## 👤 Información del Proyecto

**Estudiante**: Dayvis Calderón  
**Asignatura**: Programación Orientada a Objetos  
**Institución**: Universidad Estatal Amazónica  
**Período**: Semana 9  
**Fecha de Entrega**: 2026-08-14  
**Estado**: ✅ COMPLETADO

---

**Conclusión**: El proyecto TareaSemana9 implementa exitosamente un sistema de persistencia de datos en JSON, clonando y mejorando el trabajo de TareaSemana8 con una arquitectura robusta y extensible.


