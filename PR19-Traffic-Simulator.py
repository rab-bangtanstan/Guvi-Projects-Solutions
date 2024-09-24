import time

def traffic_light_control():
    while True:
        print("Red Light - STOP")
        time.sleep(5)  # Red light for 5 seconds
        
        print("Green Light - GO")
        time.sleep(6)  # Green light for 6 seconds
        
        print("Yellow Light - SLOW")
        time.sleep(2)  # Yellow light for 2 seconds

# Run the traffic light control
traffic_light_control()
