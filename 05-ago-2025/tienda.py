num_products = int(input("Ingrese el número de productos a registrar: "))
is_code = input("Desea agregar el código por usted mismo: si | no: ").lower() == "si"
products_list = []
end_number_code_products_list = 0


# Registrar productos
def add_product(num=1):
    for i in range(num):
        print(f"\n ----- Creando Producto #{len(products_list) + 1} ----- ")
        product = {
            "name": input("Ingrese el nombre del producto: "),
            "amount": input("Ingrese la cantidad del producto: "),
            "price": input("Ingrese el precio del producto: "),
            "code": 0,
        }
        if is_code:
            product["code"] = input("Ingrese el código del producto: ")
        else:
            if len(products_list) == 0:
                product["code"] += 1
            else:
                end_product = products_list[len(products_list) - 1]["code"]
                end_product_code_int = None
                end_type_product_code = type(end_product).__name__ != "int"
                if end_type_product_code:
                    for ix_product in range(len(products_list)):
                        if type(products_list[ix_product]["code"]).__name__ == "int":
                            end_product_code_int = products_list[ix_product]
                    print(end_product_code_int, end_type_product_code)
                    if end_product_code_int == None:
                        product["code"] = 1
                    else:
                        product["code"] = end_product_code_int["code"] + 1
                else:
                    print(end_product_code_int, end_type_product_code)
                    if end_product_code_int != None:
                        product["code"] = 1
                    else:
                        product["code"] = end_product + 1

        print(product)
        products_list.append(product)


add_product(num_products)

isConsult = input("\nQuieres realizar alguna consulta: si | no: ").lower() == "si"


def show_product(product={}, order=0):
    print(
        f"""{order}.Producto \nnombre: {product["name"]} \ncantidad: {product["amount"]} \nprecio: {product["price"]} \ncódigo: {product["code"]}\n--------------------------"""
    )


while isConsult:
    print(
        "\n---Consultar--- \n[1] Consultar Productos \n[2] Actualizar Cantidades \n[3] Calcular el valor toral del inventario \n[4] Agregar Nuevos Productos \n[5] Eliminar Producto por código"
    )
    selection = int(input("\n Seleccione una opción para hacer la consulta: "))

    if selection == 1:
        print("\n---Productos---")
        for i in range(len(products_list)):
            product = products_list[i]
            show_product(product, i + 1)
    elif selection == 2:
        print("\n--- Buscar Por --- \n[1] Nombre  \n[2] Código")
        produt_find_by = int(input("\nSeleccione una opción para hacer la consulta: "))
        search_key = (
            "name" if produt_find_by == 1 else "code" if produt_find_by == 2 else ""
        )
        if search_key:
            founed_product = input(
                f'Ingrese el {"nombre" if search_key == "name" else "código"} del producto a buscar: '
            )
            print("\n--- Actualizar Cantidad Productos---")
            amout_product_update = 0
            for i_update in range(len(products_list)):
                search = products_list[i_update]
                if str(search[search_key]) == founed_product:
                    show_product(search, i_update + 1)
                    new_amout = int(
                        input("\nIngrese el nuevo valor de la cantidad: \n")
                    )
                    search["amount"] = new_amout
                    amout_product_update += 1
            if amout_product_update:
                print("\n--- Productos Actualizados Correctamente ---")
            else:
                print("\n--- No se econtro ningún producto actualizar ---")
        else:
            print("Selecion incorrecta")
    elif selection == 3:
        print(f"\n--- Valor total del inventario: {len(products_list)} ")
    elif selection == 4:
        new_num_products = int(input("\n Ingrese el número de productos a registrar: "))
        is_code = (
            input("Desea agregar el código por usted mismo: si | no: ").lower() == "si"
        )
        add_product(new_num_products)
        print("\n--- Productos Registrados Correctamente ---")
    elif selection == 5:
        founed_product = input(f"Ingrese el código del producto a eliminar: ")
        product_delete = None
        for i_update in range(len(products_list)):
            search = products_list[i_update]
            if str(search["code"]) == founed_product:
                product_delete = products_list[i_update]
                products_list.pop(i_update)
        if product_delete == None:
            print("\n--- No se encontro ningun producto ---")
        else:
            print("\n--- Producto Eliminado Correctamente ---")
            show_product(product_delete, 1)
    else:
        print("\n--- Selecion incorrecta ---")

    isConsult = input("\nQuieres realizar alguna consulta: si | no: ").lower() == "si"
