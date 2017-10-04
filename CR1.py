import numpy as np
import matplotlib.pyplot as plt

t_0 = 0     # time - begin simulation [sec]
t_F = 0.3   # time - end simulation [sec]

C = 10 * 10**(-6)   # Capacitance [F] (ceramic capacitor)
R = 600             # Resistance [Ohm]

length = 1000  # number of datapoints along t-axis

t = np.linspace(t_0, t_F, length)
dt = np.mean(np.diff(t))

vi = np.zeros(length)   # input (square waveform, bipolar, see definition below)
q = np.zeros(length)    # output (capacitor charge)
i = np.zeros(length)    # output (current)
vc = np.zeros(length)   # output (capacitor voltage)

f = 10 # frequency of waveform (50%: +1, 50%: -1)
t_start_waveform = 0.05 # [sec]

# define input waveform:
for j in range(1, length):
    if j < t_start_waveform/(t_F-t_0)*length:
        vi[j] = 0
    elif j < (t_start_waveform + 1*(1/f)/2)/(t_F-t_0)*length:
        vi[j] = 1
    elif j < (t_start_waveform + 2*(1/f)/2)/(t_F-t_0)*length:
        vi[j] = -1
    elif j < (t_start_waveform + 3*(1/f)/2)/(t_F-t_0)*length:
        vi[j] = 1
    elif j < (t_start_waveform + 4*(1/f)/2)/(t_F-t_0)*length:
        vi[j] = -1
    else:
        vi[j] = 0

# solve circuit:
for j in range(1, length):

    q[j] = q[j - 1] + vi[j]*dt/R - q[j-1]*dt/(R*C)
    vc[j] = q[j]/C

    if j > 0:
        i[j] = ((q[j] - q[j - 1])/dt)*1e3 # convert to [mA]

# scale capacitor charge for easy plotting:
qmax = C*1 # maximum charge in [Coulomb], absolute value
for j in range(1, length):
    q[j] = q[j]/qmax


# plot vi and capacitor charge:
# -----------------------------
plt.plot(t, vi, 'g-')
plt.plot(t, q, 'b-')
plt.xlim([t_0, t_F])

plt.xlabel('t [sec]')
plt.ylabel('vi [V], q [C/C]', color='g')

plt.title('RC circuit: vi-t, q-t')
plt.grid()
plt.show()

# plot vi and current:
# --------------------
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(t, vi, 'g-')
ax2.plot(t, i, 'b-')

ax1.set_xlabel('t [sec]')
ax1.set_xlim([t_0, t_F])
ax1.set_ylabel('vi [V]', color='g')
ax2.set_ylabel('i [mA]', color='b')

plt.title('RC circuit: vi-t, i-t')
plt.grid()
plt.show()






