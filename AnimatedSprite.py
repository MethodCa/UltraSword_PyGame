import pygame as pygame
from Enum import Animation
from Enum import AnimationType
from Enum import GameState


class AnimatedSprite:
    current_frame = 0  # declare and initialise variable to control the current frame
    current_animation_time = 0  # declare and initialise variable to control the animation time
    is_animation_ended = False  # bool variable to control if the animation is ended

    def __init__(self, atlas, horizontal_loading, first_frame_position, animation_type, frame_duration,
                 total_animation_frames):
        # Constructor 
        self.atlas = atlas
        self.horizontal_loading = horizontal_loading
        self.first_frame_position = first_frame_position
        self.animation_type = animation_type
        self.frame_duration = frame_duration
        self.total_animation_frames = total_animation_frames
        self.total_animation_frames -= 1
        self.current_frame = 0
        self.current_animation_time = 0

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

    def __render__(self):
        if self.horizontal_loading:  # horizontal loading applies to the images that are stored in an horizontal fashion
            offset = self.first_frame_position.w * self.current_frame
            return pygame.Rect(self.first_frame_position.x + offset, self.first_frame_position.y,
                               self.first_frame_position.w, self.first_frame_position.h)
        else:  # horizontal loading applies to the images that are stored in a vertical fashion
            offset = self.first_frame_position.h * self.current_frame
            return pygame.Rect(self.first_frame_position.x, self.first_frame_position.y + offset,
                               self.first_frame_position.w, self.first_frame_position.h)
