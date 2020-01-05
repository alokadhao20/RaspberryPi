https://gist.github.com/prasanthj/c15a5298eb682bde34961c322c95378b
https://www.youtube.com/watch?v=ymFO0oFyXA4&t=313s
https://github.com/AnaviTechnology/anavi-docs/issues/20
https://github.com/nosretep/ir-receiver-node-raspi/blob/master/service.js
https://github.com/AnaviTechnology/anavi-docs/blob/master/anavi-infrared-phat/anavi-infrared-phat.md#setting-up-lirc

sudo apt-get install lirc 
sudo modprobe lirc_dev
sudo modprobe lirc-rpi,gpio in pin=17
sudo nano /boot/config.txt
    at last of file 
        Add:- 
            dtoverlay=lirc-rpi,gpio_in_pin=17
            // new kernal
            dtoverlay=gpio-ir,gpio_in_pin=18
            dtoverlay=gpio-ir-tx,gpio_out_pin=17
sudo reboot 
ls -l /dev/lir*

sudo nano /etc/lirc/hardware.conf
    in LIRCD_ARGS="--uinput"
        DRIVER="default"
        DEVICE="/dev/lirc0"
        MODULES="lirc_rpi"

sudo /etc/init.d/lirc stop
mode2 -d /dev/lirc0 // or 
mode2 -d /dev/lirc1

KEY_0
KEY_1
KEY_2
KEY_3
KEY_4
KEY_5
KEY_6
KEY_7
KEY_8
KEY_9
KEY_OK
KEY_UP
KEY_DOWN
KEY_RIGHT
KEY_LEFT
KEY_NUMERIC_STAR
KEY_NUMERIC_POUND


irrecord -d /dev/lirc1 ~/lircd.conf
OR
irrecord -f -d /dev/lirc1 ~/lirc.conf               - this is much better


Successfully written config file remotetestthree.lircd.conf

sudo mv ~/37 /etc/lirc/lircd.conf

sudo /etc/init.d/lircd start

sudo /etc/init.d/lircd restart

irw

########################################### nodeJS ########################################
var requirejs = require('requirejs');

requirejs.config({
    nodeRequire : require
});

requirejs([ 'child_process' ],

function(child_process) {

    var exec = child_process.exec;
    var irw = exec('irw', function(error, stdout, stderr) {
        console.log(JSON.stringify(arguments));
    });

    irw.stdout.on('data', function(data) {
        var data = String(data);
        console.log(data);
    });

});

#########################################