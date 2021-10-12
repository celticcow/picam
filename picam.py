#!/usr/bin/python3

from picamera import PiCamera
from time import sleep

def main():
    camera = PiCamera()

    camera.resolution = (800, 600)
    camera.framerate = 15

    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/pic.jpg')
    camera.stop_preview()

if __name__ == "__main__":
    main()
