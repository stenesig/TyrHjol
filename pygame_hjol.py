import sys
import pygame
import random
from time import time

import keyboard

# rpy stuff
"""import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)"""
flag = True

SPIN_BUTTON = "q"

NUMBER_OF_RESULTS = 14
WHEEL_PATH = "images/hjol.png"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():
    pygame.init()
    # size = [1920, 1080]
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_rect = screen.get_rect()
    pygame.display.set_caption("wheel")
    clock = pygame.time.Clock()
    image_orig = pygame.image.load(WHEEL_PATH).convert_alpha()
    image_orig = pygame.transform.scale(image_orig, (1000, 1000))
    image = image_orig.copy()
    image_rect = image_orig.get_rect(center=screen_rect.center)
    angle = 0
    done = False

    black_bar = pygame.image.load("images/arrow.png")
    black_bar = pygame.transform.scale(black_bar, (80, 80))
    black_bar = pygame.transform.rotate(black_bar, 180)
    angle = random.randint(0, 360)
    diff = random.randint(20, 40)
    diff_time = time()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if diff <= 0:
            diff = 0
            lst = [360 * (x / NUMBER_OF_RESULTS) for x in range(0, NUMBER_OF_RESULTS)]
            angle = lst[min(range(len(lst)), key=lambda i: abs(lst[i] - angle))]

        image = pygame.transform.rotate(image_orig, angle)
        image_rect = image.get_rect(center=image_rect.center)

        screen.fill(BLACK)
        screen.blit(image, image_rect)
        screen.blit(black_bar, (1460, 500))
        pygame.display.flip()
        clock.tick(60)
        angle -= diff
        angle %= 360
        if time() - diff_time > 0.5:
            diff -= 2
            diff_time = time()

        if keyboard.is_pressed(SPIN_BUTTON):  # and flag == True:
            angle = random.randint(0, 360)
            diff = random.randint(20, 40)
            diff_time = time()
            flag = False

        """if GPIO.input(10) != GPIO.HIGH:
            flag = True"""

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
