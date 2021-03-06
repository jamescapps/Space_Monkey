import turtle
import time
from resources.chapter2.levels import level_five

stop = False


def game():
    def scene_1():
        # Set up the screen
        new_win = turtle.Screen()
        new_win.reset()
        new_win.bgcolor('black')
        new_win.title('T h e  D r e a m')
        new_win.bgpic('img/dream/dream11.gif')

        # Register the image
        new_win.register_shape('img/dream/level_one_monkey.gif')
        new_win.register_shape('img/dream/surfboard.gif')

        # Create the player
        player = turtle.Turtle()
        player.shape('img/dream/level_one_monkey.gif')
        player.penup()
        player.speed(0)
        player.setposition(-400, -250)
        player.setheading(90)
        player_speed = 2.5

        # Create the surf board
        board = turtle.Turtle()
        board.shape('img/dream/surfboard.gif')
        board.penup()
        board.speed(0)
        board.setposition(-400, -320)
        board.setheading(90)
        board_speed = 2.5

        # Floating words
        floating_words_pen = turtle.Turtle()
        floating_words_pen.speed(0)
        floating_words_pen.color('white')
        floating_words_pen.penup()
        floating_words_pen.setposition(-50, 325)

        floating_words_string = 'I  w i s h  I  h a d  m o r e'
        floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))
        floating_words_pen.hideturtle()

        # Functions
        def move_left():
            x = player.xcor()
            x -= player_speed
            player.setx(x)

            x = board.xcor()
            x -= board_speed
            board.setx(x)

        def move_right():
            x = player.xcor()
            x += player_speed
            player.setx(x)

            x = board.xcor()
            x += board_speed
            board.setx(x)

        # Key binding
        new_win.listen()
        new_win.onkeypress(move_left, 'Left')
        new_win.onkeypress(move_right, 'Right')

        # Main loop
        while True:
            player.showturtle()

            if player.xcor() > 515:
                new_win.clear()
                scene_2()

    def scene_2():
        # Set up the screen
        new_win = turtle.Screen()
        new_win.reset()
        new_win.bgcolor('black')
        new_win.title('T h e  D r e a m')
        new_win.bgpic('img/dream/dream9.gif')

        # Register the image
        new_win.register_shape('img/dream/level_one_monkey.gif')
        new_win.register_shape('img/dream/surfboard.gif')

        # Create the player
        player = turtle.Turtle()
        player.shape('img/dream/level_one_monkey.gif')
        player.penup()
        player.speed(0)
        player.setposition(-400, -250)
        player.setheading(90)
        player_speed = 2.5

        # Create the surf board
        board = turtle.Turtle()
        board.shape('img/dream/surfboard.gif')
        board.penup()
        board.speed(0)
        board.setposition(-400, -320)
        board.setheading(90)
        board_speed = 2.5

        # Floating words
        floating_words_pen = turtle.Turtle()
        floating_words_pen.speed(0)
        floating_words_pen.color('black')
        floating_words_pen.penup()
        floating_words_pen.setposition(-350, 325)

        floating_words_string = ''
        floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))
        floating_words_pen.hideturtle()

        # Functions
        def move_left():
            x = player.xcor()
            x -= player_speed
            player.setx(x)

            x = board.xcor()
            x -= board_speed
            board.setx(x)

        def move_right():
            x = player.xcor()
            x += player_speed
            player.setx(x)

            x = board.xcor()
            x += board_speed
            board.setx(x)

        # Key binding
        new_win.listen()
        new_win.onkeypress(move_left, 'Left')
        new_win.onkeypress(move_right, 'Right')

        # Main loop
        while True:
            player.showturtle()

            if -300 <= player.xcor() < 25:
                floating_words_pen.clear()
                floating_words_string = 'And again And again And again'
                floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))

            if player.xcor() >= 25:
                floating_words_pen.clear()
                floating_words_string = 'And never'
                floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))

            if player.xcor() > 515:
                new_win.clear()
                scene_3()

    def scene_3():
        # Set up the screen
        new_win = turtle.Screen()
        new_win.reset()
        new_win.bgcolor('black')
        new_win.title('T h e  D r e a m')
        new_win.bgpic('img/dream/dream10.gif')

        # Register the image
        new_win.register_shape('img/dream/level_one_monkey.gif')
        new_win.register_shape('img/dream/surfboard.gif')

        # Create the player
        player = turtle.Turtle()
        player.shape('img/dream/level_one_monkey.gif')
        player.penup()
        player.speed(0)
        player.setposition(-400, -250)
        player.setheading(90)
        player_speed = 2.5

        # Create the surf board
        board = turtle.Turtle()
        board.shape('img/dream/surfboard.gif')
        board.penup()
        board.speed(0)
        board.setposition(-400, -320)
        board.setheading(90)
        board_speed = 2.5

        # Floating words
        floating_words_pen = turtle.Turtle()
        floating_words_pen.speed(0)
        floating_words_pen.color('black')
        floating_words_pen.penup()
        floating_words_pen.setposition(-350, 250)

        floating_words_string = ''
        floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))
        floating_words_pen.hideturtle()

        # Functions
        def move_left():
            x = player.xcor()
            x -= player_speed
            player.setx(x)

            x = board.xcor()
            x -= board_speed
            board.setx(x)

        def move_right():
            x = player.xcor()
            x += player_speed
            player.setx(x)

            x = board.xcor()
            x += board_speed
            board.setx(x)

        # Key binding
        new_win.listen()
        new_win.onkeypress(move_left, 'Left')
        new_win.onkeypress(move_right, 'Right')

        # Main loop
        while True:
            player.showturtle()

            if -300 <= player.xcor() < 25:
                floating_words_pen.clear()
                floating_words_string = 'We only have'
                floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))

            if player.xcor() >= 25:
                floating_words_pen.clear()
                floating_words_string = 'But we never really have it'
                floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))

            if player.xcor() > 515:
                new_win.clear()
                second_round()

    def second_round():

        # Set up the screen
        new_win = turtle.Screen()
        new_win.reset()
        new_win.bgcolor('black')
        new_win.title('T h e  D r e a m')
        new_win.bgpic('img/dream/zeb.gif')

        # Register the image
        new_win.register_shape('img/dream/level_one_monkey.gif')
        new_win.register_shape('img/dream/surfboard.gif')

        # Create the player
        player = turtle.Turtle()
        player.shape('img/dream/level_one_monkey.gif')
        player.penup()
        player.speed(0)
        player.setposition(-400, -250)
        player.setheading(90)
        player_speed = 2.5

        # Create the surf board
        board = turtle.Turtle()
        board.shape('img/dream/surfboard.gif')
        board.penup()
        board.speed(0)
        board.setposition(-400, -320)
        board.setheading(90)
        board_speed = 2.5

        # Floating words
        floating_words_pen = turtle.Turtle()
        floating_words_pen.speed(0)
        floating_words_pen.color('white')
        floating_words_pen.penup()
        floating_words_pen.setposition(-50, 300)

        floating_words_string = ''
        floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))
        floating_words_pen.hideturtle()

        # Functions
        def move_left():
            x = player.xcor()
            x -= player_speed
            player.setx(x)

            x = board.xcor()
            x -= board_speed
            board.setx(x)

        def move_right():
            global stop
            if not stop:
                x = player.xcor()
                x += player_speed
                player.setx(x)

                x = board.xcor()
                x += board_speed
                board.setx(x)

            if player.xcor() == 2.5:
                stop = True

        # Key binding
        new_win.listen()
        new_win.onkeypress(move_left, 'Left')
        new_win.onkeypress(move_right, 'Right')

        # Main loop
        while True:
            player.showturtle()

            if player.xcor() == 2.5:
                while True:
                    floating_words_pen.clear()
                    floating_words_string = 'S t o p'
                    floating_words_pen.write(floating_words_string, False, align='left',
                                             font=('Monospace', 20, 'normal'))

                    time.sleep(5)
                    floating_words_pen.clear()
                    floating_words_pen.setposition(10, 300)
                    floating_words_string = 'W h e n  a r e  y o u ?'
                    floating_words_pen.write(floating_words_string, False, align='center',
                                             font=('Monospace', 20, 'normal'))

                    time.sleep(5)
                    floating_words_pen.clear()
                    floating_words_string = 'S o m e t i m e s  y o u  k n o w'
                    floating_words_pen.write(floating_words_string, False, align='center',
                                             font=('Monospace', 20, 'normal'))

                    time.sleep(5)
                    floating_words_pen.clear()
                    floating_words_string = 'b u t  y o u  a l w a y s  d o.'
                    floating_words_pen.write(floating_words_string, False, align='center',
                                             font=('Monospace', 20, 'normal'))

                    time.sleep(5)
                    floating_words_pen.clear()
                    floating_words_pen.setposition(10, 300)
                    floating_words_string = 'S o  t e l l  m e .'
                    floating_words_pen.write(floating_words_string, False, align='center',
                                             font=('Monospace', 20, 'normal'))

                    answer = new_win.textinput('So tell me', 'When are you?: ')

                    if answer.lower() in ('now', 'then', 'never', 'again', 'time', 'always'):
                        new_win.clear()
                        level_five.main()

                    else:
                        # Return to beginning
                        global stop
                        stop = False
                        scene_1()

    scene_1()
