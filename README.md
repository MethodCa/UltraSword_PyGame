# UltraSword PyGame
RPG videogame written in Python using PyGame modules[^1]. Battle logic is based on the popular rock, paper, scissors game. 
The player and CPU need to wait until its time bar is complete, when the bar is full it is your turn to Attack!

<p align="center">
    <img src="https://github.com/MethodCa/UltraSword/assets/15893276/a0734897-6525-418d-b318-753d079830ea" alt="UltraSword">
</p>

The game heavily relies on visual cues to alert and inform the player of what's happening in-game, a large number of animations and sound effects were put in place to enhance the gameplay.
<p align="center">
    <img src="https://github.com/MethodCa/UltraSword/assets/15893276/9d69b330-a1bb-40d9-8d69-a47823e18315" alt="UltraSword">
    <img src="https://github.com/MethodCa/UltraSword/assets/15893276/b41ede1a-92e9-4719-ae6d-07415fe4946e" alt="UltraSword">
    <img src="https://github.com/MethodCa/UltraSword/assets/15893276/06eb1bfe-ceda-4518-b0ec-8658ab373301" alt="UltraSword">
</p>

The animations are achieved using a custom Class written for UltraSword called AnimatedSprite. AnimatedSprite is a GameObject that contains:
```python
def __init__(self, atlas, horizontal_loading, first_frame_position, animation_type, frame_duration, total_animation_frames):
```
AnimatedSprite renders and iterate the animation frames, Animations can be type LOOP, ONE_TIME or STATIC.

```python
def __update__(self, delta_time):  # updated the animation if it is a non-static
    if self.animation_type != AnimationType.STATIC:
        if self.current_animation_time >= self.frame_duration:
            self.current_frame += 1
            if self.current_frame > self.total_animation_frames:
                if self.animation_type == AnimationType.LOOP:
                    self.current_frame = 0
                else:
                    self.current_frame = self.total_animation_frames
                    self.is_animation_ended = True
            self.current_animation_time = 0
    self.current_animation_time = self.current_animation_time + delta_time
```
To render a frame AnimatedSprite iterates through the Texture2D atlas and selects the frame that should be rendered, frames can be stored in the texture atlas using Horizontal 
or Vertical alignment.
- Horizontal Aligment example.
![Animations](https://github.com/MethodCa/UltraSword/assets/15893276/37481580-d1a8-46e3-bd3f-eda9aeb61caf)

```Python
def __render__(self):
    if self.horizontal_loading:  # horizontal loading applies to the images that are stored in an horizontal fashion
        offset = self.first_frame_position.w * self.current_frame
        return pygame.Rect(self.first_frame_position.x + offset, self.first_frame_position.y,
                           self.first_frame_position.w, self.first_frame_position.h)
    else:  # horizontal loading applies to the images that are stored in a vertical fashion
        offset = self.first_frame_position.h * self.current_frame
        return pygame.Rect(self.first_frame_position.x, self.first_frame_position.y + offset,
                           self.first_frame_position.w, self.first_frame_position.h)
```

> [!NOTE]
> This game was previously written in C# using Monogame! have a look here [UltraSword PyGame](https://github.com/MethodCa/UltraSword)
> 
[^1]: [PyGame](https://www.pygame.org/) Set of Python modules designed for writing video games. 
