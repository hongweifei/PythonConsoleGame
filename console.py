




import os
import platform
import ctypes



"""
︻︼
︽︾
〒↑↓☉⊙●〇◎¤★☆■▓
「」『』◆◇▲△▼▽
◣◥◢◣◤ ◥№↑↓→←↘↙Ψ※㊣∑⌒∩
【】
〖〗＠ξζω□∮〓※》∏卐√ ╳々♀♂∞①ㄨ≡╬╭╮╰╯
╱╲ 
▂ ▂ ▃ ▄ ▅ ▆ ▇ █ 
▂▃▅▆█ 
▁▂▃▄▅▆▇█▇▆▅▄▃▂▁
"""


"""
๑•ิ.•ั๑ ๑๑ ♬✿.｡.:* ☂☃ ☄ ★ ☆ ☇ ☈ ☉ ☒☢ ☺ ☻ ☼ ☽☾ ♠ 　 ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ εїз℡❣·۰•●○● ゃōゃ♥ ♡๑۩ﺴ ☜ ☞ ☎ ☏♡ ⊙◎ ☺ ☻✖╄ஐﻬ 
► ◄ ▧ ▨ ♨ ◐ ◑ ↔ ↕ ▪ ▫ ☼ ♦ ? ▄ █▌ ?? ? ▬♦ ◊ ◦ ☼ ♠♣ ▣ ▤ ▥ ▦ ▩ ◘ ◙ ◈ ♫ ♬ ♪ ♩ ♭ ♪ の 
☆ → あぃ ￡ ＃ ＠ ＆ ＊ ￥✰ ☆ ★ ¤ ☼ ♡ ღ☻ ☺ ⊕ ☉ Θ o O ㊝ ⊙ ◎ ◑ ◐ ۰ • ● ▪ ▫ ｡ ﾟ ๑ ☜ ☞ ♨ 
☎ ☏ ︻ ︼ ︽ ︾ 〈 〉 ︿ ﹀ ∩ ∪ ﹁ ﹂﹃﹄﹝ ﹞ ＜ ＞ ≦ ≧ ﹤ ﹥ 「 」 ︵ ︶︷ ︸︹︺
〔 〕 【 】 《 》 （ ） ｛ ｝ ﹙ ﹚ 『』﹛﹜╳ ＋ － ﹢ × ÷ ＝ ≠ ≒ ∞ ˇ ± √ ⊥ ∠ ∟ ⊿ ㏒ ▶ ▷ ◀ ◁ 
★ ☆ ☉ ☒☢ ☺ ☻ ☼ ♠ ♡ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ? ? ㍿ ♝ ♞ ♯♩♪♫♬♭♮ ☎ ☏ ☪ ♈ ♨ ºº ₪ ¤ 큐 « » ™ ♂✿
 ♥ の ↑ ↓ ← → ↖ ↗ ↙ ↘ ㊣ ◎ ○ ● ⊕ ⊙ ○　 △ ▲ ☆ ★ ◇ ◆ ■ □ ▽ ▼ § ￥ 〒 ￠￡ ※ ♀ ♂ © ® ⁂ ℡ 
 ↂ? ▣ ▤ ▥ ▦ ▧ ♂ ♀ ♥ ♡ ☜ ☞ ☎ ☏ ⊙ ◎ ☺ ☻ ► ◄ ▧ ▨ ♨ ◐ ◑ ↔ ↕ ♥ ♡ ▪ ▫ ☼ ♦ ? ▄ █ ▌ ? ? ? ▬ ♦ ◊ 
 ◘ ◙ ◦ ☼ ♠ ♣ ▣ ▤ ▥ ▦ ▩ ◘ ◙ ◈ ♫ ♬ ♪ ♩ ♭ ♪ ✄☪☣☢☠ ⅰⅱⅲⅳⅴⅵⅶ ⅷⅸⅹⅺⅻⅠⅡⅢⅣⅤⅥⅦ Ⅷ Ⅷ ⅨⅩⅪⅫ
  ㊊㊋㊌㊍㊎㊏㊐㊑㊒㊓㊔㊕㊖㊗㊘㊜㊝㊞㊟㊠㊡㊢㊣㊤㊥㊦㊧㊨㊩㊪㊫㊬㊭㊮㊯㊰ ✗✘✚✪✣✤✥✦✧✩✫✬✭✮✯✰
  【】┱ ┲ ✓ ✔ ✕ ✖ *.:｡✿*ﾟ‘ﾟ･✿.｡.: ≧０≦ o(╥﹏╥)o //(ㄒoㄒ)// {{{(>_<)}}} ™ぷ▂▃▅▆█ 
  ∏卐 ※◤ ◥ ﹏﹋﹌ ∩∈∏ ╰☆╮≠→№← ︵︶︹︺【】〖〗＠﹕﹗/ ' _ < > `,·。≈{}~ ～() _ -『』√ $ 
  @ * & # ※卐 々∞Ψ ∪∩∈∏ の ℡ ぁ §∮〝〞ミ灬ξ№∑⌒ξζω＊ㄨ ≮≯ ＋－×÷﹢﹣±／＝∫∮∝ ∞ ∧∨ ∑ ∏ 
  ∥∠ ≌ ∽ ≦ ≧ ≒﹤﹥じ☆ ■♀『』◆◣◥▲Ψ ※◤ ◥ →№←㊣∑⌒〖〗＠ξζω□∮〓※∴ぷ▂▃▅▆█ ∏卐
  【】△√ ∩¤々♀♂∞①ㄨ≡↘↙▂▂ ▃ ▄ ▅ ▆ ▇ █┗┛╰☆╮ ≠ ▂ ▃ ▄ ▅┢┦aΡｐy ♡^_^♡　^_^.......
  ♧♧ ☜♥☞.︻︼─一　▄︻┻┳═一 ﹏◢ ◣ ◥ ◤ ▽ ▧ ▨ ▣ ▤ ▥ ▦ ▩ ◘ ◙ ▓ ? ? Café № ＠ ㊣ ™ ℡
   凸 の ๑۞๑ ๑۩ﺴ ﺴ۩๑ o(‧'''‧)o ❆ べò⊹⊱⋛⋋ ⋌⋚⊰⊹ ⓛⓞⓥⓔ べ ☀ ☼ ☜ ☞ ⊙® ◈ ♦ ◊ ◦ ◇ ◆ εїз 
   ☆·.¸¸.·´¯`·.¸¸.¤ ~♡のⓛⓞⓥⓔ♡~☃⊹⊱⋛⋌⋚⊰⊹✗(*w*)\ ≡[。。]≡※◦º°×°º◦εїз´¯`·»｡｡♀♡╭☆╯
   ºØØºøº¤ø,¸¸,ºº¤øøºﷲﷲ°º¤ø,¸¸, げこごさざしじすぜそぞただちぢっつづてでとどなにぬねのはば ♪♫╭
   ♥ ๑•ิ.•ัﻬஐ ✎ぱひびぴふぶぷへべぺほぼぽまみむめも ❃❂❁❀✿✾✽✼✻✺✹✸✷☀ o O ＃♡ ┽┊﹎.εїз︷
   ✿‧:﹎｡❤‧:❉:‧ .｡.:*･❀●•♪.。‧:❉:‧ °º¤ø,¸¸,ø¤º°`°º¤ø*.:｡✿*ﾟ‘ﾟ･✿.｡.:*.:｡✿*ﾟ’ﾟ･✿.｡✎*εїз ↔ 
   ↕ ▪ → ︷╅╊✿ (¯`•._.• •._.•´¯)(¯`•¸•´¯) ❤`•.¸¸.•´´¯`•• .¸¸.•´¯`•.•●•۰• ••.•´¯`•.•• 
   ••.•´¯`•.••—¤÷(`[¤* *¤]´)÷¤——(•·÷[ ]÷·•)— 〓 ☆ ★┣┓┏┫×╰ノ◢ ◣ ◥ ◤ Ω ж ф юЮ ━╃ 
   ╄━ ┛┗ ┓┏ ◇ ◆ ※ .'. ☂.'.❤ ♥ 『』 〖〗▓ ► ◄ ? ? ▓ ╮╭ ╯╰ ァ ┱ ┲☃ ☎ ☏ ☺ ☻ ▧ ▨ ♨ ◘ 
   ◙ ♠ ♧ ♣ ▣▤ ▥ ▦ ▩ ⊕ ×º°”˜`”°º× ×º°”˜`”°º×»-(¯`v´¯)-» ×÷·.·´¯`·)» «(·´¯`·.·÷×*∩_∩* ⓛⓞⓥⓔ 
   ╬ ╠ ╣∷ ღ ☃ ❆ ￡ ∆ Š Õ Ő ő ∞ © ‡ † Ž ஜ ஒ ண இ ஆ ௰ ♪♪♫▫—(•·÷[ ]÷·•)— ·÷±‡±±‡±÷· 
   Oº°‘¨ ¨‘°ºO •°o.O O.o°• ¨°o.O O.o°¨—¤÷(`[¤* *¤]´)÷¤—•·.·´¯`·.·• •·.·´¯`·.·•´`·.(`·.¸ ¸.·´).·´`·» »-(¯`v´¯)-»█┗┛↘↙╰☆╮ ≠ ☜♥☞ ︻︼─一　
   ▄︻┻┳═一 -─═┳︻　∝╬══→　::======>>　☆═━┈┈━═☆　┣▇▇▇═─ ■◆◣◥▲◤ ◥〓∴ぷ▂▃▅▆█ 【】 
   ๑۞๑ ๑۩ﺴﺴ۩๑๑۩۞۩...¤¸¸.·´¯`·.¸·..>>--» [[]] «--<<..·.¸¸·´¯`·.¸¸¤... .•:*´¨`*:•.☆۩ ۞ ۩ ۩ ۞ ۩☆•:*´¨`*:•. 
   ❤`•.¸¸.•´´¯`••.¸¸.•´´¯`•´❤ ⊹⊱⋛⋋ ⋌⋚⊰⊹ 彡 ❝❞° ﹌﹎ ╱╲ ☁ ₪ ¡ Þ ௫ μ べ ☪ ☠ ╬ ╠ ╣∷ ღ :﹗/ ' _ < > `,·。≈ 
   {}~ ～() - √ $ * & # ※＊≮≯ ＋－× ÷﹢±／＝∫∮∝ ∧∨∥∠ ≌ ∽ ≦ ≧ ≒﹤﹥じ ①②③④⑤⑥⑦⑧⑨⑩ ⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳ 
   ⒶⒷⒸⒹⓐⓑⓒⓓⓔⓕ ⓖⓗⓘⓙⓚⓛ ⓜⓝⓞⓟⓠⓡ ⓢⓣⓤⓥⓦⓧ ⓨⓩ 凸(⊙▂⊙✖ )(づ￣ ³￣)づヾ（*⌒ヮ⌒*）ゞ ( c//'-}{-*\\x) (-'๏_๏'-) 
   (◐ o ◑ ) (⊙...⊙ )｡◕‿◕｡ ๏[-ิ_•ิ]๏(•ิ_•ิ)? \(•ิ_•ิ\) (/•ิ_•ิ)/ (︶︹︺)(*-`ω´- )人(ц｀ω´ц*)(●ゝω)ノヽ(∀＜●)(ㄒoㄒ)(>_<)⊙▂⊙ 
   ⊙０⊙ ⊙︿⊙　⊙ω⊙　⊙﹏⊙　⊙△⊙　⊙▽⊙ o(‧'''‧)o (◡‿◡✿) (◕‿◕✿) (◕〝◕) (∩_∩)ミ●﹏☉ミ (≧０≦) o(╥﹏╥)o 
   ㋀ ㋁㋂㋃㋄ ㋅ ㋆ ㋇ ㋈ ㋉ ㋊ ㋋ ㏠ ㏡ ㏢ ㏣ ㏤ ㏥ ㏦㏧㏨㏩ ㏪ ㏫ ㏬ ㏭ ㏮ ㏯ ㏰ ㏱ ㏲ ㏳ ㏴ ㏵ ㏶ 
㏷㏸㏹㏺ ㏻ ㏼ ㏽ ㏾ ㍘ ㍙ ㍚ ㍛ ㍜ ㍝ ㍞ ㍟ ㍠ ㍡㍢㍣㍤ ㍥ ㍦ ㍧ ㍨ ㍩ ㍪ ㍫ ㍬ ㍭ ㍮ ㍯㍰㊛㊚
"""


