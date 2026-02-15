from manim import *

class PolynomialSmartScroll(Scene):
    def construct(self):
        # 1. 설정
        font_name = "NanumGothic"
        line_spacing = 0.85
        max_lines_before_scroll = 5  # 몇 번째 줄부터 위로 밀어올릴지 결정
        
        expressions = [
            r"\text{(a+b)}^3 \text{의 전개}", # 제목 (Text 대신 MathTex 내 한글 에러 방지를 위해 분리 권장하나 여기선 전체 흐름 중시)
            r"(a+b)^3",
            r"= (a+b)(a+b)^2",
            r"= (a+b)(a^2+2ab+b^2)",
            r"= a(a^2+2ab+b^2)+b(a^2+2ab+b^2)",
            r"= a^3+2a^2b+ab^2+a^2b+2ab^2+b^3",
            r"= a^3+(2a^2b+a^2b)+(ab^2+2ab^2)+b^3",
            r"= a^3+3a^2b+3ab^2+b^3"
        ]

        all_elements = VGroup()
        
        # 시작 위치 (화면 상단부 왼쪽)
        start_point = LEFT * 3 + UP * 2.5

        for i, expr_text in enumerate(expressions):
            # 한글 에러 방지를 위해 제목은 Text, 나머지는 MathTex로 처리하여 그룹화
            if i == 0:
                new_line = Text("(a+b)³의 전개", font=font_name, font_size=36, color=YELLOW)
                new_line.move_to(start_point, aligned_edge=LEFT)
            else:
                new_line = MathTex(expr_text, font_size=42)
                # 이전 줄 바로 아래에 배치
                new_line.next_to(all_elements[-1], DOWN, buff=0.4, aligned_edge=LEFT)

            # 2. 스마트 스크롤 로직
            # i가 설정한 임계값(예: 5줄)을 넘어가면 전체 그룹을 위로 이동
            if i >= max_lines_before_scroll:
                self.play(
                    all_elements.animate.shift(UP * line_spacing),
                    new_line.animate.shift(UP * line_spacing), # 새로 생길 라인도 같이 이동
                    run_time=0.6
                )

            # 강조 색상
            if i == 6: new_line.set_color(BLUE_B)
            if i == 7: new_line.set_color(ORANGE)

            # 수식 나타내기
            self.play(Write(new_line), run_time=0.8)
            all_elements.add(new_line)
            self.wait(0.5)

        # 마지막 결과 강조
        final_box = SurroundingRectangle(all_elements[-1], color=RED, buff=0.1)
        self.play(Create(final_box))
        self.wait(2)