def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . . # # .
        . # # # .
        . # . # .
        . . . . .
        """)
    datalogger.log(datalogger.create_cv("car", 1))
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_icon(IconNames.SKULL)
    datalogger.delete_log()
    datalogger.set_column_titles("car", "bus", "truck")
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
        # # # # #
        # # # # #
        . # . # .
        . . . . .
        """)
    datalogger.log(datalogger.create_cv("bus", 1))
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.show_leds("""
        # # . . .
        # # # # #
        # # # # #
        . # . # .
        . . . . .
        """)
    datalogger.log(datalogger.create_cv("truck", 1))
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

datalogger.set_column_titles("car", "bus", "truck")
basic.show_icon(IconNames.YES)