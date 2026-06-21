# COMANDOS DE EJECUCIÓN - Sistema de Gestión de Restaurante

## 🚀 Ejecución Rápida

### **Opción 1: Programa Principal (Recomendado)**
```bash
cd restaurante_app
python main.py
```

**Qué hace**: Demuestra el funcionamiento completo del sistema
- Crea un restaurante
- Registra 8 productos en diferentes categorías
- Registra 3 clientes
- Muestra el menú categorizado
- Muestra la lista de clientes
- Crea 2 pedidos
- Demuestra método __str__()
- Aplica descuentos

**Salida esperada**: ~140 líneas de información organizada

---

### **Opción 2: Casos Avanzados (Opcional)**
```bash
cd restaurante_app
python casos_avanzados.py
```

**Qué hace**: Demuestra casos de uso más complejos
- Prevención de duplicados
- Búsqueda case-insensitive
- Cambio de disponibilidad
- Validación de clientes duplicados
- Descuentos en cascada
- Múltiples pedidos por cliente
- Cambio de estado de cliente
- Representación de objetos

**Salida esperada**: ~80 líneas de información organizada

---

## 📍 Ubicación del Proyecto

```
C:\Users\Dayvis\OneDrive - Universidad Estatal Amazónica\UEA-REPOSITORY-2626\2626-POO-CalderonDayvis\PARCIAL 1\TareaSemana4\
```

---

## 🧩 Estructura de Ejecución

### Vista Generales
```
TareaSemana4/
├── restaurante_app/               ← Carpeta de código
│   ├── modelos/
│   │   ├── producto.py
│   │   ├── cliente.py
│   │   └── __init__.py
│   ├── servicios/
│   │   ├── restaurante.py
│   │   └── __init__.py
│   ├── main.py                    ← EJECUTAR ESTE
│   └── casos_avanzados.py         ← O ESTE
└── [Archivos de documentación]
```

---

## 📝 Antes de Ejecutar

### Verificaciones Previas
- ✓ Python 3.6+ instalado
- ✓ Estar en la carpeta `restaurante_app`
- ✓ Todos los archivos `.py` presentes

### Verificar Archivos
```bash
# En Windows PowerShell
cd restaurante_app
Get-ChildItem -Recurse -Filter "*.py"
```

Debería mostrar:
- modelos/producto.py
- modelos/cliente.py
- modelos/__init__.py
- servicios/restaurante.py
- servicios/__init__.py
- main.py
- casos_avanzados.py
- __init__.py

---

## ⚙️ Pasos Detallados de Ejecución

### Paso 1: Abrir Terminal/PowerShell
```bash
# Navegar a la carpeta TareaSemana4
cd "C:\Users\Dayvis\OneDrive - Universidad Estatal Amazónica\UEA-REPOSITORY-2626\2626-POO-CalderonDayvis\PARCIAL 1\TareaSemana4"
```

### Paso 2: Entrar a la carpeta restaurante_app
```bash
cd restaurante_app
```

### Paso 3: Ejecutar el programa
```bash
python main.py
```

### Paso 4: Ver la salida
El programa imprimirá toda la información en la consola

---

## 📊 Lo que Verás al Ejecutar

### Sección 1: Información del Restaurante
```
======================================================================
SISTEMA DE GESTIÓN DE RESTAURANTE
======================================================================

Restaurante: El Sabor Amazónico
Ubicación: Puyo, Ecuador
Productos registrados: 0
Clientes registrados: 0
```

### Sección 2: Registro de Productos
```
REGISTRANDO PRODUCTOS
✓ Producto registrado: Ceviche de Tilapia
✓ Producto registrado: Yuca frita con queso
✓ Producto registrado: Jugo de Naranja Natural
✓ Producto registrado: Agua Mineral con Gas
✓ Producto registrado: Tapioca de Yuca
✓ Producto registrado: Flan Napolitano
✓ Producto registrado: Ensalada Amazónica
✓ Producto registrado: Sopa de Pescado
```

### Sección 3: Registro de Clientes
```
REGISTRANDO CLIENTES
✓ Cliente registrado: Juan Pérez García
✓ Cliente registrado: María López Ruiz
✓ Cliente registrado: Carlos Mendoza Soto
```

