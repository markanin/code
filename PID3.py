# Example simulation PID controller

import numpy as np
import matplotlib.pyplot as plt

Kp = 0.2
Ki = 0.3
Kd = 3.0

t_0 = 0         # time - begin simulation [sec]
t_F = 180       # time - end simulation [sec]

length = 1000   # number of datapoints along t-axis

t = np.linspace(t_0, t_F, length)
dt = np.mean(np.diff(t))

r = np.zeros(length)    # setpoint
y = np.zeros(length)    # process value (measured or simulated)
e = np.zeros(length)    # error = r-y

# define setpoint (varies with time, staircase function)
for j in range(1, length):
    if j/length*(t_F-t_0) < 20:
        r[j] = 0
    elif j/length*(t_F-t_0) < 60:
        r[j] = 1
    elif j/length*(t_F-t_0) < 100:
        r[j] = 2
    else:
        r[j] = 0

ITerm = 0

tlastPID = 0

dtPID = 2 # period of PID controller execution [sec]

u = 0 #

for j in range(1, length-1):

    # simulate process value (assume motor)
    y[j] = 0.7*y[j-1]+0.5*u

    e[j] = r[j] - y[j]

    # time to update PID?
    tnow = t_0 + j/length*(t_F - t_0)
    if tnow - tlastPID > dtPID:
        print("exec time %d" % tnow)
        PTerm = Kp * e[j]
        ITerm += Ki * e[j] * dtPID
        DTerm = Kd * (e[j] - e[j-1]) / dtPID
        u = PTerm + ITerm + DTerm
        tlastPID = tnow


# plot:
# -----------------------------
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(t, y, label = 'y: process output')
ax.plot(t, r, label = 'r: setpoint')

plt.xlim([t_0, t_F])

ax.set_xlabel('t [sec]')
ax.set_ylabel('[unit]', color='g')

ax.annotate('Kp=%.2f, Ki=%.2f, Kd=%.2f' % (Kp, Ki, Kd), xy=(0.2,0.2))

ax.legend()

plt.title('PID test')
plt.grid()
plt.show()




