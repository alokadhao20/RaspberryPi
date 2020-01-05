var requirejs = require('requirejs');
var Gpio = require('onoff').Gpio; //include onoff to interact with the GPIO
var LED = new Gpio(4, 'out'); //use GPIO pin 4, and specify that it is output
requirejs.config({
    nodeRequire : require
});
var KEY1 = "00 KEY_1 LG_AKB72915207"
requirejs([ 'child_process' ],

function(child_process) {

    var exec = child_process.exec;
    var irw = exec('irw', function(error, stdout, stderr) {
        console.log(JSON.stringify(arguments));
    });

    irw.stdout.on('data', function(data) {
        var data = String(data);
        console.log(data);
var n = data.search(KEY1);
if(n != -1) {
    if (LED.readSync() === 0) { //check the pin state, if the state is 0 (or off)
        LED.writeSync(1); //set pin state to 1 (turn LED on)
      } else {
        LED.writeSync(0); //set pin state to 0 (turn LED off)
      }
}
     });

 });


