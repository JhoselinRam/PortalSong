import simpleaudio as sa
import time

def main():
    soundFile = "sound.wav"
    wave = sa.WaveObject.from_wave_file(soundFile)
    screen = Screen(111,37)

    screen.drawArea()
    print("")
    print("Adjust the screen/font size in such a way that you can only see the rectangle above without distortion, then press <Enter>")
    input("")

    screen.rectangle(0,0,55,37)
    screen.rectangle(55,0,56,17)
    #screen.image(63,17,ApertureImage)

    screen.setCursor(2,1)

    step = 0
    music = wave.play()
    timer = time.time()
    for line in lyrics:
        x = screen.cursor[1]
        y = screen.cursor[0]
        screen.setCursor(2, y+1)
        while True:
            if time.time()-timer > timing[step]:
                screen.text(line)

                if line == "%":
                    screen.image(1,1, clearlyrics)
                    screen.setCursor(2,1)

                setImage(screen, step)
                setCredits(screen, step)

                screen.draw()
                step += 1
                break
        screen.draw()








#-------------------------------------------------------------------------------

class Screen():
    def __init__(self, w, h):
        self.width  = int(w)
        self.height = int(h)
        self.cursor = [1,1]

        self._setBuffer()
        self.setCursor(1,1)

#-----------------------
    def _setBuffer(self):
        self.buffer = []

        for i in range(self.height):
            self.buffer.append([])
            for j in range(self.width):
                self.buffer[i].append(" ")

#---------------------------
    def draw(self):
        print("\n\n\n\n")
        for line in self.buffer:
            for pixel in line:
                print(pixel, end = "")
            print("")

#-------------------
    def clear(self):
        for j in range(self.height):
            for i in range(self.width):
                self.buffer[j][i] = " "

#-----------------------------------
    def rectangle(self, x, y, w, h):
        for i in range(x,x+w):
            self.buffer[y][i] = "-"
            self.buffer[y+h-1][i] = "-"

        for j in range(y+1, y+h-1):
            self.buffer[j][x] = "|"
            self.buffer[j][x+w-1] = "|"

#----------------------
    def drawArea(self):
        self.rectangle(0,0, self.width, self.height)
        self.draw()
        self.clear()

#-------------------
    def image(self, x, y, image):
        h = len(image)
        w = len(image[0])

        for j in range(h):
            for i in range(w):
                self.buffer[y+j][x+i] = image[j][i]

#------------------------------
    def setCursor(self, x, y):
        self.buffer[self.cursor[0]][self.cursor[1]] = " "
        self.cursor[0] = y
        self.cursor[1] = x
        self.buffer[self.cursor[0]][self.cursor[1]] = "_"

#------------------------
    def text(self, text):
        x = self.cursor[1]
        y = self.cursor[0]
        l = len(text)
        self.setCursor(x+l, y)

        for i in range(l):
            self.buffer[y][x+i] = text[i]

#-------------------------------------------------------------------------------

def setImage(screen, step):
    if step == 9:
        screen.image(63,17,ApertureImage)
    elif step == 13:
        screen.image(63,17,RadiationImage)
    elif step == 15:
        screen.image(63,17,ApertureImage)
    elif step == 19:
        screen.image(63,17,AtomImage)
    elif step == 21:
        screen.image(63,17,ApertureImage)
    elif step == 33:
        screen.image(63,17,HeartImage)
    elif step == 34:
        screen.image(63,17,ExplotionImage)
    elif step == 35:
        screen.image(63,17,FireImage)
    elif step == 37:
        screen.image(63,17,CheckImage)
    elif step == 42:
        screen.image(63,17,ExplotionImage)
    elif step == 43:
        screen.image(63,17,AtomImage)
    elif step == 44:
        screen.image(63,17,ApertureImage)
    elif step == 57:
        screen.image(63,17,MesaImage)
    elif step == 59:
        screen.image(63,17,CakeImage)
    elif step == 61:
        screen.image(63,17,GladosImage)
    elif step == 62:
        screen.image(63,17, RadiationImage)
    elif step == 63:
        screen.image(63,17, ApertureImage)
    elif step == 65:
        screen.image(63,17, AtomImage)
    elif step == 66:
        screen.image(63,17, ExplotionImage)
    elif step == 67:
        screen.image(63,17, ApertureImage)


