# Accelerometer example.
# Reads the accelerometer x, y, z values and prints them every tenth of a second.
# Open the serial port after running to see the output printed.
# Author: Tony DiCola
import time
import board
import adafruit_lis3dh


# Uncomment _one_ of the hardware setups below depending on your wiring:

# Hardware I2C setup:
import nativeio
i2c = nativeio.I2C(board.SCL, board.SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

# Software I2C setup:
#import bitbangio
#i2c = bitbangio.I2C(board.SCL, board.SDA)
#lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)

# Hardware SPI setup:
#import nativeio
#spi = nativeio.SPI(board.SCK, board.MOSI, board.MISO)
#cs = nativeio.DigitalInOut(board.D6)  # Set to appropriate CS pin!
#lis3dh = adafruit_lis3dh.LIS3DH_SPI(spi, cs)


# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_2_G

# Loop forever printing accelerometer values
while True:
    # Read accelerometer values (in gravities or G).  Returns a 3-tuple of x, y,
    # z axis values.
    x, y, z = lis3dh.read_accel_g()
    print('x = {}G, y = {}G, z = {}G'.format(x, y, z))
    # Small delay to keep things responsive but give time for interrupt processing.
    time.sleep(0.1)