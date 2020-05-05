class GameState():
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.game_active = True
        self.reset()
        self.game_active = False

    def reset(self):
        self.ship_left = self.ai_setting.ship_limit