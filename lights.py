from light_animations import *

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO_INPUT_SENSOR = 26
GPIO_INPUT_SENSOR_1 = 16
GPIO_INPUT_SENSOR_2 = 20

GPIO.setup(GPIO_INPUT_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_INPUT_SENSOR_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_INPUT_SENSOR_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
Orange = Color(25,255,0)
Green = Color(255, 0, 0)
Red = Color(0,255,0)
Blue = Color(0, 0, 255)
number_lights = 0
number_lights_1 = 0
number_lights_2 = 0

def handle_button(amount):
  global number_lights
  number_lights = amount
  print("original button")
  # print("button pressed:", number_lights)
  colorSequence(strip, Red, number_lights)
  # time.sleep(0.05)


def handle_button1(amount):
  global number_lights_1
  print("Button One")
  number_lights_1 = amount
  # print("button pressed:", number_lights)
  colorSequence1(strip, Green, number_lights_1)
  # time.sleep(0.05)


def handle_button2(amount):
  global number_lights_2
  print("button Two")
  number_lights_2 = amount
  # print("button pressed:", number_lights)
  colorSequence2(strip, Orange, number_lights_2)
  # time.sleep(0.05)
  


if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip1 = Adafruit_NeoPixel(LED_1_COUNT, LED_1_PIN, LED_1_FREQ_HZ, LED_1_DMA, LED_1_INVERT, LED_1_BRIGHTNESS, LED_1_CHANNEL, LED_1_STRIP)
    # strip2 = Adafruit_NeoPixel(LED_2_COUNT, LED_2_PIN, LED_2_FREQ_HZ, LED_2_DMA, LED_2_INVERT, LED_2_BRIGHTNESS, LED_2_CHANNEL, LED_2_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    strip1.begin()
    # strip2.begin()

    print('Press Ctrl-C to quit.')
    try:
        while True:
          amount = number_lights
          amount1 = number_lights_1
          amount2 = number_lights_2
          input_state_sensor = GPIO.input(GPIO_INPUT_SENSOR)
          input_state_sensor_1 = GPIO.input(GPIO_INPUT_SENSOR_1)
          # input_state_sensor_2 = GPIO.input(GPIO_INPUT_SENSOR_2)
          if input_state_sensor == False:
            amount += 1
            handle_button(amount)
            # time.sleep(0.02)
          
          if input_state_sensor_1 == False:
            amount1 += 1
            handle_button1(amount1)
            # time.sleep(0.02)

          # if input_state_sensor_2 == False:
          #   amount2 += 1
          #   handle_button2(amount2)
            # time.sleep(0.02)

    except KeyboardInterrupt:
        # if args.clear:
        colorWipe(strip, Color(0, 0, 0), 0)
