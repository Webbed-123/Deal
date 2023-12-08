import random
import math
money_amounts = [0.01,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]
cases = {}
money_amounts_left = [0.01,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]
round_cases = {1:6,2:5,3:4,4:3,5:2,6:1,7:1,8:1,9:1,10:1,11:1}

for x in range(1,27):
    num_in_case = random.randint(0,len(money_amounts)-1)
    cases[x] = money_amounts[num_in_case]
    del money_amounts[num_in_case]


def begin():
    return "Howie: Welcome to Deal or No Deal! My name is Howie Mandel. What's your name, contestant?"

def start_game():
    return "It's time to start the game. Pick a case that you think has a million dollars in it!"

def print_cases():
    return cases.keys()

def delete_cases(case):
    del cases[int(case)]

def print_money():
    return money_amounts_left

def delete_money(money_amount):
    money_amounts_left.remove(int(money_amount))

def get_num_of_cases_to_pick(round_num):
    return round_cases[int(round_num)]

def check_case(case):
    if(int(case) not in cases or (case.isdigit()) == False):
        return False
    else:
        return True
    
def player_case(case_num):
    return cases[int(case_num)]
    
def open_case(case_picked,round_num):
    cases_to_pick = int(round_cases[round_num])
    #while(cases_to_pick > 0)
    #try:
       # check_case_num(case_picked)
   # except:
       # return False
    
    case_new = cases[int(case_picked)]
    del cases[int(case_picked)]
    case_copy = case_new
    money_amounts_left.remove(case_copy)
    return(f"\nValue inside case {int(case_picked)}: ${case_new}")


def offers():
    total = 0
    for num in money_amounts_left:
        total = total + num
    average = int(total//len(money_amounts_left))
    return math.floor(average)

# def get_last_case():
#     last_case = list(cases.values()).index()
#     return last_case

def get_last_money_amounts(index):
    return money_amounts_left[index]
    
    
    

    
    