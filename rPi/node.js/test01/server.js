var Gpio = require('onoff').Gpio
var led = new Gpio(17, 'out')
    button = new Gpio(4, 'in', 'both');

    button.watch(function(err, value) {
        if (err) {
            throw err;
        }

        led.writeSync(value);
    });

    led.writeSync(1);
    var status = led.readSync();
    console.log("status - ", status);
    setTimeout(myFunction, 3000)

    function myFunction() {
        led.writeSync(0);
        var status = led.readSync();
        console.log("status - ", status);
    }
    process.on('SIGINT', function() {
        led.unexport();
        // button.unexport();
    });