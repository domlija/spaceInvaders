class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(type(cls))
        print(cls)
        if cls not in cls._instances:
            # cls._instances[cls] = super(Singleton).__get__(cls).__call__(*args, **kwargs)
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Okay, lets explain this whole construct. First we define a singleton metaclass. What is a metaclass?
# Metaclass is a class of classes, and can be used to redefine some class properties such as object creation
# Usually when creating an object of class A we use A(). This is equivalent to type.__call__(A) which then calls
# A.__new__() which in turn calls A.__init__(). When associating a class with metaclass, the __call__ method is overriden
# And metaclass.__call__() is executed instead.

# Now lets take a look at Singleton metaclass. It inherits from type class whose __call__ method implements the above defined
# flow. We override that method to check if an instance of a class has been already created. To be precise calling GameStats()
# calls Singleton.__call__(GameStats) and GameStats is stored in cls. We then check if a singleton has already been created. If not
# we create one on the spot. But how? We use super of the Singleton class which returns a type proxy. By providing cls as the second
# super argument we bind the proxy to the cls or in this case GameStats class. From there we call __call__ method. Python searches for
# it in the superclass of Singleton which is type and finds the original __call__ function. But since we bounded the cls we call
# type.__call__(cls, *args, *kwargs).

# Other approach would be to just use super(Singleton) but this proxy is unbounded and can't be used to fetch __call__ method directly
# We can use __get__ descriptor to bind the proxy to our cls variable and we can get the correct behaviour.


class GameStats(metaclass=Singleton):
    """Track statistics for Alien Invasion."""

    # _instance = None

    # def __new__(cls, *args):
    #     if not cls._instance:
    #         cls._instance = super(GameStats, cls).__new__(cls)
    #     return cls._instance

    def __init__(self, ai_settings):
        """Initialize statistics."""
        if not hasattr(self, "initialized"):
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
