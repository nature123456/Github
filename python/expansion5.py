from manim import *

# 1. 한글 처리를 위한 TexTemplate 설정
korean_template = TexTemplate()
korean_template.add_to_preamble(r"\usepackage{kotex}")

class PolynomialExpansionAligned(Scene):
    def construct(self):
        # 2. 제목 설정
        title = Tex(
            r"다항식 $(a+b+c)^2$ 전개 시각화", 
            tex_template=korean_template, 
            color=BLUE_B
        ).scale(0.8).to_edge(UP, buff=0.3)

        # --- 3. 도형 및 라벨 설정 ---
        a_s, b_s, c_s = 1.4, 0.9, 0.5
        widths, heights = [a_s, b_s, c_s], [a_s, b_s, c_s]
        colors = [PINK, PURPLE, GREEN_B, PURPLE, YELLOW_B, BLUE_B, GREEN_B, BLUE_B, ORANGE]
        texts = ["a^2", "ab", "ac", "ab", "b^2", "bc", "ac", "bc", "c^2"]

        rects = VGroup()
        inner_labels = VGroup()
        
        for i in range(3): 
            for j in range(3): 
                idx = i * 3 + j
                r = Rectangle(width=widths[j], height=heights[i], 
                              fill_opacity=0.5, color=colors[idx])
                lbl = MathTex(texts[idx]).scale(0.5)
                rects.add(r)
                inner_labels.add(lbl)

        rects.arrange_in_grid(rows=3, cols=3, buff=0)
        for i, lbl in enumerate(inner_labels):
            lbl.move_to(rects[i].get_center())

        # --- 4. 점선 보조선 및 변 길이(Brace) 설정 ---
        dimensions = VGroup()
        for j in range(3):
            target = rects[j]
            br = Brace(target, UP, buff=0.05)
            lab = br.get_tex(["a", "b", "c"][j]).scale(0.6)
            dimensions.add(br, lab)
            if j > 0: 
                dl = DashedLine(target.get_corner(UL)+UP*0.4, target.get_corner(DL)+DOWN*0.1, color=GRAY, stroke_width=2)
                dimensions.add(dl)

        for i in range(3):
            target = rects[i*3]
            br = Brace(target, LEFT, buff=0.05)
            lab = br.get_tex(["a", "b", "c"][i]).scale(0.6)
            dimensions.add(br, lab)
            if i > 0: 
                dl = DashedLine(target.get_corner(UL)+LEFT*0.4, target.get_corner(UR)+RIGHT*0.1, color=GRAY, stroke_width=2)
                dimensions.add(dl)

        # --- 5. 수식 설정 ---
        step1 = MathTex("(a+b+c)^2").scale(0.7).to_edge(LEFT, buff=0.8).to_edge(UP, buff=1.4)
        
        # [핵심] 도형 위치를 step1 높이에 맞춤
        illustration = VGroup(rects, inner_labels, dimensions).to_edge(RIGHT, buff=1.0)
        illustration.align_to(step1, UP) 

        description = Tex(
            r"$\leftarrow$ 오른쪽 정사각형의 넓이", 
            tex_template=korean_template, 
            color=YELLOW
        ).scale(0.55).next_to(step1, RIGHT, buff=0.3)

        step2 = MathTex("=", "a^2", "+ab", "+ac", "+ab", "+b^2", "+bc", "+ac", "+bc", "+c^2").scale(0.7)
        step2.next_to(step1, DOWN, aligned_edge=LEFT, buff=0.4)

        step3 = MathTex(
            "=", "a^2+b^2+c^2", "+", "ab+ab", "+", "bc+bc", "+", "ca+ca",
            tex_to_color_map={"ab+ab": PURPLE_A, "bc+bc": BLUE_A, "ca+ca": GREEN_A}
        ).scale(0.7).next_to(step2, DOWN, aligned_edge=LEFT, buff=0.4)

        step4 = MathTex("=", "a^2+b^2+c^2", "+2ab", "+2bc", "+2ca").scale(0.7)
        step4.next_to(step3, DOWN, aligned_edge=LEFT, buff=0.4)

        # --- 6. 애니메이션 실행 ---
        self.play(Write(title))
        self.play(Write(step1))
        self.play(FadeIn(description, shift=RIGHT * 0.2))
        
        self.play(FadeIn(rects), FadeIn(inner_labels), Create(dimensions))
        self.play(Indicate(illustration))
        self.wait(1)

        self.play(Write(step2[0]))
        for i in range(9):
            target_copy = inner_labels[i].copy()
            self.play(
                target_copy.animate.move_to(step2[i+1].get_center()).scale(1.2),
                run_time=0.15
            )
            self.add(step2[i+1])
            self.remove(target_copy)

        self.wait(0.5)
        collect_msg = Tex("동류항끼리 모으기", tex_template=korean_template, color=ORANGE).scale(0.5).next_to(step3, RIGHT, buff=0.5)
        self.play(Write(step3), Write(collect_msg))
        self.wait(1)
        self.play(Write(step4), FadeOut(collect_msg))
        self.play(Create(SurroundingRectangle(step4, color=YELLOW)))
        self.wait(2)