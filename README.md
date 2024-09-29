### Introduction
Reimplementation of Alien Invasion from the book *Python Crash Course*. 

I changed the graphics and refactored the code to showcase design patterns as a teaching tool. I also added multiple guns.

Some power-ups are planned in the future.

To start the code simply run `python space_invaders.py`


### Used patterns

|Pattern | Place |
|--------|------ |
|Factory| Guns abstract bullet creation from the game logic|
|Strategy| Different guns change bullet creation logic|
|Composite| Pygame Group object is a composite of Sprites|
|Prototype| Used to copy rectangles for Splitter Bullets|
|Listener | Used to update scoreboard based on game events|
|Iterator| Used to iterate over various collections with `for`|
|Decorator| **TBD** (probably for powerups e.g. shield)|
 