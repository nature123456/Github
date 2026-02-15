from manim import *
import numpy as np

class PolynomialExpansion(Scene):
    def construct(self):
        # 1. 상단 수식 설정 (VGroup을 사용하여 물리적으로 정렬)
        line1 = MathTex("(a+b)(x+y+z)", font_size=40)
        line2 = MathTex("=", "ax", "+", "ay", "+", "az", "+", "bx", "+", "by", "+", "bz", font_size=40)
        
        # 첫 번째 줄의 등호 가상 위치를 고려하여 두 번째 줄을 배치
        # line2[0]이 "=" 입니다. 이를 line1의 왼쪽 끝에 맞춰 정렬합니다.
        line2.next_to(line1, DOWN, buff=0.3)
        line2.align_to(line1, LEFT).shift(LEFT * 0.3) # 등호 정렬을 위해 살짝 조정
        
        equation = VGroup(line1, line2).to_edge(UP, buff=0.6)

        # 2. 사각형 레이아웃 설정 (기존과 동일)
        a_w, b_w = 3.5, 1.5
        x_h, y_h, z_h = 1.6, 1.1, 0.7
        rect_config = {"stroke_width": 2, "fill_opacity": 0.3}
        
        r_ax = Rectangle(width=a_w, height=x_h, color=PINK, **rect_config)
        r_ay = Rectangle(width=a_w, height=y_h, color=GREEN, **rect_config).next_to(r_ax, DOWN, buff=0)
        r_az = Rectangle(width=a_w, height=z_h, color=BLUE, **rect_config).next_to(r_ay, DOWN, buff=0)
        r_bx = Rectangle(width=b_w, height=x_h, color=YELLOW, **rect_config).next_to(r_ax, RIGHT, buff=0)
        r_by = Rectangle(width=b_w, height=y_h, color=ORANGE, **rect_config).next_to(r_bx, DOWN, buff=0)
        r_bz = Rectangle(width=b_w, height=z_h, color=PURPLE, **rect_config).next_to(r_by, DOWN, buff=0)

        grid = VGroup(r_ax, r_ay, r_az, r_bx, r_by, r_bz).center().shift(DOWN * 0.9)

        # 3. 사이드 라벨 및 내부 라벨 설정
        # 3. 밖으로 볼록한 점선 호 함수 수정
        def get_convex_dashed_label(mobject, direction, label_tex):
            # 변의 길이에 따라 적절한 곡률(radius)을 계산합니다.
            # 변의 길이(L)의 약 1.5배~2배 정도를 반지름으로 설정하면 일정한 곡률감을 줍니다.
            if np.array_equal(direction, UP):
                p1, p2 = mobject.get_corner(UL), mobject.get_corner(UR)
                side_length = np.linalg.norm(p2 - p1)
                arc_radius = -side_length * 1.2  # 길이에 비례한 곡률
            elif np.array_equal(direction, LEFT):
                p1, p2 = mobject.get_corner(DL), mobject.get_corner(UL)
                side_length = np.linalg.norm(p2 - p1)
                arc_radius = -side_length * 1.2  # 길이에 비례한 곡률
            else: 
                return VGroup()

            # 아크 생성
            arc = ArcBetweenPoints(p1, p2, radius=arc_radius)
            
            # 모든 면에서 동일한 간격을 유지하기 위한 설정
            dashed_arc = DashedVMobject(arc, num_dashes=15, dashed_ratio=0.5)
            
            # buff 값을 0.2로 통일하여 라벨이 떨어진 정도를 맞춤
            label = MathTex(label_tex, font_size=32).next_to(dashed_arc, direction, buff=0.2)
            
            return VGroup(dashed_arc, label)

        # 라벨 생성 (기존과 동일하지만 내부 함수가 개선됨)
        side_labels = VGroup(
            get_convex_dashed_label(r_ax, UP, "a"),
            get_convex_dashed_label(r_bx, UP, "b"),
            get_convex_dashed_label(r_ax, LEFT, "x"),
            get_convex_dashed_label(r_ay, LEFT, "y"),
            get_convex_dashed_label(r_az, LEFT, "z"),
        )

        # 애니메이션에 쓰일 타겟 항들 (line2의 ax, ay, az, bx, by, bz)
        # line2 인덱스: 0:"=", 1:"ax", 2:"+", 3:"ay", 4:"+", 5:"az", 6:"+", 7:"bx", 8:"+", 9:"by", 10:"+", 11:"bz"
        rhs_targets = [line2[i] for i in [1, 3, 5, 7, 9, 11]]
        plus_signs = [line2[i] for i in [2, 4, 6, 8, 10]]
        
        inner_labels = VGroup(
            MathTex("ax").move_to(r_ax), MathTex("ay").move_to(r_ay),
            MathTex("az").move_to(r_az), MathTex("bx").move_to(r_bx),
            MathTex("by").move_to(r_by), MathTex("bz").move_to(r_bz),
        )

        # --- 애니메이션 시퀀스 ---
        self.play(Write(line1)) 
        self.play(Create(grid), Create(side_labels), run_time=1.5)
        self.wait(0.5)

        # 등호 등장
        self.play(Write(line2[0])) 

        for i, (label, target) in enumerate(zip(inner_labels, rhs_targets)):
            self.play(FadeIn(label, scale=1.2), run_time=0.3)
            
            # '+' 기호 애니메이션
            if i > 0:
                self.play(Write(plus_signs[i-1]), run_time=0.1)
            
            self.play(
                TransformFromCopy(label, target),
                label.animate.set_opacity(0.3).scale(0.8),
                run_time=0.8,
                path_arc=-0.3
            )

        self.play(equation.animate.set_color(YELLOW))
        self.wait(2)