def setCredits(screen, step):
    for line in creditsText[step]:
        addCredits(line)

    screen.image(56 , 1, creditsImage)


def addCredits(text):
    for i in range(14):
        creditsImage[i] = creditsImage[i+1]

    creditsImage[14] = text




ApertureImage = [
"             .,-:;//;:=,                ",
"         . :H@@@MM@M#H/.,+%;,           ",
"      ,/X+ +M@@M@MM%=,-%HMMM@X/,        ",
"     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-     ",
"    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.   ",
"  ,%MM@@MH ,@%=            .---=-=:=,.  ",
"  -@&@@@MX .,              -%HX$$%%%+;  ",
" =-./@M@M$                  .;@MMMM@MM: ",
" X@/ -$MM/                    .+MM@@@M$ ",
",@M@H: :@:                    . -X&@@@@-",
",@@@MMX, .                    /H- ;@M@M=",
".H@@@@M@+,                    %MM+..%#$.",
" /MMMM@MMH/.                  XM@MH; -; ",
"  /%+%$XHH@$=              , .H@@@@MX,  ",
"   .=--------.           -%H.,@@@@@MX,  ",
"   .%MM@@@HHHXX$$$%+- .:$MMX -M@@MM%.   ",
"     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=     ",
"       =%@M@M#@$-.=$@MM@@@M; %M%=       ",
"         ,:+$+-,/H#MMMMMMM@- -,         ",
"               =++%%%%+/:-.             "
]

RadiationImage = [
"             =+$HM####@H%;,             ",
"          /H###############M$,          ",
"          ,@################+           ",
"           .H##############+            ",
"             X############/             ",
"              $##########/              ",
"               %########/               ",
"                /X/;;+X/                ",
"                                        ",
"                 -XHHX-                 ",
"                ,######,                ",
"#############X  .M####M.  X#############",
"##############-   -//-   -##############",
"X##############%,      ,+##############X",
"-##############X        X##############-",
" %############%          %############% ",
"  %##########;            ;##########%  ",
"   ;#######M=              =M#######;   ",
"    .+M###@,                ,@###M+.    ",
"       :XH.                  .HX:       "
]

AtomImage = [
"                 =/;;/-                 ",
"                +:    //                ",
"               /;      /;               ",
"              -X        H.              ",
".//;;;:;;-,   X=        :+   .-;:=;:;%;.",
"M-       ,=;;;#:,      ,:#;;:=,       ,@",
":%           :%.=/++++/=.$=           %=",
" ,%;         %/:+/;,,/++:+/         ;+. ",
"   ,+/.    ,;@+,        ,%H;,    ,/+,   ",
"      ;+;;/= @.  .H##X   -X :///+;      ",
"      ;+=;;;.@,  .XM@$.  =X.//;=%/.     ",
"   ,;:      :@%=        =$H:     .+%-   ",
" ,%=         %;-///==///-//         =%, ",
";+           :%-;;;;;;;;-X-           +:",
"@-      .-;;;;M-        =M/;;;-.      -X",
" :;;::;;-.    %-        :+    ,-;;-;:== ",
"              ,X        H.              ",
"               ;/      %=               ",
"                //    +;                ",
"                 ,////,                 "
]