system_name = platform.system();


#Windows系统移动光标需使用
class COORD(ctypes.Structure):

    _fields_ = [("X", ctypes.c_short),("Y", ctypes.c_short)];

    def __init__(self,x = 0,y = 0):
        self.X = x;
        self.Y = y;

class SMALL_RECT(ctypes.Structure):

    _fields_ = [("Left",ctypes.c_short),("Top", ctypes.c_short),("Right", ctypes.c_short),("Bottom", ctypes.c_short)];

    def __init__(self):
        self.Left = 0;
        self.Top = 0;
        self.Right = 0;
        self.Bottom = 0;


class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    
    _fields_ = [
        ("dwSize", COORD),
        ("dwCursorPosition", COORD),
        ("wAttributes", ctypes.c_ushort),
        ("srWindow", SMALL_RECT),
        ("dwMaximumWindowSize",COORD)
    ];

    def __init__(self):
        self.dwSize = COORD();
        self.dwCursorPosition = COORD();
        self.wAttributes = 0;
        self.srWindow = SMALL_RECT();
        self.dwMaximumWindowSize = COORD();


class CONSOLE_CURSOR_INFO(ctypes.Structure):
    
    _fields_ = [("dwSize",ctypes.c_ulong),("bVisible",ctypes.c_bool)];

    def __init__(self,size = 0,visible = True):
        self.dwSize = size;
        self.bVisible = visible;


