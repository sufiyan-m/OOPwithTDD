import datetime

class BikeRental:
    
    def __init__(self, stock=0):
        """ Constructor class for bike rental shop."""
        self.stock = stock
    
    @property
    def displayStock(self):
        """Displays the number of bikes that are available for rent."""
        #return "We currently have {} bikes available for rent.".format(self.stock)
        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock
    
    def rentByHour(self,n):
        """The bike is rented to a customer on hourly basis, the input is the number of bikes"""
        #Checking whether input is appropriate
        if n <= 0:
            print("The number of bikes you want to rent should be a positive number.")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike/bikes on hourly basis today at {} hours {} minutes.".format(n,now.hour, now.minute))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
        
            self.stock -= n
            return now
    
    def rentOnDailyBasis(self,n):
        """Rents a bike on daily basis to a customer."""
        if n <= 0:
            print("The number of bikes you want to rent should be a positive number.")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike/bikes on daily basis today at {} hours {} minutes".format(n,now.hour, now.minute))
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")
        
            self.stock -= n
            return now
        
    def rentOnWeeklyBasis(self,n):
        """Rents a bike on weekly basis to a customer"""
        if n <= 0:
            print("The number of bikes you want to rent should be a positive number.")
            return None
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike/bikes on weekly basis today at {} hours {} minutes.".format(n,now.hour,now.minute))
            print("You will be charged $60 for each day per bike.")
            print("We hope that you enjoy our service.")
        
            self.stock -= n
            return now
        
    def returnBike(self, request):
        """This method accepts a tuple input that is used to update the stock after the bike has been returned and the invoice is generated accordingly"""
        #extracting tuple
        rentalTime, rentalType, numOfBikes = request
        total_amount = 0
        
        #Proceed further if all three attributes below are available
        if rentalTime and rentalType and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
            
            # hourly bill calculation
            if rentalType == 1:
                total_amount = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
            
            # daily bill calculation
            elif rentalType == 2:
                total_amount = round(rentalPeriod.days) * 20 * numOfBikes
            
            # weekly bill calculation
            elif rentalType == 3:
                total_amount = round(rentalPeriod.days / 7) * 60 * numOfBikes
            
            else:
                return "invalid rental type"
                
            # family discount calculation
            if (3 <= numOfBikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                total_amount = total_amount * 0.7
                
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(total_amount))
            return total_amount
            
        else:
            print("Are you sure you rented a bike with us?")
            return None

class Customer:
    """It instantiates various customer attributes"""
    
    def __init__(self):
        self.total_amount = 0
        self.numOfBikes = 0 
        self.rentalType = 0
        self.rentalTime = 0
        
    def returnBike(self):
        """This method return attributes associated with customer that are then used to calculate the total amount in the Bike Rental class."""
        if self.numOfBikes and self.rentalTime and self.rentalType:
            return (self.rentalTime, self.rentalType, self.numOfBikes)
        else:
            return (0,0,0)
        
    def requestBike(self):
        """Requests a customer to input the number of bikes he/she wants to hire"""
        bikes = input("How many bikes would you like to rent?")        

        try: 
            bikes = int(bikes) # This makes sure that input is an integer
        except ValueError:
            return "Please enter a (+)ve integer"
        
        if bikes < 1:
            return "The number of bikes should be greater than 0"
        
        else:
            self.bikes = bikes
        return self.bikes
    
    
    
    
        
        
        
        
   
