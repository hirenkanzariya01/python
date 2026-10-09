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

        print(p_id, p_name, p_p_price, p_s_price, p_details, p_stock_quantity)
        products_data[p_id] = {
            "id": p_id,
            "name": p_name,
            "Purchase_Price": p_p_price,
            "Selling_Price": p_s_price,
            "product_details": p_details,
            "stock": p_stock_quantity,
        }
        print("Product Data :- ", products_data)

    if choice == 1:
        add_product()

    elif choice == 2:
        print("update Product")

    elif choice == 3:
        print("delete product")

    elif choice == 4:
        print("View Products")

    elif choice == 5:
        print("Get Report")

    else:
        print("Please Provid Valid Input ")
