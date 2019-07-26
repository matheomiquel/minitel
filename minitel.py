#!/usr/bin/python3

import curses
import sys
import os

os.system("clear")

loop = True

kill = "kill "

force_kill = "kill -9 "

menu_process_list = ["continuer","retour au menu processeur ", "retourer au menu principal","Quitter"]

list_process_list = ["voir tout", "voir les processus pour tout les Users", "montre les Processus pour un utilisateur", 
            "affiche les processus non attachés à un terminal", "retour au menu processeur", "retourer au menu principal","Quitter"]

menu_principale = ["Informations générales","Réseaux", "Processus", "Quitter"]

general_list = ["Version Systeme Exploitation", "Date", "Version du Kernel", "Informations Hardware",
           "Fichiers Ouverts", "Processus Ouverts", "Paquets", "retourner au menu prinicpal", "Quitter"]

reseau_list = ["Adresse IP", "Interfaces", "Nombre de paquets", "Routes", "Forward", "retourner au menu prinicpal", "Quitter"]

process_list = ["liste des processus", "Obtenir le détail sur un processus","kill  un processus" ,"retourner au menu prinicpal", "Quitter"]

menu_base = ["continuer","retourer au menu principal","Quitter"]

force = ["utilisation simple", "utilisation forcé"]


###############################GENERALE#######################################################

#Version du système d'exploitation

def sys_exploit():
    os.system("clear")
    sortie = os.popen("lsb_release -d").read()
    print(sortie)

#date

def date():
    os.system("clear")
    sortie = os.popen("date").read()
    print(sortie)

#Version du Kernel

def kernel():
    os.system("clear")
    sortie = os.popen("uname -mr").read()
    print(sortie)

#Informations Hardware

def hardware():
    os.system("clear")
    sortie = os.popen("lscpu").read()
    print(sortie)

#Limite de fichiers ouverts

def file_open_limit():
    os.system("clear")
    sortie = os.popen("ulimit -n").read()
    print(sortie)

#Limite de processus ouverts

def procces_open_limit():
    os.system("clear")
    sortie = os.popen("ulimit -u").read()
    print(sortie)

#liste des paquets installés

def packet_downloads():
    os.system("clear")
    sortie = os.popen("dpkg-query -l").read()
    print(sortie)


###############################RESEAU#######################################################


#Adresse IP

def ip_adress():
    os.system("clear")
    sortie = os.popen("ip address show | grep eth0 | grep / | cut -c10-18").read()
    print(sortie)

#Interfaces existantes

def interface_exist():
    os.system("clear")
    sortie = os.popen("ip link show").read()
    print(sortie)

#Nombre de paquets transmis/reçus

def package():
    os.system("clear")
    sortie = os.popen("netstat -e").read()
    print(sortie)

#Routes

def routes():
    os.system("clear")
    sortie = os.popen("sudo route -n").read()
    print(sortie)

#forward de paquet activé

def forward_activate():
    os.system("clear")
    sortie = os.popen("sudo iptables -t nat -vnL").read()
    print(sortie)


###############################PROCESS###################################################


#liste des processus

#Voir tout les processus
def list_process():
    os.system("clear")
    sortie = os.popen("ps auxc").read()
    print(sortie)

#voir les processus pour tout les Users

def list_process_a():
    os.system("clear")
    sortie = os.popen("ps a").read()
    print(sortie)

#montre les Processus pour un utilisateur

def list_process_u():
    os.system("clear")
    sortie = os.popen("ps u").read()
    print(sortie)

#affiche les processus non attachés à un terminal

def list_process_x():
    os.system("clear")
    sortie = os.popen("ps x").read()
    print(sortie)

#detail sur les processus

def detail_on_process():
    os.system("clear")
    sortie = os.popen("ps ax -f").read()
    print(sortie)

def main(select):
    attributes = {}

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    attributes['highlighted'] = curses.color_pair(2)
###############################GETCH#######################################################
    c = 0  
    option = 0  
    while c != 10:  #la touche "Entre" en ASCII
        select.erase()

        curses.use_default_colors()

        curses.init_pair(1, curses.COLOR_RED, -1)

        for i in range(len(menu)):

            if i == option:
                attr = attributes['highlighted']

            else:
                attr = attributes['normal']

            select.addstr("{0}. ".format(i + 1))
            select.addstr(menu[i] + '\n', attr)

        c = select.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1

        elif c == curses.KEY_DOWN and option < len(menu) - 1:
            option += 1

        elif c == curses.KEY_UP and option == 0:
            option += (len(menu) - 1)

        elif c == curses.KEY_DOWN and option == len(menu) - 1:
            option -= (len(menu) - 1)

    return(option)