HeartImage = [
"                          .,---.        ",
"                        ,/XM#MMMX;,     ",
"                      -%##########M%,   ",
"                     -@######%  $###@=  ",
"      .,--,         -H#######$   $###M: ",
"   ,;$M###MMX;     .;##########$;HM###X=",
",/@###########H=      ;################+",
"-+#############M/,      %##############+",
"%M###############=      /##############:",
"H################      .M#############;.",
"@###############M      ,@###########M:. ",
"X################,      -$=X#######@:   ",
"/@##################%-     +######$-    ",
".;##################X     .X#####+,     ",
" .;H################/     -X####+.      ",
"   ,;X##############,       .MM/        ",
"      ,:+$H@M#######M#$-    .$$=        ",
"           .,-=;+$@###X:    ;/=.        ",
"                  .,/X$;   .::,         ",
"                      .,    ..          "
]

FireImage = [
"                     -$-               ",
"                    .H##H,             ",
"                   +######+            ",
"                .+#########H.          ",
"              -$############@.         ",
"            =H###############@  -X:    ",
"          .$##################:  @#@-  ",
"     ,;  .M###################;  H###; ",
"   ;@#:  @###################@  ,#####:",
" -M###.  M#################@.  ;######H",
" M####-  +###############$   =@#######X",
" H####$   -M###########+   :#########M,",
"  /####X-   =########%   :M########@/. ",
"    ,;%H@X;   .$###X   :##MM@%+;:-     ",
"                 ..                    ",
"  -/;:-,.              ,,-==+M########H",
" -##################@HX%%+%%$%%%+:,,   ",
"   .-/H%%%+%%$H@###############M@+=:/+:",
"/XHX%:#####MH%=   ,---:;;;;/&&XHM,:###$",
"$@#MX %+;-                           . "
]

CheckImage = [
"                                     :X-",
"                                  :X### ",
"                                ;@####@ ",
"                              ;M######X ",
"                            -@########$ ",
"                          .$##########@ ",
"                         =M############-",
"                        +##############$",
"                      .H############$=. ",
"         ,/:         ,M##########M;.    ",
"      -+@###;       =##########M;       ",
"   =%M#######;     :#########M/         ",
"-$M###########;   :########/            ",
" ,;X###########; =#######$.             ",
"     ;H#########+######M=               ",
"       ,+#############+                 ",
"          /M########@-                  ",
"            ;M#####%                    ",
"              +####:                    ",
"               ,$M-                     "
]

ExplotionImage = [
"            .+                          ",
"             /M;                        ",
"              H#@:              ;,      ",
"              -###H-          -@/       ",
"               %####$.  -;  .%#X        ",
"                M#####+;#H :M#M.        ",
"..          .+/;%#############-         ",
" -/%H%+;-,    +##############/          ",
"    .:$M###MH$%+############X  ,--=;-   ",
"        -/H#####################H+=.    ",
"           .+#################X.        ",
"         =%M####################H;.     ",
"            /@###############+;;/%%;,   ",
"         -%###################$         ",
"       ;H######################M=       ",
"    ,%#####MH$%;+#####M###-/@####%      ",
"  :$H%+;=-      -####X.,H#   -+M##@-    ",
" .              ,###;    ;      =$##+   ",
"                .#H,               :XH, ",
"                 +                   .;-"
]

MesaImage = [
"           .-;+$XHHHHHHX$+;-.           ",
"        ,;X@@X%/;=----=:/%X@@X/,        ",
"      =$@@%=.              .=+H@X:      ",
"    -XMX:                      =XMX=    ",
"   /@@:                          =H@+   ",
"  %@X,                            .$@$  ",
" +@X.                               $@% ",
"-@@,                                .@@=",
"%@%                                  +@$",
"H@:                                  :@H",
"H@:         :HHHHHHHHHHHHHHHHHHX,    =@H",
"%@%         ;@M@@@@@@@@@@@@@@@@@H-   +@$",
"=@@,        :@@@@@@@@@@@@@@@@@@@@@= .@@:",
" +@X        :@@@@@@@@@@@@@@@M@@@@@@:%@% ",
"  $@$,      ;@@@@@@@@@@@@@@@@@M@@@@@@$. ",
"   +@@HHHHHHH@@@@@@@@@@@@@@@@@@@@@@@+   ",
"    =X@@@@@@@@@@@@@@@@@@@@@@@@@@@@X=    ",
"      :$@@@@@@@@@@@@@@@@@@@M@@@@$:      ",
"        ,;$@@@@@@@@@@@@@@@@@@X/-        ",
"           .-;+$XXHHHHHX$+;-.           "
]

