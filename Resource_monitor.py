#Importing the Psutil package
import psutil

#Setting the CPU threshold value
cpu_threshold=80.0

def compute_cpu():
    try:
        while True:
            
            #Getting the CPU Current Usage
            cpu_compute = psutil.cpu_percent(interval=1)
            print(f"Monitoring CPU usage... {cpu_compute}%")
            
            #Checking if the CPU usage is > then the threshold value
            if cpu_compute>cpu_threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_compute}%")

    except KeyboardInterrupt:
        print("Interrupted by User")
        
        #Feedback from the user:
        emergency_exit=input("Do you want to start the process again or not(Y/N): ")
        if emergency_exit =='Y':
            compute_cpu()
        else:
            print("OOPS!! Its not us its you.")
        
    
    except Exception as e:
        print(f"Error : format{e}")

# Calling the Compute_Cpu function to monitor the CPU utilization
compute_cpu()
            

            
