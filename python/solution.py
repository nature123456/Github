from manim import *

class PolynomialSolver(Scene):
    def construct(self):
        # 1. 전체 레이아웃의 기준이 되는 Title 설정
        # buff=0.3으로 설정하여 왼쪽 끝에서 아주 가깝게 시작합니다.
        title = Text("다항식 X 구하기", font_size=35).to_edge(UP).to_edge(LEFT, buff=0.3)
        
        given_a = MathTex("A = 3x^2 - 6xy + 3y^2", color=BLUE, font_size=34)
        given_b = MathTex("B = xy + 2y^2", color=GREEN, font_size=34)
        
        # 고정 요소들을 그룹화하고 title의 왼쪽 끝에 맞춥니다.
        given_group = VGroup(given_a, given_b).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        given_group.next_to(title, DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(given_group))
        self.wait(1)

        # --- 문제 (1) 풀이 ---
        # 모든 요소를 aligned_edge=LEFT로 설정하여 시작점을 통일합니다.
        prob1_label = MathTex(r"(1) \ A - X = B", font_size=34, color=YELLOW).next_to(given_group, DOWN, aligned_edge=LEFT, buff=0.8)
        
        step1_1 = MathTex("X = A - B", font_size=34).next_to(prob1_label, DOWN, aligned_edge=LEFT)
        step1_2 = MathTex(
            "X = (3x^2 - 6xy + 3y^2) - (xy + 2y^2)",
            font_size=32
        ).next_to(step1_1, DOWN, aligned_edge=LEFT)
        
        step1_ans = MathTex(
            "X = 3x^2 - 7xy + y^2",
            color=YELLOW, font_size=36
        ).next_to(step1_2, DOWN, aligned_edge=LEFT)

        self.play(Write(prob1_label))
        self.play(Write(step1_1))
        self.play(Write(step1_2))
        self.wait(1)
        self.play(TransformMatchingShapes(step1_2.copy(), step1_ans))
        self.wait(2)

        # 1번 풀이 내용만 페이드 아웃
        self.play(
            FadeOut(prob1_label), 
            FadeOut(step1_1), 
            FadeOut(step1_2), 
            FadeOut(step1_ans)
        )

        # --- 문제 (2) 풀이 ---
        prob2_label = MathTex(r"(2) \ 2(X - A) = 3B - X", font_size=34, color=YELLOW).next_to(given_group, DOWN, aligned_edge=LEFT, buff=0.8)
        
        steps2 = VGroup(
            MathTex("2X - 2A = 3B - X", font_size=34),
            MathTex("3X = 2A + 3B", font_size=34),
            MathTex(r"X = \frac{2A + 3B}{3}", font_size=34)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(prob2_label, DOWN, aligned_edge=LEFT)

        self.play(Write(prob2_label))
        for step in steps2:
            self.play(Write(step))
        
        # --- 보조 계산 (메인 풀이 오른쪽에 배치) ---
        calc_vgroup = VGroup(
            MathTex("2A = 6x^2 - 12xy + 6y^2", font_size=28),
            MathTex("3B = 3xy + 6y^2", font_size=28),
            Line(LEFT, RIGHT, color=GRAY).set_width(3.5), 
            MathTex("2A + 3B = 6x^2 - 9xy + 12y^2", font_size=28, color=BLUE_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # 전체가 왼쪽으로 쏠렸으므로 보조 계산 위치를 적절히 조정
        calc_vgroup.next_to(steps2, RIGHT, buff=1.0).shift(UP * 0.4)
        
        self.play(FadeIn(calc_vgroup, shift=LEFT))
        
        step2_ans = MathTex(
            "X = 2x^2 - 3xy + 4y^2",
            color=YELLOW, font_size=36
        ).next_to(steps2, DOWN, aligned_edge=LEFT, buff=0.6)

        self.play(Write(step2_ans))
        self.wait(3)