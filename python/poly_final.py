from manim import *

class PolynomialAnimation(Scene):
    def construct(self):
        # 1. 타이틀과 정의
        title = Text("다항식의 계산", font_size=36).to_edge(UP)
        poly_a = MathTex("A = x^2 - 3xy + 5y^2")
        poly_b = MathTex("B = 2x^2 + xy - y^2")
        defs = VGroup(poly_a, poly_b).arrange(RIGHT, buff=1).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Write(defs))
        self.wait(1)

        # 애니메이션 진행을 위해 전체 내용을 담을 메인 컨테이너
        all_contents = VGroup(title, defs)

        # --- (1) 덧셈 과정 (가로셈 -> 세로셈) ---
        add_title = MathTex("(1) A + B", color=BLUE).scale(0.8).to_edge(LEFT).shift(UP*0.5)
        
        # 세로셈 구성
        v_a_plus = MathTex("x^2", "- 3xy", "+ 5y^2")
        v_b_plus = MathTex("2x^2", "+ xy", "- y^2")
        v_calc_plus = VGroup(v_a_plus, v_b_plus).arrange(DOWN, aligned_edge=RIGHT, buff=0.3)
        
        plus_sign = MathTex("+", color=BLUE).next_to(v_b_plus, LEFT, buff=0.5)
        line_plus = Line(LEFT, RIGHT).set_width(4).next_to(v_b_plus, DOWN, buff=0.1)
        res_plus = MathTex("3x^2", "- 2xy", "+ 4y^2", color=YELLOW).next_to(line_plus, DOWN, buff=0.1).align_to(v_b_plus, RIGHT)
        
        add_section = VGroup(add_title, v_a_plus, v_b_plus, plus_sign, line_plus, res_plus).next_to(defs, DOWN, buff=0.5)

        self.play(FadeIn(add_title))
        self.play(Write(v_a_plus), Write(v_b_plus))
        self.play(Write(plus_sign), Create(line_plus))
        self.play(Write(res_plus))
        self.wait(1)

        # --- (2) 화면 위로 밀어올리기 (자연스러운 연출) ---
        # 현재 화면에 있는 모든 것을 그룹화하여 위로 이동
        current_screen = VGroup(title, defs, add_section)
        self.play(current_screen.animate.shift(UP * 3.5), run_time=1.5)
        self.wait(0.5)

        # --- (3) 뺄셈 과정 (세로셈) ---
        sub_title = MathTex("(2) A - B", color=RED).scale(0.8).to_edge(LEFT).shift(DOWN*0.5)
        
        v_a_sub = MathTex("x^2", "- 3xy", "+ 5y^2")
        v_b_sub = MathTex("2x^2", "+ xy", "- y^2")
        v_calc_sub = VGroup(v_a_sub, v_b_sub).arrange(DOWN, aligned_edge=RIGHT, buff=0.3)
        
        minus_sign = MathTex("-", color=RED).next_to(v_b_sub, LEFT, buff=0.5)
        line_sub = Line(LEFT, RIGHT).set_width(4).next_to(v_b_sub, DOWN, buff=0.1)
        
        # 뺄셈의 경우 부호 변화를 강조하기 위해 결과값 애니메이션
        res_sub = MathTex("-x^2", "- 4xy", "+ 6y^2", color=YELLOW).next_to(line_sub, DOWN, buff=0.1).align_to(v_b_sub, RIGHT)

        sub_section = VGroup(sub_title, v_a_sub, v_b_sub, minus_sign, line_sub, res_sub).next_to(add_section, DOWN, buff=1.0)

        self.play(FadeIn(sub_title))
        self.play(Write(v_a_sub), Write(v_b_sub))
        self.play(Write(minus_sign), Create(line_sub))
        self.play(
            res_sub.animate.set_color(YELLOW),
            Write(res_sub),
            run_time=2
        )
        self.wait(2)