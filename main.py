def on_button_pressed_a():
    global pos
    pos = 40
    basic.show_icon(IconNames.PITCHFORK)
    pins.servo_write_pin(AnalogPin.P16, pos)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global pos
    pos = 90
    basic.show_icon(IconNames.SCISSORS)
    pins.servo_write_pin(AnalogPin.P16, pos)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global pos
    pos = 130
    basic.show_icon(IconNames.EIGTH_NOTE)
    pins.servo_write_pin(AnalogPin.P16, pos)
input.on_button_pressed(Button.B, on_button_pressed_b)

pos = 0
pos = 90
basic.show_icon(IconNames.SCISSORS)
pins.servo_write_pin(AnalogPin.P16, pos)