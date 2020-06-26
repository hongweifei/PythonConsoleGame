




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


if system_name == "Windows":
    import msvcrt

    STD_OUTPUT_HANDLE= -11;
    console_cache_handle1 = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE);# ConsoleHandle为0时修改，1时使用
    console_cache_handle2 = ctypes.windll.kernel32.CreateConsoleScreenBuffer(0x80000000|0x40000000,0x00000001|0x00000002,0,1,0);# ConsoleHandle为1时修改，0时使用
    
    console_size = COORD(80,25);
    ctypes.windll.kernel32.SetConsoleScreenBufferSize(console_cache_handle1,console_size);
    ctypes.windll.kernel32.SetConsoleScreenBufferSize(console_cache_handle2,console_size);

    cursor_info = CONSOLE_CURSOR_INFO(0,False);
    ctypes.windll.kernel32.SetConsoleCursorInfo(console_cache_handle1,id(cursor_info));
    ctypes.windll.kernel32.SetConsoleCursorInfo(console_cache_handle2,id(cursor_info));
    
elif system_name == "Linux":
    import curses
    from curses import wrapper

    stdscr = curses.initscr();
    curses.noecho();
    curses.cbreak();
    stdscr.keypad(True)


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



def move_cursor(x:int,y:int):
    if system_name == "Windows":
        position = COORD(int(x),int(y));
        ctypes.windll.kernel32.SetConsoleCursorPosition(console_cache_handle1,position);
    elif system_name == "Linux":
        print("\033[" + y + ";" + x + "H");
    elif system_name == "Java":
        return;


def move_cache_cursor(x:int,y:int):
    if system_name == "Windows":
        position = COORD(int(x),int(y));
        
        if ConsoleHandle.handle == 0:
            ctypes.windll.kernel32.SetConsoleCursorPosition(console_cache_handle1,position);
        elif ConsoleHandle.handle == 1:
            ctypes.windll.kernel32.SetConsoleCursorPosition(console_cache_handle2,position);

    elif system_name == "Linux":
        curses.move(y,x);
    elif system_name == "Java":
        return;


def add_str(text):
    if system_name == "Windows":
        if ConsoleHandle.handle == 0:
            ctypes.windll.kernel32.WriteConsoleW(console_cache_handle1, text, len(text), 0, 0);
        elif ConsoleHandle.handle == 1:
            ctypes.windll.kernel32.WriteConsoleW(console_cache_handle2, text, len(text), 0, 0);
    elif system_name == "Linux":
        stdscr.addstr(0, 0, text);



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
                ctypes.windll.kernel32.FillConsoleOutputCharacterA(console_cache_handle1,text,25, coord, id(chars_written));
                ctypes.windll.kernel32.FillConsoleOutputAttribute(console_cache_handle1, info.wAttributes, console_size, coord, id(chars_written));
            elif ConsoleHandle.handle == 1:
                ctypes.windll.kernel32.FillConsoleOutputCharacterA(console_cache_handle2,text,25, coord, id(chars_written));
                ctypes.windll.kernel32.FillConsoleOutputAttribute(console_cache_handle2, info.wAttributes, console_size, coord, id(chars_written));

            """
            i = 0;

            move_cache_cursor(0,0);
            if ConsoleHandle.handle == 0:
                while i < 25:
                    ctypes.windll.kernel32.WriteConsoleW(console_cache_handle1, text, 80, 0, 0);
                    i += 1;

            elif ConsoleHandle.handle == 1:
                while i < 25:
                    ctypes.windll.kernel32.WriteConsoleW(console_cache_handle2, text, 80, 0, 0);
                    i += 1;

            """
            
            
                
        except Exception as e:
            move_cache_cursor(0,23);
            ctypes.windll.kernel32.WriteConsoleW(console_cache_handle2, str(e), len(str(e)), 0, 0);


    elif system_name == "Linux":
        stdscr.clear();



def getch():
    if system_name == "Windows":
        return msvcrt.getch();
    elif system_name == "Linux":
        return stdscr.getch();
    elif system_name == "Java":
        return;



def exit():
    if system_name == "Windows":
        pause();
    elif system_name == "Linux":
        pause();







