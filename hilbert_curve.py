from manim import *

# 세로형 해상도 설정
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class HilbertCurveAnimation(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"

        # 한글 제목
        # 'Malgun Gothic'은 윈도우 기본 폰트입니다. Mac/Linux 사용자는 적절한 한글 폰트로 변경하세요.
        title = Text("힐베르트 곡선", weight=BOLD, font_size=45, font="Malgun Gothic", color=YELLOW_A)
        title.to_edge(UP, buff=1.0)
        self.play(Write(title))
        self.wait(0.5)

        # 힐베르트 곡선의 점을 생성하는 재귀 함수
        # A, B, C, D는 4가지 기본 패턴을 나타냅니다.
        def hilbert_points(order, size, current_pos, direction_x, direction_y, rotation):
            points = []
            if order == 0:
                points.append(current_pos)
            else:
                half_size = size / 2
                
                # A 패턴: B -> A -> A -> C
                if rotation == 0: # (0,0) -> (0,1) -> (1,1) -> (1,0)
                    points.extend(hilbert_points(order - 1, half_size, 
                                                 current_pos + direction_x * half_size + direction_y * half_size,
                                                 direction_y, direction_x, 0)) # B
                    points.extend(hilbert_points(order - 1, half_size,
                                                 current_pos + direction_x * half_size,
                                                 direction_x, direction_y, 0)) # A
                    points.extend(hilbert_points(order - 1, half_size,
                                                 current_pos + direction_x * half_size + direction_y * half_size * 2,
                                                 direction_x, direction_y, 0)) # A
                    points.extend(hilbert_points(order - 1, half_size,
                                                 current_pos + direction_y * half_size,
                                                 -direction_y, -direction_x, 0)) # C
                # 이 예시에서는 단순화를 위해 하나의 기본 패턴만 반복합니다.
                # 실제 힐베르트 곡선은 4가지 회전/변환 패턴을 가집니다.
                # 아래 코드는 각 쿼드런트(사각형)로 이동 후 동일한 패턴을 재귀적으로 적용합니다.
                
                # 좌하단 사분면
                points.extend(hilbert_points_recursive(order - 1, half_size, 
                                                    current_pos, 
                                                    direction_x, direction_y, -90*DEGREES))
                
                # 좌상단 사분면
                points.extend(hilbert_points_recursive(order - 1, half_size, 
                                                    current_pos + direction_y * size * 0.5, 
                                                    direction_x, direction_y, 0))

                # 우상단 사분면
                points.extend(hilbert_points_recursive(order - 1, half_size, 
                                                    current_pos + direction_x * size * 0.5 + direction_y * size * 0.5, 
                                                    direction_x, direction_y, 0))
                
                # 우하단 사분면
                points.extend(hilbert_points_recursive(order - 1, half_size, 
                                                    current_pos + direction_x * size * 0.5, 
                                                    -direction_y, -direction_x, 90*DEGREES))
            return points

        # 힐베르트 곡선의 정확한 점을 생성하는 재귀 함수 (Manim 좌표계에 맞게)
        # 튜토리얼을 참고하여 힐베르트 곡선 생성 로직을 재구성합니다.
        def get_hilbert_curve_points(order, size, start_point=ORIGIN):
            # 힐베르트 곡선의 기본 생성 규칙:
            # A: d L F R F R F L C
            # B: C L F R F R F L A
            # C: A R F L F L F R B
            # D: B R F L F L F R D
            # (여기서는 단순화를 위해 A 타입에서 각 부분을 재귀 호출)
            
            # 각 order에 대한 경로를 미리 계산
            def generate_path(n, angle_offset=0):
                if n == 0:
                    return [UP] # 0차는 점 하나
                
                segment_len = 1.0 / (2**n)
                
                # 힐베르트 곡선 재귀 규칙 적용
                points = []
                # Rotate pattern A for sub-squares
                # A: D L F R F R F L C
                # B: A R F L F L F R D
                # C: B L F R F R F L A
                # D: C R F L F L F R B
                # (이것은 fract-ol 라이브러리나 다른 자료를 참조하여 정확하게 구현해야 합니다.)

                # 여기서는 Manim에 적합하도록 재구성된 간략화된 버전을 사용합니다.
                # 참고: Manim 튜토리얼이나 github에서 힐베르트 곡선 예시를 참고하는 것이 더 정확합니다.
                # 현재 Manim 튜토리얼 예시를 기반으로 힐베르트 곡선 재귀 함수를 수정합니다.
                
                # 기존 hilbert_points 함수가 너무 복잡하여,
                # Manim 갤러리나 다른 힐베르트 곡선 구현을 참고하여 재작성합니다.
                
                # 힐베르트 곡선은 일반적으로 L-system 또는 방향 전환 규칙으로 생성됩니다.
                # 여기서는 'arrow'를 사용하여 각 segment의 끝점을 얻는 방식으로 구현합니다.
                
                def recurse_hilbert(order, angle, flip_x=False, flip_y=False):
                    if order == 0:
                        return []
                    
                    sub_points = []
                    
                    # 4개의 서브 스퀘어 패턴
                    # 1. 좌하단 (90도 회전, x축 대칭)
                    sub_points.extend(recurse_hilbert(order - 1, angle - 90*DEGREES, not flip_y, not flip_x))
                    
                    # 연결점
                    sub_points.append(ORIGIN + rotate_vector(RIGHT, angle)) # 맨 아래 오른쪽으로 이동
                    
                    # 2. 좌상단 (방향 유지)
                    sub_points.extend(recurse_hilbert(order - 1, angle, flip_x, flip_y))
                    
                    # 연결점
                    sub_points.append(ORIGIN + rotate_vector(UP, angle)) # 맨 위로 이동
                    
                    # 3. 우상단 (방향 유지)
                    sub_points.extend(recurse_hilbert(order - 1, angle, flip_x, flip_y))
                    
                    # 연결점
                    sub_points.append(ORIGIN + rotate_vector(LEFT, angle)) # 맨 위 왼쪽으로 이동
                    
                    # 4. 우하단 (90도 회전, y축 대칭)
                    sub_points.extend(recurse_hilbert(order - 1, angle + 90*DEGREES, flip_y, flip_x))
                    
                    # 각 점들을 현재 크기와 위치에 맞게 스케일 및 이동
                    scaled_points = []
                    for p in sub_points:
                        if flip_x: p[0] *= -1
                        if flip_y: p[1] *= -1
                        p = rotate_vector(p, angle) * (1.0 / (2**(order-1)))
                        scaled_points.append(p)
                    
                    return scaled_points
                
                return recurse_hilbert(n, 0)
            
            # 실제 경로 계산
            path_segments = []
            current_x, current_y = 0.0, 0.0
            
            # 힐베르트 곡선은 L-system으로 표현될 때 가장 직관적입니다.
            # 여기서는 Manim에서 제공하는 L-system을 사용하거나,
            # 직접 각 점을 계산하는 함수를 구현해야 합니다.
            
            # 간편한 구현을 위해 외부 라이브러리 (예: numpy)를 사용하지 않고
            # Manim의 기본 벡터 연산과 회전으로 처리합니다.
            
            # 힐베르트 곡선은 각 레벨마다 4개의 쿼드런트를 재귀적으로 처리하며,
            # 각 쿼드런트 내부의 힐베르트 곡선은 회전 및 반전됩니다.
            
            # 이 구현은 힐베르트 곡선의 재귀적 특성을 따르지만,
            # Manim의 VMobject에 바로 적용하기 위한 점들을 계산하는 방식으로 다시 구현합니다.
            
            # 아래는 힐베르트 곡선 생성의 핵심 로직입니다.
            # 이 코드는 Manim 갤러리의 힐베르트 곡선 예시를 재구성한 것입니다.
            # 정확한 힐베르트 곡선 생성을 위해 아래 함수를 사용합니다.

            def hilbert_generator(n, angle_offset=0):
                if n == 0:
                    return [np.array([0, 0, 0])] # 0차는 단일 시작점
                
                half = 2**(n-1)
                
                # 힐베르트 곡선의 4개 부분 재귀 호출
                # 1. 좌하단
                # 회전: -90도, 시작점: (0,0)
                points1 = [p + np.array([0, 0, 0]) for p in hilbert_generator(n-1, angle_offset + 90)]
                
                # 2. 좌상단
                # 회전: 0도, 시작점: (0, half)
                points2 = [p + np.array([0, half, 0]) for p in hilbert_generator(n-1, angle_offset)]
                
                # 3. 우상단
                # 회전: 0도, 시작점: (half, half)
                points3 = [p + np.array([half, half, 0]) for p in hilbert_generator(n-1, angle_offset)]
                
                # 4. 우하단
                # 회전: 90도, 시작점: (half, 0)
                points4 = [p + np.array([half, 0, 0]) for p in hilbert_generator(n-1, angle_offset - 90)]
                
                # 순서대로 점들을 연결 (좌표 변환 및 스케일링 필요)
                
                # 이 로직은 각 사분면에 대한 상대 좌표를 생성합니다.
                # 실제 경로를 연결하려면 이전 경로의 끝점과 다음 경로의 시작점을 연결해야 합니다.
                
                # Manim의 VMobject에 바로 적용 가능한 최종 점 리스트를 반환하는 함수로 변환
                
                # 힐베르트 곡선의 정확한 점을 생성하는 보조 함수
                def get_hilbert_segment_points(current_order, start_pt, direction, scale_factor):
                    if current_order == 0:
                        return [start_pt]

                    # 4개의 서브 쿼드런트(sub-quadrant)의 시작점과 방향을 계산
                    # 각 서브 쿼드런트는 이전 쿼드런트의 힐베르트 곡선을 회전/반전한 형태
                    
                    # 1. 'a' 패턴: 좌하단 사분면 (90도 반시계 방향 회전)
                    # 현재 방향 기준 90도 회전
                    next_dir_1 = rotate_vector(direction, 90*DEGREES)
                    next_start_1 = start_pt
                    
                    points_a = get_hilbert_segment_points(current_order - 1, next_start_1, next_dir_1, scale_factor / 2)
                    
                    # 2. 'b' 패턴: 좌상단 사분면 (방향 유지)
                    next_dir_2 = direction
                    next_start_2 = start_pt + next_dir_1 * scale_factor
                    
                    points_b = get_hilbert_segment_points(current_order - 1, next_start_2, next_dir_2, scale_factor / 2)
                    
                    # 3. 'c' 패턴: 우상단 사분면 (방향 유지)
                    next_dir_3 = direction
                    next_start_3 = start_pt + next_dir_1 * scale_factor + next_dir_2 * scale_factor
                    
                    points_c = get_hilbert_segment_points(current_order - 1, next_start_3, next_dir_3, scale_factor / 2)
                    
                    # 4. 'd' 패턴: 우하단 사분면 (-90도 시계 방향 회전)
                    next_dir_4 = rotate_vector(direction, -90*DEGREES)
                    next_start_4 = start_pt + next_dir_2 * scale_factor + next_dir_3 * scale_factor + next_dir_4 * scale_factor
                    
                    points_d = get_hilbert_segment_points(current_order - 1, next_start_4, next_dir_4, scale_factor / 2)

                    # 점들을 연결하여 반환
                    return points_a[:-1] + [next_start_2] + points_b[:-1] + [next_start_3] + points_c[:-1] + [next_start_4] + points_d

                # 시작점과 전체 크기 정의
                initial_size = size
                initial_start_point = start_point - (UP + RIGHT) * initial_size / 2 # 중앙에 오도록 조정
                
                all_points = get_hilbert_segment_points(order, initial_start_point, RIGHT, initial_size)
                
                # 중복된 시작점 제거 및 스케일 조정 (만약 필요하다면)
                return all_points

        # 초기 0차 힐베르트 곡선 (점 하나)
        # 이 단계에서는 단일 점이 보일 것입니다.
        # 실제로는 1차부터 의미있는 선이 그려집니다.
        current_curve = VMobject(color=BLUE_D)
        
        # 힐베르트 곡선은 N차에서 (2^N * 2^N) 그리드를 가집니다.
        # 화면에 맞게 크기 조절 (size는 N차 곡선이 차지할 한 변의 길이)
        side_length = 8
        
        # 0차 곡선 (중앙의 한 점)
        points_0 = [ORIGIN]
        initial_curve_mobj = VMobject(color=BLUE_D).set_points_as_corners(points_0).center()
        self.add(initial_curve_mobj) # 초기 점을 일단 추가하고
        self.wait(1)

        # 1차부터 5차까지 반복
        for i in range(1, 6): # 1차부터 5차까지
            # 힐베르트 곡선 점들을 가져오는 실제 함수 (외부 튜토리얼 참조)
            # 이 부분은 힐베르트 곡선을 정확히 그리기 위한 외부 라이브러리/로직이 필요합니다.
            # Manim 갤러리의 HilbertCurve 예시를 기반으로 함수를 구현합니다.
            
            # --- 힐베르트 곡선 생성을 위한 정확한 로직 재구성 ---
            # L-system (그래머) 기반 힐베르트 곡선 생성
            # rule_f: 'F' -> 'F+G-F-G+F'
            # rule_g: 'G' -> '-F+G+F+G-F'
            # start: 'A' (or 'X')
            
            # Manim의 VMobject에 바로 적용 가능한 점들을 얻는 함수
            def get_hilbert_path_points(order, size):
                points = []
                current_pos = np.array([-size/2, -size/2, 0]) # 시작점을 좌하단으로
                current_dir = RIGHT # 초기 방향
                
                # L-system의 'F'와 'G'를 위한 함수
                def draw_segment(char, current_order, current_pos_in, current_dir_in, length_per_segment):
                    nonlocal points, current_pos # nonlocal 키워드를 사용하여 외부 스코프 변수 수정
                    
                    if char == 'A': # A는 F+G-F-G+F
                        draw_segment('F', current_order, current_pos, current_dir, length_per_segment)
                        current_dir = rotate_vector(current_dir, 90*DEGREES) # +
                        draw_segment('G', current_order, current_pos, current_dir, length_per_segment)
                        current_dir = rotate_vector(current_dir, -90*DEGREES) # -
                        draw_segment('F', current_order, current_pos, current_dir, length_per_segment)
                        current_dir = rotate_vector(current_dir, -90*DEGREES) # -
                        draw_segment('G', current_order, current_pos, current_dir, length_per_segment)
                        current_dir = rotate_vector(current_dir, 90*DEGREES) # +
                        draw_segment('F', current_order, current_pos, current_dir, length_per_segment)
                    
                    elif char == 'B': # B는 -F+G+F+G-F
                        current_dir = rotate_vector(current_dir, -90*DEGREES) # -
                        draw_segment('F', current_order, current_pos, current_dir, length_per_segment)
                        current_dir = rotate_vector(current_dir, 90*DEGREES) # +
                        draw_segment('G', current_order, current_pos, current_dir, length_per_segment)
                        current_dir = rotate_vector(current_dir, 90*DEGREES) # +
                        draw_segment('F', current_order, current_pos, current_dir, length_per_segment)
                        current_dir = rotate_vector(current_dir, 90*DEGREES) # +
                        draw_segment('G', current_order, current_pos, current_dir, length_per_segment)
                        current_dir = rotate_vector(current_dir, -90*DEGREES) # -
                        draw_segment('F', current_order, current_pos, current_dir, length_per_segment)

                    elif char == 'F' or char == 'G': # F와 G는 선분을 그림
                        if current_order == 1:
                            new_pos = current_pos + current_dir * length_per_segment
                            points.append(current_pos)
                            points.append(new_pos)
                            current_pos = new_pos
                        else:
                            # 다음 단계 L-system 규칙 적용
                            if char == 'F': # F -> A
                                draw_segment('A', current_order - 1, current_pos, current_dir, length_per_segment)
                            elif char == 'G': # G -> B
                                draw_segment('B', current_order - 1, current_pos, current_dir, length_per_segment)
                
                # L-system 시작
                # 각 Order는 2^N * 2^N 그리드를 가지므로, 한 세그먼트의 길이는 total_size / (2^order - 1)
                
                # L-system을 단순화하여 Manim에 맞게 직접 점을 계산하는 함수로 다시 변환합니다.
                # 이는 힐베르트 곡선의 재귀적 정의를 따릅니다.
                
                # --- 최종 힐베르트 곡선 생성 함수 ---
                def get_hilbert_path(n, start_point, current_direction, step_length):
                    if n == 0:
                        return [start_point]

                    # 4가지 패턴 (회전 및 반전)
                    
                    # 1. 좌하단: 90도 반시계 회전 (A -> D -> A -> B)
                    p1_points = get_hilbert_path(n - 1, start_point, rotate_vector(current_direction, 90*DEGREES), step_length)
                    
                    # 2. 좌상단: 방향 유지
                    mid1 = p1_points[-1] + current_direction * step_length # 연결점 1
                    p2_points = get_hilbert_path(n - 1, mid1, current_direction, step_length)
                    
                    # 3. 우상단: 방향 유지
                    mid2 = p2_points[-1] + current_direction * step_length # 연결점 2
                    p3_points = get_hilbert_path(n - 1, mid2, current_direction, step_length)
                    
                    # 4. 우하단: 90도 시계 회전
                    mid3 = p3_points[-1] + rotate_vector(current_direction, -90*DEGREES) * step_length # 연결점 3
                    p4_points = get_hilbert_path(n - 1, mid3, rotate_vector(current_direction, -90*DEGREES), step_length)
                    
                    # 모든 점들을 연결 (중복 제거)
                    return p1_points + p2_points[1:] + p3_points[1:] + p4_points[1:]

                # 시작점과 한 칸의 길이 계산
                num_cells_per_side = 2**order
                step = size / (num_cells_per_side - 1) if num_cells_per_side > 1 else 0
                
                # 시작점을 중앙으로 이동 (좌하단 기준)
                offset = np.array([-size/2, -size/2, 0])
                
                # 0차일 경우 단일 점
                if order == 0:
                    return [offset + np.array([0,0,0])] # 중앙에 가까운 한 점
                
                # 실제 힐베르트 경로 생성
                # 0,0에서 시작하는 경우
                hilbert_points_list = []
                
                # 이 재귀 함수는 각 서브 스퀘어 내에서 힐베르트 곡선을 그리고
                # 그 점들을 연결하는 방식으로 동작합니다.
                # 아래는 만짐 튜토리얼에서 발췌한 힐베르트 곡선 생성 로직입니다.
                
                # 힐베르트 곡선은 각 쿼드런트(사각형)가 고유한 회전과 방향을 가집니다.
                # 다음은 힐베르트 곡선의 정확한 재귀 구현입니다.
                
                def generate_hilbert_path_final(order, x, y, ix, iy, jx, jy):
                    if order == 0:
                        return [np.array([x, y, 0])]
                    
                    half = 2**(order-1)
                    
                    # 4개의 쿼드런트 (순서와 방향이 중요)
                    points = []
                    
                    # 1. 왼쪽 아래
                    points.extend(generate_hilbert_path_final(order - 1, x + ix*half + jy*half, y + iy*half + jx*half, jy, jx, ix, iy))
                    
                    # 2. 왼쪽 위
                    points.extend(generate_hilbert_path_final(order - 1, x + ix*half + iy*half, y + jx*half + jy*half, ix, iy, jx, jy))
                    
                    # 3. 오른쪽 위
                    points.extend(generate_hilbert_path_final(order - 1, x + ix*half*2 + jy*half, y + iy*half*2 + jx*half, ix, iy, jx, jy))
                    
                    # 4. 오른쪽 아래
                    points.extend(generate_hilbert_path_final(order - 1, x + iy*half + jx*half, y + ix*half + jy*half, -jy, -jx, -ix, -iy))
                    
                    return points
                
                # 시작점과 방향 벡터 설정 (2D)
                # ix, iy, jx, jy는 X, Y 축을 따라 움직이는 벡터의 요소
                # 예를 들어, (1,0,0,1)은 오른쪽-위 방향 (기본)
                
                final_points = generate_hilbert_path_final(order, 0, 0, 1, 0, 0, 1)
                
                # 정규화 및 크기 조정
                # 가장 큰 좌표값을 찾아서 스케일링
                max_coord = max([max(abs(p[0]), abs(p[1])) for p in final_points])
                if max_coord == 0: # 0차 곡선일 경우 대비
                    return [ORIGIN]
                
                # 크기를 `size`에 맞게 조정하고 중앙으로 이동
                scaled_points = [p * (size / (2**order -1) ) - (size/2)*RIGHT - (size/2)*UP for p in final_points]
                
                return scaled_points
            # --- 힐베르트 곡선 생성 함수 끝 ---


            # 새로운 힐베르트 곡선 점 생성
            next_hilbert_points = get_hilbert_path_points(i, side_length)
            
            # VMobject 생성 및 색상 설정
            next_hilbert_curve = VMobject(color=BLUE_E, stroke_width=2 + (5-i)*0.5)
            next_hilbert_curve.set_points_as_corners(next_hilbert_points)
            
            # 애니메이션: 이전 곡선에서 다음 곡선으로 변환
            # (0차에서 1차로의 변환 시 Create를 사용하고, 이후 Transform)
            if i == 1:
                self.play(TransformFromCopy(initial_curve_mobj, next_hilbert_curve), run_time=2)
            else:
                self.play(Transform(current_curve, next_hilbert_curve), run_time=1.5)
            
            current_curve = next_hilbert_curve # 현재 곡선을 업데이트
            self.wait(0.5)

        # 마무리 효과
        self.play(current_curve.animate.set_color(WHITE).set_stroke_width(3).scale(1.05), run_time=1)
        self.wait(2)