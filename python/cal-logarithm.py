from manim import *

class LogCalculationSlow(Scene):
    def construct(self):
        # 1. 환경 설정
        font_name = "NanumGothic"
        
        # 2. 전체 컨테이너
        main_container = VGroup()

        # 3. 문제 부분 (상단 배치)
        p1 = MathTex(r"\log_{10} 2=a, \log_{10} 3=b", font_size=28)
        p2 = Text("일 때, ", font=font_name, font_size=20)
        p3 = MathTex(r"\log_{10} \frac{4}{15}", font_size=28)
        p4 = Text("를 a, b에 대한 식으로 나타내시오.", font=font_name, font_size=20)
        
        problem = VGroup(p1, p2, p3, p4).arrange(RIGHT, buff=0.1)
        problem.to_edge(UP, buff=0.5)
        
        # 문제 작성 속도를 조금 늦춤 (run_time: 1.0 -> 1.5)
        self.play(Write(problem, run_time=1.5))
        self.wait(1.5) # 문제 읽을 시간 확보
        
        main_container.add(problem)

        # 4. 계산 과정 데이터
        calculations = [
            (r"= \log_{10} \frac{2^2}{3 \times 5}", "4와 15를 소인수분해"),
            (r"= 2\log_{10} 2 - \log_{10} 3 - \log_{10} 5", "로그의 성질 이용"),
            (r"= 2\log_{10} 2 - \log_{10} 3 - \log_{10} \frac{10}{2}", "5 = 10/2 변환"),
            (r"= 2\log_{10} 2 - \log_{10} 3 - (1 - \log_{10} 2)", "로그의 성질 이용"),
			(r"= 2\log_{10} 2 - \log_{10} 3 - 1 + \log_{10} 2", "괄호 풀기"),
            (r"= 3\log_{10} 2 - \log_{10} 3 - 1", "동류항 정리"),
            (r"= 3a - b - 1", "a, b 대입")
        ]

        # 5. 애니메이션 루프
        for i, (calc_raw, desc_text) in enumerate(calculations):
            line = VGroup()
            calc_part = MathTex(calc_raw, font_size=32)
            desc_part = Text(desc_text, font=font_name, font_size=15, color=GRAY)
            
            line.add(calc_part, desc_part)
            desc_part.next_to(calc_part, RIGHT, buff=1.0)
            
            # 줄 간격 압축 유지 (buff=0.3)
            line.next_to(main_container[-1], DOWN, buff=0.3, aligned_edge=LEFT)
            
            if i == 0:
                line.shift(LEFT * 1.2)

            # 스크롤 애니메이션 속도 조절
            if i >= 3:
                self.play(
                    main_container.animate.shift(UP * 0.7),
                    run_time=1.0 # 0.5에서 1.0으로 늦춤
                )

            # 수식 작성 및 설명 등장 속도 조절
            self.play(
                Write(calc_part, run_time=1.2), # 수식이 천천히 써짐
                FadeIn(desc_part, shift=RIGHT * 0.2, run_time=1.0),
            )
            
            main_container.add(line)
            self.wait(1.0) # 각 단계가 끝나고 1초간 멈춤 (기존 0.3)

        self.wait(3) # 전체 과정 종료 후 대기 시간 증가