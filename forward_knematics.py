import math
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def forward_calculate(arms, angles):
    x = 0
    y = 0
    angle_sum = 0
    points_x = [x]
    points_y = [y]

    for i in range(len(arms)):
        angle_sum += math.radians(angles[i])
        x += arms[i] * math.cos(angle_sum)
        y += arms[i] * math.sin(angle_sum)
        points_x.append(x)
        points_y.append(y)

    return points_x, points_y

def plot_2d_robot(points_x, points_y):
    lines.set_data(points_x, points_y)
    points.set_data(points_x, points_y)
    canvas.draw()

def atualizar_valores(_):
    arm_1 = arm_1_scale.get()
    angle_1 = angle_1_scale.get()
    arm_2 = arm_2_scale.get()
    angle_2 = angle_2_scale.get()
    arm_3 = arm_3_scale.get()
    angle_3 = angle_3_scale.get()

    arms = [arm_1, arm_2, arm_3]
    angles = [angle_1, angle_2, angle_3]

    points_x, points_y = forward_calculate(arms, angles)
    print(points_x, points_y)
    plot_2d_robot(points_x, points_y)
    robot_position.config(text=f"Posição do robo: {points_x[-1]:.2f}, {points_y[-1]:.2f}")

def create_2d_graph():
    return fig

root = tk.Tk()
root.title("Cinemática direta")

tk.Label(root, text="Tamanho dos braços").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Ângulos").grid(row=0, column=1, sticky="w")

arm_1_scale = tk.Scale(root, from_=0, to=10, resolution=0.1, length=300, orient="horizontal", command=atualizar_valores)
arm_1_scale.set(5)
arm_1_scale.grid(row=1, column=0, padx=5, pady=5, sticky="w")

angle_1_scale = tk.Scale(root, from_=-180, to=180, resolution=0.1, length=300, orient="horizontal", command=atualizar_valores)
angle_1_scale.set(10)
angle_1_scale.grid(row=1, column=1, padx=5, pady=5, sticky="w")

arm_2_scale = tk.Scale(root, from_=0, to=10, resolution=0.1, length=300, orient="horizontal", command=atualizar_valores)
arm_2_scale.set(5)
arm_2_scale.grid(row=2, column=0, padx=5, pady=5, sticky="w")

angle_2_scale = tk.Scale(root, from_=-180, to=180, resolution=0.1, length=300, orient="horizontal", command=atualizar_valores)
angle_2_scale.set(10)
angle_2_scale.grid(row=2, column=1, padx=5, pady=5, sticky="w")

arm_3_scale = tk.Scale(root, from_=0, to=10, resolution=0.1, length=300, orient="horizontal", command=atualizar_valores)
arm_3_scale.set(5)
arm_3_scale.grid(row=3, column=0, padx=5, pady=5, sticky="w")

angle_3_scale = tk.Scale(root, from_=-180, to=180, resolution=0.1, length=300, orient="horizontal", command=atualizar_valores)
angle_3_scale.set(10)
angle_3_scale.grid(row=3, column=1, padx=5, pady=5, sticky="w")


fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
lines, = ax.plot([], [], 'b-', linewidth=2)
points, = ax.plot([], [], 'ko', markersize=5)
ax.set_aspect('equal')
ax.grid(True)
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
graph = canvas.get_tk_widget()
graph.grid(columnspan=2)

robot_position = tk.Label(root, text="")
robot_position.grid(columnspan=2)

# Botão para atualizar os valores dos sliders
# btn_atualizar = ttk.Button(root, text="Atualizar", command=atualizar_valores)
# # btn_atualizar.pack()

ax = create_2d_graph()
root.mainloop()
