from resources import intro
from resources.chapter1 import pre_asteroid
from resources.chapter2 import pre_dream, dream
from resources.chapter2.levels import level_one, level_two, level_three, level_four, level_five


def main():
    # Title Screen and Intro
    intro.title_screen()
    intro.shooting_star()
    intro.rocket_launch()
    intro.flying_through_space_1()
    intro.flying_through_space_2()

    # Chapter 1- The Asteroid Field
    pre_asteroid.commander_convo()
    pre_asteroid.monkey_convo()
    pre_asteroid.monkey_and_commander_convo()
    # The rest of the game is ran within these functions based on outcome of conversations.
    # To skip to a section you can uncomment it below.

    # Chapter 2- The Dream
    #pre_dream.main()
    #dream.dream()
    #level_one.game()
    #level_one.scene_4()
    #level_two.scene_1()
    #level_three.main()
    #level_four.game()
    #level_five.ending()

main()
