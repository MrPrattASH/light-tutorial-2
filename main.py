# simple on/off LED code
touch = 0
brightness = 0

def on_forever():
    global touch, brightness
    # read sensor
    touch = pins.digital_read_pin(DigitalPin.P0) 
    
    
    # adjust brightness for LED
    if input.button_is_pressed(Button.A):
        #add 100 to brighness
        brightness += 100

        #check if out of range of acceptable values
        if brightness >= 1023:
            brightness = 1023
    if input.button_is_pressed(Button.B)
        #subtract 100 to brighness
        brightness -= 100

        #check if out of range of acceptable values
        if brightness <= 0:
            brightness = 0
    
    # Lastly, output chosen brightness
    pins.analog_write_pin(AnalogPin.P1,brightness)
    
    #display current brightness number on screen for debugging
    if touch == 0:
        basic.show_number(brightness)
    
basic.forever(on_forever)