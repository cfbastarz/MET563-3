from manim import *
import numpy as np

class BrachistochroneCurvesWithTimers(Scene):
    def construct(self):
        # Pontos A e B
        A = np.array([-5, 2, 0])
        B = np.array([5, -2, 0])

        # --- Curvas ---
        line_path = Line(A, B, color=BLUE)
        circle = ArcBetweenPoints(A, B, angle=-PI/3, color=GREEN)

        # Braquistócrona (cicloide)
        R = 2.0
        theta = np.linspace(0, np.pi, 100)
        x = R*(theta - np.sin(theta))
        y = -R*(1 - np.cos(theta))
        scale_x = (B[0]-A[0])/(x[-1]-x[0])
        scale_y = (B[1]-A[1])/(y[-1]-y[0])
        x = A[0] + (x - x[0]) * scale_x
        y = A[1] + (y - y[0]) * scale_y
        points = np.array([x, y, np.zeros_like(x)]).T
        cycloid_path = VMobject(color=RED)
        cycloid_path.set_points_smoothly(points)

        # Mostra as curvas
        self.add(line_path, circle, cycloid_path)

        # --- Pontos e labels ---
        dot_A = Dot(A, color=YELLOW)
        dot_B = Dot(B, color=YELLOW)
        label_A = MathTex("A").next_to(dot_A, UP)
        label_B = MathTex("B").next_to(dot_B, DOWN)
        self.add(dot_A, dot_B, label_A, label_B)

        # --- Bolinhas ---
        ball_line = Dot(A, color=BLUE)
        ball_circle = Dot(A, color=GREEN)
        ball_cycloid = Dot(A, color=RED)
        self.add(ball_line, ball_circle, ball_cycloid)

        # --- Trails (depois de adicionar as bolinhas) ---
        trail_line = TracedPath(ball_line.get_center, stroke_color=BLUE, stroke_width=4)
        trail_circle = TracedPath(ball_circle.get_center, stroke_color=GREEN, stroke_width=4)
        trail_cycloid = TracedPath(ball_cycloid.get_center, stroke_color=RED, stroke_width=4)
        self.add(trail_line, trail_circle, trail_cycloid)

        # --- Cronômetros com "s" de segundos ---
        def create_timer(color, pos):
            number = DecimalNumber(0, num_decimal_places=1, color=color).scale(0.7)
            unit = Tex("s", color=color).next_to(number, RIGHT, buff=0.1)
            timer_group = VGroup(number, unit).move_to(pos)
            return number, timer_group

        timer_line_num, timer_line = create_timer(BLUE, UP*3 + LEFT*3)
        timer_circle_num, timer_circle = create_timer(GREEN, UP*3)
        timer_cycloid_num, timer_cycloid = create_timer(RED, UP*3 + RIGHT*3)

        self.add(timer_line, timer_circle, timer_cycloid)

        # --- Tempos simulados ---
        t_line = 6
        t_circle = 4.5
        t_cycloid = 3.5

        # Atualizadores dos cronômetros
        timer_line_num.add_updater(lambda d: d.set_value(self.time if self.time <= t_line else t_line))
        timer_circle_num.add_updater(lambda d: d.set_value(self.time if self.time <= t_circle else t_circle))
        timer_cycloid_num.add_updater(lambda d: d.set_value(self.time if self.time <= t_cycloid else t_cycloid))

        # --- Movimentos simultâneos ---
        self.play(
            AnimationGroup(
                MoveAlongPath(ball_line, line_path, run_time=t_line, rate_func=linear),
                MoveAlongPath(ball_circle, circle, run_time=t_circle, rate_func=linear),
                MoveAlongPath(ball_cycloid, cycloid_path, run_time=t_cycloid, rate_func=linear),
                lag_ratio=0
            )
        )

        # Remove atualizadores após o movimento
        timer_line_num.clear_updaters()
        timer_circle_num.clear_updaters()
        timer_cycloid_num.clear_updaters()

        self.wait(1)
