let listeTAN = ["345", "786", "775", "773", "geheim", "nochGeheimer", "ABC"]
let i = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    serial.writeString("" + "Test\r\n")
    // code verbessern
    radio.sendString("" + 11 * randint(100, 200))
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString("000")
})
function on_received_string(receivedString: any) {
    serial.writeString("" + receivedString + "\r\n")
    
    //  wenn received in listeTAN:   # code verbessern !!!
    if (listeTAN.indexOf(receivedString) >= 0) {
        basic.showIcon(IconNames.Happy)
    }
    
}

