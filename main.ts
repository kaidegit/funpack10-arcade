function generate_morse_str() {
    let ran: number;
    
    num_of_char = randint(0, 2) + 3
    for (let index = 0; index < num_of_char; index++) {
        ran = randint(0, 38)
        morse_str = "" + morse_str + morse_char[ran]
        morse_code_list = "" + morse_code_list + morse_code[ran]
    }
    morse_str_lable.setText(morse_str)
    right_morse_code_lable.setText(morse_code_list)
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    my_morse_code = "" + my_morse_code + "`"
    show_my_morse_code(my_morse_code)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function on_b_pressed() {
    
    my_morse_code = "" + my_morse_code + "-"
    show_my_morse_code(my_morse_code)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function on_check_pressed() {
    if (check_my_morse_code()) {
        my_morse_code_lable_1.setText("right")
        my_morse_code_lable_2.setText("")
    } else {
        my_morse_code_lable_1.setText("error")
        my_morse_code_lable_2.setText("")
    }
    
    pause(3000)
    init()
})
function show_my_morse_code(my_morse_code: string) {
    if (my_morse_code.length > 11) {
        my_morse_code_lable_1.setText(my_morse_code.slice(0, 11))
        my_morse_code_lable_2.setText(my_morse_code.slice(11))
    } else {
        my_morse_code_lable_1.setText(my_morse_code)
    }
    
}

function check_my_morse_code(): boolean {
    let i = 0
    while (i <= morse_code_list.length - 1) {
        if (!(my_morse_code[i] == "`" && morse_code_list[i] == "a" || my_morse_code[i] == "-" && morse_code_list[i] == "b")) {
            return false
        }
        
        i += 1
    }
    return true
}

function init() {
    
    
    morse_code_list = ""
    morse_str = ""
    my_morse_code = ""
    my_morse_code_lable_1.setText("")
    my_morse_code_lable_2.setText("")
    morse_str_lable.setText("")
    generate_morse_str()
}

let morse_code_list = ""
let morse_str = ""
let num_of_char = 0
let my_morse_code_lable_2 : TextSprite = null
let my_morse_code_lable_1 : TextSprite = null
let right_morse_code_lable : TextSprite = null
let morse_str_lable : TextSprite = null
let morse_code : string[] = []
let morse_char : string[] = []
let my_morse_code = ""
music.stopAllSounds()
morse_char = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "?", "/", "-"]
//  a代表`,b代表-
morse_code = ["ab", "baaa", "baba", "baa", "a", "aaba", "bba", "aaaa", "aa", "abbb", "bab", "abaa", "bb", "ba", "bbb", "abba", "bbab", "aba", "aaa", "b", "aab", "aaab", "abb", "baab", "babb", "bbaa", "abbbb", "aabbb", "aaabb", "aaaab", "aaaaa", "baaaa", "bbaaa", "bbbaa", "bbbba", "bbbbb", "aabbaa", "baaba", "baaaab"]
morse_str_lable = textsprite.create("")
morse_str_lable.setMaxFontHeight(24)
morse_str_lable.setPosition(40, 33)
my_morse_code_lable_1 = textsprite.create("")
my_morse_code_lable_1.setMaxFontHeight(12)
my_morse_code_lable_1.setPosition(20, 73)
my_morse_code_lable_2 = textsprite.create("")
my_morse_code_lable_2.setMaxFontHeight(12)
my_morse_code_lable_2.setPosition(20, 93)
right_morse_code_lable = textsprite.create("")
right_morse_code_lable.setMaxFontHeight(12)
right_morse_code_lable.setPosition(0, 113)
init()
