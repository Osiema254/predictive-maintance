import random
import time
import pandas as pd
import matplotlib.pyplot as plt
print("Predictive Maintenance System ")
print()
print("Machine Monitoring Started........")

safe_count = 0
warning_count = 0
critical_count = 0

readings = []

for i in range(10):
    print()
    print("========== READING", i + 1, "==========")


    machine_mode = ["NORMAL", "FAULTY"]
    mode = random.choice(machine_mode)
    print("Machine Mode: ", mode)

    if mode == "NORMAL":

        temperature = random.uniform(30, 65)
        print("Temperature: ", temperature, "°C")

        vibration = random.uniform(1, 5)
        print("Vibration: ", vibration, "mm/s")

        rotation = random.randint(1300, 1600)
        print("Rotational Speed: ", rotation, "RPM")


    else:
        temperature = random.uniform(66, 110)
        print("Temperature: ", temperature, "°C")

        vibration = random.uniform(5.1, 10)
        print("Vibration: ", vibration, "mm/s")

        rotation = random.randint(1601, 2000)
        print("Rotational Speed: ", rotation, "RPM")

    if temperature <= 65:
        temperature_status = "Normal"

    elif temperature > 65 and temperature <= 90:
        temperature_status = "Warning"

    else:
        temperature_status = "Critical"
    print("Temperature Status: ", temperature_status)

    if vibration <= 5:
        vibration_status = "Normal"

    elif vibration > 5 and vibration <= 8:
        vibration_status = "Warning"

    else:
        vibration_status = "Critical"
    print("Vibration Status: ", vibration_status)

    if rotation >= 1300 and rotation <= 1600:
        rotation_status = "Normal"

    elif rotation > 1600 and rotation <= 1800:
        rotation_status = "Warning"

    else:
        rotation_status = "Critical"
    print("Rotation Status: ", rotation_status)


    if (temperature_status == "Critical" or
            vibration_status == "Critical" or
            rotation_status == "Critical"):
        overall_status = "CRITICAL"

    elif (temperature_status == "Warning" or
          vibration_status == "Warning" or
          rotation_status == "Warning"):
        overall_status = "WARNING"

    else:
        overall_status = "SAFE"

    print()
    print("Overall Machine Status:", overall_status)

    reading = {
        "temperature": temperature,
        "vibration": vibration,
        "rotation": rotation,
        "temperature_status": temperature_status,
        "vibration_status": vibration_status,
        "rotation_status": rotation_status,
        "overall_status": overall_status,
        "mode": mode
    }

    readings.append(reading)

    if overall_status == "SAFE":
        safe_count += 1

    print("Safe readings:", safe_count)

    if overall_status == "WARNING":
        warning_count += 1

    print("Warning readings:", warning_count)


    if overall_status == "CRITICAL":
        critical_count += 1

    print("Critical readings:", critical_count)


    time.sleep(2)

df = pd.DataFrame(readings)
print(df)

print()
print("DATA ANALYSIS")
print("========================")

print("Average Temperature:", df["temperature"].mean())
print("Maximum Temperature:", df["temperature"].max())
print("Average Vibration:", df["vibration"].mean())
print("Maximum Vibration:", df["vibration"].max())

print()
print("STATUS ANALYSIS")
print("========================")

print("SAFE:", (df["overall_status"] == "SAFE").sum())
print("WARNING:", (df["overall_status"] == "WARNING").sum())
print("CRITICAL:", (df["overall_status"] == "CRITICAL").sum())

print()
print("==================================")
print("         MONITORING SUMMARY")
print("==================================")

total = safe_count + warning_count + critical_count
print("Total Readings: ", total)
print("Safe Readings: ", safe_count)
print("Warning Readings: ", warning_count)
print("Critical Readings: ", critical_count)

print("===================================")

print("        MAINTENANCE ADVICE")

print("====================================")

if critical_count > 0:
    print("CRITICAL: Machine may require immediate maintenance.")
    print("Recommendation: Stop machine and inspect immediately.")

elif warning_count > 0:
    print("WARNING: Machine shows signs of abnormal operation.")
    print("Recommendation: Inspect the machine and monitor closely.")

else:
    print("SAFE: Machine operating within normal conditions.")
    print("Recommendation: Continue normal operation.")

print()
print("Number of stored readings:", len(readings))

plt.plot(df["temperature"])
plt.title("Machine Temperature")
plt.xlabel("Reading")
plt.ylabel("Temperature (°C)")
plt.show()

plt.plot(df["vibration"])
plt.title("Machine Vibration")
plt.xlabel("Reading")
plt.ylabel("Vibration (mm/s)")
plt.show()

plt.plot(df["rotation"])
plt.title("Machine Rotational Speed")
plt.xlabel("Reading")
plt.ylabel("Rotational Speed (RPM)")
plt.show()