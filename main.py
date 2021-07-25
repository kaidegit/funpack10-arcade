def generate_morse_str():
    global num_of_char, morse_str, morse_code_list
    num_of_char = randint(0, 2) + 3
    for index in range(num_of_char):
        ran = randint(0, 38)
        morse_str = "" + morse_str + morse_char[ran]
        morse_code_list = "" + morse_code_list + morse_code[ran]
    morse_str_lable.set_text(morse_str)
    right_morse_code_lable.set_text(morse_code_list)

def on_a_pressed():
    global my_morse_code
    my_morse_code = "" + my_morse_code + "`"
    show_my_morse_code(my_morse_code)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_b_pressed():
    global my_morse_code
    my_morse_code = "" + my_morse_code + "-"
    show_my_morse_code(my_morse_code)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_check_pressed():
    if check_my_morse_code():
        my_morse_code_lable_1.set_text("right")
        my_morse_code_lable_2.set_text("")
    else:
        my_morse_code_lable_1.set_text("error")
        my_morse_code_lable_2.set_text("")
    pause(3000)
    init()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_check_pressed)

def show_my_morse_code(my_morse_code: str):
    if len(my_morse_code) > 11:
        my_morse_code_lable_1.set_text(my_morse_code.slice(0, 11))
        my_morse_code_lable_2.set_text(my_morse_code.slice(11))
    else:
        my_morse_code_lable_1.set_text(my_morse_code)

def check_my_morse_code():
    i = 0
    while i <= len(morse_code_list) - 1:
        if not (((my_morse_code[i] == '`') and (morse_code_list[i] == 'a')) or
            ((my_morse_code[i] == '-') and (morse_code_list[i] == 'b'))):
            return False
        i += 1
    return True

def init():
    global morse_code_list,morse_str,my_morse_code
    global my_morse_code_lable_1,my_morse_code_lable_2,morse_str_lable
    morse_code_list = ""
    morse_str = ""
    my_morse_code = ""
    my_morse_code_lable_1.set_text("")
    my_morse_code_lable_2.set_text("")
    morse_str_lable.set_text("")
    generate_morse_str()

morse_code_list = ""
morse_str = ""
num_of_char = 0
my_morse_code_lable_2: TextSprite = None
my_morse_code_lable_1: TextSprite = None
right_morse_code_lable: TextSprite = None
morse_str_lable: TextSprite = None
morse_code: List[str] = []
morse_char: List[str] = []
my_morse_code = ""
music.stop_all_sounds()
morse_char = ["A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "?",
    "/",
    "-"]
# a代表`,b代表-
morse_code = ["ab",
    "baaa",
    "baba",
    "baa",
    "a",
    "aaba",
    "bba",
    "aaaa",
    "aa",
    "abbb",
    "bab",
    "abaa",
    "bb",
    "ba",
    "bbb",
    "abba",
    "bbab",
    "aba",
    "aaa",
    "b",
    "aab",
    "aaab",
    "abb",
    "baab",
    "babb",
    "bbaa",
    "abbbb",
    "aabbb",
    "aaabb",
    "aaaab",
    "aaaaa",
    "baaaa",
    "bbaaa",
    "bbbaa",
    "bbbba",
    "bbbbb",
    "aabbaa",
    "baaba",
    "baaaab"]
morse_str_lable = textsprite.create("")
morse_str_lable.set_max_font_height(24)
morse_str_lable.set_position(40, 33)
my_morse_code_lable_1 = textsprite.create("")
my_morse_code_lable_1.set_max_font_height(12)
my_morse_code_lable_1.set_position(20, 73)
my_morse_code_lable_2 = textsprite.create("")
my_morse_code_lable_2.set_max_font_height(12)
my_morse_code_lable_2.set_position(20, 93)
right_morse_code_lable = textsprite.create("")
right_morse_code_lable.set_max_font_height(12)
right_morse_code_lable.set_position(0, 113)
init()