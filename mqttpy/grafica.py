
from __future__ import print_function
import qwiic_max3010x
import time
import sys

sensor = qwiic_max3010x.QwiicMax3010x()

#Plotter Stuff
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xlen= 100 #sample number, increments and is used for labeling x axis in plot
xs = list(range(0,xlen))
ys = [0]*xlen
line, = ax.plot(xs, ys)
plt.title('Heartbeat over time')
plt.ylabel('IR Value')

# This function is called periodically from FuncAnimation
def animate(i, ys):
    # Read IR from MAX3010x
    ir = sensor.getIR()

    ys.append(ir)
    ys = ys[-xlen:]
    line.set_ydata(ys)
    ax.set_ylim([min(ys),max(ys)])

    return line,


def runExample():

    print("\nSparkFun MAX3010x Photodetector - Example 4\n")

    if sensor.begin() == False:
        print("The Qwiic MAX3010x device isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    else:
        print("The Qwiic MAX3010x is connected.")

    # Setup to sensor
    ledBrightness = 0x1F # Options: 0=Off to 255=50mA
    sampleAverage = 8 # Options: 1, 2, 4, 8, 16, 32
    ledMode = 3 # Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
    sampleRate = 100 # Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
    pulseWidth = 411 # Options: 69, 118, 215, 411
    adcRange = 4096 # Options: 2048, 4096, 8192, 16384

    if sensor.setup(ledBrightness, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange) == False:
        print("Device setup failure. Please check your connection", \
            file=sys.stderr)
        return
    else:
        print("Setup complete.")
    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(ys,), interval=10, blit=True)
    plt.show()


if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 4")
        sys.exit(0)
