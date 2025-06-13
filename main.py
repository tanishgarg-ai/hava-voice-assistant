from vosk import Model, KaldiRecognizer  # Voice to text(Offline)
import pvporcupine  # Wake word Detector
import pyaudio  # to use mic of the system
import struct  # To work with large Files
import arduino_conditional_lib as my_conditional_statements  # Local Library of what to do n commands
# arduino_conditional_lib as
import pyttsx3  # text to voice (Offline)
import time  # For sleep function
import pygame  # for opening and closing sounds
import time
import threading

# *****************************************************
# Please set your picovoice access key and the com port of the esp
picovoice_access_key = "please_enter_your_access_key"

# *****************************************************
# -------------------- Serial -------------------------
import serial  # To enable communication with arduino(esp32)

ser = serial.Serial('COM18', 115200)  # Change 'COM5' to your  serial port
# ser = serial.Serial('COM3', 9600)  # Change 'COM3' to your  serial port
# *****************************************************


pygame.mixer.init()
open_sound = pygame.mixer.Sound("sounds/open_sound.mp3")
close_sound = pygame.mixer.Sound("sounds/end_sound.mp3")
# ------------------------------------------------------------------------------------------------------------------------------------
import tkinter as tk
import json
import customtkinter as ctk
import math
from tkdial import Dial


# -------------------------------------------------------------

def tv_power():
    ser.write(b'power')


def tv_0():
    ser.write(b'dish_0')


def tv_1():
    ser.write(b'dish_1')


def tv_2():
    ser.write(b'dish_2')


def tv_3():
    ser.write(b'dish_3')


def tv_4():
    ser.write(b'dish_4')


def tv_5():
    ser.write(b'dish_5')


def tv_6():
    ser.write(b'dish_6')


def tv_7():
    ser.write(b'dish_7')


def tv_8():
    ser.write(b'dish_8')


def tv_9():
    ser.write(b'dish_9')


def tv_mute():
    ser.write(b'dish_mute')


def left():
    ser.write(b'dish_left')


def right():
    ser.write(b'dish_right')


def up():
    ser.write(b'dish_up')


def down():
    ser.write(b'dish_down')


def select():
    ser.write(b'dish_select')


