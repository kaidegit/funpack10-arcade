# Funpack第十期 ARCADE 的makecode arcade工程



PS：由于makecode后期的GitHub commit&push失败问题，本工程后期都由我自行修改后commit并push，故不能导入makecode。可通过下载uf2文件后导入本地工程的方式导入，也可打开main.py文件查看源码。



## 任务要求

设计一个摩斯密码练习器，选择两个按键为点与横，或者一个按键的长短按。LCD屏上随机出现一个字符，敲出对应的组合（3-5个字符即可），正确时，蜂鸣器响；错误时，振动电机发出振动。 

## 任务分析

* 使用随机数函数生成字符，使用查表法得到正确的摩斯密码
* 使用按键中断，在回调函数中向已输入的摩斯密码的buffer添加或者删除摩斯密码，同时更新LCD上已输入的摩斯密码。
* 使用按键中断，在回调函数中逐个判断摩斯密码的正确性
* 通过使用库和操作GPIO，控制蜂鸣器和转子马达

## 代码部分

本次使用Microsoft MakeCode Arcade环境开发，使用Python语言

### 初始化部分

初始化部分主要分为全局初始化和每次判断完摩斯密码正确性后的变量归零以及生成摩斯密码

```python 
cheat_code = False
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
morse_char = [
    "A","B","C","D","E","F","G",
    "H","I","J","K","L","M","N",
    "O","P","Q","R","S","T","U",
    "V","W","X","Y","Z",
    "1","2","3","4","5","6","7","8","9","0",
    "?","/","-"
]
# a代表`,b代表-
morse_code = [
    "ab",	"baaa",	"baba",	"baa",	"a",	"aaba",	"bba",
    "aaaa",	"aa",	"abbb",	"bab",	"abaa",	"bb",	"ba",
    "bbb",	"abba",	"bbab",	"aba",	"aaa",	"b",	"aab",
    "aaab",	"abb",	"baab",	"babb",	"bbaa",	
    "abbbb","aabbb","aaabb","aaaab","aaaaa","baaaa","bbaaa","bbbaa","bbbba","bbbbb",
    "aabbaa",		"baaba",		"baaaab"
]
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

def init():
    global morse_code_list,morse_str,my_morse_code
    global my_morse_code_lable_1,my_morse_code_lable_2,morse_str_lable
    music.stop_all_sounds()
    morse_code_list = ""
    morse_str = ""
    my_morse_code = ""
    my_morse_code_lable_1.set_text("")
    my_morse_code_lable_2.set_text("")
    morse_str_lable.set_text("")
    generate_morse_str()
```

### 生成摩斯密码函数

随机生成一个字符以及它的摩斯密码

```python
def generate_morse_str():
    global num_of_char, morse_str, morse_code_list, cheat_code
    # num_of_char = randint(0, 2) + 3
    num_of_char = 1
    for index in range(num_of_char):
        ran = randint(0, 38)
        morse_str = "" + morse_str + morse_char[ran]
        morse_code_list = "" + morse_code_list + morse_code[ran]
    morse_str_lable.set_text(morse_str)
    if cheat_code:
        right_morse_code_lable.set_text(morse_code_list)
```

### 各类按键的中断及中断回调函数

```python
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
        my_morse_code_lable_1.set_text("correct")
        my_morse_code_lable_2.set_text("")
        music.play_tone(Note.C, BeatFraction.BREVE)
    else:
        my_morse_code_lable_1.set_text("incorrect")
        my_morse_code_lable_2.set_text("")
        pins.pin_by_cfg(101).digital_write(True)
        pause(100)
        pins.pin_by_cfg(101).digital_write(False)
    pause(3000)
    init()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_check_pressed)

def on_back_pressed():
    global my_morse_code
    if len(my_morse_code) >= 1:
        my_morse_code = my_morse_code[:-1]
    show_my_morse_code(my_morse_code)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_back_pressed)

def cheat_code_switch():
    global cheat_code, morse_code_list
    cheat_code = not cheat_code
    if cheat_code:
        right_morse_code_lable.set_text(morse_code_list)
    else:
        right_morse_code_lable.set_text("")
controller.up.on_event(ControllerButtonEvent.PRESSED, cheat_code_switch)
```

### 摩斯密码显示函数

由于摩斯密码可能过长，分段显示

```python
def show_my_morse_code(my_morse_code: str):
    if len(my_morse_code) > 11:
        my_morse_code_lable_1.set_text(my_morse_code.slice(0, 11))
        my_morse_code_lable_2.set_text(my_morse_code.slice(11))
    else:
        my_morse_code_lable_1.set_text(my_morse_code)
```

### 验证摩斯密码的正确性

逐个对比后返回正确与否

```python
def check_my_morse_code():
    if len(my_morse_code) != len(morse_code_list):
    	return False
    i = 0
    while i <= len(morse_code_list) - 1:
        if not (((my_morse_code[i] == '`') and (morse_code_list[i] == 'a')) or
            ((my_morse_code[i] == '-') and (morse_code_list[i] == 'b'))):
            return False
        i += 1
    return True
```

## 心得体会

本次的开发板及推荐的开发环境，似乎更脱离了传统的嵌入式开发，库中大量使用了python、typescript等我们在传统嵌入式开发中不会用到的语言。微软的arcade框架的制作让尚未入门的新手或者未接触过嵌入式的开发者也能顺利找到适合自己的入门开发方式。
