import os
import re
import time


# get usage for each gpu
def get_usage(info):
    usage_indices = [i + 1 for i, x in enumerate(info) if "Utilization" in x]

    usage_str = [info[i] for i in usage_indices]

    usage = [re.search("\:(.*?)\%", ex).group(1) for ex in usage_str]
    
    usage = [int(val.replace(" ", "")) for val in usage]

    return usage


# get the pid run by each gpu
def get_pid(info):
    pid_indicies = [i + 1 for i, x in enumerate(info) if "Processes" in x]
    pid_str = [info[i] for i in pid_indicies]
    for i, s in enumerate(pid_str):
        if "Process ID" in s:
            pid_str[i] = int(re.search("\:\s*(.*)", s).group(1))
        else:
            pid_str[i] = None
            
    return pid_str


# get the user behind a pid
def get_user(pid):
    ps_command = "ps -u -p {} | cut -d' ' -f1".format(pid)

    ps_info = os.popen(ps_command).read()

    user = ps_info.split("\n")[1]
    
    return user


# map pid list to users
def get_user_list(pid_list):
    
    users = []
    
    for p in pid_list:
        if p is None:
            users.append(None)
        else:
            users.append(get_user(p))
            
    return users


# get nvidia-smi info
def get_gpu_info():
    
    stream = os.popen('nvidia-smi --query')
    output = stream.read()
    output = output.split("\n")
    
    usage = get_usage(output)
    pid_list = get_pid(output)
    user_list = get_user_list(pid_list)
    
    return [usage, pid_list, user_list]


# update gpu list
def update_data(gpu_list, data):
    for i, gpu in enumerate(gpu_list):
        gpu_list[i].new_cycle([data[0][i], data[1][i], data[2][i]])