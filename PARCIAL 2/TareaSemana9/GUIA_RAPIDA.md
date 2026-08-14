# Guía de Inicio Rápido - TareaSemana9

## 🚀 Inicio Rápido (2 minutos)

### 1. Ir a la carpeta
```bash
cd restaurante_app
```

### 2. Ejecutar el programa
```bash
python main.py
```

### 3. Ver el menú interactivo
El programa mostrará 8 opciones:
- 1-2: Registrar datos
- 3-4: Ver datos en memoria
- 5-6: Guardar/cargar JSON
- 7: Limpiar memoria
- 8: Salir

## 📋 Ejemplo de Uso

### Paso 1: Registrar un Producto
```
Opción: 1
Código: P001
Nombre: Pizza Margarita
Categoría: Platos Principales
Precio: 12.50
```

### Paso 2: Registrar un Cliente
```
Opción: 2
Identificación: 1234567890
Nombre: Juan Pérez
Correo: juan@example.com
```

### Paso 3: Guardar en JSON
```
Opción: 5
```
✓ Los datos se guardan en:
- `datos/productos.json`
- `datos/clientes.json`

### Paso 4: Cargar desde JSON
```
Opción: 6
```
✓ Los datos se cargan de los archivos

## 🧪 Ejecutar Pruebas

```bash
python pruebas.py
```

Esto ejecuta 5 pruebas automáticas que validan:
- ✓ Creación de objetos
- ✓ Conversión a diccionarios
- ✓ Guardado en JSON
- ✓ Carga desde JSON
- ✓ Validación de duplicados

## 📁 Estructura de Carpetas

```
restaurante_app/
├── main.py                  ← Ejecutar este archivo
├── pruebas.py               ← Pruebas automáticas
├── modelos/
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── restaurante.py
│   └── gestor_datos.py
└── datos/                   ← Se crea automáticamente
    ├── productos.json
    └── clientes.json
```

## 🔄 Ciclo de Vida de Datos

```
Entrada del usuario
        ↓
Crear objeto (Producto/Cliente)
        ↓
Guardar en memoria (Restaurante)
        ↓
        ├─ Ver en pantalla (opción 3-4)
        ├─ Guardar JSON (opción 5)
        ├─ Cargar JSON (opción 6)
        └─ Salir (opción 8)
```

## 💾 Archivos JSON Generados

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

## ⚙️ Validaciones Implementadas

✓ No permite códigos de producto duplicados  
✓ No permite identificaciones de cliente duplicadas  
✓ No permite campos vacíos  
✓ Valida que el precio sea positivo  
✓ Valida entrada de usuario

## 🎯 Casos de Uso Principales

### Caso 1: Guardar datos nuevos
1. Opción 1 → Registrar producto
2. Opción 2 → Registrar cliente
3. Opción 5 → Guardar en JSON

### Caso 2: Cargar datos guardados
1. Opción 6 → Cargar desde JSON
2. Opción 3 → Ver productos cargados
3. Opción 4 → Ver clientes cargados

### Caso 3: Actualizar datos
1. Opción 7 → Limpiar datos en memoria
2. Opción 6 → Cargar datos desde JSON
3. Opción 1/2 → Agregar nuevos datos
4. Opción 5 → Guardar cambios

## ❓ Preguntas Frecuentes

**P: ¿Dónde se guardan los datos?**  
R: En la carpeta `datos/` dentro de `restaurante_app/`

**P: ¿Qué pasa si elimino los archivos JSON?**  
R: Se crearán nuevos vacíos al guardar

**P: ¿Puedo editar los archivos JSON directamente?**  
R: Sí, pero respeta la estructura mostrada arriba

**P: ¿Qué pasa si cierro el programa sin guardar?**  
R: Se perderán los datos en memoria (el programa pregunta al salir)

**P: ¿Cómo agrego más datos?**  
R: Usa las opciones 1-2 del menú para cada nuevo registro

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError"
```
Solución: Asegúrate de estar en el directorio restaurante_app/
cd restaurante_app
python main.py
```

### Error: "No hay productos/clientes registrados"
```
Solución: Primero registra datos (opciones 1-2) o carga desde JSON (opción 6)
```

### Archivos JSON corrupto
```
Solución: 
1. Elimina el archivo corrupto
2. Opción 5: Guardar nuevamente
3. El archivo se recrea correctamente
```

## 📚 Recursos Adicionales

- **README.md**: Documentación completa
- **DOCUMENTACION_TECNICA.md**: Detalles técnicos
- **pruebas.py**: Ejemplo de código
- **main.py**: Código de interfaz

## ✅ Checklist de Funcionalidad

- [x] Registrar productos
- [x] Registrar clientes
- [x] Listar productos
- [x] Listar clientes
- [x] Guardar en JSON
- [x] Cargar desde JSON
- [x] Validar duplicados
- [x] Validar entrada de usuario
- [x] Convertir objetos a diccionarios
- [x] Convertir diccionarios a objetos
- [x] Pruebas automáticas

## 🎓 Conceptos Aprendidos

- ✅ Serialización de objetos
- ✅ Persistencia en JSON
- ✅ Estructura tipo diccionario
- ✅ Métodos de conversión
- ✅ Gestión de archivos
- ✅ Principios SOLID
- ✅ POO con herencia

---

**¡Listo para empezar!** 🚀

Ejecuta: `python main.py`


