import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:

    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    rango = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=rango, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.scatter(0,0, c="green", edgecolors='none', s=30)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=30)

    ax.get_xaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)

    plt.show()

    continuar = input("Another RandowWalt (s/n)")
    if continuar == 'n':
        break