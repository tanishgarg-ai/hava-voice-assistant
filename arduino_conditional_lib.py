# import serial
#
#
# # -------------------- Serial -------------------------
# ser = serial.Serial('COM5', 115200)  # Change 'COM3' to your  serial port
# # *****************************************************
import time


def conditional_statements(tl):  # tl = textlist
    num_list = [['one', 1], ['two', 2], ['three', 3], ['four', 4], ['five', 5], ['six', 6], ['seven', 7], ['eight', 8],
                ['nine', 9],["an",1]]
    # --------------------------------------------- AC Control ---------------------------------------------------------

    temp_range = [['sixteen',16], ['seventeen',17], ['eighteen',18], ['nineteen',19], ['teen',], ['twenty',20], ['thirty',30]]

    p_st = ''
    my_int = 0
    command = ''
    next_word = 0
    ard_com = ''

    channel_no = 0



    # Turning ON or OFF the AC
    if "air-conditioner" in tl or ("air" in tl and ("conditioner" in tl or "conditioning" in tl or "conditioners" in tl
        or "a. c." in tl or "easy" in tl or "esty" in tl or "isi" in tl)):
        print("air conditioner -- detected")

        # -------------- Setting Timer ------------------
        if 'timer' in tl or 'time' in tl:
            for i in range(len(num_list)):
                if num_list[i][0] in tl:
                    k = num_list[i][1]
                    # print(num_list[i][1])
                    p_st = "Setting a Timer of " + str(k) + " hours"
                    ard_com = "set_timer " + str(k)
                    # print(num_list[i][1])

        # --------- Turning on and setting temp -------------

        elif "on" in tl:  # Turning ON
            # print("Turning on the ac")
            # ser.write(b'ac_on')
            command = 'ac_on'
            p_st = "Turning on the ac"  # p_st = Print statement

        elif "off" in tl or "of" in tl:  # Turning OFF
            # print("Turning off the ac")
            # ser.write(b'ac_off')
            command = 'ac_off'
            p_st = "Turning off the ac"

        for i in range(len(temp_range)):

            if 'twenty' in tl:
                for j in range(len(tl) - 1):
                    if 'twenty' in tl[j]:
                        # print('j =',j)
                        next_word = tl[j + 1]
                for k in range(len(num_list)):
                    if next_word == num_list[k][0]:
                        next_num = num_list[k][1]
                        p_st = "Setting the temprature to " + str(20 + next_num) + " Degrees"
                        ard_com = "set_temp " + str(20 + next_num)
                        # print(num_list[k][1])
                        break
                    else:
                        ard_com = "set_temp " + str(20)

                command = ard_com
                # ser.write(b_command)

            elif temp_range[i][0] in tl:
                # print(i)
                p_st = "Setting the temprature to " + str(temp_range[i][0]) + " Degrees"
                ard_com = "set_temp " + str(temp_range[i][1])
                command = ard_com.encode('ASCII')
                # ser.write(b_command)
    # --------------------------------------------------

    channel_li = [['ktv hd', 91], ['sun music hd', 92], ['gemini tv hd', 93], ['etv hd', 94], ['zindagi', 103],
                  ['set hd', 104], ['set', 105], ['sony sab hd', 106], ['sony sab', 107], ['&tv hd', 108], ['&tv', 109],
                  ['zee tv hd', 110], ['zee tv', 111], ['star plus hd', 112], ['star plus', 113],
                  ['star bharat hd', 115], ['star bharat', 116], ['big magic', 118], ['dangal', 119],
                  ['colors hd', 120], ['colors', 121], ['abzy cool', 122], ['zee anmol', 125],
                  ['investigation discovery', 126], ['topper', 133], ['colors rishtey', 137], ['dr. shuddhi', 138],
                  ['shemaroo tv', 139], ['ezmall', 141], ['utv bindass', 145], ['zoom', 147], ['dd retro', 191],
                  ['dd national', 193], ['dd kisan', 195], ['dd bharati', 197], ['zee salaam', 203], ['dd urdu', 213],
                  ['dd kashir', 215], ['dd uttar pradesh', 229], ['dd uttarakhand', 230], ['dd madhya pradesh', 237],
                  ['dd rajasthan', 245], ['&pictures hd', 304], ['&pictures', 305], ['zee bollywood', 307],
                  ['naaptol', 308], ['zee action', 310], ['colors cineplex hd', 312], ['colors cineplex', 313],
                  ['utv movies', 336], ['utv action', 338], ['zee cinema hd', 339], ['zee cinema', 340],
                  ['wow cinema one', 341], ['sony max hd', 342], ['sony max', 343], ['box cinema', 344],
                  ['abzy movies', 345], ['cinema tv india', 348], ['sony max 2', 349], ['star gold hd', 352],
                  ['star gold', 353], ['abzy dhakad', 354], ['zee anmol cinema', 355], ['star gold 2', 357],
                  ['b4u movies', 360], ['star gold select hd', 381], ['star gold select', 382], ['maha movie', 387],
                  ['enterr10 movies', 407], ['dhinchaak', 413], ['zing', 451], ['mtv', 455], ['mtv beats hd', 458],
                  ['mtv beats', 459], ['music india', 479], ['zee cafe hd', 502], ['zee cafe', 503],
                  ['colors infinity hd', 504], ['colors infinity', 505], ['star world hd', 508], ['star world', 509],
                  ['comedy central hd', 513], ['comedy central', 514], ['disney international hd', 515],
                  ['star world premiere hd', 530], ['&prive hd', 538], ['&flix hd', 540], ['&flix', 541],
                  ['mnx hd', 542], ['mnx', 543], ['sony pix hd', 544], ['sony pix', 545], ['movies now hd', 546],
                  ['movies now', 547], ['star movies hd', 548], ['star movies', 549], ['hbo', 552],
                  ['romedy now hd', 565], ['romedy now', 566], ['mn+ hd', 576], ['star movies select hd', 577],
                  ['vh1', 585], ['star sports 1 hd', 602], ['star sports 1', 603], ['star sports 2 hd', 604],
                  ['star sports 2', 605], ['star sports 1 hindi hd', 606], ['star sports 1 hindi', 607],
                  ['sony ten 1 hd', 610], ['sony ten 1', 611], ['sony ten 2 hd', 612], ['sony ten 2', 613],
                  ['sony ten 3 hd', 614], ['sony ten 3', 615], ['sony espn hd', 620], ['sony six hd', 622],
                  ['sony six', 623], ['eurosport', 630], ['1sports', 635], ['dd sports', 639],
                  ['star sports select 1 hd', 645], ['star sports select 1', 646], ['star sports select 2 hd', 647],
                  ['star sports select 2', 648], ['star sports 3', 649], ['abp news', 650], ['zee news', 651],
                  ['india tv', 653], ['zee hindustan', 654], ['aaj tak', 655], ['tv9 bharatvarsh', 658],
                  ['ndtv india', 659], ['news nation', 660], ['news 24', 661], ['news18 india', 663],
                  ['india news', 665], ['vip news', 666], ['aaj tak tez', 677], ['sudarshan news', 679],
                  ['lok sabha tv', 695], ['rajya sabha tv', 697], ['dd news', 699], ['asianet plus', 703],
                  ['news18 urdu', 703], ['gulistan news', 705], ['zee uttar pradesh uttarakhand', 707],
                  ['amrita tv', 709], ['news state up uttarakhand', 709], ['news18 uttar pradesh uttarakhand', 711],
                  ['abp ganga', 712], ['we tv', 714], ['zee madhya pradesh chhattisgarh', 715], ['asianet movies', 716],
                  ['news18 madhya pradesh chhattisgarh', 717], ['dd chhattisgarh', 718], ['media one tv', 723],
                  ['manorama news', 725], ['mathrubhumi news', 727], ['zee rajasthan news', 727],
                  ['news18 rajasthan', 729], ['a1 tv', 730], ['janam tv', 730], ['zee business', 731],
                  ['safari tv', 731], ['cnbc awaaz', 733], ['kochu tv', 734], ['kappa tv', 735], ['goodness', 738],
                  ['et now', 751], ['cnbc prime hd', 754], ['cnbc tv18', 755], ['disha tv', 757], ['ndtv 24x7', 761],
                  ['india today', 763], ['wion', 765], ['times now world hd', 766], ['times now', 767],
                  ['cnn news18', 769], ['republic tv', 771], ['mirror now', 773], ['india ahead', 775],
                  ['dd india', 779], ['cnn international', 781], ['bbc world news', 783], ['cgtn', 785],
                  ['al jazeera', 787], ['france 24', 790], ['discovery hd world', 802], ['discovery channel', 803],
                  ['animal planet hd world', 805], ['animal planet', 806], ['national geographic hd', 808],
                  ['nat geo wild', 809], ['national geographic', 809], ['discovery science', 812],
                  ['discovery turbo', 814], ['history tv18 hd', 819], ['history tv18', 820], ['nat geo wild hd', 822],
                  ['sony bbc earth hd', 828], ['sony bbc earth', 829], ['epic', 830], ['jai maharashtra', 882],
                  ['colors super', 902], ['zee zest', 903], ['udaya music', 906], ['sri sankara tv', 907],
                  ['star suvarna plus', 908], ['news18 kannada', 910], ['fox life hd', 914], ['fox life', 915],
                  ['tlc hd', 918], ['tlc', 919], ['etv telangana', 920], ['etv andhra pradesh', 922],
                  ['gemini comedy', 923], ['gemini music', 924], ['sakshi tv', 929], ['t news', 937], ['v6 news', 938],
                  ['chutti tv', 948], ['sun news', 949], ['sirippoli', 951], ['isaiaruvi', 952],
                  ['cartoon network', 953], ['sun music', 953], ['pogo', 955], ['jaya max', 955], ['jaya tv', 956],
                  ['kalaignar tv', 957], ['raj tv', 958], ['sonic nickelodeon', 958], ['raj digital plus', 959],
                  ['captain tv', 960], ['discovery kids', 960], ['jaya plus', 962], ['adithya tv', 963],
                  ['d tamil', 965], ['mega tv', 966], ['thanthi tv', 967], ['polimer tv', 968],
                  ['puthiya thalaimurai', 969], ['vasanth tv', 970], ['makkal tv', 971], ['svbc', 973],
                  ['nick hd+', 974], ['nick', 975], ['murasu tv', 976], ['disney channel', 977], ['super hungama', 979],
                  ['gubbare', 980], ['hungama tv', 981], ['baby tv hd', 982], ['disney junior', 985], ['nick jr', 987],
                  ['sony yay', 989], ['etv bal bharat', 990], ['dd gyan darshan', 991], ['chintu tv', 1031],
                  ['divya tv', 1051], ['darshan 24', 1057], ['ishwar tv', 1057], ['satsang tv', 1065],
                  ['sanskar', 1067], ['aastha bhajan', 1073], ['ishwar bhakti', 1073], ['aastha', 1077],
                  ['shubh tv', 1079], ['god tv', 1087], ['peace of mind', 1087], ['jinvani channel', 1105],
                  ['arihant tv', 1107], ['channel win', 1113], ['chardikla time tv', 1152], ['ptc punjabi', 1154],
                  ['zee punjabi', 1156], ['dd punjabi', 1169], ['dd hisar', 1170], ['pitaara tv', 1181],
                  ['ptc chak de', 1183], ['ptc punjabi gold', 1184], ['9x tashan', 1185], ['ptc music', 1186],
                  ['mh one', 1187], ['zee punjab haryana himachal pradesh', 1189], ['ptc news', 1191],
                  ['news18 punjab haryana himachal', 1193], ['india news haryana', 1194], ['ptc simran', 1195],
                  ['zee marathi hd', 1201], ['zee marathi', 1202], ['zee yuva', 1204], ['star pravah hd', 1205],
                  ['star pravah', 1206], ['colors marathi hd', 1208], ['colors marathi', 1209], ['sony marathi', 1211],
                  ['fakt marathi', 1213], ['dd sahyadri', 1229], ['zee talkies hd', 1230], ['zee talkies', 1231],
                  ['sangeet marathi', 1241], ['zee vajwa', 1242], ['9x jhakaas', 1243], ['maiboli', 1245],
                  ['zee 24 taas', 1251], ['abp majha', 1253], ['news18 lokmat', 1255], ['tv9 marathi', 1259],
                  ['saam tv', 1261], ['lokshahi', 1263], ['colors gujarati', 1272], ['colors gujarati cinema', 1273],
                  ['dd girnar', 1279], ['news18 gujarati', 1289], ['zee 24 kalak', 1291], ['abp asmita', 1293],
                  ['sandesh news', 1296], ['cnbc bajar', 1297], ['tv9 gujarati', 1299], ['zee sarthak', 1302],
                  ['colors odia', 1304], ['tarang tv', 1307], ['manjari tv', 1309], ['dd odia', 1325],
                  ['alankar', 1331], ['tarang music', 1341], ['otv', 1351], ['zee odisha', 1353], ['news18 odia', 1355],
                  ['kalinga tv', 1357], ['kanak news', 1359], ['naxatra news', 1361], ['prameya news7', 1363],
                  ['mbc tv', 1365], ['nandighosha tv', 1367], ['argus', 1369], ['prarthana tv', 1393],
                  ['star jalsha hd', 1403], ['star jalsha', 1404], ['sony aath', 1407], ['zee bangla hd', 1408],
                  ['zee bangla', 1409], ['colors bangla hd', 1410], ['colors bangla', 1411], ['aakash aath', 1413],
                  ['sun bangla', 1415], ['ruposhi bangla', 1427], ['dd bangla', 1429], ['jalsha movies hd', 1430],
                  ['jalsha movies', 1431], ['zee bangla cinema', 1433], ['khushboo bangla', 1439],
                  ['dhoom music', 1459], ['sangeet bangla', 1461], ['calcutta news', 1471], ['kolkata tv', 1471],
                  ['news time bangla', 1473], ['zee 24 ghanta', 1475], ['abp ananda', 1477], ['news18 bangla', 1479],
                  ['r plus', 1485], ['rengoni', 1507], ['rang', 1509], ['jonack', 1511], ['dd north east', 1513],
                  ['indradhanu', 1513], ['dd arunprabha', 1514], ['ramdhenu', 1515], ['dd manipur', 1516],
                  ['dd meghalaya', 1518], ['prag news', 1525], ['assam talks', 1527], ['dy 365', 1529],
                  ['pratidin time', 1531], ['news18 assam north east', 1533], ['news live', 1535], ['nepal 1', 1537],
                  ['dd tripura', 1539], ['north east live', 1539], ['dd mizoram', 1540], ['big ganga', 1552],
                  ['bhojpuri cinema', 1554], ['b4u bhojpuri', 1560], ['dd bihar', 1565], ['dd jharkhand', 1566],
                  ['sangeet bhojpuri', 1573], ['zee bihar jharkhand', 1575], ['news18 bihar jharkhand', 1579],
                  ['zee telugu', 1602], ['etv telugu', 1604], ['star maa hd', 1605], ['star maa', 1606],
                  ['gemini tv', 1609], ['star maa gold', 1613], ['etv plus', 1615], ['etv life', 1617],
                  ['dd yadagiri', 1627], ['dd saptagiri', 1629], ['zee cinemalu', 1631], ['gemini movies', 1633],
                  ['star maa movies', 1637], ['etv cinema', 1639], ['star maa music', 1653],
                  ['abn andhra jyothi', 1675], ['subhavaartha tv', 1693], ['udaya comedy', 1702],
                  ['star suvarna', 1707], ['zee kannada', 1709], ['colors kannada hd', 1710], ['colors kannada', 1711],
                  ['udaya tv', 1715], ['dd chandana', 1729], ['udaya movies', 1731], ['colors kannada cinema', 1735],
                  ['tv9 kannada', 1766], ['asianet suvarna news', 1768], ['public tv', 1774],
                  ['dighvijay 24x7 news', 1776], ['btv news', 1778], ['sun tv', 1802], ['zee tamil', 1804],
                  ['star vijay', 1806], ['colors tamil', 1808], ['puthuyugam tv', 1833], ['star vijay super', 1835],
                  ['dd podhigai', 1849], ['star sports 1 tamil', 1865], ['seithigal', 1873],
                  ['news18 tamil nadu', 1879], ['angel tv', 1895], ['asianet hd', 1901], ['asianet', 1902],
                  ['surya tv', 1904], ['zee keralam', 1906], ['kairali tv', 1911], ['mazhavil manorama', 1915],
                  ['kaumudy tv', 1917], ['kairali we', 1919], ['flowers', 1923], ['dd malayalam', 1939],
                  ['surya movies', 1943], ['asianet news', 1961], ['news18 kerala', 1963], ['kairali news', 1971],
                  ['reporter', 1977], ['shalom tv', 1995], ['digishala', 2036], ['star sports first', 2349],
                  ['manoranjan grand', 2378], ['9x jalwa', 3981], ['manoranjan movies', 3997], ['surya cinema', 4003],
                  ['filamchi', 4005], ['sony pal', 4010], ['dd nagaland', 4011], ['star utsav', 4013],
                  ['lord buddha tv', 4014], ['surya bhojpuri', 4015], ['dd imphal', 4016], ['maha punjabi', 4018],
                  ['jantantra tv', 4018], ['sony wah', 4019], ['mastiii', 4020], ['movie plus', 4021],
                  ['manoranjan tv', 4023], ['dabang', 4030], ['9xm', 4034], ['live today', 4040], ['b4u kadak', 4044],
                  ['b4u music', 4045], ['star utsav movies', 4049], ['dd shimla', 4079], ['dd shillong', 9907]]
    if "dish" in tl or "television" in tl or "this" in tl:
        print("dish!!!!!!!!!!!")
        if "mute" in tl:
            p_st = "Muting Dish TV"
            command = "dish_mute"
        else:
            for i in range(len(channel_li) - 1):
                x = channel_li[i][0]
                y = x.split(" ")

                big_list = tl
                small_list = y

                # Check if all elements in the small list are in the big list
                all_elements_in_big_list = all(element in big_list for element in small_list)

                if all_elements_in_big_list:
                    print("All elements of the small list are in the big list.")
                    channel_no = channel_li[i][1]
                    p_st = channel_li[i][0]
                    print(p_st)
                    print(channel_no)
                    break
                else:
                    pass

            print(channel_no)
            command = "dish_ch_" + str(channel_no)
            my_str = "dish_" + str(channel_no)

        if "projecor" in tl:
            command = "projector_on"

    elif p_st == '':
        print("Pardon, Please try again")

    return p_st, command


# statement1 = ['{', '"text"', ':', '"turn', 'off', 'my', 'air', 'conditioner', 'now"', '}']
# statement2 = ['{', '"text"', ':', '"turn', 'my', 'air', 'conditioner', 'twenty','one', '}']
# statement = ['{', '"text"', ':', '"set', 'a', 'timer', 'of', 'two', 'hours', 'air', 'conditioner', '}']
# statement = ['{', '"text"', ':', '"set', 'a', '', 'history', 'tv18', 'hours', 'dish', 'conditioner', '}']
# statement = ['{', '"text"', ':', '"set', 'a', '', 'discovery', 'science', 'hours', 'dish', 'conditioner', '}']
# #
# x,y = conditional_statements(statement2)
# print("x = ",x)
# print("y = ",y)
# # sdjkfhbj = "dish_ch_820"
# # # print(sdjkfhbj[8:])