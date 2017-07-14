#!/usr/bin/python
# -*- coding:utf-8 -*-

######################################## LIBRARY ########################################

import os
import time
import sys, traceback

######################################## COLOR VARIABLES ########################################

yellow = "\033[1;33m"
normal = "\033[0;1m"
green = "\033[32;1m"
blue = "\033[34;1m"
red = "\033[31;1m"
white = "\033[0m"

######################################## LOGO CODESEC BR ########################################

codesec = """
\033[0m  ██████╗ ██████╗ ██████╗ ███████╗███████╗███████╗ ██████╗    \033[31;1m██████╗ ██████╗ 
\033[0m ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝    \033[31;1m██╔══██╗██╔══██╗
\033[0m ██║     ██║   ██║██║  ██║█████╗  ███████╗█████╗  ██║         \033[31;1m██████╔╝██████╔╝
\033[0m ██║     ██║   ██║██║  ██║██╔══╝  ╚════██║██╔══╝  ██║         \033[31;1m██╔══██╗██╔══██╗
\033[0m ╚██████╗╚██████╔╝██████╔╝███████╗███████║███████╗╚██████╗    \033[31;1m██████╔╝██║  ██║
\033[0m  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝    \033[31;1m╚═════╝ ╚═╝  ╚═╝
"""

######################################## SEPARATION LINE ########################################

line = """

\033[1;33m   **************************************************************************
"""

######################################## NETWORK SOCIAL CODESEC BR ########################################

network = """

\033[0;1m    [!] This software was based on Katoolin and was adapted for the functions of Distro Linux CodeSec BR

\033[1;33m    [+] Coded: SqueezySec                        
\033[1;33m    [+] Contact: @SqueezySec - Telegram

\033[31;1m    [!] http://fb.com/CodeSecBR            \033[0;1mFacebook
\033[31;1m    [!] http://fb.com/TerminalRoot404      \033[0;1mFacebook
\033[31;1m    [!] http://fb.com/SecretHackersTeam    \033[0;1mFacebook
\033[31;1m    [!] http://t.me/CodeSecBR              \033[0;1mTelegram
\033[31;1m    [!] http://t.me/TerminalRoot404        \033[0;1mTelegram
\033[31;1m    [!] http://github.com/CodeSecBR        \033[0;1mGithub

\033[0;1m    [!] Katoolin official script: https://github.com/LionSec/katoolin
"""

######################################## FUNTION EXIT ########################################

def exit_script():
	
	clear_logo_line()
	print(red + "    [-] Exiting the software ...\n")
	time.sleep(2)
	exit()

######################################## FUNTION CLEAR, LOGO, LINE ########################################

def clear_logo_line():

	os.system("clear")
	print codesec + line

######################################## FUNTION ADDING REPOSITORIES ########################################

def add_repo():

	clear_logo_line()
	print red + "    [+] Adding Kali Linux repositories\n" + yellow
	time.sleep(5)
	os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6 | pv -p -e -t -a -r")
	os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list | pv -p -e -t -a -r")

######################################## FUNTION UPDATING REPOSITORIES ########################################

def update():

	clear_logo_line()
	print red + "    [+] Updating repositories\n" + yellow
	time.sleep(5)
	os.system("apt-get update -m | pv -p -e -t -a -r")

######################################## FUNTION INSTALLING THE TOOLS ########################################

def install_tools():
	
	clear_logo_line()
	print red + "    [+] Installing tools for Pentest\n" + yellow
	time.sleep(5)
	os.system("apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/ | pv -p -e -t -a -r")

######################################## FUNTION REMOVING REPOSITORIES ########################################

def remo_repo():

	clear_logo_line()
	print red + "    [+] Removing repositories\n" + yellow
	time.sleep(5)
	infile = "/etc/apt/sources.list"
	outfile = "/etc/apt/sources.list"

	delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
	fin = open(infile)
	os.remove("/etc/apt/sources.list")
	fout = open(outfile, "w+")
	for line in fin:
	    for word in delete_list:
	        line = line.replace(word, "")
		fout.write(line)
	fin.close()
	fout.close()

######################################## FUNTION UPGRADE ########################################

def upgrade():

	clear_logo_line()
	print red + "    [+] Upgrading system\n" + yellow
	time.sleep(5)
	os.system("apt-get upgrade | pv -p -e -t -a -r")

######################################## FUNTION MAIN ########################################

def main():

	os.system("clear")
	print codesec + network
	time.sleep(10)
	
	add_repo()
	update()
	install_tools()
	remo_repo()
	update()
	upgrade()

################# STARTING A SCRIPT ########################################

try:

	main()

except KeyboardInterrupt:

	exit_script()
