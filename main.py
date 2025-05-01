
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


def add_product():
    while True:
        code = input("\nIngrese el código del producto (o '0' para cancelar): ").upper()
        if code == "0":
            return
        
        if code not in WAREHOUSE:
            print("Error: Código no existe. Intente nuevamente")
            continue
        
        try:
            quantity = int(input(f"Ingrese cantidad para {WAREHOUSE[code]['name']}: "))
            if quantity <= 0:
                print("Error: La cantidad debe ser mayor a 0")
                continue
        except:
            print("Error: Debe ingresar un número válido")
            continue
        
        # Agregar al carrito
        if code in SHOPPING_CAR:
            SHOPPING_CAR[code] += quantity
        else:
            SHOPPING_CAR[code] = quantity
        
        print(f"\n Se agregaron {quantity} unidad(es) de {WAREHOUSE[code]['name']} al carrito")
        return

def remove_product():
    if not SHOPPING_CAR:
        print("\nEl carrito está vacío")
        return
    
    print("\nProductos en carrito:")
    for code, quantity in SHOPPING_CAR.items():
        print(f"- {code}: {WAREHOUSE[code]['name']} (x{quantity})")
    
    code = input("\nIngrese código del producto a eliminar: ").upper()
    if code not in SHOPPING_CAR:
        print("Error: El producto no está en el carrito")
        return
    
    try:
        quantity = int(input(f"Cantidad a eliminar (actual: {SHOPPING_CAR[code]}): "))
        if quantity <= 0 or quantity > SHOPPING_CAR[code]:
            print("Error: Cantidad inválida")
            return
    except:
        print("Error: Debe ingresar un número válido")
        return
    
    SHOPPING_CAR[code] -= quantity
    if SHOPPING_CAR[code] == 0:
        del SHOPPING_CAR[code]
    
    print(f"\n Se eliminaron {quantity} unidad(es) del producto")



def clear_cart():
    SHOPPING_CAR.clear()
    print("\n Carrito vaciado correctamente")



clear_console()
show_menu()
show_catalog()
add_product ()
clear_cart ()
remove_product()



