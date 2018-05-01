
#!/usr/bin/python
# -*- encoding: utf-8 -*-

# ==============================================================
# Notes from translation
# ==============================================================
#
# English translation from this translation project:
# https://github.com/SrBrahma/RPi-12864-LCD-ST7920-lib
#
# Most of the translation is crappy. It is based on Google Translator.
# There is still missing some words that I can't find anywhere, maybe typos from author.
# 
# Czech words between "-- --" are words that I was unable to translate.
# There are few czech words followed by --[possible english translation]--
#
# Unknow terms:
#
# - mikrorow (microrow? but why that name)
# -
#
# ==============================================================
# Functions Index
# ==============================================================
# Note1: these translations are not very good.
# Note2: the Y position is inverted (like most (all?) displays), so the coordinate (0,0) is the top left.
#
# init()
#   Basic GPIO port settings - just run it once at the beginning of the program
#
# initTextMode()
#   Switches the display to text mode.
#   NOTE: However, look like to use functions that use plot(), you need to initTextMode.
#
# initGraphicMode()
#   Switches display to graphic mode.
#
# clearText()
#   Deletes the content of the text part of the display (the graphics portion remains unchanged)
#
# clearGraphic(pattern)
#   Fills the entire contents of the graphical part of the display by the byte.
#   (When 0x00 is deleted, 0xFF will fill it with white dots, other values will
#   fill the display with different vertical lines). The text part of the display remains unchanged.
#
# clearDisplay()
#   Performs both previous deletions at the same time. After returning the display is switched to text mode.
#
# defineIcon(iconId, iconData)
#   Defines one of four custom icons
#   iconId = icon identifier number 0 to 3
#   iconData = a variable that contains an array: 16x double-byte value
#
# printIcon(iconId, x, y)
#   The [x, y] coordinates print one of the four custom icons.
#   iconId = Icon identifier number 0 to 3
#   x = column 0 to 7
#   y = line 0 to 3
#
# ==== Graphic font 8x8 pixels
#   printCharGraphicMode(code, x, supers, inversion)
#     Displays one printCharGraphicMode with the ASCII code "code" at the "x" (0 to 15) coordinates,
#     posY (0 to 63) - the y position to
#     When "inverse" = True, a dark printCharGraphicMode appears on a light background.
#
#   printStringGraphicMode(text, x, supers, inversion)
#     Displays text (multiple characters) at "x" and "supers" (parameters same as "printCharGraphicMode ()").
#
# ==== Inside display font
#   printCharTextMode(code, x, y) 	Displays one printCharGraphicMode in text mode at [x, y].
#     Code is in the range 1 to 127 (from 32 to 126 it is a classic ASCII)
#     X is from 0 to 15
#     Y is a line 0 to 3
#
#   printStringTextMode(string, x, y)
#     Use large characters to display text on the display. Parameters are the
#     same as for "big_set ()" and apply to the first printCharGraphicMode of the text.
#
#
# plot(posX, posY, style)
#   At "posX" (0 to 127) and "posY" (0 to 63), it drawns, deletes,
#   or inverts one pixel. If style = 0 , point deletion is performed, 
#   style = 1 is drawn, and style = 2 changes the point status on the display.
#
# memPlot(posX, posY, style)
#   The same function as the previous "plot()", but the points do not
#   appear directly on the display, only in the temporary storage space.
#   This feature allows faster drawing. After use, however, it is necessary to transfer
#   the contents of that temporary memory to the display using the "memDump()" function.
#
# memDump()
#   Transfer the memory contents to the display after using the memPlot() command.
#
# drawHorizontalLine(posY, fromX, toX, style, use_memPlot = 0)
#   Drawing a simple horizontal line at a "supery" distance from the top edge with the
#   ability to define the beginning and end of the line (variables "from" to "to"). 
#   The "style" parameter is the same as the " plot() " function.
# All the functions that have the use_memPlot argument, can use the memPlot() instead of plot() (read memPlot() explanation) 
#
# drawHorizontalLine2(posY, fromX, toX, pattern)
#   Faster drawing of the horizontal line. In this case, the parameters "fromX" and "toX"
#   are in the range 0 to 7 (they are sixteen pixels on the display). Therefore,
#   the line can begin and end only at the coordinates on which the icons are printed.
#   The minimum length of such a line is 16 points. The "pattern" parameter specifies
#   the style of the line. Depending on the individual bits of that parameter, you can
#   set the line full, dashed, dotted, dashed ...
#
# drawVerticalLine(posX, fromY, toY, pattern, use_memPlot = 0)
#   Vertical line at arbitrary coordinates.
#   posX = X line coordinates in the range 0 to 127
#   fromY, toY = y coordinates of the beginning and end of the line in the range 0 to 63
#   The "pattern" parameter is the same as in the previous case.
# All the functions that have the use_memPlot argument, can use the memPlot() instead of plot() (read memPlot() explanation) 
#
# loadBMP12864(fileName)
#   Load a two-color image from the file into the display.
#   Beware of the correct file format!
#
# sendByte(rs, byte) 	Sends 1 byte to the display.
#   The data (1) or the command (0) register is selected using the "rs" parameter.
#
# send2Bytes(rs, byte1, byte2)
#   It sends 2 bytes at a time.
#   The data (1) or the command (0) register is selected using the "rs" parameter.



# ==== NEW FUNCTIONS BELOW!! ====
# They are not present on the original code. They aren't so complicated, but are handy.

# drawGenericLine(fromX, fromY, toX, toY, style = 1, use_memPlot = 0)
#   Draws a line from and to the specified coordinates.
#   Based on this code: http://itsaboutcs.blogspot.com.br/2015/04/bresenhams-line-drawing-algorithm.html
# All the functions that have the use_memPlot argument, can use the memPlot() instead of plot() (read memPlot() explanation) 
#
# drawCircle(circleCenterX, circleCenterY, radius, startDegree = 0, stopDegree = 360, stepDegree = 1, style = 1, use_memPlot = 0):
#   The arguments are self-explaining.
#   Increasing stepDegree increases the speed of drawing, but may result in missing pixels.
# All the functions that have the use_memPlot argument, can use the memPlot() instead of plot() (read memPlot() explanation) 
#   
# drawRadiusLine(fromX, fromY, degree, radius, style = 1, use_memPlot = 0):
#    Draws a line like a clock hand, where you enter the initial coordinate, the angle
#    in degrees and the radius (the size of the line)
# All the functions that have the use_memPlot argument, can use the memPlot() instead of plot() (read memPlot() explanation) 
#
# hideShowDisplay(state)
#    Hide all active pixels on display, but doesn't remove them from memory.
#    If you hide them (True or any value except 0), and then show them again (False or 0),
#    all active pixels will show again, on the same place.

# printString3x5(string, leftX, topY, rotation = 0, use_memPlot = 0):
#   Prints a string with the font 3x5 pixels.
#   rotation = 0: no change in the text.
#   rotation = 1: text is turned 90degrees counter-clockwise (and keeps writing up)
#   rotation = 2: text is turned 180degrees counter-clockwise (and keeps writing left)
#   rotation = 3: text is turned 270degrees counter-clockwise (and keeps writing down)
#   leftX and topY are the "top-left" position of the first char that you want to print.
# All the functions that have the use_memPlot argument, can use the memPlot() instead of plot() (read memPlot() explanation) 
# ==============================================================


