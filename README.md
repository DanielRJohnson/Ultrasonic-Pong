# Ultrasonic-Pong by Daniel Johnson

## Demo here: https://www.youtube.com/watch?v=lfq0VmZCbaI&feature=youtu.be

# About
Ultrasonic Pong is a project I made using the Raspberry Pi along with ultrasonic sensors to create a game of pong.<br><br>
Ultrasonic sensors are devices that can emit a sound higher than the frequencies we can hear, as well as recieve them. I used the HC-SR04.<br>
Using Python, we can keep track of the time we emitted and recieved the sound.<br>
Then, using the speed of sound we can calculate distance like so:<br><br>

![Image of equation](https://github.com/DanielRJohnson/Ultrasonic-Pong/blob/master/photos/equation.png)<br><br>

The HC-SR04 takes 5-Volt signals, but the Raspberry Pi GPIO pins emit at 3.3-Volts.<br>
So, instead of plugging the HC-SR04's directly into the Pi, we need some more circuitry to adapt that.<br>

![Image of full setup](https://github.com/DanielRJohnson/Ultrasonic-Pong/blob/master/photos/Full-Setup.jpg)<br>

![Image of breadboard](https://github.com/DanielRJohnson/Ultrasonic-Pong/blob/master/photos/Breadboard.jpg)<br>
Each half requires a 1k Ohm and a 2k Ohm resistor.<br><br>

To make the game, I made a very simple pygame script to simulate Pong.<br>
Pygame can be found here: https://www.pygame.org/wiki/about <br>

# How to use
To run this project, you need to recreate the setup shown above as well as:<br>
* Have a working installation of Python on the Raspberry Pi. This comes out of the box with the Raspberry Pi.<br>
* Have the Pygame module installed to that Python environment. https://www.pygame.org/wiki/GettingStarted <br><br>
Then,
* Clone/download this repo
* Navigate to where you saved the repo in a terminal
* Run the command: "python main.py"
