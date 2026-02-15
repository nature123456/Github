from manim import *
import numpy as np

# 폰트 설정
config.font = "NanumGothic"

class PolynomialExpansionSimultaneous(Scene):
    def construct(self):
        # 1. 수식 배치 및 결과항 타겟 지정
        eq_start = r"= "
        terms_raw = ["a^2", "+b^2", "+c^2", "+2ab", "+2bc", "+2ca"]
        
        equations_prev = [
            r"(a + b + c)^2 = \{(a + b) + c\}^2",
            r"= (a + b)^2 + 2(a + b)c + c^2",
            r"= (a^2 + 2ab + b^2) + (2ac + 2bc) + c^2"
        ]

        rendered_eqs = VGroup()
        for i, eq_text in enumerate(equations_prev):
            new_eq = MathTex(eq_text).scale(0.65)
            if i == 0:
                new_eq.to_corner(UL).shift(RIGHT * 0.5 + DOWN * 1.0)
            else:
                new_eq.next_to(rendered_eqs[i-1], DOWN, aligned_edge=LEFT, buff=0.4)
            rendered_eqs.add(new_eq)
            self.play(Write(new_eq), run_time=0.5)

        # 마지막 결과식 조립
        last_line_vgroup = VGroup(MathTex(eq_start).scale(0.65))
        for t in terms_raw:
            last_line_vgroup.add(MathTex(t).scale(0.65))
        
        last_line_vgroup.arrange(RIGHT, buff=0.1)
        last_line_vgroup.next_to(rendered_eqs[-1], DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(Write(last_line_vgroup))
        
        # 2. 오른쪽 도형 설정
        a_v, b_v, c_v = 1.3, 0.8, 0.5
        dims = [a_v, b_v, c_v]
        labels_text = ["a", "b", "c"]
        colors = [RED_A, BLUE_A, GREEN_A, BLUE_A, RED_B, YELLOW_A, GREEN_A, YELLOW_A, RED_C]
        contents = ["a^2", "ab", "ac", "ab", "b^2", "bc", "ac", "bc", "c^2"]

        rects = VGroup()
        area_labels = VGroup()
        total_size = sum(dims)
        start_pos = [3.8 - total_size/2, total_size/2 - 0.5, 0]
        
        curr_y = start_pos[1]
        for i in range(3):
            curr_x = start_pos[0]
            for j in range(3):
                r = Rectangle(width=dims[j], height=dims[i], stroke_width=2, color=WHITE)
                r.set_fill(colors[i*3+j], opacity=0.4)
                r.move_to([curr_x + dims[j]/2, curr_y - dims[i]/2, 0])
                txt = MathTex(contents[i*3+j]).scale(0.45).move_to(r.get_center())
                rects.add(r)
                area_labels.add(txt)
                curr_x += dims[j]
            curr_y -= dims[i]

        # 아크 점선 가이드 (바깥으로 볼록)
        arc_g = VGroup()
        x_t = rects[0].get_left()[0]
        for i in range(3):
            p1, p2 = [x_t, rects[0].get_top()[1]+0.1, 0], [x_t+dims[i], rects[0].get_top()[1]+0.1, 0]
            arc_g.add(DashedVMobject(ArcBetweenPoints(p1, p2, radius=-dims[i]*1), num_dashes=10))
            arc_g.add(MathTex(labels_text[i]).scale(0.5).next_to(arc_g[-1], UP, buff=0.1))
            x_t += dims[i]
        y_t = rects[0].get_top()[1]
        for i in range(3):
            p1, p2 = [rects[0].get_left()[0]-0.1, y_t, 0], [rects[0].get_left()[0]-0.1, y_t-dims[i], 0]
            arc_g.add(DashedVMobject(ArcBetweenPoints(p1, p2, radius=dims[i]*1), num_dashes=10))
            arc_g.add(MathTex(labels_text[i]).scale(0.5).next_to(arc_g[-1], LEFT, buff=0.1))
            y_t -= dims[i]

        self.play(Create(rects), FadeIn(area_labels), Create(arc_g))
        self.wait(1)

        # 3. [핵심] 그룹별 동시 이동 로직
        # (도형 라벨 인덱스들, 수식 타겟 인덱스)
        # area_labels 인덱스: 0:a^2, 1:ab, 2:ac, 3:ab, 4:b^2, 5:bc, 6:ac, 7:bc, 8:c^2
        # last_line_vgroup 인덱스: 1:a^2, 2:b^2, 3:c^2, 4:2ab, 5:2bc, 6:2ca
        move_groups = [
            ([0], 1),    # a^2
            ([4], 2),    # b^2
            ([8], 3),    # c^2
            ([1, 3], 4), # 2ab (동시)
            ([5, 7], 5), # 2bc (동시)
            ([2, 6], 6)  # 2ca (동시)
        ]

        self.play(last_line_vgroup.animate.set_color(YELLOW))

        for label_idxs, target_idx in move_groups:
            target_obj = last_line_vgroup[target_idx]
            guides = VGroup()
            rect_highlights = []
            label_animations = []

            for idx in label_idxs:
                lbl = area_labels[idx]
                dist = np.linalg.norm(lbl.get_center() - target_obj.get_center())
                safe_radius = dist * 0.7
                
                # 가이드라인 생성
                g = DashedVMobject(
                    ArcBetweenPoints(lbl.get_center(), target_obj.get_center(), radius=-safe_radius),
                    num_dashes=25
                ).set_stroke(color=YELLOW, width=4, opacity=0.6)
                guides.add(g)
                
                # 하이라이트 및 이동 애니메이션 준비
                rect_highlights.append(rects[idx].animate.set_fill(opacity=0.85))
                label_animations.append(lbl.animate(path_arc=-0.8).move_to(target_obj).set_opacity(0))

            # 1) 동시 강조 및 가이드라인 생성
            self.play(*rect_highlights, run_time=0.3)
            self.play(Create(guides), run_time=0.7)
            self.wait(0.5)

            # 2) 동시 이동 및 가이드라인 페이드아웃
            self.play(
                *label_animations,
                guides.animate.set_stroke(opacity=0),
                *[rects[idx].animate.set_fill(opacity=0.4) for idx in label_idxs],
                run_time=1.5
            )
            
            # 3) 결과항 강조
            self.play(target_obj.animate.scale(1.3).set_color(WHITE), run_time=0.2)
            self.play(target_obj.animate.scale(1/1.3).set_color(YELLOW), run_time=0.2)
            self.remove(guides)

        self.play(Indicate(last_line_vgroup, color=WHITE))
        self.wait(2)