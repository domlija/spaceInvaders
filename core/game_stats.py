class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            #cls._instances[cls] = super(Singleton).__get__(cls).__call__(*args, **kwargs)
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class GameStats(metaclass=Singleton):
    """Track statistics for Alien Invasion."""

    # _instance = None 

    # def __new__(cls, *args):
    #     if not cls._instance:
    #         cls._instance = super(GameStats, cls).__new__(cls)
    #     return cls._instance

    def __init__(self, ai_settings):
        """Initialize statistics."""
        if not hasattr(self, 'initialized'):
            self.ai_settings = ai_settings
            self.reset_stats()

            # Start game in an inactive state.
            self.game_active = False

            # High score should never be reset.
            self.high_score = 0
            self.initalized = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1