# Last edit: 15.7.2013 (from the original czech code)

# Display 12864 ZW display (128x64 point) SERIAL:
# Display output (purpouse) -    connected to ...
# 1  (GND)                  - RasPi (GPIO GND   - pin 6)
# 2  (+ power supply)       - RasPi (GPIO +5V   - pin 1)
# 3  VO                     - 
# 4  (RS Data/Command)      - +5V (CHIP SELECT - In serial communication)
# 5  (R/W Read/Write)       - RasPi (Serial data) - GPIO7 (pin26) 
# 6  (E - strobe)           - RasPi (serial CLOCK) - GPIO8 (pin24)
# 7  (Data bit0)            - 
# 8  (Data bit1)            - 
# 9  (Data bit2)            - 
# 10 (Data bit3)            - 
# 11 (Data bit4)            - 
# 12 (Data bit5)            - 
# 13 (Data bit6)            - 
# 14 (Data bit7)            - 
# 15 (PSB)                  - GND - Set serial communication
# 16 (NC)                   -
# 17 (Reset)                - RasPi - GPIO25(pin22)
# 18 (Vout)                 - 
# 19 (Podsvet - A)          - +5V (Or any LED brightness regulator - about 60mA)
# 20 (Podsvet - K)          - RasPi (GPIO GND - pin 6)

import os
import time              # Various operations with time (pauses)
import RPi.GPIO as GPIO  # It can only be used when attaching the E or RS signal to the GPIO in RasPi
import math              # It will only be used in the examples of drawing circles
import random            # It is used only in the indices for generating random coordinates
import subprocess
import sys
import json
import requests

api_url = 'http://localhost/admin/api.php'

# This 3x5 font wasn't present on the original code.
# Based on this font: https://robey.lag.net/2010/01/23/tiny-monospace-font.html
# Changed some chars as I thought it was better, you should do the same!
# Maybe, for code cleansing, I will move this into a file, and the user must loadFont3x5.
char3x5 = [                                 # KEY   | ASCII(dec)
[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]],    # SPACE     32
[[1,1,1,0,1]],                              # !         33
[[1,1,0,0,0], [0,0,0,0,0], [1,1,0,0,0]],    # "         34
[[1,1,1,1,1], [0,1,0,1,0], [1,1,1,1,1]],    # #         35
[[0,1,0,1,0], [1,1,1,1,1], [1,0,1,0,0]],    # $         36
[[1,0,0,1,0], [0,0,1,0,0], [0,1,0,0,1]],    # %         37
[[1,1,1,1,0], [1,1,1,0,1], [0,0,1,1,1]],    # &         38
[[1,1,0,0,0]],                              # '         39
[[0,1,1,1,0], [1,0,0,0,1]],                 # (         40
[[1,0,0,0,1], [0,1,1,1,0]],                 # )         41
[[1,0,1,0,0], [0,1,0,0,0], [1,0,1,0,0]],    # *         42
[[0,0,1,0,0], [0,1,1,1,0], [0,0,1,0,0]],    # +         43
[[0,0,0,0,1], [0,0,0,1,0]],                 # ,         44
[[0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0]],    # -         45
[[0,0,0,0,1]],                              # .         46
[[0,0,0,1,1], [0,0,1,0,0], [1,1,0,0,0]],    # /         47
[[1,1,1,1,1], [1,0,0,0,1], [1,1,1,1,1]],    # 0         48
[[1,0,0,0,1], [1,1,1,1,1], [0,0,0,0,1]],    # 1         49
[[1,0,1,1,1], [1,0,1,0,1], [1,1,1,0,1]],    # 2         50
[[1,0,1,0,1], [1,0,1,0,1], [1,1,1,1,1]],    # 3         51
[[1,1,1,0,0], [0,0,1,0,0], [1,1,1,1,1]],    # 4         52
[[1,1,1,0,1], [1,0,1,0,1], [1,0,1,1,1]],    # 5         53
[[1,1,1,1,1], [1,0,1,0,1], [1,0,1,1,1]],    # 6         54
[[1,0,0,0,0], [1,0,0,1,1], [1,1,1,0,0]],    # 7         55
[[1,1,1,1,1], [1,0,1,0,1], [1,1,1,1,1]],    # 8         56
[[1,1,1,0,1], [1,0,1,0,1], [1,1,1,1,1]],    # 9         57
[[0,1,0,1,0]],                              # :         58
[[0,0,0,0,1], [0,1,0,1,0]],                 # ;         59
[[0,0,1,0,0], [0,1,0,1,0], [1,0,0,0,1]],    # <         60
[[0,1,0,1,0], [0,1,0,1,0], [0,1,0,1,0]],    # =         61
[[1,0,0,0,1], [0,1,0,1,0], [1,1,1,1,1]],    # >         62
[[1,0,0,0,0], [1,0,1,0,1], [1,1,0,0,0]],    # ?         63
[[0,1,1,1,0], [1,0,1,0,1], [0,1,1,0,1]],    # @         64
[[1,1,1,1,1], [1,0,1,0,0], [1,1,1,1,1]],    # A         65
[[1,1,1,1,1], [1,0,1,0,1], [0,1,0,1,0]],    # B         66
[[0,1,1,1,0], [1,0,0,0,1], [1,0,0,0,1]],    # C         67
[[1,1,1,1,1], [1,0,0,0,1], [0,1,1,1,0]],    # D         68
[[1,1,1,1,1], [1,0,1,0,1], [1,0,1,0,1]],    # E         69
[[1,1,1,1,1], [1,0,1,0,0], [1,0,1,0,0]],    # F         70
[[0,1,1,1,0], [1,0,1,0,1], [1,0,1,1,1]],    # G         71
[[1,1,1,1,1], [0,0,1,0,0], [1,1,1,1,1]],    # H         72
[[1,0,0,0,1], [1,1,1,1,1], [1,0,0,0,1]],    # I         73
[[0,0,0,1,0], [0,0,0,0,1], [1,1,1,1,0]],    # J         74
[[1,1,1,1,1], [0,0,1,0,0], [1,1,0,1,1]],    # K         75
[[1,1,1,1,1], [0,0,0,0,1], [0,0,0,0,1]],    # L         76
[[1,1,1,1,1], [0,1,1,0,0], [1,1,1,1,1]],    # M         77
[[1,1,1,1,1], [0,1,1,1,0], [1,1,1,1,1]],    # N         78
[[0,1,1,1,0], [1,0,0,0,1], [0,1,1,1,0]],    # O         79
[[1,1,1,1,1], [1,0,1,0,0], [0,1,0,0,0]],    # P         80
[[0,1,1,1,0], [1,0,0,1,1], [0,1,1,1,1]],    # Q         81
[[1,1,1,1,1], [1,0,1,0,0], [0,1,0,1,1]],    # R         82
[[0,1,0,0,1], [1,0,1,0,1], [1,0,0,1,0]],    # S         83
[[1,0,0,0,0], [1,1,1,1,1], [1,0,0,0,0]],    # T         84
[[1,1,1,1,1], [0,0,0,0,1], [1,1,1,1,1]],    # U         85
[[1,1,1,1,0], [0,0,0,0,1], [1,1,1,1,0]],    # V         86
[[1,1,1,1,1], [0,0,1,1,0], [1,1,1,1,1]],    # W         87
[[1,1,0,1,1], [0,0,1,0,0], [1,1,0,1,1]],    # X         88
[[1,1,0,0,0], [0,0,1,1,1], [1,1,0,0,0]],    # Y         89
[[1,0,0,1,1], [1,0,1,0,1], [1,1,0,0,1]],    # Z         90
[[1,1,1,1,1], [1,0,0,0,1]],                 # [         91
[[1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]],    # \         92
[[1,0,0,0,1], [1,1,1,1,1]],                 # ]         93
[[0,1,0,0,0], [1,0,0,0,0], [0,1,0,0,0]],    # ^         94
[[0,0,0,0,1], [0,0,0,0,1], [0,0,0,0,1]],    # _         95
[[1,1,0,0,0]],                              # '         96
[[0,1,0,1,1], [0,1,1,0,1], [0,0,1,1,1]],    # a         97
[[1,1,1,1,1], [0,1,0,0,1], [0,0,1,1,0]],    # b         98
[[0,0,1,1,0], [0,1,0,0,1], [0,1,0,0,1]],    # c         99
[[0,0,1,1,0], [0,1,0,0,1], [1,1,1,1,1]],    # d         100
[[0,0,1,1,0], [0,1,0,1,1], [0,1,1,0,1]],    # e         101
[[0,0,1,0,0], [0,1,1,1,1], [1,0,1,0,0]],    # f         102
[[0,1,1,0,0], [1,0,1,0,1], [1,1,1,1,0]],    # g         103
[[1,1,1,1,1], [0,1,0,0,0], [0,0,1,1,1]],    # h         104
[[1,0,1,1,1]],                              # i         105
[[0,0,0,1,0], [0,0,0,0,1], [1,0,1,1,1]],    # j         106
[[1,1,1,1,1], [0,0,1,1,0], [0,1,0,0,1]],    # k         107
[[1,0,0,0,1], [1,1,1,1,1], [0,0,0,0,1]],    # l         108
[[0,1,1,1,1], [0,1,1,1,0], [0,1,1,1,1]],    # m         109
[[0,1,1,1,1], [0,1,0,0,0], [0,1,1,1,1]],    # n         110
[[0,0,1,1,0], [0,1,0,0,1], [0,0,1,1,0]],    # o         111
[[0,1,1,1,1], [0,1,0,1,0], [0,0,1,0,0]],    # p         112
[[0,0,1,0,0], [0,1,0,1,0], [0,1,1,1,1]],    # q         113
[[0,0,1,1,1], [0,1,0,0,0], [0,1,1,0,0]],    # r         114
[[0,0,1,0,1], [0,1,1,1,1], [0,1,0,1,0]],    # s         115
[[0,1,0,0,0], [1,1,1,1,1], [0,1,0,0,1]],    # t         116
[[0,1,1,1,1], [0,0,0,0,1], [0,1,1,1,1]],    # u         117
[[0,1,1,1,0], [0,0,0,0,1], [0,1,1,1,0]],    # v         118
[[0,1,1,1,1], [0,0,1,1,1], [0,1,1,1,1]],    # w         119
[[0,1,0,0,1], [0,0,1,1,0], [0,1,0,0,1]],    # x         120
[[0,1,1,0,1], [0,0,0,1,1], [0,1,1,1,0]],    # y         121
[[0,1,0,1,1], [0,1,1,1,1], [0,1,1,0,1]],    # z         122
[[0,0,1,0,0], [1,1,0,1,1], [1,0,0,0,1]],    # {         123
[[1,1,1,1,1]],                              # |         124
[[1,0,0,0,1], [1,1,0,1,1], [0,0,1,0,0]],    # ]         125
[[0,0,1,0,0], [0,1,1,0,0], [0,1,0,0,0]],    # ~         126
[[1,0,1,0,1], [0,1,0,1,0], [1,0,1,0,1]]]    # ERROR     "127" = If the ascii is out of range,
# will print this custom char instead. 



