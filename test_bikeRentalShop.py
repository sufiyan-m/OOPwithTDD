import unittest
from bikeRentalShop import BikeRental, Customer
import datetime
from unittest.mock import patch

class TestBikeRental(unittest.TestCase):
    
    def test_displayStock(self):
        
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        
        self.assertEqual(shop1.displayStock, 0)
        self.assertEqual(shop2.displayStock, 10)
        
        shop1.stock = 50
        self.assertEqual(shop1.displayStock, 50)
        
    def test_rentByHour(self):
        
        shop = BikeRental(15)
        hour = datetime.datetime.now().hour
        #Checking for negative number of bikes for rent
        self.assertEqual(shop.rentByHour(-2), None)
        #Checking for zero number of bikes for rent
        self.assertEqual(shop.rentByHour(0), None)
        #Checking for number of bikes for rent < stock
        self.assertEqual(shop.rentByHour(2).hour, hour)
        #Checking for number of bikes for rent > stock
        self.assertEqual(shop.rentByHour(17), None)
        
    def test_rentOnDailyBasis(self):
        
        shop = BikeRental(15)
        hour = datetime.datetime.now().hour
        #Checking for negative number of bikes for rent
        self.assertEqual(shop.rentOnDailyBasis(-2), None)
        #Checking for zero number of bikes for rent
        self.assertEqual(shop.rentOnDailyBasis(0), None)
        #Checking for number of bikes for rent < stock
        self.assertEqual(shop.rentOnDailyBasis(2).hour, hour)
        #Checking for number of bikes for rent > stock
        self.assertEqual(shop.rentOnDailyBasis(17), None)
        
    def test_rentOnWeeklyBasis(self):
        
        shop = BikeRental(15)
        hour = datetime.datetime.now().hour
        #Checking for negative number of bikes for rent
        self.assertEqual(shop.rentOnWeeklyBasis(-2), None)
        #Checking for zero number of bikes for rent
        self.assertEqual(shop.rentOnWeeklyBasis(0), None)
        #Checking for number of bikes for rent < stock
        self.assertEqual(shop.rentOnWeeklyBasis(2).hour, hour)
        #Checking for number of bikes for rent > stock
        self.assertEqual(shop.rentOnWeeklyBasis(17), None)
        
    def test_returnBike_invalidInput(self):
        
        shop = BikeRental(15)
        time = datetime.datetime.now() + datetime.timedelta(hours=-2)
        # Missing entry in a tuple
        input_val = (time, 2, 0)
        self.assertIsNone(shop.returnBike(input_val))
        # Wrong rental type (correct values are 1, 2, 3)
        input_val2 = (time, 8, 1)
        self.assertEqual(shop.returnBike(input_val2), "invalid rental type")
        # Wrong data type entered into the input tuple
        input_val3 = (4,1,1)
        with self.assertRaises(TypeError):
            shop.returnBike(input_val3)
            
    def test_returnBike_validInput(self):
        
        shop = BikeRental(15)
        
        # Valid input for hourly bike hire
        time_hourly = datetime.datetime.now() - datetime.timedelta(hours=2)
        input_val_hourly = (time_hourly, 1, 2)
        self.assertEqual(shop.returnBike(input_val_hourly), 20)
        
        # Valid input for daily bike hire
        time_daily = datetime.datetime.now() - datetime.timedelta(days=2)
        input_val_daily = (time_daily, 2, 8)
        self.assertEqual(shop.returnBike(input_val_daily), 320)
        
        # Valid input for weekly bike hire
        time_weekly = datetime.datetime.now() - datetime.timedelta(weeks=2)
        input_val_weekly = (time_weekly, 3, 1)
        self.assertEqual(shop.returnBike(input_val_weekly), 120)
        
        # Valid input for checking the family discount
        time = datetime.datetime.now() - datetime.timedelta(weeks = 4)
        input_discount = (time, 3, 5)
        self.assertEqual(shop.returnBike(input_discount), 840)
        
class TestCustomer(unittest.TestCase):
    
    def test_returnBike(self):
        
        cust = Customer()
        # No attribute related to customer is assigned 
        self.assertEqual(cust.returnBike(), (0,0,0))
        # rentalTime attribute is not assigned
        self.assertEqual(cust.returnBike(), (0,0,0))
        # All three attributes are assigned
        timeslot = datetime.datetime.now()
        cust.rentalTime = timeslot
        cust.rentalType = 2
        cust.numOfBikes = 5
        self.assertEqual(cust.returnBike(), (timeslot, 2, 5))    
        
    def test_requestBike(self):
        
        cust = Customer()
        # Testing for correct input, 5 bikes
        with patch('bikeRentalShop.input') as mocked:
            mocked.return_value = '5'
            self.assertEqual(cust.requestBike(), 5)
        # Testing for zero bike value
        with patch('bikeRentalShop.input') as mocked:
            mocked.return_value = '0'
            self.assertEqual(cust.requestBike(), 'The number of bikes should be greater than 0')
        # Testing for bike value being a string of characters i.e. dhdhdh
        with patch('bikeRentalShop.input') as mocked:
            mocked.return_value = 'dhdhdh'
            self.assertEqual(cust.requestBike(), 'Please enter a (+)ve integer')
        # Testing for negative input value 
        with patch('bikeRentalShop.input') as mocked:
            mocked.return_value = '-5'
            self.assertEqual(cust.requestBike(), 'The number of bikes should be greater than 0')
        # Testing for decimal input value
        with patch('bikeRentalShop.input') as mocked:
            mocked.return_value = '2.45'
            self.assertEqual(cust.requestBike(), 'Please enter a (+)ve integer')
        
if __name__ == '__main__':
    unittest.main()

    