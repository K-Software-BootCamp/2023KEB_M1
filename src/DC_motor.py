import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀 번호 (Jetson TX2 7번 핀에 연결된 GPIO 핀 번호)
led_pin = 9

# GPIO 초기화
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # LED 켜기
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED ON")
        time.sleep(5)

        # LED 끄기
        GPIO.output(led_pin, GPIO.LOW)
        print("LED OFF")
        time.sleep(5)

except KeyboardInterrupt:
    pass

# GPIO 정리
GPIO.cleanup()