class ConsoleHandle:
    handle = 0;



global console_width,console_height;
console_width = 0;
console_height = 0;
console_background_color = 0;
console_foreground_color = 7;


if system_name == "Windows":
    import msvcrt

    console_width = 80;
    console_height = 25;

    STD_OUTPUT_HANDLE= -11;
    console_cache_handle1 = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE);# ConsoleHandle为0时修改，1时使用
    console_cache_handle2 = ctypes.windll.kernel32.CreateConsoleScreenBuffer(0x80000000|0x40000000,0x00000001|0x00000002,0,1,0);# ConsoleHandle为1时修改，0时使用
    
    console_size = COORD(console_width,console_height);
    ctypes.windll.kernel32.SetConsoleScreenBufferSize(console_cache_handle1,console_size);
    ctypes.windll.kernel32.SetConsoleScreenBufferSize(console_cache_handle2,console_size);

    cursor_info = CONSOLE_CURSOR_INFO(0,False);
    ctypes.windll.kernel32.SetConsoleCursorInfo(console_cache_handle1,id(cursor_info));
    ctypes.windll.kernel32.SetConsoleCursorInfo(console_cache_handle2,id(cursor_info));


    
elif system_name == "Linux":
    import curses

    #console_width = 80;
    #console_height = 25;

    stdscr = curses.initscr();
    stdscr.keypad(True);

    curses.start_color();#获取颜色curses.color_pair(Color.BLACK.value);
    curses.curs_set(0);
    curses.noecho();
    curses.cbreak();

    #stdscr.resize(console_height,console_width);
    console_height,console_width = stdscr.getmaxyx();




