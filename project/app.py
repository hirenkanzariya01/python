products_data = {}

while True:
    print("=" * 10, "STORE MANAGEMENT SYSTEM", "=" * 10)
    print()
    print("1. for Add New Product.")
    print("2. for Update Product.")
    print("3. for Delete Product.")
    print("4. for View All Products.")
    print("5. for Get Report.")
    print("6. for sell report. ")
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
            "sell_product": 0,
        }

        print("Product Data :- ", products_data)

    def update_products():
        print("please provide following information for update a product ")
        p_id = int(input("Enter Product Id to Update A Product :- "))

        if p_id in products_data:
            new_p_name = input("Enter New Product Name :- ")
            new_p_price = int(input("Enter New Product Purchase Price :- "))
            new_p_s_price = int(input("Enter New Product Selling Price :- "))
            new_p_details = input("Enter New Product Details :- ")
            new_p_stock_quantity = int(input("Enter New Product quantity :- "))
            sell_product = int(input("Enter New sell Product quantity :- "))

            products_data[p_id] = {
                "id": p_id,
                "name": new_p_name,
                "Purchase_Price": new_p_price,
                "Selling_Price": new_p_s_price,
                "product_details": new_p_details,
                "stock": new_p_stock_quantity,
                "sell_product": sell_product,
            }
            print("Product Update Successfully")
        else:
            print("provide valid product id ")

    def delete_product():
        p_id = int(input("Enter Product Id For Delete A product :- "))
        if products_data[p_id]:
            del products_data[p_id]
            print("Product Delete Successfully ....")
        else:
            print("Please Provide Valid Product Id ")

    def view_product():
        print("\n" + "=" * 95)
        print(" " * 35 + "VIEW PRODUCTS")
        print("=" * 95)

        print(
            f"{'ID':<5}"
            f"{'Name':<12}"
            f"{'Purchase Price':<18}"
            f"{'Selling Price':<18}"
            f"{'Details':<20}"
            f"{'Stock':<10}"
            f"{'Sell':<10}"
        )

        print("-" * 95)

        for product in products_data:
            print(
                f"{products_data[product]['id']:<5}"
                f"{products_data[product]['name']:<12}"
                f"{products_data[product]['Purchase_Price']:<18}"
                f"{products_data[product]['Selling_Price']:<18}"
                f"{products_data[product]['product_details']:<20}"
                f"{products_data[product]['stock']:<10}",
                f"{products_data[product]['sell_product']:<10}",
            )
        print("=" * 95)

    def get_report():
        total_stock = 0
        total_price = 0
        total_sell = 0
        total_purchase = 0
        for i in products_data:
            total_stock = total_stock + products_data[i]["stock"]
            total_price = (
                total_price
                + products_data[i]["Purchase_Price"] * products_data[i]["stock"]
            )
            total_sell = (
                total_sell
                + products_data[i]["Selling_Price"] * products_data[i]["sell_product"]
            )
            total_purchase = (
                total_purchase
                + products_data[i]["Purchase_Price"] * products_data[i]["sell_product"]
            )

        print("Total Products :- ", len(products_data))
        print("Total Sell :- ", total_sell)
        print("Total Revenue :- ", total_sell - total_purchase)
        print("Total stock :- ", total_stock)
        print("Total Investment :- ", total_price)

        # print(len(products_data))

    def sell_report():
        p_id = int(input("Enter Product id to Sell a Product :- "))
        if p_id in products_data:
            sell_count = int(input("Enter Sell Quantity :- "))
            if products_data[p_id]["stock"] > sell_count:
                products_data[p_id]["sell_product"] = (
                    products_data[p_id]["sell_product"] + sell_count
                )
                products_data[p_id]["stock"] = products_data[p_id]["stock"] - sell_count
            else:
                print("Stock is  not avalible")

            print(products_data)

        else:
            print("Provide Valid Product id ")

    if choice == 1:
        add_product()

    elif choice == 2:
        update_products()

    elif choice == 3:
        delete_product()

    elif choice == 4:
        view_product()

    elif choice == 5:
        get_report()
    elif choice == 6:
        sell_report()

    else:
        print("Please Provid Valid Input ")
