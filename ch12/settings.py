class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_max = 3

        self.alien_speed_factor = 1
        self.aliens_drop_speed = 10
        self.aliens_direction = 1   # 1: right, -1: left