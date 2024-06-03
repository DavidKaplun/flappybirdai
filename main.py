import pygame
import neat
import time
import os
import random

WIN_WIDTH=600
WIN_HEIGHT=800

BIRDS_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))



class Bird:
    IMGS = BIRDS_IMGS
    MAX_ROTATION = 25 #how much the bird is gonna rotate when it goes up/down
    ROL_VEL = 20 #how much we gonna rotate each frame when we move the bird
    ANIMATION_TIME = 5 #how fast the bird is gonna flap its wings

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt=0#how much the image is tilted
        self.tick_count=0
        self.vel=0
        self.height = self.y
        self.img_count = 0#which image currently showing
        self.imag = self.IMGS[0]

    def jump(self):
        self.vel = - 10.5 #to go up in the screen the velocity has to be negative
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count+=1#keeps tracks of how many moves we had since the last jump
        displacement = self.vel*self.tick_count+1.5*self.tick_count**2#from the physics equation: dx = x0 + v0t + (a*t^2)/2

        if d>=16:#if we move faster than 16 pixels, set the speed to 16 pixels
            d =16

        if d<0:#fine-tunes the movement
            d -=2

        self.y +=d#apply the changes to the position of the bird

        if d<0 or self.y<self.height+50:#if the bird is moving up then tilt it upwards
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            #if it doesnt go up then it goes down so tilt down
            if self.tilt>=-90:
                self.tilt-=self.ROT_VEL

    def draw(self, win):#win represents the window that we draw the bird onto
        #to animate the bird we need to track how many times have we already shown one image
        self.img_count +=1

        #checking what image we should show based on the image count
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMG[1]
            self.img_count = self.ANIMATION_TIME*2

        #this rotates the image around the center of the bird
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x,self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