class Color():
    
    if system_name == "Windows":
        FORE_BLACK = 0;
        FORE_RED = 0x0004;
        FORE_GREEN = 0x0002;
        FORE_YELLOW = FORE_RED | FORE_GREEN;
        FORE_BLUE = 0x0001;
        FORE_MAGENTA = FORE_RED | FORE_BLUE;
        FORE_CYAN = FORE_GREEN | FORE_BLUE;
        FORE_WHITE = FORE_RED | FORE_GREEN | FORE_BLUE;

        BACK_BLACK = 0;
        BACK_RED = 0x0040;
        BACK_GREEN = 0x0020;
        BACK_YELLOW = BACK_RED | BACK_GREEN;
        BACK_BLUE = 0x0010;
        BACK_MAGENTA = BACK_RED | BACK_BLUE;
        BACK_CYAN = BACK_GREEN | BACK_BLUE;
        BACK_WHITE = BACK_RED | BACK_GREEN | BACK_BLUE;


    elif system_name == "Linux":
        color_pair = {};
        color_pair_count = 0;


    FORE = 0;
    BACK = 1;

    BLACK = 0;
    RED = 1;
    GREEN = 2;
    YELLOW = 3;
    BLUE = 4;
    MAGENTA = 5;
    CYAN = 6;
    WHITE = 7;



    @staticmethod
    def get_color(*color):
        if system_name == "Windows":
            fore = Color.FORE_WHITE;
            back = Color.BACK_BLACK;

            color_length = len(color);

            if color_length == 0:
                return 0;

            if color[Color.FORE] == Color.BLACK:
                fore = Color.FORE_BLACK;
            elif color[Color.FORE] == Color.RED:
                fore = Color.FORE_RED;
            elif color[Color.FORE] == Color.GREEN:
                fore = Color.FORE_GREEN;
            elif color[Color.FORE] == Color.YELLOW:
                fore = Color.FORE_YELLOW;
            elif color[Color.FORE] == Color.BLUE:
                fore = Color.FORE_BLUE;
            elif color[Color.FORE] == Color.MAGENTA:
                fore = Color.FORE_MAGENTA;
            elif color[Color.FORE] == Color.CYAN:
                fore = Color.FORE_CYAN;
            elif color[Color.FORE] == Color.WHITE:
                fore = Color.FORE_WHITE;

            if color_length < 2:
                return [fore];

            if color[Color.BACK] == Color.BLACK:
                back = Color.BACK_BLACK;
            elif color[Color.BACK] == Color.RED:
                back = Color.BACK_RED;
            elif color[Color.BACK] == Color.GREEN:
                back = Color.BACK_GREEN;
            elif color[Color.BACK] == Color.YELLOW:
                back = Color.BACK_YELLOW;
            elif color[Color.BACK] == Color.BLUE:
                back = Color.BACK_BLUE;
            elif color[Color.BACK] == Color.MAGENTA:
                back = Color.BACK_MAGENTA;
            elif color[Color.BACK] == Color.CYAN:
                back = Color.BACK_CYAN;
            elif color[Color.BACK] == Color.WHITE:
                back = Color.BACK_WHITE;

            return [fore,back];

        elif system_name == "Linux":
            
            color_length = len(color);

            if color_length == 1:
                return curses.color_pair(color[Color.FORE]);
            elif color_length == 0:
                return 0;

            color_name = str(color[Color.FORE]) + str(color[Color.BACK]);
            if color_name in Color.color_pair:
                return Color.color_pair[color_name];
            else:
                curses.init_pair(Color.color_pair_count + 10,color[Color.FORE],color[Color.BACK]);
                Color.color_pair[color_name] = curses.color_pair(Color.color_pair_count + 10);
                Color.color_pair_count += 1;
                return Color.color_pair[color_name];
        



