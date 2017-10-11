import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(i):
    # one point (t,y) added to the plot for every iteration
    plt.scatter(t[i], y[i], marker='x', color='b')
    plt.title('Frame %d' % i)
    print('frame %d' % i)

if __name__ == "__main__":
    # make sure FFmpeg writers are available
    print(animation.writers.list())

    # define FFmpeg writer
    # Windows: the binaries of FFmpeg need to be "reachable"
    # edit the user environment variables accordingly
    FFMpegWriter = animation.writers['ffmpeg']
    metadata = dict(title='Plot animation',
                    artist='Matplotlib',
                    comment='Tutorial plot animation')
    writer = FFMpegWriter(fps=15, metadata=metadata)

    # define function to plot
    t = np.linspace(-4, 4, 500)
    y = np.exp(-t ** 2) + np.random.normal(0, 0.05, t.shape)
    L = len(t)

    fig = plt.figure()
    fig.set_dpi(100)

    plt.xlabel('x')
    plt.ylabel('f(x) = exp[x^2] + noise')
    plt.grid(True)
    plt.xlim([min(t), max(t)])
    plt.ylim([-0.2, 1.2])

    print("Starting animation, %d frames..." % L)
    anim = animation.FuncAnimation(fig, animate, frames=L, interval=10, repeat=False)

    # save animation as video
    # or skip this line to view the animation
    anim.save('example_anim.mp4', writer=writer)

    plt.show()