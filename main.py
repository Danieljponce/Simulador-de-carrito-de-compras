
# Estructura de datos inicial
WAREHOUSE = {
    "A001": {"name": "Pan", "price": 1.50},
    "B203": {"name": "Leche", "price": 3.80},
    "C456": {"name": "Huevos", "price": 5.20}
}

SHOPPING_CAR = {}  # {código: cantidad}

def clear_console():
    """Simula limpiar la consola imprimiendo líneas vacías"""
    print("\n" * 40)

def show_menu():
    print("\n" + "-"*40)
    print("TIENDA VIRTUAL - MENÚ PRINCIPAL")
    print("-"*40)
    print("1. Ver catálogo de productos")
    print("2. Agregar producto al carrito")
    print("3. Eliminar producto del carrito")
    print("4. Vaciar carrito completamente")
    print("5. Ver contenido del carrito")
    print("6. Finalizar compra ")
    print("7. Salir del programa")
    print("-"*40)

def show_catalog():
    print("\n" + "-"*40)
    print("CÓDIGO | PRODUCTO | PRECIO")
    print("-"*40)
    for code, product in WAREHOUSE.items():
        print(f"{code:6} | {product['name']:8} | S/{product['price']:2}")
    print("-"*40)


clear_console()
show_menu()
show_catalog()
