# Python program to find upper and lower case characters

"""def string_test(s):
    d={'Upper_case':0,'Lower_case':0}
    for i in s:
        if i.islower():
            d['Lower_case']+=1
        elif i.isupper():
            d['Upper_case']+=1
        else:
            pass
    print("Upper case letters:",d['Upper_case'])
    print("Lower case letters:", d['Lower_case'])
string_test("This is Dextris Company")"""


# def string_test(s):
#     upper=0
#     lower=0
#     for i in s:
#         if i.islower():
#             lower=lower+1
#         elif i.isupper():
#             upper=upper+1
#         else:
#             pass
#     print("Upper case letters:",upper)
#     print("Lower case letters:", lower)
# string_test("This is Dextris Company")

import time
import gc


class SensorData:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.data = (i for i in range(1000000)) # Simulate large data


def collect_data():
    print("Collecting sensor data...")
    for i in range(1000):
        data_obj = SensorData(sensor_id=i)
        print(f"Sensor {i} collected")
        del data_obj  # Remove reference to free memory
        time.sleep(1)

    # Manually trigger garbage collection
    print("Forcing garbage collection...")
    gc.collect()
    print("Garbage collection complete")


collect_data()
