import matplotlib.pyplot as plt

cuadrados = [1,4,9,16,25]

x_axis = [1,2,3,4,5]

plt.style.use("seaborn-dark")

fig, ax = plt.subplots()
ax.plot(x_axis,cuadrados,linewidth=3)

ax.set_title("Números cuadrados", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Cuadrados", fontsize=14)
ax.tick_params(axis='both', labelsize=15)

plt.show()
