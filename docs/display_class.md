# None

<a id="display_class"></a>

# display\_class

Manages a 0.96 inch 128 x 64 pixel Oled display and provides functionalities for
rendering text, images, and visual effects.

This module is responsible for controlling and displaying content on an SSD1306
OLED display using the Adafruit and PIL libraries. Functionalities provided by
the module include displaying text, clearing the display, rendering full display
representations, and managing dynamic visual effects. The module uses I2C communication
to interact with the OLED display.

<a id="display_class.Image"></a>

## Image

<a id="display_class.ImageDraw"></a>

## ImageDraw

<a id="display_class.ImageFont"></a>

## ImageFont

<a id="display_class.adafruit_ssd1306"></a>

## adafruit\_ssd1306

<a id="display_class.board"></a>

## board

<a id="display_class.LcdDisplayClass"></a>

## LcdDisplayClass Objects

```python
class LcdDisplayClass()
```

Manages and controls a 0.96 inch 128 x 64 pixel Oled display.

This class is designed to manage the rendering and updating of content on an
Oled display device. It provides functionalities to display text, show images,
handle network information display, as well as create alternate visual effects
like white noise and switching between visuals. The class also allows starting
a dynamic display loop.

<a id="display_class.LcdDisplayClass.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="display_class.LcdDisplayClass.display_text"></a>

#### display\_text

```python
def display_text(text_message: str)
```

Displays the current text on an image using the specified font and renders it
on the screen.

The method uses the coordinates (0, 0) as the starting point for rendering
the text. It applies the provided font and a fill colour value of 255. After
drawing the text, it invokes the `show_image` method to display the image.

<a id="display_class.LcdDisplayClass.show_image"></a>

#### show\_image

```python
def show_image()
```

Displays an image on the LED display.

This method sets the provided image to the LED display and triggers the display

<a id="display_class.LcdDisplayClass.full_display"></a>

#### full\_display

```python
def full_display()
```

Creates a full display representation, initialises a new image object, and
renders it on the display.

This method sets up an image of lit pixels with dimensions defined in the `settings`
dictionary (`display_width` and `display_height`) and initialises a drawing
context. Finally, it renders the created image as output.

<a id="display_class.LcdDisplayClass.clear_display"></a>

#### clear\_display

```python
def clear_display()
```

Clears the display by creating a new blank image and drawing object, and then shows
the cleared image on the display.

