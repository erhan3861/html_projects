from ursina import *
import math

app = Ursina()

def create_ring(radius=2, thickness=0.05, resolution=64):
    verts = []
    tris = []

    for i in range(resolution):
        angle = math.radians(i * 360 / resolution)
        next_angle = math.radians((i+1) * 360 / resolution)

        # Dış kenar noktaları
        x1, y1 = math.cos(angle)*radius, math.sin(angle)*radius
        x2, y2 = math.cos(next_angle)*radius, math.sin(next_angle)*radius

        # İç kenar noktaları
        x3, y3 = math.cos(angle)*(radius-thickness), math.sin(angle)*(radius-thickness)
        x4, y4 = math.cos(next_angle)*(radius-thickness), math.sin(next_angle)*(radius-thickness)

        base_index = len(verts)
        verts += [(x1, 0, y1), (x2, 0, y2), (x4, 0, y4), (x3, 0, y3)]
        tris += [
            (base_index, base_index+1, base_index+2),
            (base_index, base_index+2, base_index+3)
        ]

    return Mesh(vertices=verts, triangles=tris, mode='triangle')

# Bomba objesi
bomba = Entity(model='sphere', color=color.red, scale=1)

# # İçi boş çember (halkalı)
# halo = Entity(
#     model=create_ring(radius=4, thickness=0.1),
#     color=color.rgba(255, 255, 0, 150),
#     rotation_x=90,
#     position=bomba.position
# )

# range_circle = Entity(parent=bomba, model=Circle(64, mode='line', radius=3, thickness=4), color=color.red, rotation_x=90)
range_circle = Entity(parent=bomba, model=Circle(14, mode='line', radius=3, thickness=4), color=color.red, rotation_x=90)

camera.z = -15
EditorCamera()
app.run() 