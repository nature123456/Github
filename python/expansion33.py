from manim import *

class PolynomialFixedPosition(Scene):
    def construct(self):
        # 1. 수식 데이터 정의 (LaTeX)
        raw_lines = [
            r"(p + 2q)^2 (p - 2q)^2",
            r"= (p^2 + 4pq + 4q^2)(p^2 - 4pq + 4q^2)",
            r"= \{(p^2 + 4q^2) + 4pq\}\{(p^2 + 4q^2) - 4pq\}",
            r"= (p^2 + 4q^2)^2 - (4pq)^2",
            r"= p^4 + 8p^2q^2 + 16q^4 - 16p^2q^2",
            r"= p^4 - 8p^2q^2 + 16q^4"
        ]

        # 2. 모든 수식을 미리 생성하고 위치 고정
        all_lines = VGroup(*[
            MathTex(line, font_size=38) for line in raw_lines
        ])

        # 줄 간격(buff)을 일정하게 하여 아래로 정렬
        # aligned_edge=LEFT를 사용하여 등호와 수식 시작점을 맞춤
        all_lines.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        # 수식 뭉치 전체를 화면의 적절한 위치(왼쪽 상단)에 고정
        # 화면 중앙에서 왼쪽으로 2만큼, 위쪽으로 1.5만큼 이동하여 배치
        all_lines.to_corner(UL, buff=1.5).shift(RIGHT * 1.5)

        # 3. 애니메이션 실행 (위로 밀어올리지 않고 제자리에서 등장)
        for i in range(len(all_lines)):
            # 각 줄이 순차적으로 나타남 (이전 줄들은 움직이지 않음)
            self.play(
                Write(all_lines[i]),
                run_time=1.0
            )
            self.wait(0.5)

        # 마지막 결과 라인 강조 (색상 변경)
        self.play(all_lines[-1].animate.set_color(YELLOW))
        self.wait(2)



# 실행 방법: 터미널에서 아래 명령어를 입력하세요.
# manim -pqh expansion33.py PolynomialExpansion