while loop:

    menu = menu_principale 
    test = curses.wrapper(main)
    if test == 0:


###############################INFO GENRALE###################################################
    

        general = True  
        while general:

            menu = general_list
            gen = curses.wrapper(main)
            if gen == 0:

                sys_exploit()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)


                #Version du système d'exploitation

                if verify == 0:
                    os.system("clear")
                    
                elif verify == 1:
                    menu = menu_principale
                    general = False

                elif verify == 2:
                    os.system("clear")
                    general = False
                    loop = False
            
            #Date
            elif gen == 1:
                date()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)
                if verify == 0:
                    os.system("clear")
                    
                elif verify == 1:
                    menu = menu_principale
                    general = False

                elif verify == 2:
                    os.system("clear")
                    general = False
                    loop = False

            #Version du Kernel

            elif gen == 2:
                kernel()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)

                if verify == 0:
                    os.system("clear")
                    
                elif verify == 1:
                    menu = menu_principale
                    general = False

                elif verify == 2:
                    os.system("clear")
                    general = False
                    loop = False

            #Informations Hardware

            elif gen == 3:
                hardware()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)

                if verify == 0:
                    os.system("clear")
                   
                elif verify == 1:
                    menu = menu_principale
                    general = False

                elif verify == 2:
                    os.system("clear")
                    general = False
                    loop = False

            #Limite de fichiers ouverts

            elif gen == 4:
                file_open_limit()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)
                if verify == 0:

                    os.system("clear")
                    
                elif verify == 1:
                    menu = menu_principale
                    general = False

                elif verify == 2:
                    os.system("clear")
                    general = False
                    loop = False

            #Limite de processus ouverts

            elif gen == 5:
                procces_open_limit()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)
                if verify == 0:
                    os.system("clear")
                   
                elif verify == 1:
                    menu = menu_principale
                    general = False

                elif verify == 2:
                    os.system("clear")
                    general = False
                    loop = False

            #liste des paquets installés

            elif gen == 6:
                packet_downloads()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)
                if verify == 0:
                    os.system("clear")
                   
                elif verify == 1:
                    menu = menu_principale
                    general = False

                elif verify == 2:
                    os.system("clear")
                    general = False
                    loop = False

            #retour au menu principale

            elif gen == 7:
                menu = menu_principale
                general = False

            #Quitter l'application

            elif gen == 8:
                os.system("clear")
                general = False
                loop = False


###############################RESEAU######################################################
    
    
    if test == 1:

        reseau = True
        while reseau:

            menu = reseau_list
            gen = curses.wrapper(main)
            #Adresse IP
            if gen == 0:

                ip_adress()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)

                if verify == 0:
                    os.system("clear")
                   
                elif verify == 1:
                    menu = menu_principale
                    reseau = False

                elif verify == 2:
                    os.system("clear")
                    reseau = False
                    loop = False

            #Interfaces existantes

            elif gen == 1:
                interface_exist()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)

                if verify == 0:
                    os.system("clear")
                   
                elif verify == 1:
                    menu = menu_principale
                    reseau = False

                elif verify == 2:
                    os.system("clear")
                    reseau = False
                    loop = False

            #Nombre de paquets transmis/reçus

            elif gen == 2:
                package()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)

                if verify == 0:
                    os.system("clear")
                   
                elif verify == 1:
                    menu = menu_principale
                    reseau = False

                elif verify == 2:
                    os.system("clear")
                    reseau = False
                    loop = False

            #Routes

            elif gen == 3:
                routes()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)

                if verify == 0:
                    os.system("clear")
                    
                elif verify == 1:
                    menu = menu_principale
                    reseau = False

                elif verify == 2:
                    os.system("clear")
                    reseau = False
                    loop = False

            #forward de paquet activé?

            elif gen == 4:
                forward_activate()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)

                if verify == 0:
                    os.system("clear")
                   
                elif verify == 1:
                    menu = menu_principale
                    reseau = False

                elif verify == 2:
                    os.system("clear")
                    reseau = False
                    loop = False

            #retour au menu principale

            elif gen == 5:
                menu = menu_principale
                reseau = False

            #Quitter l'application

            elif gen == 6:
                os.system("clear")
                reseau = False
                loop = False


