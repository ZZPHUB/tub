#!/home/ZZP/workspace/py_vir_env/py_vir_0/bin/python3

import sys
import json
import os
from tub.init import *
from tub.translate import *


#from_lang = 'en'
#to_lang = 'zh'
def print_result(result=list,r_format=str):
    if r_format == "t_mode":
        print('\n----------------------------------')
        print(result[0]+' '+result[1])      
        print('----------------------------------')
    elif r_format == "r_mode":

        #print('\n----------------------------------')
        print('|------',result[0],'------|')
        result_ch = str()
        result_ch = result_ch + '|'
        result_ch = result_ch + result[1][0]
        #result[1] = str(result[1])
        for i in range(1,len(result[1])):
            result_ch = result_ch +result[1][i]
            if i % 27 == 0:
                result_ch = result_ch+"|\n|"
        if len(result[1])%28 != 0:
            result_ch = result_ch +"|"
        print(result_ch)
        print('----------------------------------') 
    else:
        print('')


def argv_progress(argv,tub_info=app_info_mode):
    argv_query = str()
    for i in argv[1::]:
        if i == '-h':
            print_usage()
            sys.exit()
        elif i == '-v':
            print("tub version 2.0")
            sys.exit()
        else:
            if '-' in i:
                if i == '-e':
                    tub_info.fromlang='zh'
                    tub_info.tolang='en'
                elif i == '-c':
                   tub_info.fromlang='en'
                   tub_info.tolang='zh' 
                """   
                elif i == '-r':
                    tub_info.mode = "robot"
                    tub_info.print_format = "r_mode"
                """

            else:
                argv_query = argv_query + ' ' + i
    if  argv_query:
        result = list()
        if tub_info.mode == "translate":
            result = translate(argv_query,tub_info.fromlang,tub_info.tolang)
        #if tub_info.mode == "robot":
            #result = robot.robot_ask(argv_query)
        print_result(result,tub_info.print_format)


        #argv_result = translate(argv_translate,from_lang,to_lang)
        #print_result(argv_translate,argv_result,result_format)
    

def print_usage(tub_info = app_info_mode ):   
    info_json = open(tub_info.path+'/info.json')
    info_dict = json.load(info_json)
    for i in info_dict['usage']:
        print(info_dict['usage'][i])
    info_json.close()


def translate_recur(tub_info = app_info_mode):
    try:
        if tub_info.mode == "translate":
            print("tub "+tub_info.fromlang+" to "+tub_info.tolang+" (? or puss 'q' to quit):")
        #elif tub_info.mode == "robot":
            #print("tub robot mode,type to ask,q to exit:")
        argv_next = input()
    
        if argv_next == 'q' or argv_next == '^D':
            sys.exit
        elif argv_next == '':
            translate_recur()
            """
        elif argv_next == 'cm':
            if tub_info.mode == "translate":
                tub_info.mode = "robot"
                tub_info.print_format = "r_mode"
            else:
                tub_info.mode = "translate"
                tub_info.print_format = "t_mode"
            #print(tub_info.mode)
            translate_recur()
            """
        elif argv_next == 'cl':
            if tub_info.fromlang=='en' and tub_info.tolang=='zh':
                tub_info.fromlang = 'zh'
                tub_info.tolang = 'en'
                #print('\n')
            else:
                tub_info.fromlang='en'
                tub_info.tolang='zh'
                #print('\n')
            translate_recur(tub_info)
        elif argv_next == 'clr':
            os.system('clear')
            translate_recur(tub_info)
        elif argv_next == 'reserve':
            print('command reserve')
        else :
            result = list()
            if tub_info.mode == "translate":
                result = translate(argv_next,tub_info.fromlang,tub_info.tolang)
            #elif tub_info.mode == "robot":
                #result = robot.robot_ask(argv_next)
            print_result(result,tub_info.print_format)
            #print_result(argv_next,translate(argv_next,from_lang,to_lang),result_format)
            translate_recur(tub_info)
    except (BaseException,Exception) as e:
        print(e)
        sys.exit()