CakeImage = [
"            ,:/+/-                      ",
"            /M/              .,-=;//;-  ",
"       .:/= ;MH/,    ,=/+%$XH@MM#@:     ",
"      -$##@+$###@H@MMM#######H:.    -/H#",
" .,H@H@ X######@ -H#####@+-     -+H###@X",
"  .,@##H;      +XM##M/,     =%@###@X;-  ",
"X%-  :M##########$.    .:%M###@%:       ",
"M##H,   +H@@@$/-.  ,;$M###@%,          -",
"M####M=,,---,.-%%H####M$:          ,+@##",
"@##################@/.         :%H##@$- ",
"M###############H,         ;HM##M$=     ",
"#################.    .=$M##M$=         ",
"################H..;XM##M$=          .:+",
"M###################@%=           =+@MH%",
"@#################M/.         =+H#X%=   ",
"=+M###############M,      ,/X#H+:,      ",
"  .;XM###########H=   ,/X#H+:;          ",
"     .=+HM#######M+/+HM@+=.             ",
"         ,:/%XM####H/.                  ",
"              ,.:=-.                    "
]

GladosImage = [
"       #+ @      # #              M#@   ",
" .    .X  X.%##@;# #   +@#######X. @H%  ",
"   ,==.   ,######M+  -#####%M####M-    #",
"  :H##M%:=##+ .M##M,;#####/+#######% ,M#",
" .M########=  =@#@.=#####M=M#######=  X#",
" :@@MMM##M.  -##M.,#######M#######. =  M",
"             @##..###:.    .H####. @@ X,",
"   ############: ###,/####;  /##= @#. M ",
"           ,M## ;##,@#M;/M#M  @# X#% X# ",
".%=   ######M## ##.M#:   ./#M ,M #M ,#$ ",
"##/         $## #+;#: #### ;#/ M M- @# :",
"#+ #M@MM###M-;M #:$#-##$H# .#X @ + $#. #",
"      ######/.: #%=# M#:MM./#.-#  @#: H#",
"+,.=   @###: /@ %#,@  ##@X #,-#@.##% .@#",
"#####+;/##/ @##  @#,+       /#M    . X, ",
"   ;###M#@ M###H .#M-     ,##M  ;@@; ###",
"   .M#M##H ;####X ,@#######M/ -M###$  -H",
"    .M###%  X####H  .@@MM@;  ;@#M@      ",
"      H#M    /@####/      ,++.  / ==-,  ",
"               ,=/:, .+X@MMH@#H  #####$="
]

clearlyrics = []
for j in range(35):
    clearlyrics.append("")
    for i in range(53):
        clearlyrics[j] = f"{clearlyrics[j]} "

creditsImage = []
for j in range(15):
    creditsImage.append("")
    for i in range(54):
        creditsImage[j] = f"{creditsImage[j]} "

