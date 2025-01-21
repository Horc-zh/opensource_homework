import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(
    xlabel="time (s)", ylabel="voltage (mV)", title="About as simple as it gets, folks"
)
ax.grid()
plt.show()

np.random.seed(19680801)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor="g", alpha=0.75)
plt.xlabel("Smarts")
plt.ylabel("Probability")
plt.title("Histogram of IQ")
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = "Frogs", "Hogs", "Dogs", "Logs"
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(
    sizes, explode=explode, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90
)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

x = np.linspace(0, 1, 500)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
fig, ax = plt.subplots()

ax.fill(x, y, zorder=10)
ax.grid(True, zorder=5)
plt.show()

with plt.xkcd():
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    plt.xticks([])
    plt.yticks([])
    ax.set_ylim([-30, 10])

    data = np.ones(100)
    data[70:] -= np.arange(30)

    plt.annotate(
        "THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED",
        xy=(70, 1),
        arrowprops=dict(arrowstyle="->"),
        xytext=(15, -10),
    )

    plt.plot(data)

    plt.xlabel("time")
    plt.ylabel("my overall health")
    fig.text(0.5, 0.05, '"Stove Ownership" from xkcd by Randall Monroe', ha="center")

    # Based on "The Data So Far" from XKCD by Randall Monroe
    # http://xkcd.com/373/

    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.bar([0, 1], [0, 100], 0.25)
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.set_xticks([0, 1])
    ax.set_xlim([-0.5, 1.5])
    ax.set_ylim([0, 110])
    ax.set_xticklabels(["CONFIRMED BY\nEXPERIMENT", "REFUTED BY\nEXPERIMENT"])
    plt.yticks([])

    plt.title("CLAIMS OF SUPERNATURAL POWERS")

    fig.text(0.5, 0.05, '"The Data So Far" from xkcd by Randall Monroe', ha="center")
    plt.show()
