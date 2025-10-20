from manim import *
import numpy as np

class SixSequentialCycloids(Scene):
    def construct(self):
        # --- Parâmetros ---
        R = 0.5           # raio do círculo
        n_cycles = 8       # número total de cicloides
        t_total = 6       # duração total da animação
        circle_color = BLUE
        point_color = RED

        # --- Eixos X e Y centrados ---
        axes = Axes(
            x_range=[-1.25, 2*R*n_cycles + 1, R],
            y_range=[-1.5, 3*R, 0.5],
            x_length=16,
            y_length=4,
            axis_config={"include_numbers": False,
                         "include_ticks": False,
                         "color": WHITE},
                x_axis_config={"include_tip": False},  # remove seta do eixo x
                y_axis_config={"include_tip": False},  # remove seta do eixo y
        )
        self.add(axes)

        # --- Ajuste inicial para começar à esquerda ---
        start_x =  -1.5 * R * n_cycles  # deslocamento inicial à esquerda

        # --- Círculo ---
        circle = Circle(radius=R, color=circle_color)
        circle.move_to([start_x, R, 0])
        self.add(circle)

        # --- Ponto no centro ---
        center = Dot(circle.get_center(), color=WHITE)
        self.add(center)

        # --- Ponto na borda ---
        top = Dot(circle.get_top(), color=point_color)
        self.add(top)

        # --- Raio pontilhado ---
        radius_line = DashedLine(circle.get_center(), top.get_center(), dash_length=0.1, color=WHITE)
        self.add(radius_line)

        # --- Trail da cicloide ---
        trail = TracedPath(top.get_center, stroke_color=point_color, stroke_width=4)
        self.add(trail)

        # --- Updater para o círculo e pontos ---
        def updater(mob, dt):
            alpha = self.time / t_total * n_cycles * PI  # total de 6 arcos (π cada)

            # centro do círculo
            x_center = start_x + R * alpha
            y_center = R
            pos_center = np.array([x_center, y_center, 0])
            circle.move_to(pos_center)
            center.move_to(pos_center)

            # ponto na circunferência (cicloide para cima)
            x_point = x_center - R * np.sin(alpha)
            y_point = y_center - R * np.cos(alpha)  # invertido para cima
            top.move_to([x_point, y_point, 0])

            # atualizar raio pontilhado
            radius_line.put_start_and_end_on(pos_center, top.get_center())

        circle.add_updater(updater)

        # --- Ajuste da câmera ---
        total_width = abs(start_x) + R * n_cycles * 2 + 2
        #self.camera.frame_width = total_width  # CORRETO para v0.19
        self.camera.frame_width = 15

        self.wait(t_total)
