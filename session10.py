# Import all Libraries
from faker import Faker
from collections import namedtuple
from datetime import date, timedelta
from collections import Counter
from time import perf_counter
import random
import operator
from functools import reduce

fake = Faker()
n_times = 5
fake_prof_tup = namedtuple('fake_prof_tup',' '.join (fake.profile().keys()))

#time function
def time_func(reps):
    def timed(fn):
        from time import perf_counter
        def inner(*args, **kwargs):
            '''
                This function calculates the elapsed time for the function being passed as parameter
            '''
            total_elapsed = 0
            for _ in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_run_time = total_elapsed / reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result
        return inner
    return timed
fake_profile_list = [fake_prof_tup(*fake.profile().values()) for i in range(10000)]
@time_func(n_times)
def named_tuple_performance():
    '''
    This function creates a list of 10000 fake profiles stores in a Named Tuple and find out few aggregated values
    1. The Largest Blood Group Type (Maximum count among 10000 profiles)
    2. The Mean Location (The Input here is lat and long )
    3. The Age of the oldest Person

    Returns the
    1. Largest Blood Group
    2. Average Current Location
    3. The Age of the Oldest Person
    4. The Average Age
    '''
    #fake_profile_list = [fake_prof_tup(*fake.profile().values()) for i in range(10000)]
    largest_blood_group_type = Counter(map(lambda x:x.blood_group,fake_profile_list)).most_common()[0][0]

    lat,long=zip(*map(lambda x:x.current_location,fake_profile_list))
    avg_mean_curr_location = sum(lat)/len(lat),sum(long)/len(long)


    age_list = list(map(lambda x: (date.today()-x.birthdate)// timedelta(days=365),fake_profile_list))
    average_age = sum(age_list)/len(age_list)
    oldest_person = sorted(fake_profile_list,key=lambda x:x.birthdate)[0]
    oldest_person_age = (date.today() - oldest_person.birthdate) // timedelta(days=365)

    return f' Largest Blood Group : {largest_blood_group_type} Average current location {avg_mean_curr_location} Oldest person age is  {oldest_person_age}  Average age {average_age}'
fake_profile_dict = [fake.profile() for i in range(10000)]
@time_func(n_times)
def named_dict_performance():

    '''
    This function creates a list of 10000 fake profiles store it in a dictionary  and find out few aggregated values
    1. The Largest Blood Group Type (Maximum count among 10000 profiles)
    2. The Mean Location (The Input here is lat and long )
    3. The Age of the oldest Person

    Returns the
    1. Largest Blood Group
    2. Average Current Location
    3. The Age of the Oldest Person
    4. The Average Age
    '''

    #fake_profile_dict = [fake.profile() for i in range(10000)]
    largest_blood_group_type = Counter(map(lambda x:x['blood_group'],fake_profile_dict)).most_common()[0][0]

    lat,long=zip(*map(lambda x:x['current_location'],fake_profile_dict))
    avg_mean_curr_location = sum(lat)/len(lat),sum(long)/len(long)

    age_list = list(map(lambda x: (date.today()-x['birthdate'])// timedelta(days=365),fake_profile_dict))
    average_age = sum(age_list)/len(age_list)
    oldest_person = sorted(fake_profile_dict,key=lambda x:x['birthdate'])[0]
    oldest_person_age = (date.today() - oldest_person['birthdate']) // timedelta(days=365)

    return f' Largest Blood Group : {largest_blood_group_type} Average current location {avg_mean_curr_location} Oldest person age is  {oldest_person_age}  Average age {average_age}'

def check_performance():
    '''
    This function executes the above two functions for the number of iterations specified
    Then it calculates the time taken by both Named Tuple and Dictionary
    Finally it returns the one which took less time to execute
    '''
    start = perf_counter()
    named_tuple_performance()
    end = perf_counter()
    elapsed_time_tuple = (end-start)

    start = perf_counter()
    named_dict_performance()
    end = perf_counter()
    elapsed_time_dict = (end-start)

    if elapsed_time_tuple > elapsed_time_dict:
        print('The Tuple is Slower than the Dictionary by {elapsed_time_tuple - elapsed_time_dict} secs')
        return 'Named Tuple Slower'
    else:
        print(f' The Dictionary is Slower than the Tuple by {elapsed_time_dict - elapsed_time_tuple} secs')
        return 'Dictionary Slower'
def stock_market():
    '''
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
    '''
    # Create Fake company and random weights for each company
    company_name_list = [ fake.company() for i in range(100)]
    day_start_list = [random.randint(100,4000) for i in range(100)]
    random_weight_list = [random.uniform(0.5,1) for i in range(100)]
    var1= sum(random_weight_list)
    norm_list = list(map(lambda x: x/var1, random_weight_list) )
    # Market share list
    for_market_share = list(map(lambda x,y: x*y, day_start_list,norm_list))
    #High List
    ran_list =[random.uniform(0.8,1.2) for i  in range(len(day_start_list))]
    high_list = list(map(lambda x,y,z,w:x*y*w if x*y*w >= z else z , day_start_list,norm_list,for_market_share,ran_list ))
    #Low List
    ran1_list =[random.uniform(0.8,1.2) for i  in range(len(day_start_list))]
    low_list = list(map(lambda x,y,z,w:x*y*w if x*y*w <= z else z , day_start_list,norm_list,for_market_share,ran1_list ))
    # Close List
    ran2_list =[random.uniform(0.8,1.2) for i  in range(len(day_start_list))]
    close_list = list(map(lambda x,y,z,w:x*y*w if x*y*w <= z else z , day_start_list,norm_list,high_list,ran2_list ))
    # Named Tuple to store value
    market_tuple=namedtuple('market_tuple', 'company symbol open high low close')
    #Store All Values
    final_list = [market_tuple(company_name_list[i],company_name_list[i][0:3],for_market_share[i],high_list[i],low_list[i],close_list[i]) for i in range(100)]
    print(f' Market open index :  {reduce(operator.add, for_market_share)}, Market high rate : {reduce(operator.add, high_list)} Market Low rate : {reduce(operator.add, low_list)} Market Close Rate {reduce(operator.add, close_list)} ')
    return final_list
