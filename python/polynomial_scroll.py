from manim import *

class PolynomialFinalAnimation(Scene):
    def construct(self):
        # 1. 기초 설정
        font_name = "NanumGothic"
        
        title = Text("다항식의 혼합 계산 풀이", font_size=32, font=font_name).to_edge(UP)
        problem_def = MathTex("A = 3x^2 - 2x + 5, \ B = x^2 + 3x + 6").scale(0.7)
        target_expr = MathTex("3A - 2(A + B)", color=BLUE).scale(0.9)
        
        header = VGroup(title, problem_def, target_expr).arrange(DOWN, buff=0.25).to_edge(UP)
        self.add(header)

        # 2. 풀이 데이터
        # (수식, 설명_텍스트, 설명_수식)
        steps_data = [
            ("3A - 2A - 2B = A - 2B", "▶ 식 정리:", "3A-2(A+B)"),
            ("(3x^2 - 2x + 5) - 2(x^2 + 3x + 6)", "▶ 대입:", "A-2B"),
            ("3x^2 - 2x + 5 - 2x^2 - 6x - 12", "▶ 괄호 전개", ""),
            ("3x^2 - 2x^2 - 2x - 6x + 5 - 12", "▶ 내림차순 정렬", ""),
            ("(3-2)x^2 + (-2-6)x + (5-12)", "▶ 동류항 결합", ""),
            ("x^2 - 8x - 7", "▶ 최종 결과", "")
        ]

        # 모든 요소를 담을 그룹 (스크롤용)
        moving_mobjects = VGroup(header)
        
        # 위치 설정
        last_y = target_expr.get_bottom()[1] - 0.6
        vertical_buff = 0.7 

        for i, (eq_t, d_label, d_math) in enumerate(steps_data):
            # [좌측 수식]
            eq = MathTex("=" + eq_t if i > 1 else eq_t).scale(0.75)
            if i == len(steps_data) - 1: 
                eq.set_color(YELLOW)
            eq.move_to([-4.8, last_y, 0], aligned_edge=LEFT)

            # [우측 설명] t2c를 사용하여 '▶' 기호만 노란색으로 설정
            desc_text = Text(
                d_label, 
                font=font_name, 
                font_size=20, 
                t2c={"▶": YELLOW}, # 특정 문자 색상 지정
                color=GRAY_B       # 기본 나머지 글자 색상
            )
            
            if d_math:
                dm = MathTex(d_math).scale(0.5).set_color(GRAY_B)
                desc_group = VGroup(desc_text, dm).arrange(RIGHT, buff=0.1)
            else:
                desc_group = desc_text
            
            desc_group.move_to([1.2, last_y, 0], aligned_edge=LEFT)

            step_group = VGroup(eq, desc_group)

            # 스크롤 연출
            if last_y < -3.0:
                self.play(moving_mobjects.animate.shift(UP * 1.2), run_time=0.7)
                last_y += 1.2

            self.play(
                Write(eq),
                FadeIn(desc_group, shift=RIGHT * 0.2),
                run_time=0.8
            )

            moving_mobjects.add(step_group)
            last_y -= vertical_buff 
            self.wait(0.3)

        self.wait(2)