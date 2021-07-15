# Rent-a-Bike
A bike rental system has been devloped in Python using object oriented programming with Test Driven Development.
## Test Driven Development 
"A good programmer is someone who always looks both ways before crossing a one-way street". This quote highlights the importance of writing tests as it makes the entire 
development process more agile; thus, ensuring rapid changes whilst ensuring high quality. Unit testing framework is used in this project, which focuses on the testing 
of individual components of a software. In addition to the assertions, *Mocking* is also used where individual unit of software has external dependencies.

In this project there are a total of 8 unit tests which are written in the file named **test_bikeRentalShop.py**. Always run this file first before pushing any changes to
the production enviornment to ensure that is software is working as expected without any bugs or interuptions. You can run this file directly from your favourite IDE or via
CLI using **python -m unittest -v test_bikeRentalShop.py**

## Project Description
Customers can rent a bike on hourly ($5 per hour), daily ($20 per day) and weekly basis ($60 per week). In addition to that, a 30% family rental discount is provided if 
the number of rentals is from 3 to 5 bikes. Moreover, the rental shop can also use this program to display the available inventory, issue an invoice when customer decides
to return the bike. It can also take rental requests on hourly, daily and weekly basis by cross verifying the stock. 
Since classes are used, various customers and bike rental shops can be instantiated as needed. For simplicity we assume that any customer requests rentals of 
only one type i.e hourly, monthly or weekly but is free to choose the number of bikes he/she wants. However requested bikes should be less than available stock.


The software can be run using **python3 main.py** from CLI. 

## References

https://docs.python.org/3/library/unittest.html 

https://medium.com/@gurupratap.matharu/object-oriented-programming-project-in-python-for-your-github-portfolio-d34feaf1332c 
