from manim import *

class PolynomialCalculation(Scene):
    def construct(self):
        # 1. 문제 설정 (Polynomial definitions)
        title = Text("다항식의 계산", font_size=40).to_edge(UP)
        poly_a = MathTex("A = x^2 - 3xy + 5y^2")
        poly_b = MathTex("B = 2x^2 + xy - y^2")
        
        defs = VGroup(poly_a, poly_b).arrange(RIGHT, buff=1).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(defs))
        self.wait(1)

        # --- (1) A + B 계산 과정 ---
        ques_1 = MathTex("(1) A + B", color=BLUE).to_edge(LEFT).shift(UP*0.5)
        step1_1 = MathTex("= (x^2 - 3xy + 5y^2) + (2x^2 + xy - y^2)")
        step1_2 = MathTex("= (1+2)x^2 + (-3+1)xy + (5-1)y^2")
        step1_3 = MathTex("= 3x^2 - 2xy + 4y^2", color=YELLOW)
        
        calc_1 = VGroup(step1_1, step1_2, step1_3).arrange(DOWN, aligned_edge=LEFT).next_to(ques_1, DOWN, aligned_edge=LEFT)

        self.play(Write(ques_1))
        self.play(TransformMatchingShapes(defs.copy(), step1_1))
        self.wait(0.5)
        self.play(Write(step1_2))
        self.wait(0.5)
        self.play(Write(step1_3))
        self.wait(2)

        # 화면 정리를 위해 (1)번 풀이 페이드 아웃
        self.play(FadeOut(ques_1), FadeOut(calc_1))

        # --- (2) A - B 계산 과정 ---
        ques_2 = MathTex("(2) A - B", color=RED).to_edge(LEFT).shift(UP*0.5)
        step2_1 = MathTex("= (x^2 - 3xy + 5y^2) - (2x^2 + xy - y^2)")
        step2_2 = MathTex("= (x^2 - 3xy + 5y^2) + (-2x^2 - xy + y^2)")
        step2_3 = MathTex("= (1-2)x^2 + (-3-1)xy + (5+1)y^2")
        step2_4 = MathTex("= -x^2 - 4xy + 6y^2", color=YELLOW)
        
        calc_2 = VGroup(step2_1, step2_2, step2_3, step2_4).arrange(DOWN, aligned_edge=LEFT).next_to(ques_2, DOWN, aligned_edge=LEFT)

        self.play(Write(ques_2))
        self.play(TransformMatchingShapes(defs.copy(), step2_1))
        self.wait(0.5)
        self.play(Write(step2_2)) # 부호 반전 강조
        self.wait(0.5)
        self.play(Write(step2_3))
        self.wait(0.5)
        self.play(Write(step2_4))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(defs), FadeOut(ques_2), FadeOut(calc_2))