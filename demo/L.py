"""list=[2,4,5,6,7,9]
e=[x for x in list if x%2==0]
o=[x for x in list if x%2!=0]
print(e)
print(o)
list.reverse()
print(list)"""

"""try:
    result = 10 / 1
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")
finally:
    print("This block runs no matter what.")"""


"""def count_chars(s,char):
    count=0
    for c in s:
        if c==char:
            count+=1
    return count
demo=count_chars("dextrix",'x')
print(demo)"""

"""def factorial(n):
   fact=1
   for i in range(1,n+1):
       fact=fact*i
   return fact
num=int(input("The factorial of num: "))
result=factorial(num)
print(result)"""

"""def find_maximum(numbers):
    max_num=numbers[0]
    for num in numbers[1:]:
        if num>max_num:
            max_num=num
    return max_num
numbers=[10,30,40,70]
print(find_maximum(numbers))"""

"""def find_minimum(numbers):
    max_num=numbers[0]
    for num in numbers[1:]:
        if num<max_num:
            max_num=num
    return max_num
numbers=[10,30,40,70]
print(find_minimum(numbers))"""

# second largest element
"""def find_second_largest(numbers):
    numbers.sort()
    return numbers[-2]
numbers = [10, 30, 40, 70]
print(f"The second largest number is: {find_second_largest(numbers)}")"""


def find_second_largest(numbers):
    numbers.sort()  # Sort the list in ascending order
    if len(numbers) < 2:  # If there are fewer than 2 elements
        return None

    largest = numbers[-1]  # The largest element (last element after sorting)

    # Traverse the list from second last to the first element
    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] != largest:  # If the number is not the largest, it's the second largest
            return numbers[i]
    # If no second largest element found (i.e., all numbers are the same)
    return None

# Example usage
numbers = [10, 30, 40, 70, 70, 30]
print(f"The second largest number is: {find_second_largest(numbers)}")













