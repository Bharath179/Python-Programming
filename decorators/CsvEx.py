# import comma_seperated_values
#
# # writing to comma_seperated_values file
# with open('names.comma_seperated_values', 'w') as csvfile:
#     fields = ['Name', 'Branch']
#     writer=comma_seperated_values.DictWriter(csvfile,fieldnames=fields)
#     writer.writeheader()
#     writer.writerow({'Name':'Bharath' ,'Branch':'Automation'})
#     writer.writerow({'Name':'Vidya','Branch': 'SQL'})
#     writer.writerow({'Name':'Sweaty','Branch': 'Yoga'})

def f1():
    print("Hello")
print(f1)
print(id(f1))