lyrics = [
"Forms FORM- 29827281- 12:",
"Test Assessment Report",
"",
"",
"This was a triumph.",
"I'm making a note here:",
"HUGE SUCCESS.",
"It's hard to overstate",
"my satisfaction.",
"Aperture Science",
"We do what we must",
"because we can.",
"For the good of all of us.",
"Except the ones who are dead.",
"",
"But there's no sense crying",
"over every mistake.",
"You just keep on trying",
"till you run out of cake.",
"And the Science gets done.",
"And you make a neat gun.",
"For the people who are",
"still alive.",
"",
"%",
"Forms FORM- 55551- 5:",
"Personnel File Addendum:",
"",
"Dear <<Subject Name Here>>,",
"",
"I'm not even angry.",
"I'm being so sincere right now.",
"Even though you broke my heart.",
"And killed me.",
"And tore me to pieces.",
"And threw every piece into a fire.",
"As they burned it hurt because",
"I was so happy for you!",
"Now these points of data",
"make a beautiful line.",
"And we're out of beta.",
"We're releasing on time.",
"So I'm GLaD. I got burned.",
"Think of all the things we learned",
"for the people who are",
"still alive.",
"",
"%",
"Forms FORM- 55551- 6:",
"Personnel File Addendum Addendum:",
"",
"One last thing:",
"",
"Go ahead and leave me.",
"I think I prefer to stay inside.",
"Maybe you'll find someone else",
"to help you.",
"Maybe Black Mesa...",
"THAT WAS A JOKE. HA HA. FAT CHANCE.",
"Anyway, this cake is great.",
"It's so delicious and moist.",
"Look at me still talking",
"when there's Science to do.",
"When I look out there,",
"it makes me GLaD I'm not you.",
"I've experiments to run.",
"There is research to be done.",
"On the people who are",
"still alive.",
"%",
"",
"",
"PS: And believe me I am",
"still alive.",
"PPS: I'm doing Science and I'm",
"still alive.",
"PPPS: I feel FANTASTIC and I'm",
"still alive.",
"",
"FINAL THOUGHT:",
"While you're dying I'll be",
"still alive.",
"",
"FINAL THOUGHT PS:",
"And when you're dead I will be",
"still alive.",
"",
"",
"STILL ALIVE",
"%",
"",
""
]

