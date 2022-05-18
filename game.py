from turtle import screensize
import pygame
from characters.Player.player import Player
from Data.Map.map import MapManager



class Game:

    def __init__(self, screen):
        self.is_playing = False
        # creation de la fenetre du jeu
        self.screen = screen

        # generer un joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)

        self.pressed = {}

    def start(self):
        self.is_playing = True

    def game_over(self):
        # remettre le jeu a neuf, retirer les mponstre remmetre le joueur a 100 point de vie , jeu en attente
        self.player.current_health = self.player.max_health
        self.is_playing = False

    def move(self):
        if self.pressed.get(pygame.K_ESCAPE):
            self.is_playing = False
        if self.pressed.get(pygame.K_RIGHT):
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT):
            self.player.move_left()
        if self.pressed.get(pygame.K_UP):
            self.player.to_jump = True
            self.player.number_jump += 1
        if self.pressed.get(pygame.K_RIGHT) and self.pressed.get(pygame.K_LSHIFT):
            self.player.run_right()
        if self.pressed.get(pygame.K_LEFT) and self.pressed.get(pygame.K_LSHIFT):
            self.player.run_left()
        if self.pressed.get(pygame.K_SPACE):
            self.player.sprite.status = "attack"
            self.player.sprite.animation_speed = 0.23
        if self.pressed.get(pygame.K_LCTRL):
            self.player.launch_projectile()

    def update(self):
        self.map_manager.update()
        self.player.sprite.save_location()
        self.move()
        self.map_manager.draw()
        self.player.sprite.animate()
        self.player.update_health_bar(self.screen)






