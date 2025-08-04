# import csv
#
# with open('D:\\Reports\\data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
#
# with open('D:\\Reports\\data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Bharath', 'Python SDET', '20000'])
#     writer.writerow(['Kumar', 'Java SDET', '200000'])


import csv


# fieldnames = ['name', 'department', 'salary']
#
# with open('D:\\Reports\\data.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()

# data = [
#     {'name': 'Bharath', 'department': 'Account', 'salary': '20000'},
#     {'name': 'Kumar', 'department': 'Sales', 'salary': '15000'},
#     {'name': 'Reddy', 'department': 'Manager', 'salary': '30000'}
# ]
# with open('D:\\Reports\\data.csv', 'a', newline='') as file:
#     fieldnames = ['name', 'department', 'salary']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writerows(data)
#     print("Data written to csv file successfully")


# with open('D:\\Reports\\data.csv') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if int(row['salary']) > 15000:
#             print(row['name'], "-", row['salary'])


def two_sum(nums, target):
    indexed_nums = [(value, index) for index, value in enumerate(nums)]

    indexed_nums.sort()
    left = 0
    right = len(indexed_nums) - 1

    while left < right:
        curr_sum = indexed_nums[left][0] + indexed_nums[right][0]
        if curr_sum == target:
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return []


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))


def two_sum1(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


nums = [2, 7, 11, 15]
target = 14
print(two_sum1(nums, target))


def max_num(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest


print(max_num([2, 4, 66, 8]))

"""import csv

data = [
    ["Name", "Age", "City"],
    ["Bharath", 25, "Bangalore"],
    ["Kiran", 30, "Chennai"],
    ["Ravi", 28, "Hyderabad"]
]

with open("people.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)"""

"""import csv

# Writing with DictWriter
with open("people_dict.csv", mode="w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Bharath", "Age": 25, "City": "Bangalore"})
    writer.writerow({"Name": "Kiran", "Age": 30, "City": "Chennai"})"""

# Reading with DictReader
"""with open("people_dict.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["City"])"""

