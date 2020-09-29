import pytest
import session10
import os
#import numpy as np
import inspect
import re

README_CONTENT_CHECK_FOR = [

]

CHECK_FOR_THINGS_NOT_ALLOWED = [
    
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 250, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 0

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session10)
    spaces = re.findall('\n +.', lines)
    line_no =1
    for space in spaces:
        line_no +=1
        print('=====', line_no, space)
        #print(lines)
        #assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        #assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 
        assert re.search('[a-zA-Z#@=1234\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@=1234\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_for_fastest_time():
    #session10.n_times=5
    assert (session10.check_performance() == 'Dictionary Slower'), 'Check your code again'

def test_named_tuple_performance():
    assert bool(session10.named_tuple_performance()), 'Check your code again'

def test_named_dict_performance():
    assert bool(session10.named_dict_performance()), 'Check your code again'

def test_nt_blood_group():
    val=session10.named_tuple_performance()
    assert bool('Largest Blood Group' in val), 'Check your code again'

def test_nt_location_count():
    val=session10.named_tuple_performance()
    assert bool('Average current location' in val), 'Check your code again'

def test_nt_oldest_person():
    val=session10.named_tuple_performance()
    assert bool('Oldest person age' in val), 'Check your code again'

def test_nt_avg_age():
    val=session10.named_tuple_performance()
    assert bool('Average age' in val), 'Check your code again'

def test_dc_blood_group():
    val=session10.named_dict_performance()
    assert bool('Largest Blood Group' in val), 'Check your code again'

def test_dc_location_count():
    val=session10.named_dict_performance()
    assert bool('Average current location' in val), 'Check your code again'

def test_dc_oldest_person():
    val=session10.named_dict_performance()
    assert bool('Oldest person age' in val), 'Check your code again'

def test_dc_avg_age():
    val=session10.named_dict_performance()
    assert bool('Average age' in val), 'Check your code again'

def test_stock_market():
    final_list=session10.stock_market()
    assert bool(isinstance(final_list[0],tuple)), 'Check your code again'

def test_stock_value():
    final_list=session10.stock_market()
    assert bool(final_list[0].company), 'Check your code again'
def test_stock_code():
    final_list=session10.stock_market()
    assert bool(final_list[0].symbol), 'Check your code again'
def test_stock_open():
    final_list=session10.stock_market()
    assert bool(final_list[0].open), 'Check your code again'
def test_stock_high():
    final_list=session10.stock_market()
    assert bool(final_list[0].high), 'Check your code again'
def test_stock_low():
    final_list=session10.stock_market()
    assert bool(final_list[0].low), 'Check your code again'
def test_stock_close():
    final_list=session10.stock_market()
    assert bool(final_list[0].close), 'Check your code again'

def test_things_not_allowed():
    code_lines = inspect.getsource(session10)
    for word in CHECK_FOR_THINGS_NOT_ALLOWED:
        assert word not in code_lines, 'Have you heard of Pinocchio?'