def get_width():
    return console_width;


def get_height():
    return console_height;


def get_max_width():
    if system_name == "Windows":
        pass;
    elif system_name == "Linux":
        console_width = stdscr.getmaxyx()[1];
    return get_width();


def get_max_height():
    if system_name == "Windows":
        pass;
    elif system_name == "Linux":
        console_height = stdscr.getmaxyx()[0];
    return get_height();


def get_cursor_x():
    if system_name == "Windows":
        pass;
    elif system_name == "Linux":
        return stdscr.getyx()[1];


def get_cursor_y():
    if system_name == "Windows":
        pass;
    elif system_name == "Linux":
        return stdscr.getyx()[0];


def pause():
    if system_name == "Windows":
        os.system("pause");
    elif system_name == "Linux":
        curses.nocbreak();
        stdscr.keypad(False);
        curses.echo();
        curses.endwin();
    elif system_name == "Java":
        return;



def refresh():
    if system_name == "Windows":
        if ConsoleHandle.handle == 0:
            ConsoleHandle.handle = 1;
            ctypes.windll.kernel32.SetConsoleActiveScreenBuffer(console_cache_handle1);
        elif ConsoleHandle.handle == 1:
            ConsoleHandle.handle = 0;
            ctypes.windll.kernel32.SetConsoleActiveScreenBuffer(console_cache_handle2);

    elif system_name == "Linux":
        stdscr.refresh();



def move_cursor(x,y):
    if system_name == "Windows":
        position = COORD(int(x),int(y));
        ctypes.windll.kernel32.SetConsoleCursorPosition(console_cache_handle1,position);
    elif system_name == "Linux":
        print("\033[" + str(int(y)) + ";" + str(int(x)) + "H");
    elif system_name == "Java":
        return;


def move_cache_cursor(x,y):
    if system_name == "Windows":
        position = COORD(int(x),int(y));
        
        if ConsoleHandle.handle == 0:
            ctypes.windll.kernel32.SetConsoleCursorPosition(console_cache_handle1,position);
        elif ConsoleHandle.handle == 1:
            ctypes.windll.kernel32.SetConsoleCursorPosition(console_cache_handle2,position);

    elif system_name == "Linux":
        if x >= 0 and x < get_max_width() and y >= 0 and y < get_max_height():
            stdscr.move(y,x);
    elif system_name == "Java":
        return;


