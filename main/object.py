import pygame  # This is the framework that py2d is an interface for.

__object_tuple = ()  # Turn this into an object_manager class pls.

class rect:
    """This is a rectangle draw object, it is automatically drawn to the screen."""

    def __init__(self, rect, colour):
        """rect : [x, y, width, height], colour : [r, g, b]"""
        self._rect = rect
        self._colour = colour

    # The double underscore makes this function private.
    def __draw (self, display_surface):
        """This function draws the rectangle when given a display surface."""
        pygame.draw.rect(display_surface, self._colour, (self._rect))


def create_rect():
    """This function creates a rectangle that is automatically drawn to the screen"""
    pass
