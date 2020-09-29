Assignment 10
===============
This assignment is to demonstrate the functionalities of a Named Tuple and Why it should be considered under certain circumstances 
It also compares and proves that it is faster than dictionaries and that's why it should be choosen in many occasions 



def time_func(reps):
=====================
    This function calculates the elapsed time for the function being passed as parameter
    
def named_tuple_performance():
=================================
    This function creates a list of 10000 fake profiles stores in a Named Tuple and find out few aggregated values
    1. The Largest Blood Group Type (Maximum count among 10000 profiles)
    2. The Mean Location (The Input here is lat and long )
    3. The Age of the oldest Person

    Returns the
    1. Largest Blood Group
    2. Average Current Location
    3. The Age of the Oldest Person
    4. The Average Age
    
def named_dict_performance():
=================================

    This function creates a list of 10000 fake profiles store it in a dictionary  and find out few aggregated values
    1. The Largest Blood Group Type (Maximum count among 10000 profiles)
    2. The Mean Location (The Input here is lat and long )
    3. The Age of the oldest Person

    Returns the
    1. Largest Blood Group
    2. Average Current Location
    3. The Age of the Oldest Person
    4. The Average Age

def check_performance():
=============================
    This function executes the above two functions for the number of iterations specified
    Then it calculates the time taken by both Named Tuple and Dictionary
    Finally it returns the one which took less time to execute
def stock_market():
====================
    This function is to create a Dataset for Stock market simulation
    Here are the steps
    Using Python Faker library create a List of 100 Fake companies
    Search for random number which can show the stock value
    Generate some random weights for each company
    Multiply the random number with Open value
    Normalize the weights
    This Provides the open value for each company stock  by multiplying open value with normalized weights
    Sum over all values and find out the Overall Market index
    Generate random value between 0.8 and 1.2 to find out High value
    If high value less than Open value then set open value as high value
    Generate random value between 0.8 and 1.2 to find out low value
    If low value higher than open value then set low value as open value
    Generate random value between 0.8 and 1.2 to find out close value
    If close value higher than high value then set close value as high value
    Create a Named Tuple to store the values
    Return Market index Market open index, Market high rate, Market Low rate and Market Close Rate