#color第一个为前景色，第二个为背景色。
def add_str(text,*color):

    color_length = len(color);

    if color_length > 0 and color_length < 2:
        text_color = Color.get_color(color[Color.FORE]);
    elif color_length >= 2:
        text_color = Color.get_color(color[Color.FORE],color[Color.BACK]);
    elif color_length <= 0:
        text_color = Color.get_color(Color.WHITE,Color.BLACK);


    if system_name == "Windows":
        if ConsoleHandle.handle == 0:
            ctypes.windll.kernel32.SetConsoleTextAttribute(console_cache_handle1,text_color[Color.FORE] | text_color[Color.BACK]);
            ctypes.windll.kernel32.WriteConsoleW(console_cache_handle1, text, len(text), 0, 0);
        elif ConsoleHandle.handle == 1:
            ctypes.windll.kernel32.SetConsoleTextAttribute(console_cache_handle2,text_color[Color.FORE] | text_color[Color.BACK]);
            ctypes.windll.kernel32.WriteConsoleW(console_cache_handle2, text, len(text), 0, 0);
            
    elif system_name == "Linux":
        cursor_x = get_cursor_x();
        cursor_y = get_cursor_y();
        max_width = get_max_width();
        max_height = get_max_height();
        if cursor_x >= 0 and cursor_x + len(text) < max_width and cursor_y >= 0 and cursor_y < max_height:
            stdscr.addstr(text,text_color);

"""
def add_str(text):
    add_str(text,[console_foreground_color,console_background_color]);
"""

def clear():
    if system_name == "Windows":
        os.system("cls");
        return;
    elif system_name == "Linux":
        print("\033[2J")
        # stdscr.clear();
        return;
    elif system_name == "Java":
        return;


def clear_cache():

    if system_name == "Windows":
        coord = COORD();
        chars_written = ctypes.c_ulong();

        info = CONSOLE_SCREEN_BUFFER_INFO();
        #ctypes.windll.kernel32.GetConsoleScreenBufferInfo(console_cache_handle1,info);
        #console_size = info.dwSize.X * info.dwSize.Y;
        #console_size = 80 * 25;

        text = "                                                                            ";

        try:
            if ConsoleHandle.handle == 0:
                ctypes.windll.kernel32.FillConsoleOutputCharacterA(console_cache_handle1,text,console_height, coord, id(chars_written));
                ctypes.windll.kernel32.FillConsoleOutputAttribute(console_cache_handle1, info.wAttributes, console_size, coord, id(chars_written));
            elif ConsoleHandle.handle == 1:
                ctypes.windll.kernel32.FillConsoleOutputCharacterA(console_cache_handle2,text,console_height, coord, id(chars_written));
                ctypes.windll.kernel32.FillConsoleOutputAttribute(console_cache_handle2, info.wAttributes, console_size, coord, id(chars_written));

            """
            i = 0;

            move_cache_cursor(0,0);
            if ConsoleHandle.handle == 0:
                while i < console_height:
                    ctypes.windll.kernel32.WriteConsoleW(console_cache_handle1, text, 80, 0, 0);
                    i += 1;

            elif ConsoleHandle.handle == 1:
                while i < console_height:
                    ctypes.windll.kernel32.WriteConsoleW(console_cache_handle2, text, 80, 0, 0);
                    i += 1;

            """
            
            
                
        except Exception as e:
            move_cache_cursor(0,23);
            ctypes.windll.kernel32.WriteConsoleW(console_cache_handle2, str(e), len(str(e)), 0, 0);


    elif system_name == "Linux":
        stdscr.clear();


def wrapper(func):
    if system_name == "Windows":
        func(0);
    elif system_name == "Linux":
        curses.wrapper(func);


def getch():
    if system_name == "Windows":
        return msvcrt.getch();
    elif system_name == "Linux":
        return chr(stdscr.getch());
    elif system_name == "Java":
        return;


def getch_number():
    if system_name == "Windows":
        return ord(msvcrt.getch());
    elif system_name == "Linux":
        return stdscr.getch();
    elif system_name == "Java":
        return;



def exit():
    if system_name == "Windows":
        pause();
    elif system_name == "Linux":
        pause();







