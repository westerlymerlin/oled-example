"""
Module for initialising and displaying text on an OLED display.

This module interacts with the `LcdDisplayClass` from `display_class` to
control the OLED display and show text-based content. The functionality includes
handling the setup of an LCD screen and rendering the desired text onto the
screen.
"""

import display_class

display = display_class.LcdDisplayClass()
display.display_text("Hello World")
