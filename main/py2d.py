import pygame  # This is the framework that py2d is an interface for.
import object

g_update_loop = 0  #null
g_draw_loop = 0  #null

f_debug = False # This flag toggles debug statements being printed to the console

def init_py2d (size):
    """This function initializes pygame and creates a display surface.
        size : [width, height] : <int, int>"""

    global f_debug, g_display_surface

    if f_debug: print "py2d: INIT, START"

    pygame.init()  # Start pygame systems.
    g_display_surface = pygame.display.set_mode(size)  # Create the main render surface.

    if f_debug: print "py2d: INIT, END"

# fps is preset to 30
_fps = 30
def set_fps(value):
    global _fps
    _fps = value

# delta_time is the time in seconds that each loop took to run.
# Multiply this with move amounts to make sure the object moves the correct amount
# even if the fps drops.
delta_time = 0.0

# Call this to exit the game
def exit_game():
    global f_exit_game

    # Check for errors.
    try:
        if f_exit_game == True: print "py2d: ERR 0, Game has already been stopped."
    except NameError:
        print "py2d: ERR 1, Game has not been run yet."

    f_exit_game = True

# This starts the main game loop.
def run_py2d():
    global _fps, _delta_time, f_exit_game
    f_exit_game = False

    if f_debug: print "py2d: RUN, START"

    while not f_exit_game:
        time_at_frame_start = pygame.time.get_ticks()  # Get time before calulations

        handle_events()  # All events are handled here

        game_loop()  # All calulations are here.

        pygame.display.update()  # Refresh / update the screen here

        # Set the wait time (after calculations have been made) (in ms not seconds)
        wait_time = ((1 / float(_fps)) * 1000) - (pygame.time.get_ticks() - time_at_frame_start)
        pygame.time.wait(int(wait_time))  # Pause the program for the set amount of time.

        _delta_time = wait_time / 1000.0  # This updates the delta time variable. (in seconds not ms)

    if f_debug: print "py2d: RUN, END"

# How to return events
def handle_events():
    pass  # Nothing right now

g_inc = 0
# The main repeating game_loop
def game_loop():
    global g_inc

    g_inc += 1
    print str(g_inc)

    if g_inc > 150:
        exit_game()


print "py2d: READ, DONE"
