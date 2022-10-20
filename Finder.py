# admin panel finder for Windows or Linux

import os
import sys
import time


try:

    try:

        import requests   #  ____________________
        import colorama   # /  import librarys  /
        import colored

    except:
        pass

except ImportError:
    time.sleep(3)
    sys.exit()

from colorama import Fore , init
from colored import fg , bg


init()


class start:

    def metod_1(url , damin , metod):

        _url = url
        _damin = damin
        _metod = metod



        if _metod == "metod1":

            _url = url
            _damin = open(damin).read().split("\n")
            _metod = metod

            print(Fore.GREEN + '[ + ]' + ' ' + 'your Target ( url ) >> ' + Fore.YELLOW + _url) # | print url target |
            print('\n')

            try:
                _r = requests.get("http://" + _url)

                if (
                    _r.status_code == 404 or #  _______________
                    _r.status_code == 401 or # [ status erorrs ]
                    _r.status_code == 402 or
                    _r.status_code == 403):

                    time.sleep(3)
                    sys.exit()

            except KeyboardInterrupt:
                time.sleep(3)
                sys.exit()

            for __dmn in _damin:

                __url = ("http://" + __dmn + "." + _url)

                try:

                    try:
                        __r = requests.get(__url)
                        print(Fore.GREEN + "[ 200 ]" + " " + "Finded one login page ( Url )> " + fg('black') + bg('green') + __url + "\033[91m")   # for response 200 [ OK ]

                    except:
                        print(Fore.RED + "[ 404 ]" + " " + "Not fond ( Url )> " + fg('black') + bg('red') + __url + "\033[91m")       # for response 404 [ not fond ]


                except KeyboardInterrupt:
                    time.sleep(3)
                    sys.exit()



    def metod_2(url , damin , metod):

        try:

            _url = url
            _damin = damin
            _metod = metod

            if _metod == "metod2":

                _url = url
                _damin = open(damin).read().split("\n")
                _metod = metod

                print(Fore.GREEN + '[ + ]' + ' ' + 'your Target ( url ) >> ' + Fore.YELLOW + _url) # | print url target |

                try:
                    _r = requests.get("http://" + _url)

                    if (
                        _r.status_code == 404 or #  _______________
                        _r.status_code == 401 or # [ status erorrs ]
                        _r.status_code == 402 or
                        _r.status_code == 403):

                        time.sleep(3)
                        sys.exit()

                except KeyboardInterrupt:
                    time.sleep(3)
                    sys.exit()

                for __dmn in _damin:

                    __url = ("http://" + _url + __dmn)

                    try:

                        try:
                            __r = requests.get(__url)
                            if __r.status_code == 200:
                                print(Fore.GREEN + "[ 200 ]" + " " + "Finded one login page ( Url )> " + fg('red') + bg('black') + __url + "\033[91m")
                            else:
                                print(Fore.RED + "[ 404 ]" + " "  + "Not fond ( Url )> " + fg('red') + bg('black') + __url + "\033[91m")

                        except:
                            time.sleep(3)
                            sys.exit()



                    except KeyboardInterrupt:
                        time.sleep(3)
                        sys.exit()
        except:
            time.sleep(3)
            sys.exit()

try:
    try:
        if(sys.argv[0]):

            ___metod___ = sys.argv[1]
            ___url___ = sys.argv[2]

            if ___metod___ == "metod1":

                try:

                    if(sys.argv[3]):
                        ___damin___ = sys.argv[3]
                        start.metod_1(___url___ , ___damin___ , ___metod___) # metod1
                except:
                    ___damin___ = "dam1.txt"
                    start.metod_1(___url___ , ___damin___ , ___metod___) # metod1



            if ___metod___ == "metod2":

                try:

                    if(sys.argv[3]):
                        ___damin___ = sys.argv[3]
                        start.metod_2(___url___ , ___damin___ , ___metod___) # metod1
                except:
                    ___damin___ = "dam2.txt"
                    start.metod_2(___url___ , ___damin___ , ___metod___) # metod1



        # if ___metod___ == "metod1":
        #     if ___damin___ == "":

        #         ___damin___ = "dam1.txt"

        #         start.metod_1(___url___ , ___damin___ , ___metod___) # metod1


        # start.metod_1(___url___ , ___damin___ , ___metod___) # metod1

        # if ___metod___ == "metod2":
        #     if ___damin___ == "":

        #         ___damin___ = "dam2.txt"

        #         start.metod_2(___url___ , ___damin___ , ___metod___) # metod2


        #     start.metod_2(___url___ , ___damin___ , ___metod___) # metod2




    except:

        print("\033[92m" + '''

                _$ Admin Panel Finder $_
            ==================================
           |            By SeFi               |
            ==================================

                    [ metod1 ]:
                        find = 'admin.google.com'

                    [ metod2 ]:
                        find = 'google.com/admin'


                    [ Run ]:
                        python Finder.py --metod --url --daminlist

                        [ mesal ]:
                            python Finder.py metod2 gooogle.com daminlist.txt

        ''')

except KeyboardInterrupt:
    time.sleep(3)
    sys.exit()





pass