# Translation of Czech characters from a font file
cz2={}
cz2[345] = 128      # r s hackem
cz2[237] = 129      # i s carkou
cz2[353] = 130      # s s hackem
cz2[382] = 131      # z s hackem
cz2[357] = 132      # t s hackem
cz2[269] = 133      # c s hackem
cz2[253] = 134      # y s carkou
cz2[367] = 135      # u With a ring
cz2[328] = 136      # n s hackem
cz2[250] = 137      # u s carkou
cz2[283] = 138      # e s hackem
cz2[271] = 139      # d s hackem
cz2[225] = 140      # a s carkou
cz2[233] = 141      # e s carkou
cz2[243] = 142      # o s carkou

cz2[344] = 143      # R s hackem
cz2[205] = 144      # I s carkou
cz2[352] = 145      # S s hackem
cz2[381] = 146      # Z s hackem
cz2[356] = 147      # T s hackem
cz2[268] = 148      # C s hackem
cz2[221] = 149      # Y s carkou
cz2[366] = 150      # U With a ring
cz2[327] = 151      # N s hackem
cz2[218] = 152      # U s carkou
cz2[282] = 153      # E s hackem
cz2[270] = 154      # D s hackem
cz2[193] = 155      # A s carkou
cz2[201] = 156      # E s carkou
cz2[211] = 157      # O s carkou

cz2[228] = 228      # pronounced a
cz2[235] = 235      # pronounced e
cz2[239] = 239      # pronounced i
cz2[246] = 246      # pronounced o
cz2[252] = 252      # pronounced u
cz2[196] = 196      # pronounced A
cz2[214] = 214      # pronounced O
cz2[220] = 220      # pronounced U

cz2[176] = 176      # degree
cz2[177] = 177      # plus minus
cz2[171] = 171      # Double arrow on the left
cz2[166] = 166      # Interrupted vertically
cz2[223] = 223      # beta

# Assign GPIO pin
sData_Pin = 7       # (pin 26 = GPIO7)   = DATA    
sClk_Pin = 8        # (pin 24 = GPIO8)   = CLOCK  
reset_Pin = 25      # (pin 22 = GPIO25)  = RESET   

mapa={}             # Memory to store the current status of the displayed pixels on the display
txtmapa={}          # Memory to which the current text status on the display is saved
font2={}            # The memory in which the font is stored is retrieved from the external file
iconData={}         # The variable through which the graphical Icons will be defined


#==============================================================
# Main program
#==============================================================

