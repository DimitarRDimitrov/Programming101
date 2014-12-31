from animals import Animals
from zoo import Zoo
from json_adder import Animal_Add
import json


def printer1():  # Printva, nekvi na4alni gluposti :D
    print("\n\n\nThis is a simulator of Zoo!")
    print("And its not perfect so one month is aways 30 days")
    print("and one year is aways %s days\n" % (30*12))
    print("Lets start making the Zoo:")


def zoo_init():  # Inicializira zoo
    print("First we will need the capacity of the zoo.")
    print("How many animals(max) you want your Zoo to get?")
    capacity = int(input())
    print("Now we need some monny for the start. How much starting monny you want?")
    budget = int(input())
    return Zoo(capacity, budget)


def interval_to_days():
    print("Enter the interval of time:")
    interval_of_time = input()
    print("Enter the period:")
    period = int(input())
    period_of_days = 0
    if interval_of_time == "days":
        period_of_days = period
    elif interval_of_time == "months":
        period_of_days = period * 30
    elif interval_of_time == "weeks":
        period_of_days = period * 7
    elif interval_of_time == "years":
        period_of_days = period * 360
    else:
        print("Invalid interval of time!")
        interval_to_days()
    return period_of_days


def growing_of_animals(zoo, days):
    months_to_grow = days // 30
    for animal in zoo.see_animals():
        if months_to_grow > 0:
            for i in range(1, months_to_grow):
                animal.grow()
                if animal.is_it_die():
                    



def starter_pack_animals_for_new_zoo(zoo):
    pesho_tiger = Animals("Pesho", 2, "tiger", "male", 3)
    ivo_panda = Animals("Ivo", 3, "panda", "male", 5)
    gosho_lion = Animals("Gosho", 4, "lion", "male", 4)
    penka_tiger = Animals("Penka", 2, "tiger", "female", 2)
    ani_panda = Animals("Ani", 3, "panda", "female", 4)
    desi_lion = Animals("Desi", 4, "lion", "female", 3)
    zoo.accommodate(pesho_tiger)
    zoo.accommodate(ivo_panda)
    zoo.accommodate(gosho_lion)
    zoo.accommodate(penka_tiger)
    zoo.accommodate(ani_panda)
    zoo.accommodate(desi_lion)


def check_funds(zoo, days):
    if days == 1:
        return(zoo.zoo_daily_balance())
    for days in range(1, days - 1):
        if zoo.zoo_daily_balance() < 1:
            print("Insufficient funds. The zoo has been closed!")
    return(zoo.zoo_daily_balance())


def main():
    #month = 30 * day
    #year = month * 12
    printer1()
    #initializing zoo
    my_zoo = zoo_init()
    #converting user input of period to days
    days_to_simulate = interval_to_days()
    #adding initial animals to the zoo
    starter_pack_animals_for_new_zoo(my_zoo)
    growing_of_animals(my_zoo, days_to_simulate)
    #checking balance
    check_funds(my_zoo, days_to_simulate)



if __name__ == '__main__':
    main()
