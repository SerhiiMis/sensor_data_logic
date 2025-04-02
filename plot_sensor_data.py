import time
import matplotlib.pyplot as plt

values = []
plt.ion()
fig, ax = plt.subplots()

while True:
    try:
        with open("sensor_data.txt", "r") as file:
            lines = file.readlines()
            values = [int(line.strip()) for line in lines if line.strip().isdigit()] # Filter out non-integer lines

            ax.clear()
            ax.plot(values, label='Sensor Value')
            ax.set_ylim(0, 100)
            ax.set_title("Live Sensor Data")
            ax.set_xlabel("Time")
            ax.set_ylabel("Value")
            ax.legend()
            plt.pause(0.5)

    except KeyboardInterrupt:
        print("Stopped by user.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(1)