# ---------------------------------------------------------
def TV():
    w1 = ctk.CTk()
    w1.title("HA Interface-TV")
    w1.attributes("-fullscreen", True)
    # screen_width=w1.winfo_screenwidth()
    # screen_height=w1.winfo_screenheight()
    # w1.winfo_screenheight()
    # print(screen_width)
    # print(screen_height)

    lwel = ctk.CTkLabel(w1, text="H.A.V.A.I.", text_color="cyan", font=("Ariel", 45))
    lwel.place(relx=0.43, rely=0.03)
    lwel2 = ctk.CTkLabel(w1, text="Television", text_color="cyan", font=("Ariel", 35))
    lwel2.place(relx=0.5, rely=0.13, anchor=ctk.CENTER)

    b_close = ctk.CTkButton(w1, text="X", fg_color="red", command=w1.destroy, width=40, height=30)
    b_close.place(relx=0.95, rely=0.05, anchor=ctk.CENTER)

    b_on = ctk.CTkButton(w1, text="ON", fg_color="green", command=tv_power)
    b_on.place(relx=0.25, rely=0.25, anchor=ctk.CENTER)
    b_off = ctk.CTkButton(w1, text="OFF", fg_color="red", command=tv_power)
    b_off.place(relx=0.25, rely=0.3, anchor=ctk.CENTER)

    # Number Buttons
    b1 = ctk.CTkButton(w1, text="1", width=20, height=20, command=tv_1)
    b1.place(relx=0.2, rely=0.35, anchor=ctk.CENTER)
    b2 = ctk.CTkButton(w1, text="2", width=20, height=20, command=tv_2)
    b2.place(relx=0.25, rely=0.35, anchor=ctk.CENTER)
    b3 = ctk.CTkButton(w1, text="3", width=20, height=20, command=tv_3)
    b3.place(relx=0.3, rely=0.35, anchor=ctk.CENTER)
    b4 = ctk.CTkButton(w1, text="4", width=20, height=20, command=tv_4)
    b4.place(relx=0.2, rely=0.4, anchor=ctk.CENTER)
    b5 = ctk.CTkButton(w1, text="5", width=20, height=20, command=tv_5)
    b5.place(relx=0.25, rely=0.4, anchor=ctk.CENTER)
    b6 = ctk.CTkButton(w1, text="6", width=20, height=20, command=tv_6)
    b6.place(relx=0.3, rely=0.4, anchor=ctk.CENTER)
    b7 = ctk.CTkButton(w1, text="7", width=20, height=20, command=tv_7)
    b7.place(relx=0.2, rely=0.45, anchor=ctk.CENTER)
    b8 = ctk.CTkButton(w1, text="8", width=20, height=20, command=tv_8)
    b8.place(relx=0.25, rely=0.45, anchor=ctk.CENTER)
    b9 = ctk.CTkButton(w1, text="9", width=20, height=20, command=tv_9)
    b9.place(relx=0.3, rely=0.45, anchor=ctk.CENTER)
    b0 = ctk.CTkButton(w1, text="0", width=20, height=20, command=tv_0)
    b0.place(relx=0.25, rely=0.5, anchor=ctk.CENTER)

    # Channel Search Box
    L = ['ktv hd-91', 'sun music hd-92', 'gemini tv hd-93', 'etv hd-94', 'zindagi-103', 'set hd-104',
         'set-105',
         'sony sab hd-106', 'sony sab-107', '&tv hd-108', '&tv-109', 'zee tv hd-110', 'zee tv-111',
         'star plus hd-112', 'star plus-113', 'star bharat hd-115', 'star bharat-116', 'big magic-118',
         'dangal-119', 'colors hd-120', 'colors-121', 'abzy cool-122', 'zee anmol-125',
         'investigation discovery-126', 'topper-133', 'colors rishtey-137', 'dr. shuddhi-138',
         'shemaroo tv-139',
         'ezmall-141', 'utv bindass-145', 'zoom-147', 'dd retro-191', 'dd national-193', 'dd kisan-195',
         'dd bharati-197', 'zee salaam-203', 'dd urdu-213', 'dd kashir-215', 'dd uttar pradesh-229',
         'dd uttarakhand-230', 'dd madhya pradesh-237', 'dd rajasthan-245', '&pictures hd-304',
         '&pictures-305',
         'zee bollywood-307', 'naaptol-308', 'zee action-310', 'colors cineplex hd-312', 'colors cineplex-313',
         'utv movies-336', 'utv action-338', 'zee cinema hd-339', 'zee cinema-340', 'wow cinema one-341',
         'sony max hd-342', 'sony max-343', 'box cinema-344', 'abzy movies-345', 'cinema tv india-348',
         'sony max 2-349', 'star gold hd-352', 'star gold-353', 'abzy dhakad-354', 'zee anmol cinema-355',
         'star gold 2-357', 'b4u movies-360', 'star gold select hd-381', 'star gold select-382',
         'maha movie-387',
         'enterr10 movies-407', 'dhinchaak-413', 'zing-451', 'mtv-455', 'mtv beats hd-458', 'mtv beats-459',
         'music india-479', 'zee cafe hd-502', 'zee cafe-503', 'colors infinity hd-504', 'colors infinity-505',
         'star world hd-508', 'star world-509', 'comedy central hd-513', 'comedy central-514',
         'disney international hd-515', 'star world premiere hd-530', '&prive hd-538', '&flix hd-540',
         '&flix-541',
         'mnx hd-542', 'mnx-543', 'sony pix hd-544', 'sony pix-545', 'movies now hd-546', 'movies now-547',
         'star movies hd-548', 'star movies-549', 'hbo-552', 'romedy now hd-565', 'romedy now-566',
         'mn+ hd-576',
         'star movies select hd-577', 'vh1-585', 'star sports 1 hd-602', 'star sports 1-603',
         'star sports 2 hd-604', 'star sports 2-605', 'star sports 1 hindi hd-606', 'star sports 1 hindi-607',
         'sony ten 1 hd-610', 'sony ten 1-611', 'sony ten 2 hd-612', 'sony ten 2-613', 'sony ten 3 hd-614',
         'sony ten 3-615', 'sony espn hd-620', 'sony six hd-622', 'sony six-623', 'eurosport-630',
         '1sports-635',
         'dd sports-639', 'star sports select 1 hd-645', 'star sports select 1-646',
         'star sports select 2 hd-647',
         'star sports select 2-648', 'star sports 3-649', 'abp news-650', 'zee news-651', 'india tv-653',
         'zee hindustan-654', 'aaj tak-655', 'tv9 bharatvarsh-658', 'ndtv india-659', 'news nation-660',
         'news 24-661', 'news18 india-663', 'india news-665', 'vip news-666', 'aaj tak tez-677',
         'sudarshan news-679', 'lok sabha tv-695', 'rajya sabha tv-697', 'dd news-699', 'asianet plus-703',
         'news18 urdu-703', 'gulistan news-705', 'zee uttar pradesh uttarakhand-707', 'amrita tv-709',
         'news state up uttarakhand-709', 'news18 uttar pradesh uttarakhand-711', 'abp ganga-712', 'we tv-714',
         'zee madhya pradesh chhattisgarh-715', 'asianet movies-716', 'news18 madhya pradesh chhattisgarh-717',
         'dd chhattisgarh-718', 'media one tv-723', 'manorama news-725', 'mathrubhumi news-727',
         'zee rajasthan news-727', 'news18 rajasthan-729', 'a1 tv-730', 'janam tv-730', 'zee business-731',
         'safari tv-731', 'cnbc awaaz-733', 'kochu tv-734', 'kappa tv-735', 'goodness-738', 'et now-751',
         'cnbc prime hd-754', 'cnbc tv18-755', 'disha tv-757', 'ndtv 24x7-761', 'india today-763', 'wion-765',
         'times now world hd-766', 'times now-767', 'cnn news18-769', 'republic tv-771', 'mirror now-773',
         'india ahead-775', 'dd india-779', 'cnn international-781', 'bbc world news-783', 'cgtn-785',
         'al jazeera-787', 'france 24-790', 'discovery hd world-802', 'discovery channel-803',
         'animal planet hd world-805', 'animal planet-806', 'national geographic hd-808', 'nat geo wild-809',
         'national geographic-809', 'discovery science-812', 'discovery turbo-814', 'history tv18 hd-819',
         'history tv18-820', 'nat geo wild hd-822', 'sony bbc earth hd-828', 'sony bbc earth-829', 'epic-830',
         'jai maharashtra-882', 'colors super-902', 'zee zest-903', 'udaya music-906', 'sri sankara tv-907',
         'star suvarna plus-908', 'news18 kannada-910', 'fox life hd-914', 'fox life-915', 'tlc hd-918',
         'tlc-919',
         'etv telangana-920', 'etv andhra pradesh-922', 'gemini comedy-923', 'gemini music-924',
         'sakshi tv-929',
         't news-937', 'v6 news-938', 'chutti tv-948', 'sun news-949', 'sirippoli-951', 'isaiaruvi-952',
         'cartoon network-953', 'sun music-953', 'pogo-955', 'jaya max-955', 'jaya tv-956', 'kalaignar tv-957',
         'raj tv-958', 'sonic nickelodeon-958', 'raj digital plus-959', 'captain tv-960', 'discovery kids-960',
         'jaya plus-962', 'adithya tv-963', 'd tamil-965', 'mega tv-966', 'thanthi tv-967', 'polimer tv-968',
         'puthiya thalaimurai-969', 'vasanth tv-970', 'makkal tv-971', 'svbc-973', 'nick hd+-974', 'nick-975',
         'murasu tv-976', 'disney channel-977', 'super hungama-979', 'gubbare-980', 'hungama tv-981',
         'baby tv hd-982', 'disney junior-985', 'nick jr-987', 'sony yay-989', 'etv bal bharat-990',
         'dd gyan darshan-991', 'chintu tv-1031', 'divya tv-1051', 'darshan 24-1057', 'ishwar tv-1057',
         'satsang tv-1065', 'sanskar-1067', 'aastha bhajan-1073', 'ishwar bhakti-1073', 'aastha-1077',
         'shubh tv-1079', 'god tv-1087', 'peace of mind-1087', 'jinvani channel-1105', 'arihant tv-1107',
         'channel win-1113', 'chardikla time tv-1152', 'ptc punjabi-1154', 'zee punjabi-1156',
         'dd punjabi-1169',
         'dd hisar-1170', 'pitaara tv-1181', 'ptc chak de-1183', 'ptc punjabi gold-1184', '9x tashan-1185',
         'ptc music-1186', 'mh one-1187', 'zee punjab haryana himachal pradesh-1189', 'ptc news-1191',
         'news18 punjab haryana himachal-1193', 'india news haryana-1194', 'ptc simran-1195',
         'zee marathi hd-1201', 'zee marathi-1202', 'zee yuva-1204', 'star pravah hd-1205', 'star pravah-1206',
         'colors marathi hd-1208', 'colors marathi-1209', 'sony marathi-1211', 'fakt marathi-1213',
         'dd sahyadri-1229', 'zee talkies hd-1230', 'zee talkies-1231', 'sangeet marathi-1241',
         'zee vajwa-1242',
         '9x jhakaas-1243', 'maiboli-1245', 'zee 24 taas-1251', 'abp majha-1253', 'news18 lokmat-1255',
         'tv9 marathi-1259', 'saam tv-1261', 'lokshahi-1263', 'colors gujarati-1272',
         'colors gujarati cinema-1273', 'dd girnar-1279', 'news18 gujarati-1289', 'zee 24 kalak-1291',
         'abp asmita-1293', 'sandesh news-1296', 'cnbc bajar-1297', 'tv9 gujarati-1299', 'zee sarthak-1302',
         'colors odia-1304', 'tarang tv-1307', 'manjari tv-1309', 'dd odia-1325', 'alankar-1331',
         'tarang music-1341', 'otv-1351', 'zee odisha-1353', 'news18 odia-1355', 'kalinga tv-1357',
         'kanak news-1359', 'naxatra news-1361', 'prameya news7-1363', 'mbc tv-1365', 'nandighosha tv-1367',
         'argus-1369', 'prarthana tv-1393', 'star jalsha hd-1403', 'star jalsha-1404', 'sony aath-1407',
         'zee bangla hd-1408', 'zee bangla-1409', 'colors bangla hd-1410', 'colors bangla-1411',
         'aakash aath-1413', 'sun bangla-1415', 'ruposhi bangla-1427', 'dd bangla-1429',
         'jalsha movies hd-1430',
         'jalsha movies-1431', 'zee bangla cinema-1433', 'khushboo bangla-1439', 'dhoom music-1459',
         'sangeet bangla-1461', 'calcutta news-1471', 'kolkata tv-1471', 'news time bangla-1473',
         'zee 24 ghanta-1475', 'abp ananda-1477', 'news18 bangla-1479', 'r plus-1485', 'rengoni-1507',
         'rang-1509',
         'jonack-1511', 'dd north east-1513', 'indradhanu-1513', 'dd arunprabha-1514', 'ramdhenu-1515',
         'dd manipur-1516', 'dd meghalaya-1518', 'prag news-1525', 'assam talks-1527', 'dy 365-1529',
         'pratidin time-1531', 'news18 assam north east-1533', 'news live-1535', 'nepal 1-1537',
         'dd tripura-1539',
         'north east live-1539', 'dd mizoram-1540', 'big ganga-1552', 'bhojpuri cinema-1554',
         'b4u bhojpuri-1560',
         'dd bihar-1565', 'dd jharkhand-1566', 'sangeet bhojpuri-1573', 'zee bihar jharkhand-1575',
         'news18 bihar jharkhand-1579', 'zee telugu-1602', 'etv telugu-1604', 'star maa hd-1605',
         'star maa-1606',
         'gemini tv-1609', 'star maa gold-1613', 'etv plus-1615', 'etv life-1617', 'dd yadagiri-1627',
         'dd saptagiri-1629', 'zee cinemalu-1631', 'gemini movies-1633', 'star maa movies-1637',
         'etv cinema-1639',
         'star maa music-1653', 'abn andhra jyothi-1675', 'subhavaartha tv-1693', 'udaya comedy-1702',
         'star suvarna-1707', 'zee kannada-1709', 'colors kannada hd-1710', 'colors kannada-1711',
         'udaya tv-1715',
         'dd chandana-1729', 'udaya movies-1731', 'colors kannada cinema-1735', 'tv9 kannada-1766',
         'asianet suvarna news-1768', 'public tv-1774', 'dighvijay 24x7 news-1776', 'btv news-1778',
         'sun tv-1802',
         'zee tamil-1804', 'star vijay-1806', 'colors tamil-1808', 'puthuyugam tv-1833',
         'star vijay super-1835',
         'dd podhigai-1849', 'star sports 1 tamil-1865', 'seithigal-1873', 'news18 tamil nadu-1879',
         'angel tv-1895', 'asianet hd-1901', 'asianet-1902', 'surya tv-1904', 'zee keralam-1906',
         'kairali tv-1911', 'mazhavil manorama-1915', 'kaumudy tv-1917', 'kairali we-1919', 'flowers-1923',
         'dd malayalam-1939', 'surya movies-1943', 'asianet news-1961', 'news18 kerala-1963',
         'kairali news-1971',
         'reporter-1977', 'shalom tv-1995', 'digishala-2036', 'star sports first-2349',
         'manoranjan grand-2378',
         '9x jalwa-3981', 'manoranjan movies-3997', 'surya cinema-4003', 'filamchi-4005', 'sony pal-4010',
         'dd nagaland-4011', 'star utsav-4013', 'lord buddha tv-4014', 'surya bhojpuri-4015', 'dd imphal-4016',
         'maha punjabi-4018', 'jantantra tv-4018', 'sony wah-4019', 'mastiii-4020', 'movie plus-4021',
         'manoranjan tv-4023', 'dabang-4030', '9xm-4034', 'live today-4040', 'b4u kadak-4044',
         'b4u music-4045',
         'star utsav movies-4049', 'dd shimla-4079', 'dd shillong-9907']

    def on_submit():
        selected_item = cb.get()

        def extract_channel_number(channel_string):
            parts = channel_string.split('-')
            if len(parts) == 2:
                return int(parts[1])
            else:
                return None

        # Example usage:
        channel_number = extract_channel_number(selected_item)
        print(channel_number)
        if channel_number is not None:
            for i in range(len(str(channel_number))):
                print(str(channel_number)[i])
                # ser.write((str(channel_no[i])))
                # print(channel_no[i])
                ch_num = "dish_" + str(channel_number)[i]
                byte_data = str(ch_num).encode('ASCII')
                print(byte_data)
                ser.write(byte_data)
                asd = False
                time.sleep(2)
        else:
            print(f"Invalid format for '{channel_number}'")

    cb = ctk.CTkComboBox(w1, values=L)
    cb.place(relx=0.5, rely=0.45, anchor=ctk.CENTER)
    b_cb_submit = ctk.CTkButton(w1, text="Submit", width=100, height=40, command=on_submit)
    b_cb_submit.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)
    # print(cb.get())
    # --------------------------------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------------------------------

    # Arrow Keys
    b_up = ctk.CTkButton(w1, text="Up", width=50, height=50, command=up)
    b_up.place(relx=0.75, rely=0.25, anchor=ctk.CENTER)
    b_select = ctk.CTkButton(w1, text="Select", width=50, height=50, command=select)
    b_select.place(relx=0.75, rely=0.35, anchor=ctk.CENTER)
    b_down = ctk.CTkButton(w1, text="Down", width=50, height=50, command=down)
    b_down.place(relx=0.75, rely=0.45, anchor=ctk.CENTER)
    b_left = ctk.CTkButton(w1, text="Left", width=50, height=50, command=left)
    b_left.place(relx=0.65, rely=0.35, anchor=ctk.CENTER)
    b_right = ctk.CTkButton(w1, text="Right", width=50, height=50, command=right)
    b_right.place(relx=0.85, rely=0.35, anchor=ctk.CENTER)

    # Volume
    volume = ctk.CTkSlider(w1, from_=0, to=100)
    volume.place(relx=0.4, rely=0.65)
    vol_value = volume.get()
    l_vol = ctk.CTkLabel(w1, text="Volume :", text_color="green", font=("Ariel", 25))
    l_vol.place(relx=0.35, rely=0.6)
    w1.mainloop()
    #def update_vol_value(value,label):

    #   label.config(text="Volume : "+str(value))


