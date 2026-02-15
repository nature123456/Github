from manim import *

class PanoEduBranding(Scene):
    def construct(self):
        # 1. 폰트 및 스타일 설정
        # 시스템에 설치된 나눔고딕 폰트명을 입력하세요. 
        # (설치 여부에 따라 "NanumGothic", "NanumGothicBold", "나눔고딕" 등으로 시도)
        main_font = "NanumGothic"
        bold_font = "NanumGothicBold"
        
        # ---------------------------------------------------------
        # 1. 인트로 섹션 (배경: 고등학교수학-1.jpg)
        # ---------------------------------------------------------
        intro_bg = ImageMobject("고등학교수학-1.jpg")
        intro_bg.scale_to_fit_width(config.frame_width)
        
        # 채널명: 그라데이션 적용
        channel_name = Text("panoedu-math", font=bold_font, font_size=64)
        channel_name.set_color_by_gradient(BLUE, YELLOW)
        
        # 인트로 애니메이션
        self.play(FadeIn(intro_bg))
        self.play(Write(channel_name), run_time=1.5)
        self.play(channel_name.animate.set_glow(0.5), run_time=0.5) # 살짝 빛나는 효과
        self.wait(1.5)
        
        # 전환: 수식 풀이로 넘어가기 전 페이드 아웃
        self.play(FadeOut(channel_name), intro_bg.animate.set_opacity(0.2))
        self.clear()
        self.wait(0.5)

        # ---------------------------------------------------------
        # 2. 아웃트로 섹션 (배경: 고등학교수학-2.jpg)
        # ---------------------------------------------------------
        outro_bg = ImageMobject("고등학교수학-1.jpg")
        outro_bg.scale_to_fit_height(config.frame_height)
        
        thanks_msg = Text("시청해주셔서 감사합니다!", font=main_font, font_size=36)
        subscribe_msg = Text("구독과 좋아요는 큰 힘이 됩니다", font=main_font, font_size=24, color=YELLOW)
        
        # 그룹화 및 중앙 배치
        final_group = VGroup(thanks_msg, subscribe_msg).arrange(DOWN, buff=0.5)
        
        # [에러 해결] CENTER 대신 ORIGIN을 사용하여 정중앙 배치
        final_group.move_to(ORIGIN) 

        # 아웃트로 애니메이션
        self.play(FadeIn(outro_bg))
        self.play(FadeIn(final_group, shift=UP)) # 아래에서 위로 올라오며 등장
        self.play(Indicate(subscribe_msg, color=YELLOW, scale_factor=1.2)) # 강조 효과
        self.wait(2.5)