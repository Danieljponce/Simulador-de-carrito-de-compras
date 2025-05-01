WAREHOUSE = [
    {
        "code" : "A001" ,
        "name": "Pan",
        "price": 1.50
    },
    {   "code": "B203",
        "name" : "Leche",
        "price": 3.80
    }
] 


def show_menu():
    print("""
    1. Ver catálogo 
    2. Agregar producto al carrito 
    3. Eliminar producto del carrito 
    4. vaciar carrito 
    5. Mostrar carrito 
    6. Finalizar compra 
    7. salir """)

def show_catalog() :
    print (f"Codigo | Producto | Precio")
    for product in WAREHOUSE: 
        print (f"Codigo: {product["code"]}  | Producto: | {product["name"]} | Precio: s/{product["price"]}")


#show_catalog

show_catalog()


    