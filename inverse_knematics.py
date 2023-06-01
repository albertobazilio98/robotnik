import matplotlib.pyplot as plt
import math
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def hip(cat1, cat2):
    return math.sqrt(cat1**2 + cat2**2)

def inverse_calculate(point, arms):
    l1 = arms[0]
    l2 = arms[1]
    x = point[0]
    y = point[1]

    distance = hip(x, y)

    if distance > l1 + l2 or distance < abs(l1 - l2):
        print("Coordenadas fora do alcance do robô")
        return None, None

    theta2 = math.acos((x**2 + y**2 - l1**2 - l2**2)/(2*l1*l2))

    beta = math.atan2(x, y)
    psi = math.acos((x**2 + y**2 + l1**2 - l2**2)/(2*l1*math.sqrt(x**2 + y**2)))
    theta1 = beta + (psi if theta2 < 0 else - psi)


    return [theta1, theta2], [math.degrees(theta1), math.degrees(theta2)]

def forward_calculate(arms, rad_angles):
    x = 0
    y = 0

    points_x = [x]
    points_y = [y]

    for i in range(len(arms)):
        x += arms[i] * math.cos(sum(rad_angles[:i+1]))
        y += arms[i] * math.sin(sum(rad_angles[:i+1]))
        points_x.append(x)
        points_y.append(y)

    return points_x, points_y

def plot_2d_robot(points_x, points_y):
    lines.set_data(points_x, points_y)
    points.set_data(points_x, points_y)
    canvas.draw()

def atualizar_valores(_):
    arm_1 = arm_1_scale.get()
    arm_2 = arm_2_scale.get()
    x_point = x_scale.get()
    y_point = y_scale.get()

    arms = [arm_1, arm_2]
    coord = [x_point, y_point]
    print(coord)

    angles_rad, angles_deg = inverse_calculate(coord, arms)

    if angles_rad == None or angles_deg == None:
        robot_position.config(text="Posição inválida\n")
        plot_2d_robot([0,0], [0,0])
        return

    points_x, points_y = forward_calculate(arms, angles_rad)
    print(points_x, points_y)
    plot_2d_robot(points_x, points_y)
    robot_position.config(text=f"angulo 1: {angles_deg[0]:.2f} | angulo 2: {angles_deg[1]:.2f}\n coordenadas: {points_x[-1]:.2f}, {points_y[-1]:.2f}")

root = tk.Tk()
root.title("Cinemática direta")

tk.Label(root, text="Tamanho dos braços").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Posições").grid(row=0, column=1, sticky="w")

arm_1_scale = tk.Scale(root, from_=0, to=10, resolution=0.1, length=300, orient="horizontal", command=atualizar_valores)
arm_1_scale.set(10)
arm_1_scale.grid(row=1, column=0, padx=5, pady=5, sticky="w")

x_scale = tk.Scale(root, from_=-20, to=20, resolution=0.1, length=300, orient="horizontal", command=atualizar_valores)
x_scale.set(7)
x_scale.grid(row=1, column=1, padx=5, pady=5, sticky="w")

arm_2_scale = tk.Scale(root, from_=0, to=10, resolution=0.1, length=300, orient="horizontal", command=atualizar_valores)
arm_2_scale.set(10)
arm_2_scale.grid(row=2, column=0, padx=5, pady=5, sticky="w")

y_scale = tk.Scale(root, from_=-20, to=20, resolution=0.1, length=300, orient="horizontal", command=atualizar_valores)
y_scale.set(7)
y_scale.grid(row=2, column=1, padx=5, pady=5, sticky="w")


fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
lines, = ax.plot([], [], 'b-', linewidth=2)
points, = ax.plot([], [], 'ko', markersize=5)
ax.set_aspect('equal')
ax.grid(True)
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
graph = canvas.get_tk_widget()
graph.grid(columnspan=2)

robot_position = tk.Label(root, text="")
robot_position.grid(columnspan=2)

root.mainloop()
