import pygame
from resources.resuable_functions import update_and_flip, dialogue, good_luck
from resources.chapter2 import dream
from resources.chapter2.Choices import pre_dream_choices_3


def have_a_chat():
    # Commander
    update_and_flip()
    dialogue(' What\'s on your mind?                  ', 490, 100, 15)
    dialogue('                                        ', 490, 150, 15)
    dialogue('                                        ', 490, 200, 15)
    dialogue('                                        ', 490, 250, 15)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) What should I expect during hibernation? ', 243, 600, 15)
        dialogue(' (2) Get personal                             ', 243, 625, 15)
        dialogue(' (3) Nothing.. I am ready...                  ', 243, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) What should I expect during hibernation? ', 248, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_3.hybernation_explanation()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Get personal                             ', 248, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_3.get_personal()

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) Nothing.. I am ready...                  ', 248, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    good_luck()
                    dream.dream()


def something_nice():
    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) It has been a pleasure Commander.        ', 243, 600, 15)
        dialogue(' (2) I will miss you...                       ', 243, 625, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) It has been a pleasure Commander.        ', 248, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_3.pleasure()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) I will miss you...                       ', 248, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_3.miss_you()


def something_mean():
    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) I have never liked you.                  ', 243, 600, 15)
        dialogue(' (2) I will not miss you...                   ', 243, 625, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) I have never liked you.                  ', 248, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_3.never_liked_you()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) I will not miss you...                    ', 248, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_3.not_miss_you()
