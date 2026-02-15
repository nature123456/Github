from manim import *

class PolynomialExpansion(Scene):
    def construct(self):
        # 1. 수식을 인덱스별로 분리하여 정의 (화살표 연결을 위해)
        # index:      0      1  2  3  4  5
        equation1 = MathTex("(", "x-2y", ")", "(", "3x", "+", "y", ")")
        equation1.scale(1.2)
        
        # 2. 전개 과정 단계별 수식
        step1 = MathTex("=", "(x - 2y)", "3x", "+", "(x - 2y)", "y")
        step2 = MathTex("=", "(3x^2 - 6xy)", "+", "(xy - 2y^2)")
        step3 = MathTex("=", "3x^2", "+ (-6xy + xy)", "- 2y^2")
        step4 = MathTex("=", "3x^2", "- 5xy", "- 2y^2")

        # 레이아웃 정리
        group = VGroup(equation1, step1, step2, step3, step4).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        group.move_to(ORIGIN)

        # --- 애니메이션 시작 ---
        self.play(Write(equation1))
        self.wait(0.5)

        # 3. 화살표 설정 (정확한 위치 지정)
        # 위로 볼록한 빨간색 화살표: (x-2y)에서 3x로
        arrow_top = CurvedArrow(
            start_point=equation1[1].get_top() + UP * 0.1, 
            end_point=equation1[4].get_top() + UP * 0.1, 
            angle=-TAU / 4, # 위로 볼록하게 (음수 값)
            color=RED_A
        )

        # 아래로 볼록한 파란색 화살표: (x-2y)에서 y로
        arrow_bottom = CurvedArrow(
            start_point=equation1[1].get_bottom() + DOWN * 0.1, 
            end_point=equation1[6].get_bottom() + DOWN * 0.1, 
            angle=TAU / 4,  # 아래로 볼록하게 (양수 값)
            color=BLUE_A
        )

        # 화살표 그리기
        self.play(Create(arrow_top))
        self.play(Create(arrow_bottom))
        self.wait(1)

        # 이후 전개 과정
        self.play(Write(step1))
        self.play(Write(step2))
        self.play(Write(step3))
        self.play(Write(step4))
        
        # 최종 결과 강조
        rect = SurroundingRectangle(step4, color=YELLOW, buff=0.1)
        self.play(Create(rect))
        self.wait(2)