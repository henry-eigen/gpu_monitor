
A simple bot to monitor gpu usage and message users whose idle processes are taking up server resources.

A messaging function (e.g. slack or twilio) should be used to replace the print statement in the GPU.send_message function in gpu_class.py

In its current state, the program only tracks the stats of nvidia gpus
