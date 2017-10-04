import numpy as np
import matplotlib.pyplot as plt
import math

t_0 = 0     # time - begin simulation [sec]
t_F = 0.3   # time - end simulation [sec]

L = 0.50        # Inductance [H]
R = 100         # Resistance [Ohm]
C = 10*1e-6     # Capacitance [F]

length = 1000 # number of datapoints along t-axis

def input_voltage_sinewave():
    '''
    define input sinewave
    '''
    for j in range(1, length):
        vi[j] = math.sin(2 * math.pi * f * j / length * (t_F - t_0))

def input_bipolar_square():
    t_start_waveform = 0.05  # [sec]

    # define input waveform:
    for j in range(1, length):
        if j < t_start_waveform / (t_F - t_0) * length:
            vi[j] = 0
        elif j < (t_start_waveform + 1 * (1 / f) / 2) / (t_F - t_0) * length:
            vi[j] = 1
        elif j < (t_start_waveform + 2 * (1 / f) / 2) / (t_F - t_0) * length:
            vi[j] = -1
        elif j < (t_start_waveform + 3 * (1 / f) / 2) / (t_F - t_0) * length:
            vi[j] = 1
        elif j < (t_start_waveform + 4 * (1 / f) / 2) / (t_F - t_0) * length:
            vi[j] = -1
        else:
            vi[j] = 0

t = np.linspace(t_0, t_F, length)
dt = np.mean(np.diff(t))

vi = np.zeros(length)   # input (sinewave)
i = np.zeros(length)    # output (current)
w = np.zeros(length)    # output (w(t) = di(t)/dt = ul/L)
qc = np.zeros(length)   # output (capacitor charge)
vc = np.zeros(length)   # output (capacitor voltage)

f = 10 # sinewave frequency

#input_voltage_sinewave()
input_bipolar_square()

# solve circuit:
for j in range(1, length):
    i[j] = i[j-1] + w[j-1]*dt
    w[j] = w[j-1] - R/L*w[j-1]*dt - 1/(L*C)*i[j-1]*dt + (vi[j]-vi[j-1])
    qc[j] = qc[j-1] + i[j-1]*dt
    vc[j] = qc[j]/C

# scale for easy plotting:
for j in range(1, length):
    i[j] = i[j] * 1000 # [mA]

# plot vi(t) and capacitor voltage vc(t):
# -----------------------------
plt.plot(t, vi, 'g-')
plt.plot(t, vc, 'b-')
plt.xlim([t_0, t_F])

plt.xlabel('t [sec]')
plt.ylabel('vi [V], vc [V]', color='g')

plt.title('RLC circuit: vi-t, vc-t')
plt.grid()
plt.show()

# plot vi(t) and current i(t):
# -----------------------------
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(t, vi, 'g-')
ax2.plot(t, i, 'b-')

ax1.set_xlabel('t [sec]')
ax1.set_xlim([t_0, t_F])
ax1.set_ylabel('vi [V]', color='g')
ax2.set_ylabel('i [mA]', color='b')

plt.title('RLC circuit: vi-t, i-t')
plt.grid()
plt.show()







