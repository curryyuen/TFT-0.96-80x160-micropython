from ST7735 import TFT
from sysfont import sysfont
from machine import SPI, Pin

# Initialize SPI and TFT
spi = SPI(1, baudrate=20000000, polarity=0, phase=0)
tft = TFT(spi, 3, 2, 4)  # DC=3, RES=2, CS=4

# Initialize the display (using red tab version)
tft.initr()
tft.rgb(False)
tft.invertcolor(True)

# Clear screen and display text
tft.rotation(1)
tft.fill(TFT.BLACK)
tft.text((0, 0), "Hello World!", TFT.WHITE, sysfont, 1)