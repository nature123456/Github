from manim import *

# 한글 처리를 위한 템플릿 설정
korean_template = TexTemplate()
korean_template.add_to_preamble(r"\usepackage{kotex}")

class CubicExpansionScroll(Scene):
    def construct(self):
        # 1. 한글 폰트 설정
        Text.set_default(font="NanumGothic")
        
        # --- 레이아웃 설정 ---
        eq_group = VGroup() # 수식들을 담을 그룹
        
        # 2. 제목 설정 (고정)
        title = Tex(
            r"다항식 $(a+b)^3$ 전개 시각화", 
            tex_template=korean_template, 
            color=BLUE_B
        ).scale(0.8).to_edge(UP, buff=0.5)
        self.add(title) # 처음부터 고정

        # 3. 수식 단계 설정
        steps = [
            r"(a + b)^3",
            r"= (a + b)(a + b)^2",
            r"= (a + b)(a^2 + 2ab + b^2)",
            r"= a(a^2 + 2ab + b^2) + b(a^2 + 2ab + b^2)", # 전개 과정을 더 명확히 수정
            r"= a^3 + 2a^2b + ab^2 + a^2b + 2ab^2 + b^3",
            r"= a^3 + 3a^2b + 3ab^2 + b^3"
        ]

        # 4. 애니메이션 (밀려 올라가지 않음)
        for i, s in enumerate(steps):
            new_eq = MathTex(s).scale(0.65) # 크기를 약간 줄여 한 화면에 담기게 함
            
            if i == 0:
                # 첫 번째 수식 위치 (제목 아래)
                new_eq.next_to(title, DOWN, buff=0.6).align_to(title, LEFT).shift(LEFT * 0.5)
            else:
                # 이전 수식 바로 아래에 정렬
                new_eq.next_to(eq_group[-1], DOWN, buff=0.3, aligned_edge=LEFT)
            
            self.play(Write(new_eq))
            eq_group.add(new_eq)
            
            # 중간 단계 강조
            if i == 2:
                self.play(Indicate(new_eq[0][6:], color=YELLOW)) 
            
            self.wait(0.5)

        # 5. 최종 결과 강조
        final_rect = SurroundingRectangle(eq_group[-1], color=YELLOW, buff=0.1)
        self.play(Create(final_rect))
        
        conclusion = Tex(
            r"총 8개의 입체(1개 $a^3$, 3개 $a^2b$, 3개 $ab^2$, 1개 $b^3$)로 구성됨",
            tex_template=korean_template,
            color=GREEN_B
        ).scale(0.5).next_to(final_rect, DOWN, buff=0.5)
        
        self.play(FadeIn(conclusion))
        self.wait(2)