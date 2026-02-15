from manim import *

class PolynomialSubstitution(Scene):
    def construct(self):
        # 1. 초기 설정 및 정의
        kw = {"font": "NanumGothic"}
        p_str = "-2x^2 + 2x - 5"
        q_str = "3x^2 - x"
        r_str = "-x^2 - x + 5"

        # 상단 정의 (아주 작게 최상단 배치)
        defs = MathTex(
            f"P = {p_str}, \\quad Q = {q_str}, \\quad R = {r_str}",
            font_size=36
        ).to_edge(UP, buff=0.2).set_color(GRAY)
        self.add(defs)

        # 2. 전개 과정 (변수 상태) - 위치를 전체적으로 위로 올림
        origin_expr = MathTex(r"3P - [2\{Q - (2R - P)\} - 3(Q - R)]", color=YELLOW, font_size=32)
        origin_expr.to_edge(UP, buff=1.0).shift(LEFT * 2) # 왼쪽 정렬을 위해 shift
        
        self.play(Write(origin_expr))
        
        step_texts = [
            r"= 3P - [2\{Q - 2R + P\} - 3Q + 3R]",
            r"= 3P - [2Q - 4R + 2P - 3Q + 3R]",
            r"= 3P - [-Q - R + 2P]",
            r"= 3P + Q + R - 2P"
        ]
        
        all_steps = VGroup(origin_expr)
        for text in step_texts:
            step = MathTex(text, font_size=30).next_to(all_steps[-1], DOWN, aligned_edge=LEFT)
            self.play(Write(step), run_time=0.3)
            all_steps.add(step)

        # 3. 정리된 최종 변수 식 (=P+Q+R)
        final_var = MathTex("=", "P", "+", "Q", "+", "R", color=GREEN, font_size=38)
        final_var.next_to(all_steps[-1], DOWN, aligned_edge=LEFT)
        self.play(Write(final_var))
        self.wait(0.5)

        # 4. 실제 수식 대입 준비 (겹침 방지를 위해 미리 그룹화 및 정렬)
        p_poly = MathTex(f"({p_str})", color=BLUE, font_size=30)
        q_poly = MathTex(f"({q_str})", color=TEAL, font_size=30)
        r_poly = MathTex(f"({r_str})", color=ORANGE, font_size=30)

        # '=' 와 '+' 기호들을 복사하여 새 행 구성
        substituted_row = VGroup(
            MathTex("=", font_size=30),
            p_poly,
            MathTex("+", font_size=30),
            q_poly,
            MathTex("+", font_size=30),
            r_poly
        ).arrange(RIGHT, buff=0.12).scale(0.9)

        # 위치 설정: final_var 바로 아래에 배치
        substituted_row.next_to(final_var, DOWN, buff=0.5).align_to(final_var, LEFT)

        # 5. 애니메이션: final_var는 그대로 두고, 그 아래에 대입된 수식이 나타남
        # (변수에서 수식이 날아와 꽂히는 연출)
        self.play(
            ReplacementTransform(final_var[1].copy(), p_poly),
            ReplacementTransform(final_var[3].copy(), q_poly),
            ReplacementTransform(final_var[5].copy(), r_poly),
            Write(substituted_row[0]), # '='
            Write(substituted_row[2]), # '+'
            Write(substituted_row[4]), # '+'
            run_time=1.5
        )
        self.wait(1)

        # 6. 동류항 정리 과정 (유지)
        calc_step = MathTex(
            r"= (-2+3-1)x^2 + (2-1-1)x + (-5+5)",
            font_size=30, color=GRAY_B
        ).next_to(substituted_row, DOWN, buff=0.5).align_to(substituted_row, LEFT)

        self.play(Write(calc_step))
        self.wait(1)

        # 7. 최종 결과 = 0
        final_zero = MathTex("= 0", color=YELLOW, font_size=60).next_to(calc_step, DOWN, buff=0.4).align_to(calc_step, LEFT)
        rect = SurroundingRectangle(final_zero, color=YELLOW, buff=0.1)

        self.play(Write(final_zero))
        self.play(Create(rect))
        self.play(Indicate(final_zero))
        self.wait(3)
	
	
	# 실행: manim -pqh expansion55.py 