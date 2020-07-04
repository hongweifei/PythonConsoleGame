




import os
from platform import system
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


system_name = system();


class SystemName():
    windows = "Windows";
    linux = "Linux";
    java = "Java";


class SystemClass():
    nt = "nt";
    posix = "posix";
    java = "java";



class Color():
    
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


    if system_name == SystemName.windows:
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


        @staticmethod
        def get_color(*color):
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


    elif system_name == SystemName.linux:
        color_pair = {};
        color_pair_count = 0;


        @staticmethod
        def get_color(*color):
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






if system_name == SystemName.windows:

    #库
    import struct


    #Windows系统移动光标需使用
    class COORD(ctypes.Structure):

        _fields_ = [("X", ctypes.c_short),("Y", ctypes.c_short)];

        """
        def __init__(self, *args, **kw):
                super().__init__(*args, **kw);
        """

        
        def __init__(self,x = 0,y = 0):
            self.X = x;
            self.Y = y;
        
    


    class SMALL_RECT(ctypes.Structure):

        _fields_ = [("Left",ctypes.c_short),("Top", ctypes.c_short),("Right", ctypes.c_short),("Bottom", ctypes.c_short)];

        def __init__(self, *args, **kw):
                super().__init__(*args, **kw)

        """
        def __init__(self):
            self.Left = 0;
            self.Top = 0;
            self.Right = 0;
            self.Bottom = 0;
        """

    
    class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
        
        _fields_ = [
            ("dwSize", COORD),
            ("dwCursorPosition", COORD),
            ("wAttributes", ctypes.c_ushort),
            ("srWindow", SMALL_RECT),
            ("dwMaximumWindowSize",COORD)
        ];

        
        def __init__(self, *args, **kw):
                super().__init__(*args, **kw);


        """
        def __init__(self):
            self.dwSize = COORD();
            self.dwCursorPosition = COORD();
            self.wAttributes = 0;
            self.srWindow = SMALL_RECT();
            self.dwMaximumWindowSize = COORD();
        """
        


    class CONSOLE_CURSOR_INFO(ctypes.Structure):
        
        _fields_ = [("dwSize",ctypes.c_ulong),("bVisible",ctypes.c_bool)];

        def __init__(self,size = 0,visible = True):
            self.dwSize = size;
            self.bVisible = visible;



    class ConsoleScreenBuffer:
        GENERIC_READ = 0x80000000;
        GENERIC_WRITE = 0x40000000;
        GENERIC_EXECUTE = 0x20000000;
        GENERIC_ALL = 0x10000000;


        FILE_SHARE_READ = 0x00000001;
        FILE_SHARE_WRITE = 0x00000002;


    
    kernel32 = ctypes.LibraryLoader(ctypes.WinDLL).kernel32;


    def pause():
        os.system("pause");


    def get_buffer_cursor_x(console_buffer):
        info = ctypes.create_string_buffer(22);
        kernel32.GetConsoleScreenBufferInfo(console_buffer,info);
        (bufx, bufy, cursor_x, cursor_y, wattr,left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", info);
        return cursor_x;


    def get_buffer_cursor_y(console_buffer):
        info = ctypes.create_string_buffer(22);
        kernel32.GetConsoleScreenBufferInfo(console_buffer,info);
        (bufx, bufy, cursor_x, cursor_y, wattr,left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", info);
        return cursor_y;



    def get_buffer_info(console_buffer):
        info = ctypes.create_string_buffer(22);
        kernel32.GetConsoleScreenBufferInfo(console_buffer,info);

        return struct.unpack("hhhhHhhhhhh", info);

    

    def get_buffer_width(console_buffer):
        info = get_buffer_info(console_buffer);
        return info[0];


    def get_buffer_height(console_buffer):
        info = get_buffer_info(console_buffer);
        return info[1];


    def get_buffer_max_width(console_buffer):
        info = get_buffer_info(console_buffer);
        return info[9];


    def get_buffer_max_height(console_buffer):
        info = get_buffer_info(console_buffer);
        return info[10];




    def set_buffer_size(console_buffer,width,height):
        size = COORD(width,height);
        ctypes.windll.kernel32.SetConsoleScreenBufferSize(console_buffer,size);


    def set_buffer(console_buffer):
        ctypes.windll.kernel32.SetConsoleActiveScreenBuffer(console_buffer);


    def MoveBufferCursor(console_buffer,x:int,y:int):
        position = COORD(x,y);
        ctypes.windll.kernel32.SetConsoleCursorPosition(console_buffer,position);

    
    #color第一个为前景色，第二个为背景色。
    def add_str_to_buffer(console_buffer,text:str,*color:int):

        color_length = len(color);

        if color_length > 0 and color_length < 2:
            text_color = Color.get_color(color[Color.FORE]);
        elif color_length >= 2:
            text_color = Color.get_color(color[Color.FORE],color[Color.BACK]);
        elif color_length <= 0:
            text_color = Color.get_color(Color.WHITE,Color.BLACK);


        ctypes.windll.kernel32.SetConsoleTextAttribute(console_buffer,text_color[Color.FORE] | text_color[Color.BACK]);
        ctypes.windll.kernel32.WriteConsoleW(console_buffer, text, len(text), 0, 0);


    def clear_buffer(console_buffer):

        coord = COORD(0,0);
        chars_written = ctypes.c_ulong();
        info = get_buffer_info(console_buffer);
        text = "                                                                            ";
        ctypes.windll.kernel32.FillConsoleOutputCharacterA(console_buffer,text,info.dwSize.Y, coord, id(chars_written));

    




elif system_name == SystemName.linux:
    import curses


    



class ConsoleCacheBuffer:


    clear_text = "                                                                            ";


    if system_name == SystemName.windows:
        
        
        def __init__(self,width = 80,height = 25):
            super().__init__();

            self.buffer = ctypes.windll.kernel32.CreateConsoleScreenBuffer(ConsoleScreenBuffer.GENERIC_READ|ConsoleScreenBuffer.GENERIC_WRITE,
            ConsoleScreenBuffer.FILE_SHARE_READ|ConsoleScreenBuffer.FILE_SHARE_WRITE,0,1,0);

            set_buffer_size(self.buffer,width,height);
            
            info = get_buffer_info(self.buffer);
            self.width = info[0];
            self.height = info[1];
            self.curosr_x = info[2];
            self.curosr_y = info[3];
            self.max_width = info[9];
            self.max_height = info[10];


        

        def updata(self):
            #bufx, bufy, cursor_x, cursor_y, wattr,left, top, right, bottom, maxx, maxy
            info = get_buffer_info(self.buffer);

            self.width = info[0];
            self.height = info[1];
            self.curosr_x = info[2];
            self.curosr_y = info[3];
            #self.wAttributes = info[4];
            #self.left = info[5];
            #self.top = info[6];
            #self.right = info[7];
            #self.bottom = info[8];
            self.max_width = info[9];
            self.max_height = info[10];

        
        def active(self):
            set_buffer(self.buffer);

        
        def set_cursor_info(self,size = 0,visible = False):
            cursor_info = CONSOLE_CURSOR_INFO(size,visible);
            kernel32.SetConsoleCursorInfo(self.buffer,id(cursor_info));

        
        def set_size(self,width,height):
            size = COORD(width,height);
            kernel32.SetConsoleScreenBufferSize(self.buffer,size);
            self.width = width;
            self.height = height;

        
        def set_cursor_position(self,x:int,y:int):
            MoveBufferCursor(self.buffer,x,y);
            self.curosr_x = x;
            self.curosr_y = y;


        def move_cursor(self,x:int,y:int):
            MoveBufferCursor(self.buffer,x,y);
            self.curosr_x = x;
            self.curosr_y = y;


        def clear(self):
            coord = COORD(0,0);
            chars_written = ctypes.c_ulong();
            console_size = self.width * self.height;
            ctypes.windll.kernel32.FillConsoleOutputCharacterA(self.buffer, ConsoleCacheBuffer.clear_text, self.height, coord, id(chars_written));
            ctypes.windll.kernel32.FillConsoleOutputAttribute(self.buffer, 0, console_size, coord, id(chars_written));
            self.updata();




    elif system_name == SystemName.linux:
        


        def __init__(self,width = 80,height = 25):
            super().__init__();

            self.buffer = curses.newwin(height,width);
    
    








if system_name == SystemName.windows:

    import msvcrt

    STD_OUTPUT_HANDLE= -11;



    class ConsoleHandle:
        handle = 0;


    console_background_color = 0;
    console_foreground_color = 7;


    console_buffer_handle1 = ConsoleCacheBuffer();
    console_buffer_handle2 = ConsoleCacheBuffer();

    console_buffer_handle1.set_cursor_info(0,False);
    console_buffer_handle2.set_cursor_info(0,False);


    def buffer_info_updata():
        if ConsoleHandle.handle == 0:
            console_buffer_handle1.updata();
        elif ConsoleHandle.handle == 1:
            console_buffer_handle2.updata();


    def get_width():
        if ConsoleHandle.handle == 0:
            return console_buffer_handle1.width;
        elif ConsoleHandle.handle == 1:
            return console_buffer_handle2.width;


    def get_height():
        if ConsoleHandle.handle == 0:
            return console_buffer_handle1.height;
        elif ConsoleHandle.handle == 1:
            return console_buffer_handle2.height;


    def get_max_width():
        if ConsoleHandle.handle == 0:
            return console_buffer_handle1.max_width;
        elif ConsoleHandle.handle == 1:
            return console_buffer_handle2.max_width;


    def get_max_height():
        if ConsoleHandle.handle == 0:
            return console_buffer_handle1.max_height;
        elif ConsoleHandle.handle == 1:
            return console_buffer_handle2.max_height;


    def get_cursor_x():
        if ConsoleHandle.handle == 0:
            return console_buffer_handle1.cursor_x;
        elif ConsoleHandle.handle == 1:
            return console_buffer_handle2.cursor_x;


    def get_cursor_y():
        if ConsoleHandle.handle == 0:
            return console_buffer_handle1.cursor_y;
        elif ConsoleHandle.handle == 1:
            return console_buffer_handle2.cursor_y;





    def refresh():
        if ConsoleHandle.handle == 0:
            ConsoleHandle.handle = 1;
            console_buffer_handle1.active();
        elif ConsoleHandle.handle == 1:
            ConsoleHandle.handle = 0;
            console_buffer_handle2.active();

        buffer_info_updata();




    def move_cursor(x,y):
        console_buffer_handle1.move_cursor(x,y);


    def move_buffer_cursor(x,y):
        
        if ConsoleHandle.handle == 0:
            console_buffer_handle1.move_cursor(x,y);
        elif ConsoleHandle.handle == 1:
            console_buffer_handle2.move_cursor(x,y);



    #color第一个为前景色，第二个为背景色。
    def add_str(text,*color):

        color_length = len(color);

        if color_length > 0 and color_length < 2:
            text_color = Color.get_color(color[Color.FORE]);
        elif color_length >= 2:
            text_color = Color.get_color(color[Color.FORE],color[Color.BACK]);
        elif color_length <= 0:
            text_color = Color.get_color(Color.WHITE,Color.BLACK);


        if ConsoleHandle.handle == 0:
            ctypes.windll.kernel32.SetConsoleTextAttribute(console_buffer_handle1.buffer,text_color[Color.FORE] | text_color[Color.BACK]);
            ctypes.windll.kernel32.WriteConsoleW(console_buffer_handle1.buffer, text, len(text), 0, 0);
        elif ConsoleHandle.handle == 1:
            ctypes.windll.kernel32.SetConsoleTextAttribute(console_buffer_handle2.buffer,text_color[Color.FORE] | text_color[Color.BACK]);
            ctypes.windll.kernel32.WriteConsoleW(console_buffer_handle2.buffer, text, len(text), 0, 0);
        

        buffer_info_updata();
            

    """
    def add_str(text):
        add_str(text,[console_foreground_color,console_background_color]);
    """

    def clear():
        os.system("cls");


    def clear_buffer():


        if ConsoleHandle.handle == 0:
            console_buffer_handle1.clear();
        elif ConsoleHandle.handle == 1:
            console_buffer_handle2.clear();

        """
        i = 0;

        move_buffer_cursor(0,0);
        if ConsoleHandle.handle == 0:
            while i < console_height:
                ctypes.windll.kernel32.WriteConsoleW(console_buffer_handle1, text, 80, 0, 0);
                i += 1;

        elif ConsoleHandle.handle == 1:
            while i < console_height:
                ctypes.windll.kernel32.WriteConsoleW(console_buffer_handle2, text, 80, 0, 0);
                i += 1;

        """



    def wrapper(func):
        func(0);


    def getch():
        return msvcrt.getch();


    def getch_number():
        return ord(msvcrt.getch());





    




    



    
            



    

            
            


























    
elif system_name == SystemName.linux:

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


    def get_width():
        return console_width;


    def get_height():
        return console_height;


    def get_max_width():
        console_width = stdscr.getmaxyx()[1];
        return get_width();


    def get_max_height():
        console_height = stdscr.getmaxyx()[0];
        return get_height();


    def get_cursor_x():
        return stdscr.getyx()[1];


    def get_cursor_y():
        return stdscr.getyx()[0];


    def pause():
        curses.nocbreak();
        stdscr.keypad(False);
        curses.echo();
        curses.endwin();



    def refresh():
        stdscr.refresh();



    def move_cursor(x,y):
        print("\033[" + str(int(y)) + ";" + str(int(x)) + "H");



    def move_buffer_cursor(x,y):
        if x >= 0 and x < get_max_width() and y >= 0 and y < get_max_height():
            stdscr.move(y,x);


    #color第一个为前景色，第二个为背景色。
    def add_str(text,*color):

        color_length = len(color);

        if color_length > 0 and color_length < 2:
            text_color = Color.get_color(color[Color.FORE]);
        elif color_length >= 2:
            text_color = Color.get_color(color[Color.FORE],color[Color.BACK]);
        elif color_length <= 0:
            text_color = Color.get_color(Color.WHITE,Color.BLACK);


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
        print("\033[2J")
        # stdscr.clear();


    def clear_buffer():
        stdscr.clear();


    def wrapper(func):
        curses.wrapper(func);


    def getch():
        return chr(stdscr.getch());


    def getch_number():
        return stdscr.getch();






        

"""

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


"""


"""
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
            ctypes.windll.kernel32.SetConsoleActiveScreenBuffer(console_buffer_handle1);
        elif ConsoleHandle.handle == 1:
            ConsoleHandle.handle = 0;
            ctypes.windll.kernel32.SetConsoleActiveScreenBuffer(console_buffer_handle2);

    elif system_name == "Linux":
        stdscr.refresh();


"""



"""

def move_cursor(x,y):
    if system_name == "Windows":
        position = COORD(int(x),int(y));
        ctypes.windll.kernel32.SetConsoleCursorPosition(console_buffer_handle1,position);
    elif system_name == "Linux":
        print("\033[" + str(int(y)) + ";" + str(int(x)) + "H");
    elif system_name == "Java":
        return;


def move_buffer_cursor(x,y):
    if system_name == "Windows":
        position = COORD(int(x),int(y));
        
        if ConsoleHandle.handle == 0:
            ctypes.windll.kernel32.SetConsoleCursorPosition(console_buffer_handle1,position);
        elif ConsoleHandle.handle == 1:
            ctypes.windll.kernel32.SetConsoleCursorPosition(console_buffer_handle2,position);

    elif system_name == "Linux":
        if x >= 0 and x < get_max_width() and y >= 0 and y < get_max_height():
            stdscr.move(y,x);
    elif system_name == "Java":
        return;

"""


"""
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
            ctypes.windll.kernel32.SetConsoleTextAttribute(console_buffer_handle1,text_color[Color.FORE] | text_color[Color.BACK]);
            ctypes.windll.kernel32.WriteConsoleW(console_buffer_handle1, text, len(text), 0, 0);
        elif ConsoleHandle.handle == 1:
            ctypes.windll.kernel32.SetConsoleTextAttribute(console_buffer_handle2,text_color[Color.FORE] | text_color[Color.BACK]);
            ctypes.windll.kernel32.WriteConsoleW(console_buffer_handle2, text, len(text), 0, 0);
            
    elif system_name == "Linux":
        cursor_x = get_cursor_x();
        cursor_y = get_cursor_y();
        max_width = get_max_width();
        max_height = get_max_height();
        if cursor_x >= 0 and cursor_x + len(text) < max_width and cursor_y >= 0 and cursor_y < max_height:
            stdscr.addstr(text,text_color);

"""


"""
def add_str(text):
    add_str(text,[console_foreground_color,console_background_color]);
"""


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


def clear_buffer():

    if system_name == "Windows":
        coord = COORD();
        chars_written = ctypes.c_ulong();

        info = CONSOLE_SCREEN_BUFFER_INFO();
        #ctypes.windll.kernel32.GetConsoleScreenBufferInfo(console_buffer_handle1,info);
        #console_size = info.dwSize.X * info.dwSize.Y;
        #console_size = 80 * 25;

        text = "                                                                            ";

        try:
            if ConsoleHandle.handle == 0:
                ctypes.windll.kernel32.FillConsoleOutputCharacterA(console_buffer_handle1,text,console_height, coord, id(chars_written));
                ctypes.windll.kernel32.FillConsoleOutputAttribute(console_buffer_handle1, info.wAttributes, console_size, coord, id(chars_written));
            elif ConsoleHandle.handle == 1:
                ctypes.windll.kernel32.FillConsoleOutputCharacterA(console_buffer_handle2,text,console_height, coord, id(chars_written));
                ctypes.windll.kernel32.FillConsoleOutputAttribute(console_buffer_handle2, info.wAttributes, console_size, coord, id(chars_written));


            
            i = 0;

            move_buffer_cursor(0,0);
            if ConsoleHandle.handle == 0:
                while i < console_height:
                    ctypes.windll.kernel32.WriteConsoleW(console_buffer_handle1, text, 80, 0, 0);
                    i += 1;

            elif ConsoleHandle.handle == 1:
                while i < console_height:
                    ctypes.windll.kernel32.WriteConsoleW(console_buffer_handle2, text, 80, 0, 0);
                    i += 1;

            
            
            
                
        except Exception as e:
            move_buffer_cursor(0,23);
            ctypes.windll.kernel32.WriteConsoleW(console_buffer_handle2, str(e), len(str(e)), 0, 0);


    elif system_name == "Linux":
        stdscr.clear();

"""


"""
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



"""



