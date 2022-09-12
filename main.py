listeTAN = ["345", "786", "775", "773", "geheim", "nochGeheimer","ABC"]
i = 0

def on_button_pressed_a():
    #code verbessern
    radio.send_string(str(11*randint(100,200)))
    

def on_button_pressed_b():
    radio.send_string("000")

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_string(receivedString):
    serial.write_string("" +receivedString+ ("\r\n"))
    global verbrauchteTAN
    # wenn received in listeTAN:   # code verbessern !!!
    if int(receivedString) %11 == 0:
        basic.show_icon(IconNames.HAPPY)
        verbrauchteTAN.push(str(int(receivedString) %11) )
    else:
        basic.clear_screen(radio.on()
    
radio.on_received_string(on_received_string)


