import pygame
from resuable_functions import dialogue, update_and_flip
from Choices import asteroid_choices

size = (800, 800)
screen = pygame.display.set_mode(size)
black = (0, 0, 0)
white = (255, 255, 255)

commander = pygame.image.load('img/commander.png').convert()
comms_photo = pygame.image.load('img/comms_photo.png').convert()


def commander_convo():
    while True:
        screen.blit(commander, [300, 200])
        update_and_flip()

        dialogue(' Space Monkey! Are you there?  Do you read me?... ', 400, 500, 20)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.fill(black)
                break


def monkey_convo():
    while True:
        update_and_flip()
        screen.blit(comms_photo, [300, 200])
        update_and_flip()

        dialogue(' Loud and clear Commander! ', 420, 500, 20)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.fill(black)
                break


def monkey_and_commander_convo():
    while True:
        screen.blit(comms_photo, [500, 500])
        update_and_flip()
        screen.blit(commander, [50, 40])

        # Commander
        dialogue(' You are approaching the asteroid belt?', 500, 150, 15)
        dialogue(' Do you remember the Prime Directive?', 490, 200, 15)

        # Monkey
        dialogue(' (1) No ', 243, 600, 15)
        dialogue(' (2) Yes ', 246, 625, 15)
        dialogue(' (3) More Choices ', 286, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) No ', 248, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    asteroid_choices.say_no_1()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Yes ', 242, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    asteroid_choices.say_yes_1()

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) More Choices ', 286, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    asteroid_choices.say_more_choices_1()