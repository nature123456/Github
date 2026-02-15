from manim import *

class IdentityExpansion(Scene):
    def construct(self):
        # 1. 수식 데이터 정의 (합차 공식 우선 적용 전략)
        # 1단계: 원래 식
        # 2단계: 제곱을 밖으로 묶기 (a^2 b^2 = (ab)^2)
        # 3단계: 괄호 안에서 합차 공식 적용
        # 4단계: 완전제곱식 전개
        raw_lines = [
            r"(p + 2q)^2 (p - 2q)^2",
            r"= \{ (p + 2q)(p - 2q) \}^2",
            r"= (p^2 - (2q)^2)^2",
            r"= (p^2 - 4q^2)^2",
            r"= (p^2)^2 - 2(p^2)(4q^2) + (4q^2)^2",
            r"= p^4 - 8p^2q^2 + 16q^4"
        ]

        # 2. 수식 객체 생성 및 초기 설정
        all_lines = VGroup(*[
            MathTex(line, font_size=40) for line in raw_lines
        ])

        # 등호(=)를 기준으로 왼쪽 정렬하며 아래로 배치
        all_lines.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        # 화면 왼쪽 상단에 고정 (밀려 올라가지 않도록)
        all_lines.to_corner(UL, buff=1.5).shift(RIGHT * 1.5)

        # 3. 단계별 애니메이션 및 핵심 공식 하이라이트
        
        # [1단계] 문제 등장
        self.play(Write(all_lines[0]))
        self.wait(1)

        # [2단계] 지수 법칙 (a^n b^n = (ab)^n)
        self.play(Write(all_lines[1]))
        self.wait(1)

        # [3단계] 합차 공식 적용 강조
        # 괄호 안의 합차 공식을 보여주기 위해 박스 표시 (선택사항)
        box = SurroundingRectangle(all_lines[1][0][2:14], color=BLUE, buff=0.1)
        self.play(Create(box))
        self.play(Write(all_lines[2]))
        self.play(FadeOut(box))
        
        # [4단계] 정리
        self.play(Write(all_lines[3]))
        self.wait(1)

        # [5단계] 완전제곱식 전개 (a-b)^2
        # (p^2 - 4q^2)^2 부분에 강조
        box2 = SurroundingRectangle(all_lines[3][0][1:9], color=ORANGE, buff=0.1)
        self.play(Create(box2))
        self.play(Write(all_lines[4]))
        self.play(FadeOut(box2))

        # [6단계] 최종 결과
        self.play(Write(all_lines[5]))
        all_lines[5].set_color(YELLOW) # 최종 결과 강조
        self.wait(2)

# 실행: manim -pqh expansion44.py IdentityExpansion