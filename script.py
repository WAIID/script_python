########################################################
#-Script de Florian Rioufreyt                          #
#-Recuperation de donnees reseau                       #
########################################################
import os
import errno
import shutil
#import char_set

def creation_dossier():
        try:
           os.mkdir("info_Network")
        except OSError:
           print("Ce Dossier existe Deja")
           pass
        else:
     	    print("Dossier info_network cree")
        pass
creation_dossier()

def creation_dossier_bind():
        try:
           os.mkdir("info_Network/bind")
        except OSError:
           print("Ce Dossier existe Deja")
           pass
        else:
           print("Le sous dossier Bind cree")
        pass
creation_dossier_bind()


def add_bind():
        try:
                shutil.rmtree('info_Network/bind/')
                shutil.copytree('/etc/bind/','info_Network/bind')
        except IOError:
                print("Dossier bind ajoute ")
                pass
        else:
                print("non")
add_bind()


def commandsoutput():
        commands = ("ifconfig"," ")
        commands1 = ("route -n"," " )
        commands2 = ("iptables -L -n -v"," ")
        with open('info_Network/ifconfig_route_iptables.txt','w') as outfile:
                for command in commands:
                        outfile.write("-------------------- ifconfig -------------------- \n")
                        outfile.write(os.popen(command).read()+ "\n")
                        break
                for command in commands1:
                        outfile.write("-------------------- route -------------------- \n")
                        outfile.write(os.popen(command).read()+ "\n")
                        break
                for command in commands2:
                        outfile.write("-------------------- IPtables -------------------- \n")
                        outfile.write(os.popen(command).read()+ "\n")
                        break
commandsoutput()


#
#La copie s'effectue mais pas le try
#
def add_regionxml():
	try:
	   shutil.copy('/usr/share/era/modeles/region.xml','info_Network')
	except IOError:
      	   print("Region.xml est ajoute ")
	else:
	   print("Region.xml non ajoute ")
add_regionxml()

def add_agriates():
        try:
           shutil.copy('/var/lib/creole/agriates.zone.xml','info_Network')
        except EnvironmentError:
           print("agriates.xml est ajoute")
           pass
        else:
           print("agriates.xml non ajouter")
add_agriates()
