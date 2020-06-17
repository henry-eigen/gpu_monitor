import os
import time

from utils import *
from gpu_class import GPU


gpu_list = [GPU(0), GPU(1), GPU(2), GPU(3)]

for gpu in gpu_list:
    gpu.message_frequency = 3
    gpu.allowed_cycles = 8


print("\nAllowed idle time = 4 seconds\nMessage frequency = 1.5 seconds\n")
time.sleep(2)

# dummy data
data = [[0, 0, 0, 10], [None, None, None, 7], [None, None, None, 'john_doe']]
count = 0

def test_cycles(num_cycles):
    for i in range(num_cycles):
        update_data(gpu_list, data)
        time.sleep(0.5)
        print("    cycle:", count + i)

print("john_doe starts process")
time.sleep(2)
test_cycles(4)
count += 4


data[0][3] = 0
print("john_doe's process goes idle")
time.sleep(2)
test_cycles(10)
count += 10


data[1][3] = None
print("john_doe kills process")
time.sleep(2)
test_cycles(4)
count += 4


data[1][3] = 18
data[2][3] = "emily_smith"
print("emily_smith starts idle process")
time.sleep(2)
test_cycles(15)