### Sección 4: Menú del Restaurante
```
MENÚ DEL RESTAURANTE - El Sabor Amazónico

BEBIDAS
Jugo de Naranja Natural: $4.50
Agua Mineral con Gas: $2.50

ENTRADAS
Yuca frita con queso: $12.00
Ensalada Amazónica: $10.00
[... más productos...]
```

### Sección 5: Clientes Registrados
```
CLIENTES REGISTRADOS

Cliente: Juan Pérez García
    Email: juan.perez@email.com
    Teléfono: 0987654321
    Dirección: Av. 10 de Agosto, Puyo
    Estado: Activo
    Pedidos realizados: 0
```

### Sección 6: Creación de Pedidos
```
CREACIÓN DE PEDIDOS

Pedido creado: PED-0001
  Cliente: Juan Pérez García
  Total: $59.00

Pedido creado: PED-0002
  Cliente: María López Ruiz
  Total: $59.50
```

### Sección 7: Métodos Especiales
```
DEMOSTRACIÓN DE MÉTODOS ESPECIALES

Detalle de producto (usando __str__()):
[PLATOS_PRINCIPALES] Ceviche de Tilapia - $25.00
    Descripción: Ceviche fresco preparado con tilapia del río
    Estado: Disponible

Detalle de cliente (usando __str__()):
Cliente: Juan Pérez García
    Email: juan.perez@email.com
    Teléfono: 0987654321
    Dirección: Av. 10 de Agosto, Puyo
    Estado: Activo
    Pedidos realizados: 1

Total gastado por este cliente: $59.00
```

### Sección 8: Aplicación de Descuentos
```
APLICACIÓN DE DESCUENTO

Precio original: $12.00
Precio con 15% descuento: $10.20
```

### Fin de la Ejecución
```
======================================================================
FIN DE LA EJECUCIÓN
======================================================================
```

---

## 🔍 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'modelos'"
**Solución**: Asegúrate de estar en la carpeta `restaurante_app` antes de ejecutar

```bash
# ✓ CORRECTO
cd restaurante_app
python main.py

# ✗ INCORRECTO
cd TareaSemana4
python restaurante_app/main.py
```

### Error: "No such file or directory"
**Solución**: Verifica la ruta exacta:
```bash
pwd  # Ver ubicación actual
ls   # Ver archivos
```

### El programa no muestra salida
**Solución**: Reinicia la terminal o usa:
```bash
python -u main.py  # Desactiva buffering
```

---

## 💡 Variaciones de Ejecución

### Ejecutar y Guardar Salida en Archivo
```bash
python main.py > salida.txt
```

### Ejecutar con Timing
```bash
# En PowerShell
Measure-Command { python main.py }
```

### Ejecutar Casos Avanzados
```bash
python casos_avanzados.py
```

### Ejecutar Ambos (Secuencialmente)
```bash
python main.py
echo.
python casos_avanzados.py
```

---

## 📚 Archivos Relacionados

Después de ejecutar, puedes leer:

1. **README.md** - Guía general
2. **TareaSemana4_explicacion.md** - Explicación técnica
3. **ARQUITECTURA.md** - Diagramas
4. **ENTREGA.md** - Requisitos
5. **RESUMEN.md** - Resumen ejecutivo

---

## ✅ Validación Post-Ejecución

Después de ejecutar, verifica:
- ✓ No hay errores en la consola
- ✓ Se registraron 8 productos
- ✓ Se registraron 3 clientes
- ✓ Se crearon 2 pedidos
- ✓ Se mostró información __str__()
- ✓ Se aplicó descuento correctamente
- ✓ Programa terminó sin excepciones

---

## 📞 Información Adicional

**Lenguaje**: Python 3.6+  
**Dependencias**: Ninguna externa  
**Requisitos**: Solo Python  
**Tiempo de Ejecución**: < 1 segundo  

---

## 🎯 Próximos Pasos

1. ✓ Ejecutar `python main.py`
2. ✓ Revisar la salida en consola
3. ✓ Leer la documentación (README.md)
4. ✓ Analizar el código en los archivos .py
5. ✓ Ejecutar `python casos_avanzados.py` para ver más funcionalidades

---

**Estado**: ✅ LISTO PARA USAR

**Última Verificación**: 2026-06-21

