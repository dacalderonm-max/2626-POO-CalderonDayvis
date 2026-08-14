# TareaSemana9 - Sistema de Restaurante con Persistencia JSON

## 🎯 Descripción General

Sistema completo de gestión de restaurante que clona y mejora el software de **TareaSemana8**, implementando **persistencia de datos en archivos JSON** con una estructura tipo **diccionario**.

## ✨ Características Principales

### ✅ Clonación de TareaSemana8
- Base sólida de modelos y servicios
- Interfaz interactiva mejorada
- Lógica de validación robusta

### ✅ Persistencia en JSON
- Guardar productos en `datos/productos.json`
- Guardar clientes en `datos/clientes.json`
- Recuperar datos entre sesiones
- Estructura tipo diccionario

### ✅ Serialización Bidireccional
- Convertir objetos → diccionarios (JSON)
- Convertir diccionarios → objetos (desde JSON)
- Preservación completa de datos
- Codificación UTF-8

## 📁 Estructura del Proyecto

```
TareaSemana9/
├── 📖 GUIA_RAPIDA.md                    ← Comienza aquí
├── 📖 DOCUMENTACION_TECNICA.md          ← Detalles técnicos
├── 📖 RESUMEN_PROYECTO.md               ← Resumen ejecutivo
├── 📖 VERIFICACION_REQUISITOS.md        ← Checklist de requisitos
│
└── restaurante_app/
    ├── 🚀 main.py                       ← EJECUTAR ESTE ARCHIVO
    ├── 🧪 pruebas.py                    ← Script de pruebas
    ├── 📖 README.md                     ← Documentación detallada
    │
    ├── modelos/
    │   ├── producto.py                  ← Modelo con serialización
    │   └── cliente.py                   ← Modelo con serialización
    │
    ├── servicios/
    │   ├── restaurante.py               ← Lógica de negocio
    │   └── gestor_datos.py              ← Persistencia JSON
    │
    └── datos/                           ← Se crea automáticamente
        ├── productos.json               ← Datos guardados
        └── clientes.json                ← Datos guardados
```

## 🚀 Inicio Rápido

### Opción 1: Interfaz Interactiva
```bash
cd restaurante_app
python main.py
```
Menú interactivo con 8 opciones para gestionar datos.

### Opción 2: Ejecutar Pruebas
```bash
cd restaurante_app
python pruebas.py
```
Ejecuta 5 pruebas automatizadas que validan todas las funcionalidades.

## 📋 Menú Principal (8 opciones)

```
1. Registrar producto       → Agregar nuevo producto
2. Registrar cliente        → Agregar nuevo cliente
3. Listar productos         → Ver todos los productos en memoria
4. Listar clientes          → Ver todos los clientes en memoria
5. Guardar datos en JSON    → Persistir datos a archivos
6. Cargar datos desde JSON  → Recuperar datos guardados
7. Limpiar datos memoria    → Borrar datos en memoria (no JSON)
8. Salir                    → Terminar el programa
```

## 📊 Estructura de Datos JSON

### productos.json
```json
[
    {
        "codigo": "P001",
        "nombre": "Pizza Margarita",
        "categoria": "Platos Principales",
        "precio": 12.5,
        "tipo": "Producto"
    }
]
```

### clientes.json
```json
[
    {
        "identificacion": "1234567890",
        "nombre": "Juan Pérez",
        "correo": "juan@example.com"
    }
]
```

## 🔄 Ciclo de Datos

```
Entrada de Usuario
      ↓
Validación
      ↓
Crear Objeto (Producto/Cliente)
      ↓
Gestionar en Memoria (Restaurante)
      ↓
┌─────┴──────────┐
│ ¿Guardar JSON? │
└─────┬──────────┘
      │
   SI │─→ Convertir a diccionario
      │   Serializar con JSON
      │   Guardar en archivo
      │
   NO └─→ Solo en memoria

Próxima ejecución:
      ↓
Cargar desde JSON (opción 6)
      ↓
Recuperar en memoria
```

## 🧪 Pruebas Ejecutadas

```
✅ PRUEBA 1: Creación de Modelos
   └─ Crear objetos y convertir a diccionarios

✅ PRUEBA 2: Persistencia en JSON
   └─ Guardar datos en archivos

✅ PRUEBA 3: Carga desde JSON
   └─ Recuperar datos desde archivos

✅ PRUEBA 4: Validación de Duplicados
   └─ Prevenir códigos e IDs duplicados

✅ PRUEBA 5: Estructura JSON
   └─ Validar formato y campos
```

**Resultado**: ✅ TODAS LAS PRUEBAS PASADAS

## 💡 Métodos Principales

### Modelo Producto
```python
# Crear producto
producto = Producto("P001", "Pizza", "Platos", 12.50)

# Convertir a diccionario (para JSON)
diccionario = producto.a_diccionario()

# Recuperar desde diccionario
producto = Producto.desde_diccionario(diccionario)
```

