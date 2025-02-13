def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}") #This will print 0

my_numbers_with_zero = [10, 0, 30, 40, 50]
average_with_zero = calculate_average(my_numbers_with_zero)
print(f"The average with zeros is: {average_with_zero}") #this will print 26.0

my_numbers_string = [10, "20", 30, 40, 50]
average_string = calculate_average(my_numbers_string) #This will raise a TypeError