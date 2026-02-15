from manim import *

class LogProofTightened(Scene):
    def construct(self):
        font_name = "NanumGothic"
        LINE_BUFF = 0.5  # 줄 간격
        
        steps_data = [
            ["주어진 조건: ", r"a > 0, a \neq 1, M > 0, N > 0", " 일 때,"],
            [r"\log_a \frac{M}{N} = \log_a M - \log_a N", " 이 성립함을 보이시오."],
            [r"\log_a M = m, \log_a N = n", " 으로 놓으면"],
            ["로그의 정의에 의하여 ", r"M = a^m, N = a^n"],
            ["지수법칙에 의하여 ", r"\frac{M}{N} = \frac{a^m}{a^n} = a^{m-n}"],
            ["로그의 정의에 의하여 ", r"\log_a \frac{M}{N} =\log_a a^{m-n} = m - n"],
            ["따라서 ", r"\log_a \frac{M}{N} = \log_a M - \log_a N"]
        ]

        all_lines = VGroup()

        # 1. 모든 줄을 먼저 생성하여 VGroup에 담기
        for step in steps_data:
            line = VGroup()
            for part in step:
                if any(c in part for c in ["\\", "=", ">", "_", "^"]):
                    obj = MathTex(part, font_size=32)
                else:
                    obj = Text(part, font=font_name, font_size=24)
                
                if len(line) > 0:
                    obj.next_to(line[-1], RIGHT, buff=0.1)
                line.add(obj)
            all_lines.add(line)

        # 2. 줄들을 수직으로 정렬 (왼쪽 기준 정렬)
        all_lines.arrange(DOWN, buff=LINE_BUFF, aligned_edge=LEFT)
        
        # 3. 전체 그룹을 화면 중앙에 배치 (미리 위치를 잡아둠)
        all_lines.center()

        # 4. 하나씩 화면에 그리기
        for i, line in enumerate(all_lines):
            self.play(Write(line), run_time=1.8)
            self.wait(3.5)

        # 5. 마지막 결과 강조 박스 (정확히 마지막 줄에 위치)
        focus_rect = SurroundingRectangle(all_lines[-1], color=YELLOW, buff=0.15)
        self.play(Create(focus_rect))
        self.wait(2)