"""
Manages a 0.96 inch 128 x 64 pixel Oled display and provides functionalities for
rendering text, images, and visual effects.

This module is responsible for controlling and displaying content on an SSD1306
OLED display using the Adafruit and PIL libraries. Functionalities provided by
the module include displaying text, clearing the display, rendering full display
representations, and managing dynamic visual effects. The module uses I2C communication
to interact with the OLED display.
"""

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import board

class LcdDisplayClass:
    """
    Manages and controls a 0.96 inch 128 x 64 pixel Oled display.

    This class is designed to manage the rendering and updating of content on an
    Oled display device. It provides functionalities to display text, show images,
    handle network information display, as well as create alternate visual effects
    like white noise and switching between visuals. The class also allows starting
    a dynamic display loop.
    """
    def __init__(self):
        self.led_display = None
        self.width = 128
        self.height = 64
        self.i2c_address = 0x3C
        self.image = Image.new('1', (self.width, self.height), color=0)
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default(11)
        try:
            i2c = board.I2C()
            output = i2c.scan()
            print(output)
            if len(output) > 0:
                if self.i2c_address in output:
                    print('display i2c device found')
                    self.led_display = adafruit_ssd1306.SSD1306_I2C(self.width, self.height, i2c,
                                                                    addr=self.i2c_address)
        except ValueError:
            print('Display not found')
        except NameError:
            print('Board library not loaded - I2C Device not available')

    def display_text(self, text_message: str):
        """
        Displays the current text on an image using the specified font and renders it
        on the screen.

        The method uses the coordinates (0, 0) as the starting point for rendering
        the text. It applies the provided font and a fill colour value of 255. After
        drawing the text, it invokes the `show_image` method to display the image.
        """
        self.draw.text((0, 0), text_message, font=self.font, fill=255)
        self.show_image()

    def show_image(self):
        """
        Displays an image on the LED display.

        This method sets the provided image to the LED display and triggers the display
        """
        self.led_display.image(self.image)
        self.led_display.show()

    def full_display(self):
        """
        Creates a full display representation, initialises a new image object, and
        renders it on the display.

        This method sets up an image of lit pixels with dimensions defined in the `settings`
        dictionary (`display_width` and `display_height`) and initialises a drawing
        context. Finally, it renders the created image as output.
        """
        self.image = Image.new('1', (self.width, self.height), color=255)
        self.draw = ImageDraw.Draw(self.image)
        self.show_image()

    def clear_display(self):
        """
        Clears the display by creating a new blank image and drawing object, and then shows
        the cleared image on the display.
        """
        self.image = Image.new('1', (self.width, self.height), color=0)
        self.draw = ImageDraw.Draw(self.image)
        self.show_image()