def main():

    init()              # Basic HW system setup - port directions on the expander and reset the display
    clearDisplay(0)     # Complete deletion of the display
        

    while True:
    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
        #cmd = "hostname -I | cut -d\' \' -f1"
        cmd = "hostname -I | cut -d\' \' -f1 | tr '\n' ' '"
        #cmd = "hostname -I | cut -f1"
        IP = subprocess.check_output(cmd, shell = True )
        # cmd = "hostname"
        cmd = "hostname | tr '\n' ' '"
        HOST = subprocess.check_output(cmd, shell = True )
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell = True )
        # cmd = "/opt/vc/bin/vcgencmd measure_temp | awk -F = '{print $2}'"
        cmd = "/opt/vc/bin/vcgencmd measure_temp | awk -F = '{print $2}' | tr '\n' ' '"
        TEMP1 = subprocess.check_output(cmd, shell = True )
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell = True )
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell = True )

        # Pi Hole data!
        try:
            r = requests.get(api_url)
            data = json.loads(r.text)
            DNSQUERIES = data['dns_queries_today']
            ADSBLOCKED = data['ads_blocked_today']
            CLIENTS = data['unique_clients']
        except:
            time.sleep(1)
            continue
        '''    
        print("IP: "+str(IP)+" "+str(HOST))
        print(str(CPU )+" T: "+str(TEMP1))
        print(str(MemUsage))
        print(str(Disk))
        print("Ads Blocked: " + str(ADSBLOCKED))
        print("Clients:     " + str(CLIENTS))
        print("DNS Queries: " + str(DNSQUERIES))
        '''

        # Write two lines of text.
        
        initGraphicMode()
        # IP and Hostname
        printString3x5("IP: "+str(IP)+" "+str(HOST)+" ", 0, 0, rotation = 0, use_memPlot = 0)
        
        drawHorizontalLine(7, 0, 128, 1, 0)
        # CPU and Temp 
        printString3x5(str(CPU )+" T: "+str(TEMP1), 0, 10, rotation = 0, use_memPlot = 0)
        # mem usage
        printString3x5(str(MemUsage), 0, 17, rotation = 0, use_memPlot = 0)
        # disk usage
        printString3x5(str(Disk), 0, 24, rotation = 0, use_memPlot = 0)

        drawHorizontalLine(31, 0, 128, 1, 0)
        # PIhole data
        printString3x5("Ads Blocked: " + str(ADSBLOCKED), 0, 34, rotation = 0, use_memPlot = 0)
        printString3x5("Clients:     " + str(CLIENTS), 0, 41, rotation = 0, use_memPlot = 0)
        printString3x5("DNS Queries: " + str(DNSQUERIES), 0, 48, rotation = 0, use_memPlot = 0)
        '''
        statvfs = os.statvfs('/')
        grootte = statvfs.f_frsize * statvfs.f_blocks
        vrij = statvfs.f_frsize * statvfs.f_bfree
        flap = vrij / (grootte / 100)
        hoek = flap * 3.6
        hoek = int(hoek)
        drawCircle(100, 20, 10, startDegree = 0 , stopDegree = hoek, stepDegree = 1, style = 1, use_memPlot = 0)
        drawCircle(100, 20, 9, startDegree = 0 , stopDegree = hoek, stepDegree = 1, style = 1, use_memPlot = 0)
        drawCircle(100, 20, 8, startDegree = 0 , stopDegree = hoek, stepDegree = 1, style = 1, use_memPlot = 0)
        '''
        
        
        time.sleep(.1)





#==============================================================
#               All subroutines are:
#==============================================================



#==============================================================
# One of the 4 defined 16 x 16 pixel icons at position [x, y]
# X is in the range 0 to 7 (translated to 0, 16, 32, 48, 64, 80, 96, 112)
# Y ranges from 0 to 3 (translated to 0, 16, 32, 48)
def printIcon(iconId, x, y):
    shift = x
    if (y == 1): shift = shift + 16
    if (y == 2): shift = shift + 8
    if (y == 3): shift = shift + 24
    sendByte(0, 0b10000000 + shift)  # Address Counter to the required position
    send2Bytes(1, 0, iconId * 2)







#==============================================================
# Draw a horizontal line point by point
def drawHorizontalLine(posY, fromX = 0, toX=127, style = 1, use_memPlot = 0):  
    if use_memPlot:
        customPlot = memPlot
    else:
        customPlot = plot
        
    for posX in range(fromX, toX + 1):
        customPlot(posX, posY, style)


#==============================================================
# Draw horizontal line from the edge to the edge after the bytes
def drawHorizontalLine2(posY = 0, fromByte = 0, toByte = 5, pattern = 0b11111111):  
    shift = fromByte
    if (posY >= 32):
        posY = posY - 32
        shift = shift + 8     

    send2Bytes( 0, 0b10000000 + posY, 0b10000000 + shift )     
    for r in range(toByte - fromByte + 1):
        send2Bytes(1, pattern, pattern)     
        mapa[shift + r, posY, 0] = pattern 
        mapa[shift + r, posY, 1] = pattern 
    
    
#==============================================================
# Draw a vertical line using bit masks
# NOTICE: if given a pattern != 255 and if style == 2, style = 1.
def drawVerticalLine(posX, fromY = 0, toY = 63, style = 1, pattern = 255, use_memPlot = 0):
    if use_memPlot:
        customPlot = memPlot
    else:
        customPlot = plot  
        
    bitSelector = 0                              # The bit position in the pattern
    pixelStyle = style                # Gives it the style value, as plot uses the pixelStyle var.
    for posY in range(fromY , toY + 1):
        if (pattern != 255):
            bitValue = pattern & (0b10000000 >> (bitSelector % 8))  # According to the given pattern, selects individual bits
                                                                    # Which will either be displayed or deleted on the display
            if (bitValue == 0):                      
                pixelStyle = 0
            else:
                pixelStyle = 1
                
            if (style == 0):  # inverts the pixelStyle if the style is == 0 (delete)
                pixelStyle = not pixelStyle
            bitSelector = bitSelector + 1
            
        customPlot(posX, posY, pixelStyle)
        


