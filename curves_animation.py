from manim import *
import numpy as np

# 가로형 해상도 설정 (1920 x 1080)
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 8.0 # Y축 스케일
config.frame_width = 14.22 # X축 스케일 (16:9 비율)

class PolarAndCartesianCurves(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a1a"

        # 1. 제목 설정
        # 운영체제에 맞는 한글 폰트를 사용하세요 (예: "Malgun Gothic", "AppleGothic")
        title = Text("Polar vs Cartesian Curves", weight=BOLD, font_size=40, font="Malgun Gothic", color=BLUE_A)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # 2. 극좌표계 (Polar Coordinates) 설정
        polar_axes = PolarPlane(
    radius_max=3,
    size=6,
    azimuth_units="PI radians", # 각도 단위를 PI 라디안으로 설정
    azimuth_step=PI/4,          # 45도(PI/4) 간격으로 눈금 표시
    background_line_style={
        "stroke_color": BLUE_D,
        "stroke_width": 1,
        "stroke_opacity": 0.5
    }
)
        polar_axes.next_to(ORIGIN, LEFT, buff=1.5) # 좌측에 배치
        
        polar_label = Text("Polar Curve: r = 3cos(3θ)", font_size=24, color=YELLOW).next_to(polar_axes, UP)

        self.play(Create(polar_axes), Write(polar_label))
        self.wait(1)

        # 2-1. 장미 곡선(Rose Curve) 애니메이션 (r = a * cos(n * theta))
        # r = 3 * cos(3 * theta) -> 3개의 꽃잎
        a = 3
        n = 3

        def polar_func(theta):
            r = a * np.cos(n * theta)
            # 극좌표 (r, theta)를 직교좌표 (x, y)로 변환
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            return polar_axes.coords_to_point(x, y) # 극좌표계의 점으로 매핑

        # ParametricFunction을 사용하여 곡선 생성
        rose_curve = ParametricFunction(
            polar_func,
            t_range=[0, 2 * PI, 0.01], # 0에서 2파이까지
            color=YELLOW_B,
            stroke_width=3
        )

        # 곡선 그리기 애니메이션
        self.play(Create(rose_curve, run_time=3, rate_func=linear))
        self.wait(2)
        
        # 3. 직교좌표계 (Cartesian Coordinates) 설정
        cartesian_axes = Axes(
            x_range=[-PI, PI, PI/2], # X축 범위
            y_range=[-1.5, 1.5, 0.5], # Y축 범위
            x_length=6, # X축 길이
            y_length=4, # Y축 길이
            axis_config={"color": GRAY_A},
            x_axis_config={"numbers_to_include": [-PI, -PI/2, 0, PI/2, PI], "font_size": 20},
            y_axis_config={"numbers_to_include": [-1, 0, 1], "font_size": 20}
        )
        cartesian_axes.next_to(ORIGIN, RIGHT, buff=1.5) # 우측에 배치

        # x축, y축 라벨 추가
        x_label = cartesian_axes.get_x_axis_label("x", edge=DOWN, direction=DOWN)
        y_label = cartesian_axes.get_y_axis_label("y", edge=LEFT, direction=LEFT)

        cartesian_label = Text("Cartesian Curve: y = sin(x)", font_size=24, color=RED).next_to(cartesian_axes, UP)

        self.play(Create(cartesian_axes), Write(cartesian_label), Write(x_label), Write(y_label))
        self.wait(1)

        # 3-1. 사인 곡선(Sine Curve) 애니메이션 (y = sin(x))
        def cartesian_func(x):
            return cartesian_axes.coords_to_point(x, np.sin(x))

        sine_curve = ParametricFunction(
            cartesian_func,
            t_range=[-PI, PI, 0.01],
            color=RED_B,
            stroke_width=3
        )

        # 곡선 그리기 애니메이션
        self.play(Create(sine_curve, run_time=3, rate_func=linear))
        self.wait(2)

        # 4. 마무리
        # 두 곡선을 동시에 강조하며 정리
        self.play(
            FadeOut(title),
            rose_curve.animate.set_stroke(width=5).set_color(YELLOW).scale(1.1),
            sine_curve.animate.set_stroke(width=5).set_color(RED).scale(1.1),
            run_time=1.5
        )
        self.wait(1)

        # 모든 요소 페이드 아웃
        self.play(
            FadeOut(polar_axes), FadeOut(polar_label), FadeOut(rose_curve),
            FadeOut(cartesian_axes), FadeOut(cartesian_label), FadeOut(sine_curve),
            FadeOut(x_label), FadeOut(y_label)
        )
        self.wait(1)