import pygame  # This is the framework that py2d is an interface for.

g_display_surface = 0

g_update_loop = 0  #null
g_draw_loop = 0  #null

# size == [width, height] [int, int]
def init_py2d (size):
    pygame.init()  # Start pygame systems.
    g_display_surface = pygame.display.set_mode(size)

# fps is preset to 30
_fps = 30
def set_fps(value):
    _fps = value

# _delta_time is the time in seconds that each loop took to run
_delta_time = 0.0
def get_delta_time():
    return _delta_time

# This starts the main game loop.
#g_exit_game = False
def run_py2d():
    global _fps, _delta_time

    while True:
        before_time = pygame.time.get_ticks()  # Get time before calulations

        game_loop()  # All calulations are here.

        pygame.display.update()

        wait_time = ((1 / float(_fps)) * 1000) - (pygame.time.get_ticks() - before_time)  # Set the wait time (after calculations)
        pygame.time.wait(int(wait_time))  # Pause the program for the set amount of time.

        _delta_time = wait_time / 1000.0  # This updates the delta time variable.

    x = input("dun!")

g_inc = 0
# The main repeating game_loop
def game_loop():
    global g_inc

    g_inc += 1
    print str(g_inc)
