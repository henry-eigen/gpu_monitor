import time

class GPU():
    def __init__(self, num):
        self.num = num
        self.activity = []
        self.pids = []
        self.users = []
        self.message_frequency = 10800 # message every ~3 hours
        self.allowed_cycles = 750 # message after ~8 hours
        self.message_sent = False
            
    def reset(self):
        self.activity.clear()
        self.pids.clear()
        self.users.clear()
        self.message_sent = False
        
    def add_data(self, info):
        self.activity.append(info[0])
        self.pids.append(info[1])
        self.users.append(info[2])
        
    def send_message(self):
        
        self.message_sent = time.time()
        
        idle_time = len(self.activity) / 120
        
        message = "{} has left GPU {} idle for {:.10} hours".format(self.users[-1], self.num, idle_time)
        
        # ...
        print(message)
        # Send message via Slack 
        # ...
        
    def try_message(self):
        if not self.message_sent:
            self.send_message()
        
        #elif time.time() - self.message_sent > 10800: # if it's been 3 hours since last message
        elif (time.time() - self.message_sent) > self.message_frequency: # if it's been 3 hours since last message
            self.send_message()
        
    def new_cycle(self, info):
        
        # skip cycle if no process
        if info[1] is None:
            self.reset()
            return
        
        # skip cycle if gpu is active
        if info[0] > 0:
            self.reset()
            return
        
        # skip cycle if no previous activity
        if len(self.pids) == 0:
            self.add_data(info)
            return
            
        # skip cycle if new process
        if info[1] != self.pids[-1]:
            self.reset()
            self.add_data(info)
            return
        
        # skip cycle if inactivity is brief
        #if len(self.activity) < 750: # roughly 8 hours
        if len(self.activity) < self.allowed_cycles: # roughly 8 hours
            self.add_data(info)
            return
     
        self.add_data(info)
        self.try_message()