input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . . # # .
        . # # # .
        . # . # .
        . . . . .
        `)
    datalogger.log(datalogger.createCV("car", 1))
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Skull)
    datalogger.deleteLog()
    datalogger.setColumnTitles(
    "car",
    "bus",
    "truck"
    )
    basic.showIcon(IconNames.Yes)
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . . . .
        # # # # #
        # # # # #
        . # . # .
        . . . . .
        `)
    datalogger.log(datalogger.createCV("bus", 1))
    basic.clearScreen()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showLeds(`
        # # . . .
        # # # # #
        # # # # #
        . # . # .
        . . . . .
        `)
    datalogger.log(datalogger.createCV("truck", 1))
    basic.clearScreen()
})
datalogger.setColumnTitles(
"car",
"bus",
"truck"
)
basic.showIcon(IconNames.Yes)
