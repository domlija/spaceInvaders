class Singleton(type):
    #TODO: implement singleton metaclass
    pass


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

    game_active = False
    def __init__(self, ai_settings):
        """Initialize statistics."""
        #TODO: implement init
        pass

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        #TODO: implement stats reset mechanism
