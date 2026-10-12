products_data = {}

while True:
    print("=" * 10, "STORE MANAGEMENT SYSTEM", "=" * 10)
    print()
    print("1. for Add New Product.")
    print("2. for Update Product.")
    print("3. for Delete Product.")
    print("4. for View All Products.")
    print("5. for Get Report.")
    print()

    choice = int(input("Enter Your Choice :- "))

    def add_product():
        print("Please provid following information For Add New Product ")
        p_id = int(input("Enter Product Id :- "))
        p_name = input("Enter Product Name :- ")
        p_p_price = int(input("Enter Product Purchase Price :- "))
        p_s_price = int(input("Enter Product Selling Price :- "))
        p_details = input("Enter Product Details :- ")
        p_stock_quantity = int(input("Enter Product quantity :- "))

        products_data[p_id] = {
            "id": p_id,
            "name": p_name,
            "Purchase_Price": p_p_price,
            "Selling_Price": p_s_price,
            "product_details": p_details,
            "stock": p_stock_quantity,
        }
        print("Product Data :- ", products_data)

    def update_products():
        print("please provide following information for update a product ")
        p_id = int(input("Enter Product Id to Update A Product :- "))
        print(products_data[p_id])
        # new_p_name = input("Enter New Product Name :- ")
        # new_p_price = int(input("Enter New Product Purchase Price :- "))
        # new_p_s_price = int(input("Enter New Product Selling Price :- "))
        # new_p_details = input("Enter New Product Details :- ")
        # new_p_stock_quantity = int(input("Enter New Product quantity :- "))

        # products_data[p_id] = {
        #     "id": p_id,
        #     "name": new_p_name,
        #     "Purchase_Price": new_p_price,
        #     "Selling_Price": new_p_s_price,
        #     "product_details": new_p_details,
        #     "stock": new_p_stock_quantity,
        # }

        print("1 for update name ")
        print("2 for update p price ")
        print("3 for update s price ")
        print("4 for update details price ")
        print("5 for update quantity price ")

        choice = int(input("Enter Your Choice:- "))

        if choice == 1:
            new_p_name = input("Enter New Product Name :- ")
            products_data[p_id]["name"] = new_p_name
            
        print(products_data)

    if choice == 1:
        add_product()

    elif choice == 2:
        update_products()

    elif choice == 3:
        print("delete product")

    elif choice == 4:
        print("View Products")

    elif choice == 5:
        print("Get Report")

    else:
        print("Please Provid Valid Input ")
