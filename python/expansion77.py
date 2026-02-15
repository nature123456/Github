from manim import *

class MultiplicationFormulas(Scene):
    def construct(self):
        # 1. 폰트 및 설정
        font_name = "NanumGothic" # 시스템에 설치된 폰트명 확인 필요
        title_text = "다항식의 곱셈 공식 10선"
        
        # 2. 제목
        title = Text(title_text, font=font_name, font_size=30).to_edge(UP, buff=0.3)
        self.play(Write(title))

        # 3. 데이터 정의
        raw_data = [
            ("①", r"(a+b)^2=a^2+2ab+b^2,\ (a-b)^2=a^2-2ab+b^2"),
            ("②", r"(a+b)(a-b)=a^2-b^2"),
            ("③", r"(x+a)(x+b)=x^2+(a+b)x+ab"),
            ("④", r"(ax+b)(cx+d)=acx^2+(ad+bc)x+bd"),
            ("⑤", r"(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca"),
            ("⑥", r"(a+b)^3=a^3+3a^2b+3ab^2+b^3,\ (a-b)^3=a^3-3a^2b+3ab^2-b^3"),
            ("⑦", r"(a+b)(a^2-ab+b^2)=a^3+b^3,\ (a-b)(a^2+ab+b^2)=a^3-b^3"),
            ("⑧", r"(x+a)(x+b)(x+c)=x^3+(a+b+c)x^2+(ab+bc+ca)x+abc"),
            ("⑨", r"(a+b+c)(a^2+b^2+c^2-ab-bc-ca)=a^3+b^3+c^3-3abc"),
            ("⑩", r"(a^2+ab+b^2)(a^2-ab+b^2)=a^4+a^2b^2+b^4")
        ]

        colors = [RED_A, ORANGE, YELLOW, GREEN_A, BLUE_A, PURPLE_A, PINK, TEAL_A, GOLD_A, MAROON_A]
        
        # 공식들을 담을 그룹 정의 (이 변수가 정의되어 있어야 나중에 에러가 나지 않습니다)
        formula_rows = VGroup()

        # 4. 공식 생성 및 등장 (크고 굵게 나타났다가 자리를 잡음)
        for i, ((num, formula_tex), color) in enumerate(zip(raw_data, colors)):
            # 최종 위치에 놓일 객체
            num_obj = Text(num, font=font_name, font_size=20, color=color)
            tex_obj = MathTex(formula_tex, color=color).scale(0.6)
            row = VGroup(num_obj, tex_obj).arrange(RIGHT, buff=0.2)

            if i == 0:
                row.next_to(title, DOWN, buff=0.4)
            else:
                row.next_to(formula_rows[-1], DOWN, buff=0.2, aligned_edge=LEFT)

            # 강조용 임시 객체 (중앙에서 크게 등장)
            highlight_row = VGroup(
                Text(num, font=font_name, font_size=35, color=color, stroke_width=1.5),
                MathTex(formula_tex, color=color, stroke_width=1.5).scale(1.0)
            ).arrange(RIGHT, buff=0.3).move_to(ORIGIN)

            self.play(Write(highlight_row), run_time=0.6)
            self.play(ReplacementTransform(highlight_row, row), run_time=0.6)
            
            formula_rows.add(row)

        self.wait(1)

        # 5. 플로팅 효과: 위에서 아래로 (Top -> Down)
        for row in formula_rows:
            self.play(
                Indicate(row, scale_factor=1.2, color=row[0].get_color()), 
                run_time=0.3
            )

        self.wait(0.5)

        # 6. 플로팅 효과: 아래에서 위로 역순 (Bottom -> Up)
        for row in reversed(formula_rows):
            # 살짝 커졌다 돌아오는 애니메이션
            self.play(
                row.animate.scale(1.15).set_color(WHITE),
                run_time=0.15
            )
            self.play(
                row.animate.scale(1/1.15).set_color(row[0].get_color()), 
                run_time=0.15
            )

        # ... (이전 코드: 6. 플로팅 효과 역순까지 완료된 상태) ...

        # 7. 특정 공식(6번, 7번) 집중 강조 효과
        # 인덱스는 0부터 시작하므로 ⑥번은 index 5, ⑦번은 index 6입니다.
        target_indices = [5, 6] 
        
        for idx in target_indices:
            target_row = formula_rows[idx]
            
            # (1) 공식이 중앙으로 약간 이동하며 커짐 + 노란색으로 강조
            self.play(
                target_row.animate.scale(1.5).set_color(YELLOW).set_z_index(1),
                run_time=0.6
            )
            
            # (2) 좌우로 흔들리는 효과 (Wiggle)
            self.play(Wiggle(target_row), run_time=0.6)
            
            # (3) 원래 위치와 색상으로 복귀
            self.play(
                target_row.animate.scale(1/1.5).set_color(colors[idx]),
                run_time=0.6
            )
            self.wait(0.2)

        self.wait(2)
	
	
	# 실행: manim -pqh expansion77.py