class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3

        self.bullet_max = 3
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        
        self.aliens_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.init_dynamic_setting()

    def init_dynamic_setting(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        
        self.aliens_direction = 1   # 1: right, -1: left
        self.alien_point = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)
        # print(self.alien_point)