# ------------------------------------------------ AC -------------------------------------

def b_ac_on():
    ser.write(b'ac_on')


def b_ac_off():
    ser.write(b'ac_off')


def ac_mode_cool():
    ser.write(b'ac_cool_mode')


def ac_mode_fan():
    ser.write(b'ac_mode_fan')


def ac_mode_auto():
    ser.write(b'ac_mode_auto')


def ac_mode_heat():
    ser.write(b'ac_mode_heat')


def tamp_sender(temp_value):
    ard_com = "set_temp " + str(temp_value)
    ser.write(ard_com.encode('ASCII'))


def AC():
    w2 = ctk.CTk()
    w2.title("HA Interface-AC")
    w2.attributes("-fullscreen", True)

    lwel = ctk.CTkLabel(w2, text="H.A.V.A.I.", text_color="cyan", font=("Ariel", 45))
    lwel.place(relx=0.43, rely=0.03)
    lwel2 = ctk.CTkLabel(w2, text="Air Conditioner", text_color="cyan", font=("Ariel", 35))
    lwel2.place(relx=0.5, rely=0.13, anchor=ctk.CENTER)

    b_on = ctk.CTkButton(w2, text="ON", fg_color="green", command=b_ac_on)
    b_on.place(relx=0.1, rely=0.25, anchor=ctk.CENTER)
    b_off = ctk.CTkButton(w2, text="OFF", fg_color="red", command=b_ac_off)
    b_off.place(relx=0.1, rely=0.3, anchor=ctk.CENTER)

    # Temperature
    l_temp = ctk.CTkLabel(w2, text="Temperature", text_color="Orange", font=("Ariel", 25))
    l_temp.place(relx=0.1, rely=0.45, anchor=ctk.CENTER)
    temp_var = tk.StringVar(value="0.0")
    temp_sp = ctk.FloatSpinbox(w2, width=150, step_size=1, min_value=16, max_value=30)
    temp_sp.place(relx=0.1, rely=0.55, anchor=ctk.CENTER)


    def on_submit():
        # global temp_value
        temp_value = temp_sp.get()
        ard_com = "set_temp " + str(temp_value)
        ser.write(ard_com.encode('ASCII'))

    b_cb_submit = ctk.CTkButton(w2, text="Submit", width=100, height=40, command=on_submit)
    b_cb_submit.place(relx=0.1, rely=0.60, anchor=ctk.CENTER)

    # Update gauge on focus out

    l_mode = ctk.CTkLabel(w2, text="Mode", text_color="violet", font=("Ariel", 25))
    l_mode.place(relx=0.1, rely=0.7, anchor=ctk.CENTER)

    b_close = ctk.CTkButton(w2, text="X", fg_color="red", command=w2.destroy, width=40, height=30)
    b_close.place(relx=0.95, rely=0.05, anchor=ctk.CENTER)

    selected_mode = tk.IntVar()
    selected_mode.set(1)

    rauto = ctk.CTkRadioButton(w2, text="Auto", value=1, variable=selected_mode, command=ac_mode_auto)
    rauto.place(relx=0.05, rely=0.8, anchor=ctk.CENTER)
    rcool = ctk.CTkRadioButton(w2, text="Cool", value=2, variable=selected_mode, command=ac_mode_cool)
    rcool.place(relx=0.1, rely=0.8, anchor=ctk.CENTER)
    rfan = ctk.CTkRadioButton(w2, text="Fan", value=3, variable=selected_mode, command=ac_mode_fan)
    rfan.place(relx=0.15, rely=0.8, anchor=ctk.CENTER)
    rheat = ctk.CTkRadioButton(w2, text="Heat", value=4, variable=selected_mode, command=ac_mode_heat)
    rheat.place(relx=0.2, rely=0.8, anchor=ctk.CENTER)


    ser_val = ser.readline()
    print(ser_val)
    start_time = time.time()

    humidity_val = 50
    temp_val = 24
    if "b'Humidity: " in str(ser_val):
        humidity_val = str(ser_val)[12:14]
        # print(humidity_val)
    if "b'Temperature: " in str(ser_val):
        temp_val = str(ser_val)[15:17]
        # print(temp_val)

    # Temperature Dial
    color_combinations = ("cyan", "blue")
    dial = Dial(master=w2, color_gradient=color_combinations, text_color="gray14", unit_length=10, radius=150,
                needle_color="cyan")
    dial.place(relx=0.4, rely=0.5, anchor=ctk.CENTER)
    val_temp_sp = int(temp_sp.get())
    val_dial = (val_temp_sp / 31) * 100

    dial.set(val_dial)
    txt = "Temperature Set: {}C"
    l_dial_1 = ctk.CTkLabel(w2, text=txt.format(val_temp_sp), font=("Ariel", 15), text_color="cyan")
    l_dial_1.place(relx=0.4, rely=0.8, anchor=ctk.CENTER)

    color_combinations = ("yellow", "red")
    dial = Dial(master=w2, color_gradient=color_combinations, text_color="gray14", unit_length=10, radius=80,
                needle_color="red")
    dial.place(relx=0.7, rely=0.5, anchor=ctk.CENTER)
    value_temp = 22
    val_dial = (value_temp / 31) * 100

    dial.set(val_dial)
    txt = "Temperature: {}C"
    value_temp = temp_val
    l_dial_2 = ctk.CTkLabel(w2, text=txt.format(value_temp), font=("Ariel", 15), text_color="yellow")
    l_dial_2.place(relx=0.7, rely=0.65, anchor=ctk.CENTER)

    color_combinations = ("white", "blue")
    dial = Dial(master=w2, color_gradient=color_combinations, text_color="gray14", unit_length=10, radius=80,
                needle_color="blue")
    dial.place(relx=0.9, rely=0.5, anchor=ctk.CENTER)

    txt1 = "Humidity: {}%"
    value_hum = humidity_val
    dial.set(value_hum)
    l_dial_3 = ctk.CTkLabel(w2, text=txt1.format(value_hum), font=("Ariel", 15), text_color="cyan")
    l_dial_3.place(relx=0.9, rely=0.65, anchor=ctk.CENTER)

    w2.mainloop()


