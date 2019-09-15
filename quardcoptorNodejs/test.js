const Gpio = require('pigpio').Gpio;
 
const motor = new Gpio(4, {mode: Gpio.OUTPUT});
 
let pulseWidth = 1000;
let increment = 100;
 console.log("setting pulse width");
setInterval(() => {
  motor.servoWrite(pulseWidth);
  
  console.log("incrementing pulse width");
  pulseWidth += increment;
  if (pulseWidth >= 2000) {
    console.log(" pulse greter than 2000 decresing by 100 pulse width");
    increment = -100;
  } else if (pulseWidth <= 1000) {
    console.log(" pulse less than 1000 incresing by 100 pulse width");
    increment = 100;
  }
}, 1000);


