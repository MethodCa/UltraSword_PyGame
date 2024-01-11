from AnimatedSprite import AnimatedSprite
import pygame as pygame
from Enum import Animation


class GameObject:

    def __init__(self, position, animation_list, max_health, max_stamina, strength):
        # Constructor
        self.position = position
        self.animation_list = animation_list
        self.health = max_health
        self.max_health = max_health
        self.stamina = 0
        self.max_stamina = max_stamina
        self.strength = strength
        self.current_animation = Animation.IDLE
        self.choice = -1

    def __update__(self, delta_time):  # updates the current animation for the game object
        self.check_finished_animation()
        current_sprite = self.animation_list[self.current_animation]
        current_sprite.__update__(delta_time)

    def __draw__(self, screen):  # draws the current animation for the game object
        current_sprite = self.animation_list[self.current_animation]
        screen.blit(current_sprite.atlas, self.position, current_sprite.__render__())

    def play_animation(self, animation):
        current_sprite = self.animation_list[self.current_animation]
        if animation != self.current_animation:
            current_sprite.current_frame = 0
        elif current_sprite.is_animation_ended:
            current_sprite.current_frame = 0
        self.current_animation = animation
        current_sprite.is_animation_ended = False

    def check_finished_animation(self):  # if animation is ended set the new animation for the game object
        current_sprite = self.animation_list[self.current_animation]
        if current_sprite.is_animation_ended and not self.current_animation == Animation.DEAD:
            self.play_animation(Animation.IDLE)
