from manim import *

class PolynomialExpansionAligned(Scene):
    def construct(self):
        # 1. 수식 정의 (상단 배치)
        eq1 = MathTex("(x - 2y)", "(3x + y)").to_edge(UP, buff=0.7)
        red_rect = SurroundingRectangle(eq1[0], color=RED, buff=0.1)
        
        self.play(Write(eq1), Create(red_rect))

        # 2. 연결선 (겹치지 않게 더 넓게 그림)
        arc_top = CurvedArrow(
            eq1[0].get_top() + UP*0.2, 
            eq1[1][1:3].get_top() + UP*0.2, 
            color=PINK, angle=-TAU/3
        )
        arc_bottom = CurvedArrow(
            eq1[0].get_bottom() + DOWN*0.2, 
            eq1[1][4].get_bottom() + DOWN*0.2, 
            color=BLUE, angle=TAU/3
        )
        
        self.play(Create(arc_top), Create(arc_bottom))
        self.wait(1)

        # 3. 전개 과정 수식들 (기준점 설정을 위해 리스트로 관리)
        # 각 줄의 시작에 '='를 포함하여 작성
        eq2 = MathTex("=", "(x - 2y)3x", "+", "(x - 2y)y")
        eq3 = MathTex("=", "(3x^2 - 6xy)", "+", "(xy - 2y^2)")
        eq4 = MathTex("=", "3x^2", "+", "(-6xy + xy)", "-", "2y^2")
        final_eq = MathTex("=", "3x^2", "-", "5xy", "-", "2y^2")

        # 4. 수식 정렬 로직
        # eq2를 eq1의 왼쪽 끝 위치에 맞추어 아래에 배치
        eq2.next_to(eq1, DOWN, buff=0.8).align_to(eq1, LEFT)
        
        # 나머지는 eq2의 왼쪽 끝(LEFT)에 맞춰서 순차적으로 아래에 배치
        eq3.next_to(eq2, DOWN, buff=0.5).align_to(eq2, LEFT)
        eq4.next_to(eq3, DOWN, buff=0.5).align_to(eq3, LEFT)
        final_eq.next_to(eq4, DOWN, buff=0.5).align_to(eq4, LEFT)

        # 결과 박스
        yellow_rect = SurroundingRectangle(final_eq, color=YELLOW, buff=0.2)

        # 5. 애니메이션 실행
        self.play(FadeOut(arc_top), FadeOut(arc_bottom), FadeOut(red_rect))
        
        self.play(Write(eq2))
        self.play(Write(eq3))
        self.play(Write(eq4))
        self.play(Write(final_eq))
        self.play(Create(yellow_rect))
        self.wait(2)