input.onButtonPressed(Button.A, function () {
    pos = 40
    basic.showIcon(IconNames.Pitchfork)
    pins.servoWritePin(AnalogPin.P16, pos)
})
input.onButtonPressed(Button.AB, function () {
    pos = 90
    basic.showIcon(IconNames.Scissors)
    pins.servoWritePin(AnalogPin.P16, pos)
})
input.onButtonPressed(Button.B, function () {
    pos = 130
    basic.showIcon(IconNames.EigthNote)
    pins.servoWritePin(AnalogPin.P16, pos)
})
let pos = 0
pos = 90
basic.showIcon(IconNames.Scissors)
pins.servoWritePin(AnalogPin.P16, pos)
