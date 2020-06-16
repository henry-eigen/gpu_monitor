import os
import time

from utils import *
from gpu_class import GPU


data = [[0, 0, 0, 0], [None, None, None, 7], [None, None, None, 'john doe']]


# test with dummy data

gpu_list = [GPU(0), GPU(1), GPU(2), GPU(3)]

for gpu in gpu_list:
    gpu.message_frequency = 3
    gpu.allowed_cycles = 10

data[1][3] = 18

for i in range(13):
    update_data(gpu_list, data)
    time.sleep(0.5)
    print("cycle", i)
    
print("idle process killed")
data[1][3] = 7

for i in range(23):
    update_data(gpu_list, data)
    time.sleep(0.5)
    print("cycle", i + 13)