#==============================================================
# Displaying one printCharGraphicMode from the 8x8 point font
# bytePosX = x printCharGraphicMode position (0 to 15, translated to multiples of 8 up to 128), posY = 0 to 63
def printCharGraphicMode(ascii8bitCode, bytePosX, posY , invert = False):  

    # Control of lightning parameters and their possible override at the limit
    if (ascii8bitCode <  32): ascii8bitCode = 32
    if (ascii8bitCode > 255): ascii8bitCode = 255
    if (bytePosX <  0): bytePosX = 0  
    if (bytePosX > 15): bytePosX = 15  
    if (posY > 63): posY = 63
    if (posY <  0): posY = 0

    ascii8bitCode = ascii8bitCode - 32     # In the font file, the space with the 32 code is defined as the first printCharGraphicMode
    posX = bytePosX * 8

    # The font of the printCharGraphicMode from the font will be gradually transferred to the byte byte display in 8 steps (top down)
    for adr_font in range(ascii8bitCode * 8, (ascii8bitCode * 8) + 8):

        # Calculate the horizontal and vertical addresses in the display memory
        horiz = posX // 16 
        dis_adr_y = posY
        if (dis_adr_y >= 32):
            dis_adr_y = dis_adr_y - 32
            horiz = horiz + 8
    
        minibit = posX % 16     # The position of the bit to work with, in the double-bin
     
        send2Bytes(0, 0b10000000 + dis_adr_y, 0b10000000 + horiz)  # Setting the graphics address
    
        originalLeftByte  = mapa[horiz,dis_adr_y, 0]  # To find out the current status of the two-byte on the display
        originalRightByte = mapa[horiz,dis_adr_y, 1]

        if(minibit < 8):         # When the minibit is <8, change only the left byte from the double byte
            if (invert == False):  # Normal text (write everything that is below the text)
                leftByte = font2[adr_font]
            if (invert == True):   # Inverse text (write everything that is below the text)
                leftByte = ~font2[adr_font]
                
            rightByte = originalRightByte   # right byte z dvojbyteu bude beze zmeny
    
        else:  # When the minibit >= 8, change only the right byte from the double-bin
            if (invert == False):  # Normal text (write everything that is below the text)
                rightByte = font2[adr_font]
            if (invert == True):   # Inverse text (write everything that is below the text)
                rightByte = ~font2[adr_font]

            leftByte = originalLeftByte     # The left byte of the two-bit will be unchanged
    
        send2Bytes(1, leftByte, rightByte)       # Prepress the two bytes to enter the address in the display
        mapa[horiz, dis_adr_y, 0] = leftByte        # The same value remembers the variable map []
        mapa[horiz, dis_adr_y, 1] = rightByte

        posY = posY + 1   # Change the current micro-bars by one



#==============================================================
# Displaying several characters behind the 8x8 font
# bytePosX = the position of the first printCharGraphicMode in the text is in column 0 to 15; posY = 0 to 63 (upper margin of the printCharGraphicMode)
def printStringGraphicMode(string, bytePosX, posY, invert = False):  

    if (isinstance(string, str) == False):   # If the string is not in unicode, then transfer it
        string = str(string, "utf-8")          # Convert string from UTF-8 to unicode

    # All the string scroll printCharGraphicMode after printCharGraphicMode and print
    for letter in range (len(string)):
        if (bytePosX < 16): # Screen overlay
            if (ord(string[letter:letter + 1]) > 127):   # As for the ASCII printCharGraphicMode, proceed as described in the table above
                try:                    # If there is no special code defined in the table, ...
                    printCharGraphicMode(cz2[ord(string[letter:letter + 1])], bytePosX, posY, invert)
                except:                 # ... the program will terminate the error of the non-existent index of the variable cz2 [].
                    printCharGraphicMode(164, bytePosX, posY, invert)  # In this case, replace the undefined printCharGraphicMode printCharGraphicMode "wheel with teckama"
                    
            else:
                printCharGraphicMode(ord(string[letter:letter + 1]), bytePosX, posY, invert) # ASCII charactery tisknout normalne
            bytePosX = bytePosX + 1





#==============================================================
# Load 8x8 point font from file to list "font2 []"
def loadTextFont(fileName):
    # Here are two ways to get the font.txt file path. I will leave them there
    # for future referencies to myself. You can take them as lessons :)
    #
    # asbolute path relative to the program caller' path
    # fullPathFileName = os.path.join(os.path.dirname(os.path.realpath('__file__')), fileName)
    
    # absolute path relative to this library path  (https://stackoverflow.com/a/25612797)
    script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
    script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
    fullPathFileName = os.path.join(script_dir, fileName)
    
    # print (fullPathFileName)
    
    fontfile = open(fullPathFileName, "r")
    adresafontu = 0
    for row in fontfile:
        rozlozeno = row.split(",")                          # Saturation of individual bytes from one line ...
        for byte in range(8):                               # 8 byte on one row in a file
            font2[adresafontu] = int(rozlozeno[byte][-4:], 0) # ... and save everyone on the list
            adresafontu = adresafontu + 1
    fontfile.close()
    


#==============================================================
# Subroutine for string display obrim font (8x16 point)
# Font definition is a part of the ROM in the display - therefore not Czech characters
# bytePosX = Initial column where the string will begin to print [0 to 16]
# Row is in the range [0 to 3]
def printStringTextMode(string, column, row): 

    if (len(string) + column > 16):    # If the line is longer than 16 characters,
        string = string[0:16 - column]  # ... so the end is cut off
 
    setTextCursorPos(column, row)     # The start position of the text is sent to the display
    for printCharGraphicMode in range(len(string)):
        sendByte(1, ord(string[printCharGraphicMode:printCharGraphicMode+1]))  # Characters from the text are gradually streaked into the display
        pomtext = txtmapa[row][:column + printCharGraphicMode] + string[printCharGraphicMode:printCharGraphicMode + 1] + txtmapa[row][column+printCharGraphicMode+1:]
        txtmapa[row] = pomtext            # Memory for text mode



#==============================================================
# Single printCharGraphicMode display in text mode
def printCharTextMode(code, bytePosX, row): 
    setTextCursorPos(bytePosX, row)  # The start position of the text is sent to the display
    sendByte(1, code)                # The printCharGraphicMode code is sent to the display
    pomtext = txtmapa[row][:bytePosX] + chr(code) + txtmapa[row][bytePosX + 1:]
    txtmapa[row] = pomtext           # Memory for text mode



#==============================================================
# Print position setting for text mode (for characters 8x16 point)
# Column (0 to 15) and line (0 to 3)
def setTextCursorPos(column , row):  
    shift = column
    if (row == 1): shift = column + 32
    if (row == 2): shift = column + 16
    if (row == 3): shift = column + 48

    sendByte( 0, 0b10000000 + int(shift / 2))  # Address Counter na pozadovanou pozici

    # In the case of --lichen-- columns, the printCharGraphicMode must be filled in with the printCharGraphicMode on the display before the new printout
    if (column / 2.0 != column / 2):
        orignal_predcharacter = txtmapa[row][column - 1:column] # "Predcharacter" is determined from the auxiliary text memory
        sendByte(1, ord(orignal_predcharacter)) 

#==============================================================
# New function.
# Draws a line from and to the specified coordinates.
# Based on this code: http://itsaboutcs.blogspot.com.br/2015/04/bresenhams-line-drawing-algorithm.html
# NEW FUNCTION!
def drawGenericLine(fromX, fromY, toX, toY, style = 1, use_memPlot = 0):
    if use_memPlot:
        customPlot = memPlot
    else:
        customPlot = plot
        
    # Bresenham Line Drawing Algorithm For All Kind Of Slopes Of Line
    dx = abs(fromX - toX)
    dy = abs(toY - fromY)
    if (float(dx) == 0): slope = 10
    else: slope = dy/float(dx)
    
    x, y = fromX, fromY   

    customPlot(x, y, style)
    
    # checking the slope if slope > 1 
    # then interchange the role of x and y
    if slope > 1:
        inverted = True
        dx, dy = dy, dx
        x, y = y, x
        toX, toY = toY, toX
    else: inverted = False
    # initialization of the inital decision parameter
    p = 2 * dy - dx
    
    for k in range(2, dx):
        if p > 0:
            y = y + 1 if y < toY else y - 1
            p = p + 2*(dy - dx)
        else:
            p = p + 2*dy
 
        x = x + 1 if x < toX else x - 1
        if inverted:
            customPlot(y, x, style)
            
        else:
            customPlot(x, y, style)
            
