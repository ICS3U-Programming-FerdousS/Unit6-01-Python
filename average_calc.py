#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: March 23, 2022
# This program we generate random number (0-100)
# then we store them in a list and display the average of the
# and numbers.

# import math random
import random
import Constant

def main():
    # variables
    max_size = 10
    min_num = 0
    max_num = 100
    # empty list
    list_of_number =[]
    # loop counter
    counter = 0
    num_sum = 0
    
    # loop to generate random number and append it to list
    for counter in range(0, max_size, 1):
        # set random number between 0-100
        random_number = random.randint(0, 100)
        list_of_number.append(random_number)
        print(random_number, "added to the list in position", counter)
    
    # loop to add the list number
    for counter in range(0, max_size, 1):
        num_sum = num_sum + list_of_number[counter]

    # calculate and display the number 
    average_num = num_sum / len(list_of_number)
    print("The average is {:.1f} ".format(average_num))
        
    


if __name__ == "__main__":
    main()
