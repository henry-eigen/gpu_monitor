import os
import time

from utils import *
from gpu_class import GPU


gpu_list = [GPU(0), GPU(1), GPU(2), GPU(3)]

while True:
    
    data = get_gpu_info()
    
    update_data(gpu_list, data)
    
    time.sleep(30)