#==============================================================
# New function.
# Draws a rectangle. If fill, all the internal part will be painted.
# NEW FUNCTION!
def drawRectangle(fromX, fromY, toX, toY, fill = 0, style = 1, use_memPlot = 0):
    if use_memPlot:
        customPlot = memPlot
    else:
        customPlot = plot
        
    if (fromX > toX):
        fromX, toX = toX, fromX
    if (fromY > toY):
        fromY, toY = toY, fromY
    
    for xPos in range (fromX, toX + 1):
        customPlot(xPos, fromY, style)
        customPlot(xPos, toY, style)
        
    for yPos in range (fromY + 1, toY):
        customPlot(fromX, yPos, style)
        customPlot(toX, yPos, style)
        
    if fill:
        for yPos in range (fromY + 1, toY):
            for xPos in range (fromX + 1, toX):
                customPlot(xPos, yPos, style)
        
    
#==============================================================
# New function.
# The arguments are self-explaining.
# Increasing stepDegree increases the speed of drawing, but may result in missing pixels.
# NEW FUNCTION
def drawCircle(circleCenterX, circleCenterY, radius, startDegree = 0, stopDegree = 360, stepDegree = 1, style = 1, use_memPlot = 0):
    if use_memPlot:
        customPlot = memPlot
    else:
        customPlot = plot
        
    for degree in range (startDegree, stopDegree + 1, stepDegree):
        posX = int(round(math.cos(math.radians(degree)) * radius + circleCenterX))
        posY = int(round(math.sin(math.radians(degree)) * (- radius) + circleCenterY))
        customPlot (posX, posY, style)
        
#==============================================================
# New function.
# Draws a line like a clock hand, where you enter the initial coordinate, the angle
# in degrees and the radius (the size of the line)
# NEW FUNCTION!
def drawRadiusLine(fromX, fromY, degree, radius, style = 1, use_memPlot = 0):
    targetX = int(round(math.cos(math.radians(degree)) * radius + fromX))
    targetY = int(round(math.sin(math.radians(degree)) * (- radius) + fromY))
    drawGenericLine(fromX, fromY, targetX, targetY, style, use_memPlot)

#==============================================================
# Prints a string with the font 3x5 pixels.
#   rotation = 0: no change in the text.
#   rotation = 1: text is turned 90degrees counter-clockwise (and keeps writing up)
#   rotation = 2: text is turned 180degrees counter-clockwise (and keeps writing left)
#   rotation = 3: text is turned 270degrees counter-clockwise (and keeps writing down)
# leftX and topY are the "top-left" position of the first char that you want to print.
# This function can be improved/optimized a lot. As I need this for yesterday, will leave the improvements for later.
# As I usually prefer Performance over code readbility, I copied and changed the plotting section, to meet different rotations.
# NEW FUNCTION!
def printString3x5(string, leftX, topY, rotation = 0, use_memPlot = 0):
    if use_memPlot:
        customPlot = memPlot
    else:
        customPlot = plot
        
    actualX = leftX
    actualY = topY
    firstRun = True
    
    if not rotation:       
        for char in string:
            char = ord(char)
            
            if (32 > char or char > 126): char = 127
            
            char -= 32
                
            # Draw the separator (a blank column) between the chars
            if (not firstRun):
                for row in range (5):
                    customPlot(actualX, actualY + row, 0) 
                actualX += 1
            else:
                firstRun = False
                
            for column in range(len(char3x5[char])):
                for row in range(len(char3x5[char][column])):
                    customPlot(actualX, actualY + row, char3x5[char][column][row])
                actualX += 1
                

    elif rotation == 1:# if rotation == 3 or any other number not cased in previous conditionals
        for char in string:
            char = ord(char)

            if (32 > char or char > 126): char = 127
            
            char -= 32
                
            # Draw the separator (a blank column) between the chars
            if (not firstRun):
                for row in range (5):
                    customPlot(actualX + row, actualY, 0) 
                actualY -= 1
            else:
                firstRun = False
                
            for column in range(len(char3x5[char])):
                for row in range(len(char3x5[char][column])):
                    customPlot(actualX + row, actualY, char3x5[char][column][row])
                actualY -= 1
                
    elif rotation == 2:      
        for char in string:
            char = ord(char)
            
            if (32 > char or char > 126): char = 127
            
            char -= 32
                
            # Draw the separator (a blank column) between the chars
            if (not firstRun):
                for row in range (5):
                    customPlot(actualX, actualY - row, 0) 
                actualX -= 1
            else:
                firstRun = False
                
            for column in range(len(char3x5[char])):
                for row in range(len(char3x5[char][column])):
                    customPlot(actualX, actualY - row, char3x5[char][column][row])
                actualX -= 1
                
    else: # if rotation == 3 or any other number not cased in previous conditionals
        for char in string:
            char = ord(char)

            if (32 > char or char > 126): char = 127
            
            char -= 32
                
            # Draw the separator (a blank column) between the chars
            if (not firstRun):
                for row in range (5):
                    customPlot(actualX - row, actualY, 0) 
                actualY += 1
            else:
                firstRun = False
                
            for column in range(len(char3x5[char])):
                for row in range(len(char3x5[char][column])):
                    customPlot(actualX - row, actualY, char3x5[char][column][row])
                actualY += 1
            
    
        
#==============================================================
# Uploading a two-color BMP image of a 128x64 point to a variable map []
# CAUTION: Without any test for a correct BMP file format!
def loadBMP12864(imageRelativePath):
    fileBMP = open(imageRelativePath, "rb")  # Load an image into a data variable []
    data = fileBMP.read()  
    fileBMP.close()                          # File closure

    # The detailed BMP master file specification is here:
    # http://www.root.cz/clanky/graficky-format-bmp-pouzivany-a-pritom-neoblibeny
    # The start of the image data determines 4 bytes in a file in positions 10 to 13 (ten) from the beginning of the file
    zacatekdat = data[10] + (data[11] * 256) + (data[12] * 65536) + (data[13] * 16777216)
    byte = zacatekdat

    for mikrorow in range (63, -1, -1):  # Read data variables [] byte after byte and store in memory (map [])
        posY = mikrorow
        if (mikrorow > 31):
            posY = posY - 32
            shift = 8
        else:
            shift = 0
        send2Bytes(0, 0b10000000 + posY, 0b10000000 + shift)  # Setting the graphics address
        for column in range (8):
            leftByte = data[byte]
            rightByte = data[byte+1]
            send2Bytes(1, leftByte, rightByte)     # 
            mapa[column + shift , posY,0] = leftByte
            mapa[column+shift , posY,1] = rightByte

            byte = byte + 2          # Passes to another double-out of graphical data


