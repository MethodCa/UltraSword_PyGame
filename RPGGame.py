from pygame import Rect
from GameObject import GameObject
from AssetFactory import AssetFactory
from Enum import Animation
from Enum import GameState
from File import FileManager
import pygame as pygame
import random
import pygame.freetype


class RPGGame:
    # System
    _screen: pygame.surface  # declare variable to store the access to the screen
    # External Assets
    _s_atlas: pygame.surface  # declare variable to store the screen atlas
    _c_atlas: pygame.surface  # declare variable to store the character atlas
    _b_atlas: pygame.surface  # declare variable to store the background atlas
    _h_atlas: pygame.surface  # declare variable to store the hud atlas
    _help_screen: pygame.surface  # declare variable to store the help screen
    _font: pygame.freetype.Font  # declare variable to store the font
    _font_small: pygame.freetype.Font  # declare variable to store the font
    _file = FileManager  # declare variable to store the access to the FileManager class
    # Game logic
    _game_state = None  # declare variable to store the game state
    _round = 0  # declare variable to store the round number
    _character = True  # declare variable to control the character
    _wait_time = 0  # declare variable to store the wait time
    _change_enemy = False  # declare variable to control the change of enemy
    _score: int = 0  # declare variable to store the score
    _battle_result: bool  # declare variable to store the battle result
    _use_potion = False  # declare variable to control the use of potions
    _potions = 0  # declare variable to store the number of potions available
    # Animated GameObjects
    _hero: [GameObject]  # declare variable to store the gameObject hero
    _foe: [GameObject]  # declare variable to store the gameObject foe
    _enemies: []  # declare array to store the enemies
    _warriors: []  # declare array to store the heroes
    _candles = GameObject  # declare gameObject to store the candles gameObjects
    _flag_attack: GameObject  # declare gameObject to store the attack flag gameObject
    _flag_defend: GameObject  # declare gameObject to store the defend flag gameObject
    _flag_wait: GameObject  # declare gameObject to store the wait flag gameObject
    _random: GameObject  # declare gameObject to store the random choice for the pc gameObject
    # Sprites    
    _cursor: tuple  # tuple to store the cursor position
    # Text
    _announcer_text: tuple  # tuple to store the announcement text
    _hiscore_text: tuple  # tuple to store the high score text
    _hiscore_table: tuple  # tuple to store the high score table text
    _name = ''  # name of the player to register in the high score table
    _potions_text: tuple  # tuple to store the text
    # input
    _mouse_pos: pygame.Rect  # declare collider for the mouse
    # Colliders
    _rock_collider: pygame.Rect  # declare collider for the rock
    _paper_collider: pygame.Rect  # declare collider for the paper
    _scissor_collider: pygame.Rect  # declare collider for the scissors
    _potion_collider: pygame.Rect  # declare collider for the potions
    # Animation logic
    _arrived = False  # declare variable to control if the attacker is in the attack position
    _move_hero = False  # declare variable to control if the hero has to move
    _move_foe = False  # declare variable to control if the foe has to move

    #########
    # SFX
    _sword_slash: pygame.mixer.Sound  # declare variable to store SFX sound
    _sword_clash: pygame.mixer.Sound  # declare variable to store SFX sound
    _hud_select1: pygame.mixer.Sound  # declare variable to store SFX sound
    _hud_select2: pygame.mixer.Sound  # declare variable to store SFX sound
    _hud_select3: pygame.mixer.Sound  # declare variable to store SFX sound
    _hud_hover: pygame.mixer.Sound  # declare variable to store SFX sound
    _hero_damage: pygame.mixer.Sound  # declare variable to store SFX sound
    _hero_death: pygame.mixer.Sound  # declare variable to store SFX sound
    _foe_damage: pygame.mixer.Sound  # declare variable to store SFX sound
    _foe_death: pygame.mixer.Sound  # declare variable to store SFX sound
    _take_potion: pygame.mixer.Sound  # declare variable to store SFX sound
    _current_sfx_play = -1  # declare variable to control what SFX should be played
    # announcer SFX
    _current_sfx_announcer = 0  # declare variable to control what SFX should be played by the announcer
    _announcer_select_hero: pygame.mixer.Sound  # declare variable to store SFX sound
    _announcer_attack: pygame.mixer.Sound  # declare variable to store SFX sound
    _announcer_defend: pygame.mixer.Sound  # declare variable to store SFX sound
    _announcer_gameover: pygame.mixer.Sound  # declare variable to store SFX sound

    def __init__(self):
        self._screen = pygame.display.set_mode((960, 540), 0, 0, 0, 1)
        pygame.display.set_caption("Ultrasword - The RPG Game")
        self._file = FileManager("Data/Scores.txt")
        self._game_state = GameState.START
        pygame.mouse.set_visible(False)

    @property
    def game_state(self):
        return self._game_state

    @game_state.setter
    def game_state(self, new_state):
        self._game_state = new_state

    def load_content(self):
        self._s_atlas = pygame.image.load('Assets/screen_atlas.png').convert_alpha()
        self._c_atlas = pygame.image.load('Assets/character_atlas.png').convert_alpha()
        self._b_atlas = pygame.image.load('Assets/background_atlas.png').convert_alpha()
        self._h_atlas = pygame.image.load('Assets/hud_atlas.png').convert_alpha()
        self._help_screen = pygame.image.load('Assets/help.png').convert_alpha()
        self._font = pygame.freetype.Font('Assets/fonts/Alkhemikal.ttf', 35)
        self._font_small = pygame.freetype.Font('Assets/fonts/Alkhemikal.ttf', 25)
        icon = pygame.image.load('Assets/icon.png')
        pygame.display.set_icon(icon)
        # music and SFX
        self._sword_slash = pygame.mixer.Sound('Assets/music/sword_slash.wav')
        self._sword_clash = pygame.mixer.Sound('Assets/music/sword_clash.wav')
        self._hud_select1 = pygame.mixer.Sound('Assets/music/select1.wav')
        self._hud_select2 = pygame.mixer.Sound('Assets/music/select2.wav')
        self._hud_select3 = pygame.mixer.Sound('Assets/music/select3.wav')
        self._hud_hover = pygame.mixer.Sound('Assets/music/option.wav')
        self._hero_damage = pygame.mixer.Sound('Assets/music/hero_damage.wav')
        self._hero_death = pygame.mixer.Sound('Assets/music/hero_death.wav')
        self._foe_damage = pygame.mixer.Sound('Assets/music/foe_damage.wav')
        self._foe_death = pygame.mixer.Sound('Assets/music/foe_death.wav')
        self._take_potion = pygame.mixer.Sound('Assets/music/potion.wav')
        self._announcer_select_hero = pygame.mixer.Sound('Assets/music/announcer_select_hero.wav')
        self._announcer_attack = pygame.mixer.Sound('Assets/music/announcer_attack.wav')
        self._announcer_defend = pygame.mixer.Sound('Assets/music/announcer_defend.wav')
        self._announcer_gameover = pygame.mixer.Sound('Assets/music/announcer_gameover.wav')
        self._sword_clash.set_volume(0.2)
        self._sword_slash.set_volume(0.3)
        self._hud_select1.set_volume(0.3)
        self._hud_select2.set_volume(0.3)
        self._hud_select3.set_volume(0.3)
        self._hud_hover.set_volume(0.3)
        self._hero_death.set_volume(1)
        self._hero_damage.set_volume(0.9)
        self._foe_death.set_volume(0.9)
        self._foe_damage.set_volume(0.7)
        pygame.mixer_music.load('Assets/music/main_theme.wav')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(loops=-1)

    def initialize(self):
        pygame.init()
        # Load all external Assets
        self.load_content()
        # Initialize game state
        self._game_state = GameState.START
        # cursor
        self._cursor = self._h_atlas, (0, 0), pygame.Rect(558, 0, 28, 28)
        # Asset creation
        factory = AssetFactory(self._c_atlas, self._b_atlas, self._h_atlas)
        # Characters
        samurai = GameObject(pygame.Vector2(200, 120), factory.get_asset(2), 500, 5000, 75)
        knight = GameObject(pygame.Vector2(200, 120), factory.get_asset(1), 500, 2500, 100)
        # Enemies
        skeleton = GameObject(pygame.Vector2(500, 120), factory.get_asset(3), 500, 6000, 75)
        skeleton2 = GameObject(pygame.Vector2(500, 120), factory.get_asset(4), 600, 4000, 80)
        crow = GameObject(pygame.Vector2(500, 120), factory.get_asset(5), 700, 2000, 100)
        self._enemies = [skeleton, skeleton2, crow]
        self._warriors = [samurai, knight]
        self._hero = samurai
        self._foe = skeleton
        # BG
        self._candles = GameObject(pygame.Vector2(0, 134), factory.get_asset(20), 0, 0, 0)
        # HUD // status bar
        self._flag_attack = GameObject(pygame.Vector2(50, 100), factory.get_asset(21), 0, 0, 0)
        self._flag_defend = GameObject(pygame.Vector2(50, 100), factory.get_asset(22), 0, 0, 0)
        self._flag_wait = GameObject(pygame.Vector2(50, 100), factory.get_asset(23), 0, 0, 0)
        self._random = GameObject(pygame.Vector2(786, 252), factory.get_asset(24), 0, 0, 0)
        # colliders
        self._rock_collider = pygame.Rect(71, 254, 50, 50)
        self._paper_collider = pygame.Rect(117, 254, 50, 50)
        self._scissor_collider = pygame.Rect(163, 254, 50, 50)
        self._potion_collider = pygame.Rect(35, 350, 24, 24)
        # Texts
        self._announcer_text = self._font.render("Wait until is time to take action!", (255, 255, 255))
        self._hiscore_text = self._font.render("", (255, 255, 255))
        self._hiscore_table = self._font.render("", (255, 255, 255))
        self._potions_text = self._font_small.render("", (255, 255, 255))
        self._character = True

    def update(self, delta_time):

        keys = pygame.key.get_pressed()  # if the escape key is pressed the game is ended.
        if keys[pygame.K_ESCAPE]:
            global playing
            playing = False

        match self._game_state:
            case GameState.START:  # the start screen will give them option to load the hiscore table or to select
                # the character
                if not self._wait_time > 0:  # wait time controls how often the inputs are received.
                    if keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
                        self._game_state = GameState.CHARACTER_SELECT
                        self._wait_time = 10
                    if pygame.MOUSEBUTTONUP:
                        clic = pygame.mouse.get_pressed(num_buttons=3)
                        if clic[0]:
                            self._game_state = GameState.CHARACTER_SELECT
                            self._wait_time = 10
                            self._announcer_select_hero.play()
                        if clic[2]:
                            self._game_state = GameState.HISCORE
                            self._wait_time = 10

            case GameState.HISCORE:  # at the hiscore table the user can return to the start screen if the left click
                # is pressed
                if not self._wait_time > 0:
                    if pygame.MOUSEBUTTONUP:
                        clic = pygame.mouse.get_pressed(num_buttons=3)
                        if clic[2]:
                            self._game_state = GameState.START
                            self._wait_time = 10

            case GameState.CHARACTER_SELECT:  # when the user clicks on a character, the battle screen is load.
                if not self._wait_time > 0:
                    if pygame.MOUSEBUTTONUP:
                        clic = pygame.mouse.get_pressed(num_buttons=3)
                        pos = pygame.mouse.get_pos()
                        if clic[2]:
                            self._game_state = GameState.START
                            self._wait_time = 10
                        if pos[0] > 30 and pos[0] < 455 and pos[1] > 135 and pos[1] < 430:
                            self._character = True
                            self._hero = self._warriors[0]
                            self._potions = 2
                            if not self._current_sfx_play == 5:
                                self._hud_hover.play()
                                self._current_sfx_play = 5
                            if clic[0]:
                                self._game_state = GameState.BATTLE
                                self._wait_time = 20
                                self._hud_select1.play()
                                pygame.mixer_music.load('Assets/music/battle.wav')
                                pygame.mixer_music.set_volume(0.5)
                                pygame.mixer_music.play(loops=-1)
                        elif pos[0] > 495 and pos[0] < 920 and pos[1] > 135 and pos[1] < 430:
                            self._character = False
                            self._hero = self._warriors[1]
                            self._potions = 1
                            if not self._current_sfx_play == 6:
                                self._hud_hover.play()
                                self._current_sfx_play = 6
                            if clic[0]:
                                self._game_state = GameState.BATTLE
                                self._wait_time = 10
                                self._hud_select2.play()
                                pygame.mixer_music.load('Assets/music/battle.wav')
                                pygame.mixer_music.set_volume(0.5)
                                pygame.mixer_music.play(loops=-1)

            case GameState.BATTLE:  # if h key is press the help screen will be displayed, and the game will be paused.
                keys = pygame.key.get_pressed()
                if keys[pygame.K_h]:
                    self._game_state = GameState.HELP_S

                    # battle is when the game starts and the user choose options to fight the foe
                if self._wait_time <= 0:
                    if self._hero.stamina >= self._hero.max_stamina or self._foe.stamina >= self._foe.max_stamina:
                        self._foe.choice = cpu_random_choice()  # if the stamina bar is full the foe will fight the hero
                        if self._hero.stamina >= self._hero.max_stamina:
                            if self._current_sfx_announcer == 0:
                                self._announcer_attack.play()
                                self._current_sfx_announcer = 1
                            self._announcer_text = self._font.render("Time to attack!, choose wisely!", (
                                255, 255, 255))  # messages are display to indicate that is time to attack or deffend
                        else:
                            if self._current_sfx_announcer == 0:
                                self._announcer_defend.play()
                                self._current_sfx_announcer = 2
                            self._announcer_text = self._font.render("Time to defend yourself!, choose wisely!",
                                                                     (255, 255, 255))
                        self._hero.choice = self.mouse_events(0)
                        if not self._hero.choice == 0:
                            if self._hero.stamina >= self._hero.max_stamina:
                                attacker, defender = self._hero, self._foe  # copy objects to re use code weather the player or foe is attacking
                                self._move_hero = True  # if it's time to attack the hero will move
                            else:
                                attacker, defender = self._foe, self._hero
                                self._move_foe = True  # if it's time to defend the foe will move
                            self._battle_result = battle(attacker.choice,
                                                         defender.choice)  # calculates if points have to be discounted for the respective attacker

                            if self._battle_result:
                                self._sword_slash.play()  # Play SFX
                                defender.health = defender.health - attacker.strength  # reduces health points if the attacked was not blocked
                                attacker.play_animation(Animation.ATTACK)  # play the attack animation
                                if defender.health <= 0:
                                    defender.play_animation(Animation.DEAD)
                                else:
                                    defender.play_animation(Animation.DAMAGE)
                            else:
                                self._sword_clash.play()  # play SFX
                                defender.play_animation(Animation.DEFEND)
                                attacker.play_animation(Animation.ATTACK)

                            if self._hero.stamina >= self._hero.max_stamina:  # evaluates if the hero has attacked
                                if self._battle_result:  # display message
                                    self._foe_damage.play()
                                    self._announcer_text = self._font.render(
                                        f"The attack has reduced the enemy's health by  {self._hero.strength}",
                                        (255, 255, 255))
                                    self._score = self._score + 10
                                    self._wait_time = 150
                                else:  # evaluates if the foe has attacked
                                    self._announcer_text = self._font.render(
                                        "The attack has been blocked by the enemy!", (255, 255, 255))
                                    self._wait_time = 150
                                self._foe.health = defender.health  # assign values to the original object
                                self._hero.stamina = 0  # restart stamina to wait for its turn
                            else:
                                if self._battle_result:
                                    self._hero_damage.play()  # play SFX
                                    self._announcer_text = self._font.render(
                                        f"The attack has reduced the Hero's health by {self._foe.strength} points",
                                        (255, 255, 255))
                                    self._wait_time = 150
                                else:  # display message
                                    self._announcer_text = self._font.render(
                                        "The attack has been blocked by the Hero!", (255, 255, 255))
                                    self._wait_time = 150
                                self._hero.health = defender.health  # assign values to the original object
                                self._foe.stamina = 0  # restart stamina to wait for its turn

                            if self._hero.health <= 0:
                                self._hero_death.play()  # play SFX
                                self._wait_time = 180
                                self._announcer_text = self._font.render(f"You are dead!",
                                                                         (255, 255, 255))  # display message
                            if self._foe.health <= 0:
                                self._foe_death.play()  # Play SFX
                                self._wait_time = 180
                                self._announcer_text = self._font.render(f"The enemy is dead!",
                                                                         (255, 255, 255))  # display message
                    else:
                        self._hero.stamina += delta_time  # add delta time to wait for its turn to play
                        self._foe.stamina += delta_time  # add delta time to wait for its turn to play
                        self._current_sfx_announcer = 0

                if self._wait_time <= 0:
                    if self._foe.health <= 0:
                        if self._round >= 2:  # calculates if the player fought all the enemies to end the game
                            self._game_state = GameState.GAMEOVER
                            self._announcer_gameover.play()  # Play SFX
                            pygame.mixer_music.load('Assets/music/gameover.wav')  # Change music
                            pygame.mixer_music.set_volume(0.3)  # Set attributes for the music
                            pygame.mixer_music.play(loops=-1)
                        else:
                            self._potions += 1  # calculates if the player won the round to award the prize and
                            # change the enemy
                            self._round += 1
                            self._foe = self._enemies[self._round]
                            self._announcer_text = self._font.render("A new foe has appeared! do your best hero!",
                                                                     (255, 255, 255))
                    if self._hero.health <= 0:
                        self._game_state = GameState.GAMEOVER  # if the player has no health means that lost the game
                        self._announcer_gameover.play()  # Play SFX
                        pygame.mixer_music.load('Assets/music/gameover.wav')  # Change music
                        pygame.mixer_music.set_volume(0.3)  # Set attributes for the music
                        pygame.mixer_music.play(loops=-1)

                if self._move_hero:  # invokes to move the character or foe
                    self.move_hero(delta_time)
                if self._move_foe:
                    self.move_foe(delta_time)

                # BG elements updates animations for background, characters and other visual assist.
                self._candles.__update__(delta_time)
                # Character elements
                self._hero.__update__(delta_time)
                self._foe.__update__(delta_time)
                # HUD elements
                self._flag_attack.__update__(delta_time)
                self._flag_defend.__update__(delta_time)
                self._flag_wait.__update__(delta_time)
                self._random.__update__(delta_time)

            case self._game_state.HELP_S:
                if not self._wait_time > 0:
                    if pygame.MOUSEBUTTONUP:
                        clic = pygame.mouse.get_pressed(num_buttons=3)
                        if clic[2]:
                            self._game_state = GameState.BATTLE
                            self._wait_time = 10

            case self._game_state.GAMEOVER:
                keys = pygame.key.get_pressed()  # detects keys pressed to get the initials
                if (keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]) and not self._name == '':
                    self._file.add_new_score(f"{self._name}" + " " + f"{self._score}")  # add new score to the text file
                    self._game_state = GameState.HISCORE  # after the initials are entered, the high score table will be displayed
                    self._name = ''  # re start status for all game objects for a new game
                    self._hero.health = self._hero.max_health
                    self._hero.current_animation = Animation.IDLE
                    self._hero.stamina = 0
                    self._announcer_text = self._font.render("Wait until is time to take action!", (255, 255, 255))
                    pygame.mixer_music.load('Assets/music/main_theme.wav')  # Load main theme music
                    pygame.mixer_music.set_volume(0.3)
                    pygame.mixer_music.play(loops=-1)
                    for enemy in self._enemies:  # reset values for enemies
                        enemy.health = enemy.max_health
                        enemy.current_animation = Animation.IDLE
                        enemy.stamina = 0
                    self._round = 0
                    self._score = 0
                    self._foe = self._enemies[self._round]  # assigns the enemy based on the current round

        if self._wait_time > 0:
            self._wait_time -= 1  # reduce the wait time by one
        # Update mouse position for collision calculations
        self._mouse_pos = pygame.Rect(*pygame.mouse.get_pos(), 1,
                                      1)  # update collider of the mouse to detect collisions

    def draw(self):
        match self._game_state:
            case GameState.START:
                self._screen.blit(self._s_atlas, (0, 0), pygame.Rect(0, 1084, 960, 540))  # draws background

            case GameState.CHARACTER_SELECT:
                if self._character:
                    self._screen.blit(self._s_atlas, (0, 0),
                                      pygame.Rect(0, 0, 960, 540))  # draws background with Samurai character selected
                else:
                    self._screen.blit(self._s_atlas, (0, 0),
                                      pygame.Rect(962, 0, 960, 540))  # draws background with Knight character selected

            case GameState.HISCORE:
                scores_table_read = self._file.read_file_hiscore()  # draws table score
                self._screen.blit(self._s_atlas, (0, 0),
                                  pygame.Rect(0, 542, 960, 540))  # draws background for hiscore screen
                print_x = 380  # position  where the text is going to be drawn in x
                print_y = 160  # position  where the text is going to be drawn in y
                counter = 0  # int counter to control the while loop
                while counter < len(scores_table_read):
                    self._hiscore_table = self._font.render(f'{scores_table_read[counter][0]}', (0, 255, 0))
                    self._screen.blit(self._hiscore_table[0], (print_x, print_y))
                    self._hiscore_table = self._font.render(f'{scores_table_read[counter][1]}', (0, 255, 0))
                    self._screen.blit(self._hiscore_table[0], (print_x + 150, print_y))
                    counter = counter + 1
                    print_y = print_y + 50

            case GameState.BATTLE:
                # BG elements
                self._screen.blit(self._b_atlas, (0, 0),
                                  pygame.Rect(1000, 0, 960, 540))  # draws background for battle screen
                self._candles.__draw__(self._screen)  # candles animation per frame
                # Help
                self._help = self._font_small.render(f"Press H to see how to play.", (255, 255, 153))
                self._screen.blit(self._help[0], (45, 515))
                # HUD elements
                self.draw_hud()  # draws visual background items
                self._screen.blit(self._h_atlas, (0, 415),
                                  pygame.Rect(0, 526, 958, 102))  # draws announcements section #435
                self._screen.blit(self._announcer_text[0], (45, 440))  # 460
                self._hiscore_text = self._font.render(f"Score: {self._score}", (255, 255, 255))
                self._screen.blit(self._hiscore_text[0], (765, 20))

                if self._arrived:  # calculates if the attacker got to the attack position
                    if self._battle_result:
                        pygame.draw.rect(self._screen, (100, 0, 10), pygame.Rect(0, 0, 960, 540))
                    else:
                        pygame.draw.rect(self._screen, (92, 93, 113), pygame.Rect(0, 0, 960, 540))
                if self._use_potion:  # draws when the potion is use by the player
                    pygame.draw.rect(self._screen, (85, 255, 0), pygame.Rect(0, 0, 960, 540))
                    self._use_potion = False

                # draws characters
                self._hero.__draw__(self._screen)
                self._foe.__draw__(self._screen)

            case GameState.HELP_S:
                self._screen.blit(self._help_screen, (0, 0),
                                  pygame.Rect(0, 0, 960, 540))  # draws background for help screen

            case GameState.GAMEOVER:
                self._name = self._name.upper()  # display the name in upper case
                self._screen.blit(self._s_atlas, (0, 0), pygame.Rect(962, 542, 960, 540))  # draws high score background
                self._hiscore_text = self._font.render(f'Score : {self._score}', (0, 255, 0))
                self._screen.blit(self._hiscore_text[0], (380, 250))
                self._hiscore_text = self._font.render(f'{self._name}', (0, 255, 0))
                self._screen.blit(self._hiscore_text[0], (550, 430))

        # Cursor
        if not self._game_state == GameState.HELP_S:
            self.mouse_events(1)  # draw any mouse-over interaction
        self._screen.blit(self._cursor[0], pygame.mouse.get_pos(), self._cursor[2])  # draws the mouse cursor as a sword

    def draw_bar(self, pos, size, border_c, bar_c, progress, bar_type):
        inner_pos = (pos.x + 2, pos.y + 2)  # draws the type of bar with the color and the position received.
        inner_size = ((size[0] - 4) * progress, size[1] - 4)
        pygame.draw.rect(self._screen, border_c, (*pos, *size), 2)
        pygame.draw.rect(self._screen, bar_c, (*inner_pos, *inner_size))
        if bar_type:
            self._screen.blit(self._h_atlas, (pos.x - 25, pos.y - 5), pygame.Rect(438, 0, 24, 24))  # health icon
        else:
            self._screen.blit(self._h_atlas, (pos.x - 25, pos.y - 5), pygame.Rect(462, 0, 24, 24))  # stamina icon

    def draw_hud(self):
        flag_pole_sprite_rect: Rect = pygame.Rect(846, 54, 14, 170)
        scroll_hero_active_rect: Rect = pygame.Rect(0, 458, 208, 68)
        scroll_hero_disabled_rect: Rect = pygame.Rect(0, 390, 208, 68)
        scroll_hero_empty_rect: Rect = pygame.Rect(0, 254, 208, 68)
        scroll_foe_rect: Rect = pygame.Rect(2, 324, 72, 64)

        self._screen.blit(self._h_atlas, (38, 100), flag_pole_sprite_rect)  # draw flag pole sprite
        flag_sprite = self._flag_defend
        scroll_rect = scroll_hero_active_rect

        if self._hero.stamina >= self._hero.max_stamina:
            flag_sprite = self._flag_attack
            scroll_rect = scroll_hero_active_rect
        if self._hero.stamina < self._hero.max_stamina and self._foe.stamina < self._foe.max_stamina:
            flag_sprite = self._flag_wait
            scroll_rect = scroll_hero_disabled_rect

        flag_sprite.__draw__(self._screen)
        self._screen.blit(self._h_atlas, (37, 244), scroll_rect)  # hero's Scroll sprite - Attack mode
        self._screen.blit(self._h_atlas, (775, 244), scroll_foe_rect)  # foe's Scroll sprite

        if self._wait_time > 0:
            match self._foe.choice:
                case 1:
                    self._screen.blit(self._h_atlas, (786, 252), pygame.Rect(150, 0, 50, 50))
                case 2:
                    self._screen.blit(self._h_atlas, (786, 252), pygame.Rect(200, 0, 50, 50))
                case 3:
                    self._screen.blit(self._h_atlas, (786, 252), pygame.Rect(250, 0, 50, 50))

            match self._hero.choice:
                case 1:
                    self._screen.blit(self._h_atlas, (71, 254), pygame.Rect(150, 0, 50, 50))
                case 2:
                    self._screen.blit(self._h_atlas, (117, 254), pygame.Rect(200, 0, 50, 50))
                case 3:
                    self._screen.blit(self._h_atlas, (163, 254), pygame.Rect(250, 0, 50, 50))

        if self._hero.stamina >= self._hero.max_stamina or self._foe.stamina >= self._foe.max_stamina:
            self._screen.blit(self._h_atlas, (775, 244), scroll_foe_rect)
            self._random.__draw__(self._screen)

        # Hero bars
        self.draw_bar(pygame.Vector2(60, 315), (180, 12), (0, 0, 0), (40, 80, 150),
                      self._hero.stamina / self._hero.max_stamina, False)  # health Bar
        self.draw_bar(pygame.Vector2(60, 333), (180, 12), (0, 0, 0), (100, 0, 10),
                      self._hero.health / self._hero.max_health, True)  # stamina Bar
        # Foe bars
        self.draw_bar(pygame.Vector2(725, 315), (180, 12), (0, 0, 0), (40, 80, 150),
                      self._foe.stamina / self._foe.max_stamina, False)  # health Bar
        self.draw_bar(pygame.Vector2(725, 333), (180, 12), (0, 0, 0), (100, 0, 10),
                      self._foe.health / self._foe.max_health, True)  # stamina Bar

        # potions
        self._screen.blit(self._h_atlas, (35, 350), pygame.Rect(486, 0, 24, 24))
        self._potions_text = self._font_small.render(f" x {self._potions}", (255, 255, 255))
        self._screen.blit(self._potions_text[0], (55, 353))

    def move_hero(self, delta_time):
        if self._hero.position[0] < 400 and not self._arrived:  # calculates if the player character has gotten to
            # the attack position, if it has will return to the idle position
            self._hero.position = (self._hero.position[0] + delta_time, self._hero.position[1])
        else:
            self._arrived = True
            if self._hero.position[0] > 200:
                self._hero.position = (self._hero.position[0] - delta_time, self._hero.position[1])
            else:
                self._move_hero = False
                self._arrived = False

    def move_foe(self, delta_time):
        if self._foe.position[0] > 300 and not self._arrived:  # calculates if the foe has gotten to the attack
            # position, if it has will return to the idle position
            self._foe.position = (self._foe.position[0] - delta_time, self._foe.position[1])
        else:
            self._arrived = True
            if self._foe.position[0] < 500:
                self._foe.position = (self._foe.position[0] + delta_time, self._foe.position[1])
            else:
                self._move_foe = False
                self._arrived = False

    def mouse_events(self, mouse_event_type):
        collide_rock = pygame.Rect.colliderect(self._rock_collider,
                                               self._mouse_pos)  # detects if there have been a collision with one of the items
        collide_paper = pygame.Rect.colliderect(self._paper_collider, self._mouse_pos)
        collide_scissor = pygame.Rect.colliderect(self._scissor_collider, self._mouse_pos)
        collide_potion = pygame.Rect.colliderect(self._potion_collider, self._mouse_pos)

        if mouse_event_type == 0:
            clic = pygame.mouse.get_pressed(num_buttons=3)  # detects the clicks of the mouse
            if clic[0]:
                if collide_rock:
                    self._hud_select1.play()  # Play SFX
                    return 1
                elif collide_paper:
                    self._hud_select2.play()  # Play SFX
                    return 2
                elif collide_scissor:
                    self._hud_select3.play()  # Play SFX
                    return 3
                elif collide_potion:
                    if self._potions > 0:  # if potions available will increment health
                        self._take_potion.play()
                        self._potions -= 1
                        self._use_potion = True
                        self._wait_time = 60  # set a wait time to allow clicks
                        self._announcer_text = self._font.render(
                            "You have used a potion, your health has been restored 100 points",
                            # display message to indicate that a potion has been used.
                            (255, 255, 255))
                        if (self._hero.health + 100) <= self._hero.max_health:
                            self._hero.health += 100
                        else:
                            self._hero.health = self._hero.max_health
            else:
                return 0  # if return 0 indicated that an error occurred

        if mouse_event_type == 1:  # detects the hover of the mouse
            if self._hero.stamina >= self._hero.max_stamina or self._foe.stamina >= self._foe.max_stamina:
                if collide_rock:  # if stamina bar is full the item will be highlighted
                    if not self._current_sfx_play == 0:
                        self._hud_hover.play()
                        self._current_sfx_play = 0
                    self._screen.blit(self._h_atlas, (71, 254), pygame.Rect(150, 0, 50, 50))
                elif collide_paper:
                    if not self._current_sfx_play == 1:
                        self._hud_hover.play()
                        self._current_sfx_play = 1
                    self._screen.blit(self._h_atlas, (117, 254), pygame.Rect(200, 0, 50, 50))
                elif collide_scissor:
                    if not self._current_sfx_play == 2:
                        self._hud_hover.play()
                        self._current_sfx_play = 2
                    self._screen.blit(self._h_atlas, (163, 254), pygame.Rect(250, 0, 50, 50))
                elif collide_potion:
                    if not self._current_sfx_play == 3:
                        self._hud_hover.play()
                        self._current_sfx_play = 3
                    self._screen.blit(self._h_atlas, (35, 350), pygame.Rect(486, 24, 24, 24))
        return 0

    def handle_input(self, event):
        if event.type == pygame.TEXTINPUT:
            for char in event.text:
                if char.isalpha():  # accepts letters only
                    if len(self._name) < 5:  # caps the input to 5 letters
                        self._name += char
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self._name = self._name[:-1]


def cpu_random_choice():
    choices = [1, 2, 3]
    computer_choice = random.choice(choices)  # gets the choice
    return computer_choice


def battle(attacker, defender):
    if attacker == defender:  # if the chose option is the same to the opposite gets damage
        return True
    elif (attacker == 1 and defender == 3) or (attacker == 2 and defender == 1) or (
            attacker == 3 and defender == 2):
        return True  # paper wins over rock - scissors wins over paper - rock wins over scissors
    else:
        return False  # if false no damage is cause  to the character attacked


game = RPGGame()  # declaration local variable to access class functions
game.initialize()  # initializing game features
clock = pygame.time.Clock()  # declaration local variable to access the time
playing = True  # declaration local boolean variable to control the loop while playing

# Game loop
while playing:
    for event in pygame.event.get():  # loop for to access events during the execution of the game
        if event.type == pygame.QUIT:
            playing = False  # if the window is closed the loop will be ended
        if game.game_state == GameState.GAMEOVER:
            game.handle_input(event)  # handle input detects the pressed keys

    game.update(clock.tick(60))  # call the update function to execute the logic
    game.draw()  # call draw function to draw after the logic has been executed
    pygame.display.update()  # updates what is display on the game window

pygame.quit()  # deactivates the pygame library