### Modelo Cliente
```python
# Crear cliente
cliente = Cliente("123456", "Juan", "juan@email.com")

# Convertir a diccionario (para JSON)
diccionario = cliente.a_diccionario()

# Recuperar desde diccionario
cliente = Cliente.desde_diccionario(diccionario)
```

### GestorDatos (NUEVO)
```python
# Inicializar
gestor = GestorDatos()

# Guardar
exito, msg = gestor.guardar_productos(productos)
exito, msg = gestor.guardar_clientes(clientes)

# Cargar
exito, productos, msg = gestor.cargar_productos()
exito, clientes, msg = gestor.cargar_clientes()
```

## 🎯 Casos de Uso

### Caso 1: Guardar Datos Nuevos
1. Opción `1` - Registrar producto
2. Opción `2` - Registrar cliente
3. Opción `5` - Guardar en JSON
4. Opción `8` - Salir

### Caso 2: Cargar y Usar Datos Guardados
1. Opción `6` - Cargar desde JSON
2. Opción `3` - Ver productos
3. Opción `4` - Ver clientes
4. Opción `8` - Salir

### Caso 3: Limpiar y Recargar
1. Opción `7` - Limpiar memoria
2. Opción `6` - Cargar desde JSON
3. Opción `1` - Agregar nuevos datos
4. Opción `5` - Guardar cambios

## 🎓 Conceptos Aplicados

- ✅ **Serialización** - Convertir objetos a JSON
- ✅ **Deserialización** - Convertir JSON a objetos
- ✅ **Persistencia** - Guardar datos en disco
- ✅ **POO** - Programación Orientada a Objetos
- ✅ **SOLID** - Principios de diseño
- ✅ **Validación** - Entrada robusta
- ✅ **Manejo de Archivos** - I/O en Python

## 📚 Documentación

Este proyecto incluye **5 documentos**:

1. **GUIA_RAPIDA.md** ⭐ Comienza aquí
   - Instrucciones de inicio rápido
   - Ejemplos prácticos
   - FAQs

2. **DOCUMENTACION_TECNICA.md**
   - Arquitectura del sistema
   - Métodos de serialización
   - Principios SOLID

3. **RESUMEN_PROYECTO.md**
   - Objetivos cumplidos
   - Características
   - Comparativa con TareaSemana8

4. **VERIFICACION_REQUISITOS.md**
   - Checklist de requisitos
   - Resultados de pruebas
   - Criterios de aceptación

5. **restaurante_app/README.md**
   - Guía detallada de uso
   - Ejemplos de código
   - Mejoras futuras

## 🔑 Archivos Clave

| Archivo | Descripción |
|---------|-------------|
| `main.py` | Interfaz interactiva principal |
| `pruebas.py` | 5 pruebas automatizadas |
| `modelos/producto.py` | Modelo con serialización |
| `modelos/cliente.py` | Modelo con serialización |
| `servicios/restaurante.py` | Lógica de negocio |
| `servicios/gestor_datos.py` | **NUEVO** - Persistencia JSON |

## ✅ Requisitos Cumplidos

- [x] Clonar software de TareaSemana8
- [x] Implementar persistencia JSON
- [x] Usar estructura tipo diccionario
- [x] Métodos de serialización
- [x] Métodos de deserialización
- [x] Validación robusta
- [x] Documentación completa
- [x] Pruebas automatizadas

## 🎉 Mejoras sobre TareaSemana8

| Aspecto | TareaSemana8 | TareaSemana9 |
|--------|---------|-----------|
| **Almacenamiento** | Solo memoria | Memory + JSON |
| **Persistencia** | ❌ No | ✅ Sí |
| **Serialización** | ❌ No | ✅ Sí |
| **Menú** | 6 opciones | 8 opciones |
| **GestorDatos** | ❌ No | ✅ Nuevo |
| **Pruebas** | Básicas | 5 completas |

## 🚀 Próximas Mejoras Sugeridas

- [ ] Búsqueda avanzada por categoría
- [ ] CRUD completo (actualizar/eliminar)
- [ ] Exportar a CSV
- [ ] Interfaz gráfica (GUI)
- [ ] Base de datos SQLite
- [ ] API REST con Flask
- [ ] Validación de email
- [ ] Sistema de pedidos

## 📞 Información

**Estudiante**: Dayvis Calderón  
**Asignatura**: Programación Orientada a Objetos  
**Institución**: Universidad Estatal Amazónica  
**Semana**: 9  
**Fecha**: 2026-08-14  
**Estado**: ✅ COMPLETADO

## 🎯 Comienza Aquí

### 1️⃣ Leer la guía rápida
```
GUIA_RAPIDA.md
```

### 2️⃣ Ejecutar el programa
```bash
cd restaurante_app
python main.py
```

### 3️⃣ Ejecutar pruebas
```bash
cd restaurante_app
python pruebas.py
```

### 4️⃣ Explorar el código
```
modelos/     - Estructura de datos
servicios/   - Lógica de negocio
datos/       - Archivos JSON generados
```

---

**¡Listo para usar!** 🚀

El sistema está completamente funcional con persistencia JSON, validación robusta y documentación exhaustiva.