#==============================================================
# 1-point display / deletion / inversion at posX coordinates (0 to 127) and posY (0 to 63)
def plot(posX, posY, style = 1):

    # Checking for the correct range of coordinates and optionally adjusting them to the extreme values
    # You can comment these, if you sure your program won't need them. It speeds the code a little
    if (posX > 127): posX = 127
    elif (posX < 0  ): posX = 0
    if (posY > 63 ): posY = 63
    elif (posY < 0  ): posY = 0


    horiz = posX // 16 # Same as / 16
    if (posY >= 32):
        posY -= 32
        horiz += 8

    minibit = posX & 15 # Same as posX % 16 (my way looks CPU faster)
 
    send2Bytes (0, 0b10000000 + posY, 0b10000000 + horiz)  # Setting the graphics address

    
    originalLeftByte  = mapa[horiz, posY, 0]
    originalRightByte = mapa[horiz, posY, 1]
    
    if (minibit < 8):
        
        if (style == 1):  # Draw a point
            leftByte = (0b10000000 >> minibit) | originalLeftByte
        elif (style == 0):  # Delete point
            leftByte = ~(0b10000000 >> minibit) & originalLeftByte
        else:  # Delete point
            leftByte = (0b10000000 >> minibit) ^ originalLeftByte
        mapa[horiz, posY, 0] = leftByte
        rightByte = originalRightByte
        
    else:
        
        if (style == 1):  # Draw a point
            rightByte = (0b10000000 >> (minibit-8)) | originalRightByte
        elif (style == 0):  # Delete point
            rightByte = ~(0b10000000 >> (minibit-8)) & originalRightByte
        else:  # Delete point
            rightByte = (0b10000000 >> (minibit-8)) ^ originalRightByte
        mapa[horiz, posY, 1] = rightByte
        leftByte = originalLeftByte

    send2Bytes(1, leftByte, rightByte)
    
    



#==============================================================
# 1-pixel [display/deletion/inversion] at posX coordinates (0 to 127) and posY (0 to 63)
def memPlot(posX, posY, style = 1):
    horiz = posX >> 4 # Same as / 16
    
    if (posY >= 32):
        posY -= 32
        horiz += 8

    minibit = posX & 15    # Same as posX % 16 (my way looks CPU faster)
 
    
    

    if (minibit < 8):
        originalLeftByte  = mapa[horiz, posY, 0]
        if (style == 1):  # Draw a point
            leftByte = (0b10000000 >> minibit) | originalLeftByte
        elif (style == 0):  # Delete point
            leftByte = ~(0b10000000 >> minibit) & originalLeftByte
        elif (style == 2):  # Invert point
            leftByte = (0b10000000 >> minibit) ^ originalLeftByte

        #rightByte = originalRightByte
        mapa[horiz, posY, 0] = leftByte
        
        
    #Right byte
    else:
        originalRightByte = mapa[horiz, posY, 1]
        if (style == 1):  # Draw a point
            rightByte = (0b10000000 >> (minibit-8)) | originalRightByte
        elif (style == 0):  # Delete point
            rightByte = ~(0b10000000 >> (minibit-8)) & originalRightByte
        elif (style == 2):  # Invert point
            rightByte = (0b10000000 >> (minibit-8)) ^ originalRightByte

        #leftByte = originalLeftByte
        mapa[horiz, posY, 1] = rightByte

    
    


#==============================================================
# Overwrite the graphical memory (variable map []) to the display
def memDump():

    for mikrorow in range(32):
        send2Bytes( 0, 0b10000000 + mikrorow , 0b10000000 )  # Setting the graphics address
        for horizontal in range (16):
            leftByte  = mapa[horizontal , mikrorow , 0] 
            rightByte = mapa[horizontal , mikrorow , 1]
            send2Bytes( 1, leftByte, rightByte)    
             
             

#==============================================================
# Delete graphical display time
def clearGraphic(pattern = 0): 
    initGraphicMode()
    sendByte(0, 0b00110110)  # function set (extend instruction set)
    sendByte(0, 0b00110100)  # function set (graphic OFF) - aby nebylo videt postupne mazani displeje
    sendByte(0, 0b00001000)  # displ.=OFF , cursor=OFF , blink=OFF
    
    for vertical in range(32):  
        send2Bytes(0, 0b10000000 + vertical, 0b10000000 )  # Setting the address on the display at the beginning of the micro-bar
        for horizontal in range (16):
            send2Bytes(1, pattern, pattern)     # Double-bits fill the entire display with the same code   
 
            # And this code still writes to individual positions in the cache
            mapa[horizontal, vertical, 0] = pattern    
            mapa[horizontal, vertical, 1] = pattern
            
    sendByte( 0, 0b00110110)  # function set (graphic ON) - smazany displej se zobrazi okamzite



#==============================================================
# Delete the text part of the display
def clearText(): 
    sendByte(0, 0b00110000)  # function set (8 bit)
    sendByte(0, 0b00110000)  # function set (basic instruction set)
    sendByte(0, 0b00001100)  # displ.=ON , cursor=OFF , blink=OFF
    sendByte(0, 0b00000001)  # clear

    # Erase the text memo
    txtmapa[0] = "                "
    txtmapa[1] = "                "
    txtmapa[2] = "                "
    txtmapa[3] = "                "



#==============================================================
# Delete the graphical text and the text part of the display.
# CAUTION: the display is set in the TEXT mode
def clearDisplay(pattern=0):
    clearGraphic(pattern)
    clearText()



#==============================================================
# Set the display to the graphic mode
def initGraphicMode():  
    sendByte(0, 0b00110010)  # function set (8 bit)
    sendByte(0, 0b00110110)  # function set (extend instruction set)
    sendByte(0, 0b00110110)  # function set (graphic ON)
    sendByte(0, 0b00000010)  # nable CGRAM after being reset to BASIC instruction set



#==============================================================
# Set the display to text mode
def initTextMode():  
    sendByte(0, 0b00110000)  # function set (8 bit)
    sendByte(0, 0b00110100)  # function set (extend instruction set)
    sendByte(0, 0b00110110)  # function set (graphic OFF)
    sendByte(0, 0b00000010)  # Enable CGRAM (after reset to BASIC instruction set)
    sendByte(0, 0b00110000)  # function set (basic instruction set)
    sendByte(0, 0b00001100)  # displ.=ON , cursor=OFF , blink=OFF
    sendByte(0, 0b10000000)  # Address Counter na left horni roh


#==============================================================
# Definition of a graphical shape of 4 icons with the size of 16x16 points
# Icon = Number Icons 0 to 3
# iconData = 16-byte double-byte value
def defineIcon(iconId, iconData):
    initTextMode()
    sendByte(0, 64 + (iconId * 16) )  # Setting the graphics address
    for dat in range(16):
        leftByte  = iconData[dat] // 256
        rightByte = iconData[dat] % 256
        send2Bytes(1, leftByte, rightByte)



#==============================================================
# Blink cursor after the last printCharGraphicMode entered in text mode
# Is designed for Chinese characters, so a 16x16-dot large square
# (It's useless for European characters (8x16 points))
def blinkLastChineseChar(state):
    initTextMode()
    if (state):
        sendByte(0, 0b00001111)  # displ.=ON , cursor=ON , blink=ON
    else:
        sendByte(0, 0b00001100)  # displ.=ON , cursor=OFF , blink=OFF

