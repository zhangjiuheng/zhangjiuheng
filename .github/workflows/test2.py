import time

while True:
    current_time = time.strftime("%H:%M:%S")
    print("Current time is:", current_time)
    time.sleep(1)
    break
