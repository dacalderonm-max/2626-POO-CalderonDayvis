# Sistema básico de gestión de restaurante en Python

## Estudiante

**Nombre completo:** Dayvis Aly Calderon Mendoza

## Descripción

Este proyecto implementa un sistema básico de gestión de restaurante usando Programación Orientada a Objetos (POO) en Python. El objetivo es demostrar el uso de clases, objetos, atributos, métodos, listas e importaciones dentro de un proyecto modular.

No se desarrolla una interfaz gráfica ni un menú interactivo; el programa funciona en **modo consola**, crea objetos, los registra en un servicio central y muestra la información en terminal.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

## Responsabilidad de cada archivo

- `modelos/producto.py`: contiene la clase `Producto`, que representa un plato, bebida u otro producto del restaurante.
- `modelos/cliente.py`: contiene la clase `Cliente`, que representa a una persona registrada en el sistema.
- `servicios/restaurante.py`: contiene la clase `Restaurante`, encargada de administrar listas de productos y clientes.
- `main.py`: crea los objetos, los registra en el servicio principal y muestra la información en consola.

## Clases y tipos de datos utilizados

### `Producto`
- `nombre: str`
- `descripcion: str`
- `precio: float`
- `categoria: str`
- `disponible: bool`

### `Cliente`
- `nombre: str`
- `email: str`
- `telefono: str`
- `direccion: str`
- `activo: bool`
- `historial_pedidos: list`

### `Restaurante`
- `nombre: str`
- `ubicacion: str`
- `productos: list`
- `clientes: list`
- `contador_pedidos: int`

## Cómo ejecutar el programa

1. Abra una terminal en la carpeta `restaurante_app`.
2. Ejecute el archivo principal:

```bash
python main.py
```

### Resultado esperado
La ejecución debe mostrar en consola el resumen del restaurante, el listado de productos y el listado de clientes registrados.

## Reflexión

Usar identificadores descriptivos ayuda a entender el propósito de cada clase, atributo y método sin necesidad de revisar todo el código. Además, elegir tipos de datos adecuados evita errores y hace que el programa sea más claro. Las listas, por su parte, permiten almacenar varios objetos y facilitan la administración de productos y clientes dentro de una estructura modular.

## Observación final

Este proyecto fue diseñado para ser simple, claro y coherente con los requisitos de la actividad, manteniendo una organización modular y una estructura fácil de comprender.