def voice_assistant():
    # ----------------------------- Vosk -----------------------------------
    model = Model("vosk-model-en-in-0.5")
    # In this we give the path to the downloaded model from the website

    recognizer = KaldiRecognizer(model, 16000)  # we initialise the recognizer, the first argument is the model path,
    # second is the
    # 16000 is the sample rate of the audio input that is used by the vosk speech recognition library.
    # It means that the audio signal is sampled 16000 times per second to create a digital representation of the sound.

    mic = pyaudio.PyAudio()
    stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
    stream.start_stream()
    # *****************************************************

    # -------------------- Porcupine(Wake Word) -------------------------
    # Get your AccessKey from Picovoice Console
    access_key = picovoice_access_key

    # Get the path to your custom wake word model file
    keyword_path = "Hello-Ben_en_windows_v3_0_0\\Hello-Ben_en_windows_v3_0_0.ppn"

    # Create an instance of Porcupine engine
    handle = pvporcupine.create(access_key=access_key, keyword_paths=[keyword_path])

    # Get the required audio input parameters
    pa = pyaudio.PyAudio()
    sample_rate = handle.sample_rate
    frame_length = handle.frame_length
    channels = 1
    audio_format = pyaudio.paInt16
    transcribed_text = ''
    # Open an audio stream with the required parameters
    stream = pa.open(
        rate=sample_rate,
        channels=channels,
        format=audio_format,
        input=True,
        frames_per_buffer=frame_length)
    # *****************************************************

    # -------------------- pyttsx3 -------------------------
    engine = pyttsx3.init()
    # *****************************************************

    # Loop until interrupted
    start_time = time.time()

    try:
        while True:
            # Read a frame of audio samples from the stream
            pcm = stream.read(frame_length)
            pcm = struct.unpack_from("h" * frame_length, pcm)

            # Process the frame with Porcupine engine
            keyword_index = handle.process(pcm)

            asd = True

            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)

            # Humidity Timer
            if time.time() - start_time > 5:
                ser_val = ser.readline()
                print(ser_val)
                start_time = time.time()
                f = open("tempandHumidity_a.txt", 'a')
                f.write(str(ser_val))
                f.write("\n")
                f.close()
                if "b'Humidity: " in str(ser_val):
                    str_val = str(current_time) + "- Humidity: " + str(ser_val)[12:14]
                    print(str_val)
                elif "b'Temperature: " in str(ser_val):
                    str_val = str(current_time) + "- Temprature: " + str(ser_val)[15:17]
                    print(str_val)


            # Check if the wake word is detected
            if keyword_index == 0:
                # Do something, e.g. print a message or trigger an action
                print("Wake word detected!")
                open_sound.play()

                # ----------------------------------------------------
                while True:
                    data = stream.read(4096)
                    if len(data) == 0:
                        break  # Break the loop if no more data is available

                    if recognizer.AcceptWaveform(data):
                        result = recognizer.Result()
                        # print(result)
                        transcribed_text = result  # Append the recognized text to the variable
                        close_sound.play()

                        text_list = transcribed_text.split()
                        for i in [3, -2]:
                            asd = str(text_list[i])
                            qwe = asd.replace('"', '')
                            text_list.pop(i)
                            text_list.insert((i + 1), qwe)

                        print(text_list)

                        print_statement, ard_command = my_conditional_statements.conditional_statements(text_list)

                        print("print_statement", print_statement)

                        if len(ard_command) > 0:
                            if len(ard_command) > 8 and ard_command[:8] == "dish_ch_":
                                channel_no = (ard_command[8:])
                                print(channel_no)
                                for i in range(len(str(channel_no))):
                                    # ser.write((str(channel_no[i])))
                                    # print(channel_no[i])
                                    ch_num = "dish_" + channel_no[i]
                                    byte_data = str(ch_num).encode('ASCII')
                                    print(byte_data)
                                    ser.write(byte_data)
                                    asd = False
                                    time.sleep(2)

                                    # print
                        byte_data = str(ard_command).encode('ASCII')
                        print(byte_data)

                        if asd:  # if asd == True
                            ser.write(byte_data)
                            # ser.write(ard_command)

                        engine.say(print_statement)
                        engine.runAndWait()

                        # Check if the recognized text contains a line break or period to end the loop
                        if '\n' in result or '.' in result:
                            break
    # ----------------------------------------------------
    except KeyboardInterrupt:
        print("Stopping...")

    # Close the audio stream and Porcupine engine
    stream.stop_stream()
    stream.close()
    handle.delete()


