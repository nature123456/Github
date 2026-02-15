from manim import *

# 클래스 이름을 LogCalculationFixed로 설정했습니다.
class LogCalculationFixed(Scene):
    def construct(self):
        # 1. 시스템에 설치된 한글 폰트 설정
        # 폰트가 없으면 기본 폰트로 출력되도록 예외 처리를 하거나 일반 Text를 사용합니다.
        my_font = "NanumGothic"
        
        steps_data = [
            ("2 \log_3 \sqrt{6} - \log_3 \\frac{1}{9} + \log_3 0.5", "주어진 로그 식을 적습니다."),
            ("= 2 \log_3 \sqrt{6} - \log_3 \\frac{1}{9} + \log_3 \\frac{1}{2}", "소수 0.5를 분수 1/2로 바꿉니다."),
            ("= \log_3 (\sqrt{6})^2 - \log_3 9^{-1} + \log_3 2^{-1}", "지수 법칙과 로그 성질을 이용합니다."),
            ("= \log_3 6 + \log_3 9 - \log_3 2", "거듭제곱과 역수를 정리합니다."),
            ("= \log_3 \\frac{6 \\times 9}{2}", "로그의 합(+)은 곱으로, 차(-)는 나눗셈으로!"),
            ("= \log_3 27 = \log_3 3^3", "진수를 계산하여 거듭제곱으로 만듭니다."),
            ("= 3", "로그 정의에 따라 최종 결과는 3입니다.")
        ]

        equations = VGroup()
        
        for i, (math_text, explanation) in enumerate(steps_data):
            # TextArea 대신 Text(또는 MathTex)를 사용하여 오류 방지
            new_line = MathTex(math_text, font_size=36)
            
            if i == 0:
                new_line.to_edge(UP, buff=1.0).shift(LEFT * 1.5)
                self.play(Write(new_line))
            else:
                # 이전 줄의 아래에 정렬하여 배치
                new_line.next_to(equations[-1], DOWN, aligned_edge=LEFT, buff=0.4)
                
                # 화면이 꽉 차지 않도록 전체를 위로 슬라이드
                self.play(
                    VGroup(equations, new_line).animate.shift(UP * 0.7),
                    Write(new_line),
                    run_time=1
                )
            
            # 설명 텍스트 (우측 배치)
            # TextArea 오류를 피하기 위해 Text 객체 사용
            desc = Text(explanation, font=my_font, font_size=18, color=BLUE_B)
            desc.next_to(new_line, RIGHT, buff=0.8)
            
            self.play(FadeIn(desc, shift=LEFT * 0.2))
            equations.add(new_line)
            self.wait(1.5)
            self.play(FadeOut(desc))

        # 마지막 결과 강조
        self.play(new_line.animate.set_color(YELLOW).scale(1.1))
        self.wait(2)