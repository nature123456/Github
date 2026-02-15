from manim import *

korean_template = TexTemplate()
korean_template.add_to_preamble(r"\usepackage{kotex}")
class PolynomialExpansionFinal(Scene):
    def construct(self):
        # 1. 한글 폰트 설정
        Text.set_default(font="NanumGothic")
        
        # --- 레이아웃 설정 ---
        # 수식들을 담을 그룹
        eq_group = VGroup()
        
        # --- 2. 도형 및 라벨 설정 (오른쪽 상단으로 이동) ---
        a_s, b_s, c_s = 1.8, 1.1, 0.7  # 화면에 잘 담기도록 크기 미세 조정
        
        def get_labeled_rect(w, h, txt, col):
            rect = Rectangle(width=w, height=h, fill_opacity=0.5, color=col)
            label = MathTex(txt).scale(0.7).move_to(rect.get_center())
            return VGroup(rect, label)

        # 각 칸 생성
        r_a2 = get_labeled_rect(a_s, a_s, "a^2", PINK)
        r_ab1 = get_labeled_rect(b_s, a_s, "ab", PURPLE).next_to(r_a2, RIGHT, buff=0)
        r_ac1 = get_labeled_rect(c_s, a_s, "ac", GREEN_B).next_to(r_ab1, RIGHT, buff=0)
        
        r_ab2 = get_labeled_rect(a_s, b_s, "ab", PURPLE).next_to(r_a2, DOWN, buff=0)
        r_b2 = get_labeled_rect(b_s, b_s, "b^2", YELLOW_B).next_to(r_ab2, RIGHT, buff=0)
        r_bc1 = get_labeled_rect(c_s, b_s, "bc", BLUE_B).next_to(r_b2, RIGHT, buff=0)
        
        r_ac2 = get_labeled_rect(a_s, c_s, "ac", GREEN_B).next_to(r_ab2, DOWN, buff=0)
        r_bc2 = get_labeled_rect(b_s, c_s, "bc", BLUE_B).next_to(r_ac2, RIGHT, buff=0)
        r_c2 = get_labeled_rect(c_s, c_s, "c^2", ORANGE).next_to(r_bc2, RIGHT, buff=0)

        # 전체 도형 묶음
        whole_rect = VGroup(r_a2, r_ab1, r_ac1, r_ab2, r_b2, r_bc1, r_ac2, r_bc2, r_c2)
        
        # --- 3. 변의 길이 표시 (BraceLabel) ---
        top_guides = VGroup(
            BraceLabel(r_a2, "a", UP),
            BraceLabel(r_ab1, "b", UP),
            BraceLabel(r_ac1, "c", UP)
        )
        left_guides = VGroup(
            BraceLabel(r_a2, "a", LEFT),
            BraceLabel(r_ab2, "b", LEFT),
            BraceLabel(r_ac2, "c", LEFT)
        )
        guides = VGroup(top_guides, left_guides)
        
        # 도형과 가이드를 합쳐서 화면 우측 상단으로 이동
        illustration = VGroup(whole_rect, guides).to_edge(RIGHT, buff=0.8).shift(UP * 0.5)

        # --- 4. 애니메이션 실행 ---
        # 제목을 아주 높게 배치
        title = Tex(r"다항식 $(a+b+c)^2$ 전개 시각화", tex_template=korean_template,     color=BLUE_B).scale(0.6).to_edge(UP, buff=0.3)
        self.play(Write(title))

        steps = [
            r"(a + b + c)^2",
            r"= \{(a + b) + c\}^2",
            r"= (a + b)^2 + 2(a + b)c + c^2",
            r"= a^2 + 2ab + b^2 + 2ac + 2bc + c^2",
            r"= a^2 + b^2 + c^2 + 2ab + 2bc + 2ca"
        ]

        for i, s in enumerate(steps):
            new_eq = MathTex(s).scale(0.7)
            
            # 수식 시작점을 화면 왼쪽 상단 끝으로 배치
            if i == 0:
                new_eq.to_edge(LEFT, buff=0.8).to_edge(UP, buff=1.2)
            else:
                new_eq.next_to(eq_group[-1], DOWN, buff=0.4, aligned_edge=LEFT)
            
            # 스크롤 효과: 수식이 아래로 길어지면 전체를 위로 조금씩 이동
            if i >= 3:
                self.play(
                    VGroup(eq_group, title).animate.shift(UP * 0.7),
                    illustration.animate.shift(UP * 0.2), # 도형도 약간 보조를 맞춰 올라감
                    run_time=0.8
                )
                new_eq.next_to(eq_group[-1], DOWN, buff=0.4, aligned_edge=LEFT)

            self.play(Write(new_eq))
            eq_group.add(new_eq)
            
            # 도형 등장 시점 (첫 번째 변형 단계 이후)
            if i == 1:
                self.play(FadeIn(illustration, shift=LEFT))
            
            self.wait(0.5)

        # 최종 결과 강조
        final_rect = SurroundingRectangle(eq_group[-1], color=YELLOW, buff=0.1)
        self.play(Create(final_rect))
        self.play(Indicate(whole_rect))
        self.wait(2)