def GUI():
    while True:
        w3 = ctk.CTk()
        screen_width = w3.winfo_screenwidth()
        screen_height = w3.winfo_screenheight()
        w3.title("HA Interface-Main Menu")
        screen_dimension = str(screen_width) + 'x' + str(screen_height)
        w3.geometry(screen_dimension)
        # w3.attributes("-fullscreen",True)

        b_close = ctk.CTkButton(w3, text="X", fg_color="red", command=w3.destroy, width=40, height=30)
        b_close.place(relx=0.95, rely=0.05, anchor=ctk.CENTER)

        lwel = ctk.CTkLabel(w3, text="Welcome To H.A.V.A.I.", text_color="cyan", font=("Ariel", 45))
        lwel.place(relx=0.35, rely=0.1)
        lwel2 = ctk.CTkLabel(w3, text="Home Automation Voice Assistant Interface", text_color="cyan",
                             font=("Ariel", 35))
        lwel2.place(relx=0.525, rely=0.25, anchor=ctk.CENTER)

        b_tv = ctk.CTkButton(w3, text="TV", width=80, height=50, command=TV)
        b_tv.place(relx=0.05, rely=0.3, anchor=ctk.CENTER)
        on_tv = ctk.CTkButton(w3, text="ON", width=40, height=40, fg_color="green", command=tv_power)
        on_tv.place(relx=0.04, rely=0.4, anchor=ctk.CENTER)
        off_tv = ctk.CTkButton(w3, text="OFF", width=40, height=40, fg_color="red", command=tv_power)
        off_tv.place(relx=0.07, rely=0.4, anchor=ctk.CENTER)

        b_ac = ctk.CTkButton(w3, text="AC", width=80, height=50, command=AC)
        b_ac.place(relx=0.95, rely=0.3, anchor=ctk.CENTER)
        on_tv = ctk.CTkButton(w3, text="ON", width=40, height=40, fg_color="green", command=b_ac_on)
        on_tv.place(relx=0.97, rely=0.4, anchor=ctk.CENTER)
        off_tv = ctk.CTkButton(w3, text="OFF", width=40, height=40, fg_color="red", command=b_ac_off)
        off_tv.place(relx=0.94, rely=0.4, anchor=ctk.CENTER)

        # ----------------------------------------------------------
        ser_val = ser.readline()
        print(ser_val)
        start_time = time.time()
        f = open("tempandHumidity.txt", 'a')
        f.write(str(ser_val))
        f.write("\n")
        f.close()
        humidity_val = 50
        temp_val = 24
        if "b'Humidity: " in str(ser_val):
            humidity_val = str(ser_val)[12:14]
            print(humidity_val)
        if "b'Temperature: " in str(ser_val):
            temp_val = str(ser_val)[15:17]
            print(temp_val)

        color_combinations = ("yellow", "red")
        dial2 = Dial(master=w3, color_gradient=color_combinations, text_color="gray14", unit_length=10, radius=100,
                     needle_color="red")
        dial2.place(relx=0.9, rely=0.65, anchor=ctk.CENTER)
        # value_temp=
        value_temp = int(temp_val)

        val_dial = (value_temp / 40) * 100

        dial2.set(val_dial)
        txt = "Temperature: {}C"
        l_dial_2 = ctk.CTkLabel(w3, text=txt.format(value_temp), font=("Ariel", 15), text_color="yellow")
        l_dial_2.place(relx=0.9, rely=0.8, anchor=ctk.CENTER)

        color_combinations = ("white", "blue")
        dial3 = Dial(master=w3, color_gradient=color_combinations, text_color="gray14", unit_length=10, radius=100,
                     needle_color="blue")
        dial3.place(relx=0.65, rely=0.65, anchor=ctk.CENTER)

        txt1 = "Humidity: {}%"
        value_hum = int(humidity_val)
        l_dial_3 = ctk.CTkLabel(w3, text=txt1.format(value_hum), font=("Ariel", 15), text_color="cyan")
        l_dial_3.place(relx=0.65, rely=0.8, anchor=ctk.CENTER)
        dial3.set(value_hum)

        w3.mainloop()


thread1 = threading.Thread(target=voice_assistant)
thread2 = threading.Thread(target=GUI)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
