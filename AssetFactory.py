from AnimatedSprite import AnimatedSprite
from Enum import AnimationType
import pygame as pygame


class AssetFactory:
    # The purpose of this function is to return a list of animations ready to be used with the GameObject class.
    # 1 - Knight
    # 2 - Samurai
    # 3 - Skeleton

    def __init__(self, c_atlas, b_atlas, h_atlas):
        self._c_atlas = c_atlas  # character atlas
        self._b_atlas = b_atlas  # background atlas
        self._h_atlas = h_atlas  # status bar atlas

    def get_asset(self, asset_id):  # returns the respective animation from the respective atlas
        match asset_id:
            case 1:
                knight_idle = AnimatedSprite(self._c_atlas, True, pygame.Rect(0, 0, 256, 256), AnimationType.LOOP, 100,
                                             4)
                knight_attack = AnimatedSprite(self._c_atlas, True, pygame.Rect(1280, 0, 256, 256),
                                               AnimationType.ONE_TIME, 60, 5)
                knight_damage = AnimatedSprite(self._c_atlas, True, pygame.Rect(256, 256, 256, 256),
                                               AnimationType.ONE_TIME, 200, 2)
                knight_dead = AnimatedSprite(self._c_atlas, True, pygame.Rect(2560, 0, 256, 256),
                                             AnimationType.ONE_TIME, 100, 6)
                knight_defend = AnimatedSprite(self._c_atlas, True, pygame.Rect(0, 256, 256, 256),
                                               AnimationType.ONE_TIME, 800, 1)
                return [knight_idle, knight_attack, knight_defend, knight_damage, knight_dead]

            case 2:
                samurai_idle = AnimatedSprite(self._c_atlas, True, pygame.Rect(768, 256, 256, 256), AnimationType.LOOP,
                                              200, 6)
                samurai_attack = AnimatedSprite(self._c_atlas, True, pygame.Rect(2304, 256, 256, 256),
                                                AnimationType.ONE_TIME, 100, 4)
                samurai_defend = AnimatedSprite(self._c_atlas, True, pygame.Rect(1536, 512, 256, 256),
                                                AnimationType.ONE_TIME, 300, 2)
                samurai_damage = AnimatedSprite(self._c_atlas, True, pygame.Rect(3328, 256, 256, 256),
                                                AnimationType.ONE_TIME, 300, 3)
                samurai_dead = AnimatedSprite(self._c_atlas, True, pygame.Rect(0, 512, 256, 256),
                                              AnimationType.ONE_TIME, 300, 6)
                return [samurai_idle, samurai_attack, samurai_defend, samurai_damage, samurai_dead]

            case 3:
                skeleton_idle = AnimatedSprite(self._c_atlas, True, pygame.Rect(2048, 512, 256, 256),
                                               AnimationType.LOOP, 100, 7)
                skeleton_attack = AnimatedSprite(self._c_atlas, True, pygame.Rect(0, 768, 256, 256),
                                                 AnimationType.ONE_TIME, 100, 4)
                skeleton_defend = AnimatedSprite(self._c_atlas, True, pygame.Rect(1792, 768, 256, 256),
                                                 AnimationType.ONE_TIME, 300, 2)
                skeleton_damage = AnimatedSprite(self._c_atlas, True, pygame.Rect(1280, 768, 256, 256),
                                                 AnimationType.ONE_TIME, 100, 2)
                skeleton_dead = AnimatedSprite(self._c_atlas, True, pygame.Rect(1536, 768, 256, 256),
                                               AnimationType.ONE_TIME, 200, 4)
                return [skeleton_idle, skeleton_attack, skeleton_defend, skeleton_damage, skeleton_dead]

            case 4:
                skeleton_idle = AnimatedSprite(self._c_atlas, True, pygame.Rect(0, 1024, 256, 256), AnimationType.LOOP,
                                               100, 6)
                skeleton_attack = AnimatedSprite(self._c_atlas, True, pygame.Rect(2560, 768, 256, 256),
                                                 AnimationType.ONE_TIME, 100, 6)
                skeleton_defend = AnimatedSprite(self._c_atlas, True, pygame.Rect(1536, 1024, 256, 256),
                                                 AnimationType.ONE_TIME, 200, 3)
                skeleton_damage = AnimatedSprite(self._c_atlas, True, pygame.Rect(1536, 1024, 256, 256),
                                                 AnimationType.ONE_TIME, 100, 3)
                skeleton_dead = AnimatedSprite(self._c_atlas, True, pygame.Rect(1536, 1024, 256, 256),
                                               AnimationType.ONE_TIME, 200, 7)
                return [skeleton_idle, skeleton_attack, skeleton_defend, skeleton_damage, skeleton_dead]

            case 5:
                crow_idle = AnimatedSprite(self._c_atlas, True, pygame.Rect(0, 1280, 256, 256), AnimationType.LOOP, 100,
                                           6)
                crow_attack = AnimatedSprite(self._c_atlas, True, pygame.Rect(1536, 1280, 256, 256),
                                             AnimationType.ONE_TIME, 100, 5)
                crow_defend = AnimatedSprite(self._c_atlas, True, pygame.Rect(0, 1536, 256, 256),
                                             AnimationType.ONE_TIME, 100, 3)
                crow_damage = AnimatedSprite(self._c_atlas, True, pygame.Rect(3328, 1024, 256, 256),
                                             AnimationType.ONE_TIME, 100, 3)
                crow_dead = AnimatedSprite(self._c_atlas, True, pygame.Rect(0, 1536, 256, 256), AnimationType.ONE_TIME,
                                           100, 6)
                return [crow_idle, crow_attack, crow_defend, crow_damage, crow_dead]
            case 20:
                candle_idle = AnimatedSprite(self._b_atlas, False, pygame.Rect(0, 0, 960, 94), AnimationType.LOOP, 50,
                                             8)
                return [candle_idle]
            case 21:
                flag_attack_idle = AnimatedSprite(self._h_atlas, False, pygame.Rect(220, 50, 208, 68),
                                                  AnimationType.LOOP, 60, 7)
                return [flag_attack_idle]
            case 22:
                flag_defend_idle = AnimatedSprite(self._h_atlas, False, pygame.Rect(432, 50, 208, 68),
                                                  AnimationType.LOOP, 70, 7)
                return [flag_defend_idle]
            case 23:
                flag_wait_idle = AnimatedSprite(self._h_atlas, False, pygame.Rect(640, 50, 208, 68), AnimationType.LOOP,
                                                80, 7)
                return [flag_wait_idle]
            case 24:
                random = AnimatedSprite(self._h_atlas, True, pygame.Rect(150, 0, 50, 50), AnimationType.LOOP, 80,
                                        3)  # Animation for the options for the pc when attacking/defending
                return [random]
