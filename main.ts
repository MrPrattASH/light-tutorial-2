//  simple on/off LED code
let touch = 0
let brightness = 0
basic.forever(function on_forever() {
    
    //  read sensor
    touch = pins.digitalReadPin(DigitalPin.P0)
    //  adjust brightness for LED
    if (input.buttonIsPressed(Button.A)) {
        // add 100 to brighness
        brightness += 100
        // check if out of range of acceptable values
        if (brightness >= 1023) {
            brightness = 1023
        }
        
    }
    
    //  Lastly, output chosen brightness
    if (touch == 1) {
        // turn off LED - note ANALOG write
        pins.analogWritePin(AnalogPin.P1, brightness)
    } else {
        // turn on LED
        pins.analogWritePin(AnalogPin.P1, brightness)
    }
    
})
