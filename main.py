from bikeRentalShop import BikeRental, Customer

def main():
    
    shop = BikeRental(65)
    customer = Customer()

    while True:
        
        print("""
        ====== Bike Rental Shop =================
        
        Please choose from the following options:
            
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike
        6. Exit
        
        """)
        
        option = input("How can I help you? ")
        
        try:
            option = int(option)
        except ValueError:
            print("That's not an integer!")
            continue
        
        if option == 1:
            shop.displayStock
        
        elif option == 2:
            customer.rentalTime = shop.rentByHour(customer.requestBike())
            customer.rentalType = 1

        elif option == 3:
            customer.rentalTime = shop.rentOnDailyBasis(customer.requestBike())
            customer.rentalType = 2

        elif option == 4:
            customer.rentalTime = shop.rentOnWeeklyBasis(customer.requestBike())
            customer.rentalType = 3

        elif option == 5:
            customer.total_amount = shop.returnBike(customer.returnBike())
            customer.rentalType, customer.rentalTime, customer.numOfBikes = 0,0,0        
        elif option == 6:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")        
    print("Thank you for using the bike rental system.")
    
if __name__ == '__main__':
    main()
    
