# Module Documentation


This document contains the documentation for all the modules in this project.

---

## Contents


[display_class](./display_class.md)  
Manages a 0.96 inch 128 x 64 pixel Oled display and provides functionalities for
rendering text, images, and visual effects.

This module is responsible for controlling and displaying content on an SSD1306
OLED display using the Adafruit and PIL libraries. Functionalities provided by
the module include displaying text, clearing the display, rendering full display
representations, and managing dynamic visual effects. The module uses I2C communication
to interact with the OLED display.

[main](./main.md)  
Module for initialising and displaying text on an OLED display.

This module interacts with the `LcdDisplayClass` from `display_class` to
control the OLED display and show text-based content. The functionality includes
handling the setup of an LCD screen and rendering the desired text onto the
screen.


---


  
-------
#### Copyright (C) 2026 Gary Twinn  

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.  
  
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.  
  
  ##### Author: Gary Twinn  
  
 -------------
  