###############################PROCESS#########################################################


    if test == 2:
        process = True
        while process:
            menu = process_list
            gen = curses.wrapper(main)
            #liste des processus
            if gen == 0:
                process_detail = True

                while process_detail:
                
                    menu = list_process_list
                    verify_process = curses.wrapper(main)

                    if verify_process == 0:
                        list_process()
                        input("appuyer sur ENTRER pour continuer")
                        menu = menu_process_list
                        verify = curses.wrapper(main)

                        if verify == 0:
                            os.system("clear")
                   
                        elif verify == 1:
                            menu = process_list
                            process_detail = False

                        elif verify == 2:
                            menu = menu_principale
                            process_detail = False
                            process_list = False

                       

                    elif verify_process == 1:
                        list_process_a()
                        input("appuyer sur ENTRER pour continuer")
                        menu = menu_process_list
                        verify = curses.wrapper(main)

                        if verify == 0:
                            os.system("clear")
                   
                        elif verify == 1:
                            os.system("clear")
                            menu = process_list
                            process_detail = False

                        elif verify == 2:
                            os.system("clear")
                            menu = menu_principale
                            process_detail = False
                            process_list = False

                        elif verify == 3:
                            os.system("clear")
                            process_detail = False
                            process = False
                            loop = False

                    elif verify_process == 2:
                        list_process_u()
                        input("appuyer sur ENTRER pour continuer")
                        menu = menu_process_list
                        verify = curses.wrapper(main)
                        if verify == 0:
                            os.system("clear")
                   
                        elif verify == 1:
                            os.system("clear")
                            menu = process_list
                            process_detail = False

                        elif verify == 2:
                            os.system("clear")
                            menu = menu_principale
                            process_detail = False
                            process_list = False

                        elif verify == 3:
                            os.system("clear")
                            process_detail = False
                            process = False
                            loop = False

                    elif verify_process == 3:
                        list_process_x()
                        input("appuyer sur ENTRER pour continuer")
                        menu = menu_process_list
                        verify = curses.wrapper(main)
                        if verify == 0:
                            os.system("clear")
                   
                        elif verify == 1:
                            os.system("clear")
                            menu = process_list
                            process_detail = False

                        elif verify == 2:
                            os.system("clear")
                            menu = menu_principale
                            process_detail = False
                            process_list = False

                        elif verify == 3:
                            os.system("clear")
                            process_detail = False
                            process = False
                            loop = False
                    

                    elif verify_process == 4:
                            os.system("clear")
                            process_detail = False


                    elif verify_process == 5:
                            os.system("clear")
                            menu = menu_principale
                            process_detail = False
                            process = False
                            

                    elif verify_process == 6:
                            os.system("clear")
                            menu = menu_principale
                            process_detail = False
                            process = False
                            loop = False

                
            #detail sur les processus
            elif gen == 1:
                detail_on_process()
                input("appuyer sur ENTRER pour continuer")
                menu = menu_base
                verify = curses.wrapper(main)
                if verify == 0:
                    os.system("clear")
                   
                elif verify == 1:
                    menu = menu_principale
                    process = False
                elif verify == 2:
                    os.system("clear")
                    process = False
                    loop = False
                    
            #KILL un processus

            elif gen == 2:

                os.system("clear")
                PID = input("rentrer le PID du processus a arreter: ")
                
                if PID == "":
                    os.system("clear")
                    input("vous n'avez pas rentrer de valeur")
                    break
                    

                os.system("clear")
                menu = force
                verify = curses.wrapper(main)

                
                    
                if verify == 0:
                    os.system("clear")
                    result =  "kill " + PID    
                    os.system(result)
                
                elif verify == 1:
                    os.system("clear")
                    result = "kill -9 "  + PID
                    os.system(result)
                
                
            #retour au menu principale
              
            elif gen == 3:
                menu = menu_principale
                process = False

            #Quitter l'application
            elif gen == 4:
                os.system("clear")
                process = False
                loop = False


###############################EXIT#######################################################


    #Quitter l'application

    if test == 3:
        os.system("clear")
        loop = False