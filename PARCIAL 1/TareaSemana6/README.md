# 🍽️ Sistema de Restaurante — Semana 6

**Asignatura:** Programación Orientada a Objetos  
**Parcial:** 1  
**Semana:** 6  
**Estudiante:** Calderón Dayvis  
**Institución:** Universidad Estatal Amazónica

---

## 📌 Descripción del sistema

Sistema modular desarrollado en Python que representa los productos disponibles en un restaurante. Aplica los tres principios fundamentales de la Programación Orientada a Objetos: **herencia**, **encapsulación** y **polimorfismo**, organizados en una arquitectura de carpetas limpia y escalable.

---

## 📂 Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py       # Exporta las clases del paquete
│   ├── producto.py       # Clase padre: Producto
│   ├── platillo.py       # Clase hija: Platillo
│   └── bebida.py         # Clase hija: Bebida
├── servicios/
│   ├── __init__.py       # Exporta la clase Restaurante
│   └── restaurante.py    # Clase de servicio: Restaurante
└── main.py               # Punto de arranque del programa
```

---

## 🔗 Relación de herencia aplicada

```
Producto  (clase padre)
├── Platillo  (clase hija — hereda de Producto)
└── Bebida    (clase hija — hereda de Producto)
```

- `Producto` define los atributos comunes: `nombre`, `__precio` y `disponible`.
- `Platillo` extiende `Producto` con: `calorias`, `tipo_platillo` y `tiempo_prep`.
- `Bebida` extiende `Producto` con: `volumen_ml`, `tipo_bebida` y `es_alcoholica`.
- Ambas clases hijas utilizan `super().__init__(...)` para reutilizar el constructor de la clase padre.

---

## 🔒 Atributo encapsulado

El atributo `__precio` en la clase `Producto` está **encapsulado** mediante el prefijo de doble guión bajo (`__`), lo que impide su modificación directa desde fuera de la clase.

Se controla su acceso a través de:
- `obtener_precio()` → retorna el precio actual.
- `cambiar_precio(nuevo_precio)` → actualiza el precio solo si es mayor que cero.

```python
# Acceso correcto mediante getter
print(producto.obtener_precio())

# Modificación con validación
producto.cambiar_precio(8.50)   # OK
producto.cambiar_precio(0.00)   # Error: precio inválido
producto.cambiar_precio(-2.00)  # Error: precio inválido
```

---

## 🔄 Método para demostrar polimorfismo

El método `mostrar_informacion()` está definido en la clase padre `Producto` y **sobrescrito** en las clases hijas `Platillo` y `Bebida`. Al recorrer la lista de productos en `Restaurante.mostrar_menu()`, Python ejecuta automáticamente la versión correcta del método según el tipo real de cada objeto.

```python
# Polimorfismo en acción
for producto in lista_de_productos:
    producto.mostrar_informacion()  # Se llama a Platillo o Bebida según corresponda
```

---

## ▶️ Cómo ejecutar el programa

Desde la terminal, situarse dentro de la carpeta `restaurante_app` y ejecutar:

```bash
python main.py
```

---

## 💡 Reflexión

Aplicar los principios de la POO en un proyecto Python modular permite construir código más organizado, reutilizable y fácil de mantener. La **herencia** evita duplicar atributos y comportamientos comunes; la **encapsulación** protege los datos internos y garantiza su integridad mediante validaciones; y el **polimorfismo** permite tratar objetos distintos de manera uniforme, lo que simplifica el código que los consume. Estos principios no solo mejoran la calidad del software, sino que también acercan el diseño del programa a la forma en que modelamos el mundo real.

