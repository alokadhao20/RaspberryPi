# Raspberry Pi sketch compilation
This directory is full of my Python sketches designed for the Raspberry Pi
platforms.

These sketches are available for educational purposes only, and any damage
resulting from the use of any code found here is the sole responsibility of the
user.

Any sketches that invoke the use of GPIO must be run using the `sudo` command in
order to access hardware level systems.  Without this command, the GPIO will not
function properly.

Any sketches which do not call upon GPIO can/will function properly without the
use of root level access.  This can be accomplished using `python app_name.py`
in Terminal.  These sketches will function on both the first generation (A/B)
and second generation (A+/B+/2) Pi systems alike.

Any sketches which do not call any of the GPIO above 26 will function properly
with the older A/B systems.  These will also require root level access via the
`sudo` command for GPIO access, but will require no further alterations.  Some
sketches which call upon GPIO above the number 26 may be altered to work with
fewer GPIO, but this is up to the end user, and is done at the risk of the user.

## Raspberry Pi 2
![Pi2 top](https://bytebucket.org/stillborn86/python/raw/835fe61c11328ba57874134bf70cec4f274f6e96/images/raspberry_pi_2_top.png?token=c5b511bbea49c97c419a87b76dd15cc5a35f20f8)
![Pi2 bottom](https://bytebucket.org/stillborn86/python/raw/835fe61c11328ba57874134bf70cec4f274f6e96/images/raspberry_pi_2_bottom.jpg?token=25e5088cb0f3ba4250b761e1fb4a0832d803c035)

## Raspberry Pi A+
![A+](http://www.raspberrypi.org/wp-content/uploads/2014/11/A-_Overhead.jpg)

## cleanup_template.py
This is a standard template to build all sketches from in order to assure that
all GPIO functionality is properly cleaned up at the end of all sketches.  This
template takes into account `Ctrl+C` interrupts as well as any type of fatal
error during the code.

If a sketch does not invoke GPIO functionality, this template is unnecessary.

## Help folder
The help folder is filled with small sketch "bites" consisting of example code,
each doing different things. These tiny sketches are examples of smaller code
demonstrating mathematical functions, tuples, and other esoteric bits for the
Python language.

## Tutorial folder
The tutorial folder is full of sketches that were either designed by others or
created with the help of others.  It was designed to be used as a helpful tool
for writing sketches in the future.

## Image files
The images are references, such as standard, 40-pin GPIO pinouts.

![GPIO](https://bytebucket.org/stillborn86/python/raw/c6c8a65d1ee7e42cb45e3feedb72c6189ae20d25/images/bplus_gpio_pinout.jpeg?token=cbc5d7ef6dc071f9ad8117f7bbf18269ff278dda)

