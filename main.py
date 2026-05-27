"""
Module for initializing and displaying text on an LCD display.

This module interacts with the `LcdDisplayClass` from `display_class` to
control the LCD display and show text-based content. The functionality includes
handling the setup of an LCD screen and rendering the desired text onto the
screen.
"""

import display_class

display = display_class.LcdDisplayClass()
display.display_text("Hello World")