#==============================================================
# Hide all active pixels on display, but doesn't remove them from memory.
# If you hide them (True or any value except 0), and then show them again (False or 0),
# all active pixels will show again, on the same place.
# I was trying to make a function to turn off the light from the display,
# but doesn't look possible.
def hideShowDisplay(state):
    initTextMode()
    if (state):
        sendByte(0, 0b00001100)  # displ.=ON , cursor=OFF , blink=OFF
    else:
        sendByte(0, 0b00001000)  # displ.=OFF , cursor=OFF , blink=OFF

#==============================================================
# A weird command. It's like the hideShowDisplay(), but idk right
# what it does.
def standby():
    sendByte(0, 0b00110000)  # function set (8 bit)
    sendByte(0, 0b00110100)  # function set (extend instruction set)
    sendByte(0, 0b00000001)  # Standby command
    
#==============================================================
# Set the position to the appropriate column (0 to 7) and the row (0 to 3)
# For big characters and Icons (16x16 points)
def setIconPos(column, row): 

    shift = column
    if (row == 1): shift = column + 16
    if (row == 2): shift = column + 8
    if (row == 3): shift = column + 24

    sendByte(0, 0b10000000 + shift)  # Address Counter to the desired position



#==============================================================
# Set the data pin for serial communication to "0" or "1"
def setDataPin(bit):

    if (bit):
        GPIO.output(sData_Pin, True)
    else:
        GPIO.output(sData_Pin, False)



#==============================================================
# A short one-clock pulse on serialized communications
# I was able to run changing the time.sleep() values, but rarely I was getting some
# artifacts on display, so I decided to leave them there.
# Before strobe4 and 5, this library was using a "for x in range (4): strobe()"
# It was called so many times that it was taking a considerably amount of time
# Now the code runs a little faster.
# Using this quickSleep instead of time.sleep(0.0...1) made a 3.5s code run in 2.7s.
# If there are artifacts in screen, add another y to the expression.
# Leaving the last quickSleep() commented is working, but uncomment if needed.
def quickSleep():
    time.sleep(0)
    # Using the lines below we can achieve a higher speed, but is a lot more cpu consuming.
    # I need to find a way to sleep faster (time.sleep isn't fast enough)
    # y = 1.1
    # x = y + y + y + y + y + y + y + y + y + y + y + y + y + y + y + y + y
    
def strobe():
    GPIO.output(sClk_Pin, True)
    quickSleep()
    GPIO.output(sClk_Pin, False)
    #quickSleep()

def strobe4():
    GPIO.output(sClk_Pin, True)
    quickSleep()
    GPIO.output(sClk_Pin, False)
    quickSleep()
    GPIO.output(sClk_Pin, True)
    quickSleep()
    GPIO.output(sClk_Pin, False)
    quickSleep()
    GPIO.output(sClk_Pin, True)
    quickSleep()
    GPIO.output(sClk_Pin, False)
    quickSleep()
    GPIO.output(sClk_Pin, True)
    quickSleep()
    GPIO.output(sClk_Pin, False)
    #quickSleep()
  
def strobe5():
    GPIO.output(sClk_Pin, True)
    quickSleep()
    GPIO.output(sClk_Pin, False)
    quickSleep()
    GPIO.output(sClk_Pin, True)
    quickSleep()
    GPIO.output(sClk_Pin, False)
    quickSleep()
    GPIO.output(sClk_Pin, True)
    quickSleep()
    GPIO.output(sClk_Pin, False)
    quickSleep()
    GPIO.output(sClk_Pin, True)
    quickSleep()
    GPIO.output(sClk_Pin, False)
    quickSleep()
    GPIO.output(sClk_Pin, True)
    quickSleep()
    GPIO.output(sClk_Pin, False)
    #quickSleep()
  
#==============================================================
# Subprogram for sending two bytes after serial communication without interrupting between individual bytes
def send2Bytes(rs, byte1, byte2):
        
    setDataPin(1)                # The beginning of the communication is done with the "synchro" sequence of 5 singles
    strobe5()
    
    setDataPin(0)                # Then the RW bit is sent (when set to "0")
    strobe()
    setDataPin(rs)               # Then the RS bit is sent (commands = "0"; data = "1")
    strobe()
    setDataPin(0)                # Followed by zero bit
    strobe()
 
    # Decomposing these next for loops didn't made the code run significantly faster.
    for i in range(7, 3, -1):         # And then top four bits from the first byte
        setDataPin(byte1 & (1 << i))    # The original code used "bit = (byte1 & (2**i)) >> i"
        strobe()                        # I removed the "bit" var (putted the expression directly at the function)
                                                                        # And changed the expression. Well, thess improvements made code runs faster.

    setDataPin(0)                     # The next is the 4x "0"
    strobe4()

    for i in range(3, -1, -1):    
        setDataPin(byte1 & (1 << i))
        strobe()

    setDataPin(0)                      # Then the separation sequence is again 4x "0"
    strobe4()

    # Byte types were sent immediately without "head" (without 5x "1" + RW bit + RS bit + "0")
    for i in range(7, 3, -1):        # Even this kind of byte is divided into 2 parts (upper 4 bits)
        setDataPin(byte2 & (1 << i))
        strobe()

    setDataPin(0)                        # Separation sequence 4x "0"
    strobe4()

    for i in range(3, -1, -1):       # Bottom 4 bits
        setDataPin(byte2 & (1 << i))
        strobe()

    setDataPin(0)                        # Last separating sequence 4x "0"
    strobe4()



#==============================================================
# Send one byte after serial communication
def sendByte(rs,  byte):

    setDataPin(1)                # the beginning of the communication is done with the "synchro" sequence of 5 singles
    strobe5()
    
    setDataPin(0)                    # Then the RW bit is sent (when set to "0")        
    strobe()                                                                                  
    setDataPin(rs)                    # Then send the RS bit (commands = "0"; data = "1")            
    strobe()                                                                                                                                           
    setDataPin(0)                     # Followed by zero bit                                                        
    strobe()
    
    for i in range(7, 3, -1):     # And then up four bits of the sent byte
        setDataPin(byte & (1 << i))
        strobe()

    setDataPin(0)                     # Then the separation sequence is sent 4x "0"
    strobe4()

    for i in range(3, -1, -1):    # Followed by the rest of the data (the bottom 4 bits of the sent byte)
        setDataPin(byte & (1 << i))
        strobe()

    setDataPin(0)                      # To restart the separation sequence 4x "0"
    strobe4()



#==============================================================
# HW initial setting + reset the display
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sData_Pin, GPIO.OUT)    # (pin 26 = GPIO7)   = DATA
    GPIO.setup(sClk_Pin, GPIO.OUT)     # (pin 24 = GPIO8)   = CLOCK
    GPIO.setup(reset_Pin, GPIO.OUT)    # (pin 22 = GPIO25)  = RESET

    GPIO.output(sData_Pin, False)      # DATA to "0"
    GPIO.output(sClk_Pin, False)       # CLOCK to "0"
    GPIO.output(reset_Pin, False)      # RESET to "0"
    time.sleep(0.1)   
    GPIO.output(reset_Pin, True)       # RESET to "1"
    loadTextFont("font2.txt")  # Retrieve an external font from the file


#==============================================================
if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()