creditsText = [
["                                                      "],
["                                                      "],
["                                                      "],
["                                                      "],
["                                                      "],
[" >LIST PERSONNEL                                      ",
 "                                                      ",
 "                                                      ",
 " Guautam Babbar                                       "],
[" Ted Backman                                          ",
 " Kelly Bailey                                         ",
 " Jeff Balling                                         "],
[" Aaron Barber                                         ",
 " Jeep Barnett                                         ",
 " Jeremy Ben                                           "],
[" Dan Berger                                           ",
 " Yahn Bernier                                         ",
 " Ken Birdwel                                          "],
[" Derrick Birum                                        ",   #10
 " Mike Blaszczak                                       ",
 " Iestyn Bleasdale-Shepherd                            ",
 " Chris Bokitch                                        "],
[" Steve Bond                                           ",
 " Matt Boone                                           ",
 " Antoine Bourdon                                      ",
 " Jamaal Bradley                                       "],
[" Jason Brashill                                       ",
 " Charlie Brown                                        "],
[" Charlie Burgin                                       ",
 " Andrew Burke                                         ",
 " Augusta Butlin                                       ",
 " Julie Caldwell                                       "],
[" Dario Casali                                         ",
 " Chris Cliffe                                         ",
 " Phil Co                                              ",
 " John Cook                                            "],
[" Christen Coomer                                      "],
[" Greg Coomer                                          ",
 " Scoot Dalton                                         "],
[" Kerry Davis                                          ",
 " Jason Deakins                                        "],
[" Joe Demers                                           ",
 " Ariel Diaz                                           ",
 " Quintin Doroquez                                     "],
[" Jim Dose                                             ",
 " Chris Douglass                                       "],
[" Laura Dubuk                                          ",  #20
 " Mike Dunkle                                          "],
[" Mike Dussault                                        ",
 " Dhabih Eng                                           "],
[" Katie Engel                                          ",
 " Chet Faliszek                                        "],
[" Adrian Finol                                         ",
 " Bill Fletcher                                        "],
[" Moby Francke                                         ",
 " Stephane Gaudette                                    "],
[" Kathy Gehrig                                         "],
[" Vitally Genkin                                       ",
 " Paul Graham                                          "],
[" Chris Grinstead                                      "],
[" John Guthrie                                         ",
 " Aaron Halifax                                        "],
[" Reagan Halifax                                       "],
[" Leslie Hall                                          ",   #30
 " Jeff Hameluck                                        "],
[" Joe Han                                              ",
 " Don Holden                                           "],
[" Jason Holtman                                        ",
 " Gray Horsfield                                       ",
 " Keith Huggins                                        ",
 " Jim Hughes                                           ",
 " Jon Huisingh                                         ",
 " Brian Jacobson                                       "],
[" Lars Jungels                                         ",
 " Erik Johnson                                         ",
 " Jakob Jungels                                        ",
 " Rich Kaethler                                        "],
[" Steve Kalning                                        ",
 " Aaron Kearly                                         ",
 " Iikka Keranen                                        ",
 " David Kircher                                        "],
[" Eric Kirchmer                                        ",
 " Scoot Klintworth                                     ",
 " Alden Kroll                                          ",
 " Marc Laidlaw                                         ",
 " Jeff Lane                                            "],
[" Tim Larkin                                           ",
 " Dan LeFree                                           ",
 " Isabelle LeMay                                       ",
 " Tom Leonard                                          ",
 " Jeff Lind                                            ",
 " Doug Lombardi                                        "],
[" Biaca Loomis                                         ",
 " Richard Lord                                         ",
 " Realm Lovejoy                                        ",
 " Randy Lunde                                          "],
[" Scoot Lynch                                          ",
 " Ido Magal                                            ",
 " Mick Maggiore                                        "],
[" John McCaskey                                        ",
 " Patrick McClard                                      "],
[" Steve McClure                                        ",   #40
 " Hamish McKenzie                                      "],
[" Gary McTaggart                                       ",
 " Jason Mitchell                                       "],
[" Mike Morasky                                         ",
 " John Morello II                                      "],
[" Bryn Moslow                                          ",
 " Arsenio Navarro                                      "],
[" Gabe Newell                                          ",
 " Milton Ngan                                          ",
 " Jake Nicholson                                       "],
[" Martin Otten                                         ",
 " Nick Papineau                                        "],
[" Karen Prell                                          ",
 " Bay Raitt                                            "],
[" Tristan Reidford                                     "],
[" Alfred Reynolds                                      "],
[" Matt Rhoten                                          "],
[" Garret Rickey                                        "],   #50
[" Dave Riller                                          "],
[" Elan Ruskin                                          "],
[" Matthew Russell                                      "],
[" Jason Ruymen                                         "],
[" David Sawyer                                         ",
 " Marc Scaparro                                        ",
 " Wade Schin                                           ",
 " Matthew Scoot                                        "],
[" Aaron Seeler                                         ",
 " Jennifer Seeley                                      ",
 " Taylor Sherman                                       ",
 " Eric Smith                                           ",
 " Jeff Sorenser                                        ",
 " David Speyre                                         "],
[" Jay Stelly                                           ",
 " Jeremy Stone                                         ",
 " Eric Strand                                          ",
 " Kim Swift                                            "],
[" Kelly Thornton                                       ",
 " Eric Twelker                                         ",
 " Carl Uhlman                                          ",
 " Doug Valente                                         ",
 " Bill Van Buren                                       "],
[" Gabe Van Engel                                       ",
 " Alex Vlachos                                         ",
 " Robin Walker                                         ",
 " Joshua Weier                                         "],
[" Andrea Wicklund                                      ",     #60
 " Greg Winkler                                         ",
 " Erik Wolpaw                                          ",
 " Doug Wood                                            ",
 " Matt T. Wood                                         ",
 " Danika Wright                                        "],
[" Matt Wright                                          ",
 " Shawn Zabecki                                        ",
 " Torsten Zabka                                        ",
 "                                                      ",
 "                                                      ",
 "                                                      ",
 "                                                      "],
[" 'Still Alive' by:                                    ",
 " Jhonathan Coulton                                    ",
 "                                                      ",
 "                                                      ",
 "                                                      ",
 " Voices:                                              "],
[" Ellen McLain - GlaDos, Turrers                       "],
[" Mike Patton - THE ANGER SPHERE                       ",
 "                                                      ",
 "                                                      ",
 "                                                      ",
 "                                                      "],
[" Voice Casting:                                       "],
[" Shana Landsburg/Teri Fiddleman                       ",
 "                                                      ",
 "                                                      ",
 "                                                      ",
 "                                                      "],
[" Voice Recording:                                     ",
 " Pure Audio, Seattle, WA                              "],
["                                                      ",
 "                                                      ",
 "                                                      ",
 "                                                      ",
 " Voice recording                                      "],
[" scheduling and logistics:                            "],
[" Pat Cockburn, Pure Audio                             ",     #70
 "                                                      ",
 "                                                      ",
 "                                                      ",
 "                                                      "],
[" Translations :                                       "],
[" SDL                                                  "],
["                                                      "],
["                                                      "],
["                                                      ",
 "                                                      ",
 " Crack Legal Team:                                    "],
[" Liam Laverty                                         ",
 " Karl Quackenbush                                     "],
[" Kristen Boraas                                       ",
 " Kevin Rosenflield                                    "],
[" Alan Bruggeman                                       ",
 " Dennis Tessier                                       "],
["                                                      ",
 "                                                      ",
 "                                                      "],
[" Thanks for the use of their face:                    ",   #80
 " Alesia Glidewell - Chell                             "],
["                                                      ",
 "                                                      "],
["                                                      "],
[" Special thanks to everyone at:                       "],
[" Alienware                                            ",
 " ATI                                                  "],
[" Dell                                                 ",
 " Falcon Northwest                                     "],
[" Havok                                                "],
[" SOFTIMAGE                                            "],
[" and Don Kemmis, SKL Technologies                     ",
 "                                                      ",
 "                                                      "],
["                                                      ",
 "                                                      ",
 "                                                      ",
"                                                      ",
 "                                                      ",
 "                                                      "],
["                                                      ",  #90
 " THANK YOU FOR PARTICIPATING                          ",
 " IN THIS                                              ",
 " ENRICHMENT CENTER ACTIVITY!                          ",
 "                                                      ",
 "                                                      ",
 "                                                      ",
 "                                                      ",
 "                                                      ",
 "                                                      ",
 "                                                      "],
 [],
 []
]

timing = [1.98,  3.96, 5.94, 7.92, 7.97, 11.8, 13.98, 16.78, 19.02, 23.97,
          27.75, 29.5, 32.97, 36.28, 37.08, 38.52, 40.5, 42.47, 44.48, 46.48,
          48.48, 50.46, 52.24, 53, 53.95, 54.9, 55.85, 56.8, 57.75, 58.7,
          59.65, 63.97, 68.95, 72.47, 75.72, 79.72, 84.96, 88.28, 90.47, 92.48,
          94.55, 96.47, 98.49, 100.47, 102.47, 104.21, 105.71, 106.6, 107.49, 108.39,
          109.27, 110.16, 111.05, 111.95, 115.73, 120.95, 124.46, 127.97, 131.97, 136.97,
          140.23, 142.47, 144.48, 146.47, 148.44, 150.47, 152.47, 154.47, 156.20, 157.61,
          157.89, 158.17 , 158.47, 160.11, 162.27, 164.14, 166.24, 168.26, 168.99, 169.72,
          170.47, 172.21, 172.88, 173.55,  174.24, 176.08,176.76, 177.44, 178.14, 180.13,
          184.69, 185, 185.2]

if __name__ == "__main__":
    main()
