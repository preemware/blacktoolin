#!/usr/bin/python

import os
import sys, traceback

def main():
	try:
		print ('''
\033[91m
M#"""""""'M  dP                   dP       M""""""""M                   dP oo          
##  mmmm. `M 88                   88       Mmmm  mmmM                   88             
#'        .M 88 .d8888b. .d8888b. 88  .dP  MMMM  MMMM .d8888b. .d8888b. 88 dP 88d888b. 
M#  MMMb.'YM 88 88'  `88 88'  `"" 88888"   MMMM  MMMM 88'  `88 88'  `88 88 88 88'  `88 
M#  MMMM'  M 88 88.  .88 88.  ... 88  `8b. MMMM  MMMM 88.  .88 88.  .88 88 88 88    88 
M#       .;M dP `88888P8 `88888P' dP   `YP MMMM  MMMM `88888P' `88888P' dP dP dP    dP 
M#########M                                MMMMMMMMMM                                  
                                                                                       \033[1;m
 \033[91m+ -- -- +=[ Author: Zatiel And Zayotic | Homepage: patreon.com/zatiel\033[1;m
 \033[91m+ -- -- +=[ 333 Tools \033[1;m


\033[1;91m[W] Before updating your system , please remove all blackarch repositories to avoid any kind of problem .\033[1;m
		''')
		def inicio1():
			while True:
				print ('''
1) Add BlackArch repositories & Update 
2) View Categories
3) Help

			''')
				if sys.version_info[0] < 3:
					opcion0 = raw_input("\033[91mbt > \033[1;m")
				else:
					opcion0 = input("\033[91mbt > \033[1;m")
				if opcion0 == "3":
					print (''' 
****************** +Commands+ ******************
\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m
\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m
		''')
			
				while opcion0 == "1":
					print ('''
1) Add BlackArch repositories
2) Update
3) Remove all BlackArch repositories
4) View the contents of pacman.conf file

					''')
					if sys.version_info[0] < 3:
						repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					else:
						repo = input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("curl -O https://blackarch.org/strap.sh")
						cmd2 = os.system("chmod +x strap.sh")
						cmd3 = os.system("./strap.sh")
					elif repo == "2":
						cmd3 = os.system("pacman -Sy")
					elif repo == "3":
						infile = "/etc/pacman.conf"
						outfile = "/etc/pacman.conf"

						delete_list = ["[blackarch]\n", "Include = /etc/pacman.d/blackarch-mirrorlist\n"]
						fin = open(infile)
						os.remove("/etc/pacman.conf")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print ("\033[1;31m\nAll blackarch repositories have been deleted !\n\033[1;m")
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "4":
						file = open('/etc/pacman.conf', 'r')

						print (file.read())

					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m")			


				def inicio():
					while opcion0 == "2":
						print ('''
\033[91m**************************** All Categories *****************************\033[1;m

1) Information Gathering			8) Exploitation Tools
2) Vulnerability Analysis			9) Forensics Tools
3) Wireless Attacks				10) Stress Testing
4) Web Applications				11) Password Attacks
5) Sniffing & Spoofing				12) Reverse Engineering
6) Maintaining Access				13) Hardware Hacking
7) Reporting Tools 				14) Extra
									
0) All

			 ''')
						print ("\033[1;32mSelect a category or press (0) to install all BlackArch linux tools .\n\033[1;m")
						if sys.version_info[0] < 3:
							opcion1 = raw_input("\033[91mbt > \033[1;m")
						else:
							opcion1 = input("\033[91mbt > \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "0":
							cmd = os.system("pacman -S acccheck ace amap tekdefense-automater braa casefile cdpsnarf cisco-torch cookie-cadger cisco-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce forager firewalk flashlight bing-ip2hosts ghost-phisher golismero goofile lbd maltego masscan metagoofil machinae nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark-qt wol-e xplico inundator intrace hping bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch cisco-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql-injection lynis nmap ohrwurm openvas oscanner powerfuzzer sfuzz sidguesser ntop dbpwaudit commix siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mitmap multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap fuxploider grabber jboss-autopwn joomscan jsql-injection maltego padbuster paros parsero plecost powerfuzzer proxyscan recon-ng skipfish sqlmap sqlninja sqlsus uatester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster hexinject iaxflood inviteflood inundator mitmproxy ohrwurm protos-sip rebind responder rtpbreak sipffer snapception sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark-qt xspy yersinia zaproxy cymothoa dbd dns2tcp httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis-ce magictree metagoofil nipper pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego set shellnoob sqlmap thc-ipv6 yersinia beef binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphoneanalyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig fuxploider iaxflood inviteflood ipv6toolkit mdk3 reaver rtp-flood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash hashcat hashid hexorbase john johnny keimpx maltego maskprocessor cryptohazemultiforcer ncrack oclhashcat pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab zaproxy android-apktool dex2jar disitool edb-debugger jad javasnoop radare2 ollydbg smali valgrind yara android-sdk android-apktool arduino dex2jar sakis3g smali bing-ip2hosts")	
						while opcion1 == "1":
							print ('''
\033[91m=+[ Information Gathering\033[1;m

 1) acccheck					30) lbd
 2) ace-voip					31) Maltego
 3) Amap					32) masscan
 4) Automater					33) Metagoofil
 5) bing-ip2hosts				34) machinae
 6) braa					35) Nmap
 7) CaseFile					36) ntop
 8) CDPSnarf					37) p0f
 9) cisco-torch					38) Parsero
10) Cookie Cadger				39) Recon-ng
11) copy-router-config				40) SET
12) DMitry					41) smtp-user-enum
13) dnmap					42) snmpcheck
14) dnsenum					43) sslcaudit
15) dnsmap					44) SSLsplit
16) DNSRecon					45) sslstrip
17) dnstracer					46) SSLyze
18) dnswalk					47) THC-IPV6
19) DotDotPwn					48) theHarvester
20) enum4linux					49) TLSSLed
21) enumIAX					50) twofi
22) exploitdb					51) URLCrazy
23) Fierce					52) Wireshark
24) Firewalk					53) WOL-E
25) Flashlight					54) Xplico
26) Forager					55) inundator
27) Ghost Phisher				56) InTrace
28) GoLismero					57) hping
29) goofile

0) Install all Information Gathering tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S acccheck")
							elif opcion2 == "2":
								cmd = os.system("pacman -S ace")
							elif opcion2 == "3":
								cmd = os.system("pacman -S amap")
							elif opcion2 == "4":
								cmd = os.system("pacman -S tekdefense-automater")
							elif opcion2 == "5":
								cmd = os.system("pacman -S bing-ip2hosts")
							elif opcion2 == "6":
								cmd = os.system("pacman -S braa")
							elif opcion2 == "7":
								cmd = os.system("pacman -S casefile")
							elif opcion2 == "8":
								cmd = os.system("pacman -S cdpsnarf")
							elif opcion2 == "9":
								cmd = os.system("pacman -S cisco-torch")
							elif opcion2 == "10":
								cmd = os.system("pacman -S cookie-cadger")
							elif opcion2 == "11":
								cmd = os.system("pacman -S cisco-router-config")
							elif opcion2 == "12":
								cmd = os.system("pacman -S dmitry")
							elif opcion2 == "13":
								cmd = os.system("pacman -S dnmap")
							elif opcion2 == "14":
								cmd = os.system("pacman -S dnsenum")
							elif opcion2 == "15":
								cmd = os.system("pacman -S dnsmap")
							elif opcion2 == "16":
								cmd = os.system("pacman -S dnsrecon")
							elif opcion2 == "17":
								cmd = os.system("pacman -S dnstracer")
							elif opcion2 == "18":
								cmd = os.system("pacman -S dnswalk")
							elif opcion2 == "19":
								cmd = os.system("pacman -S dotdotpwn")
							elif opcion2 == "20":
								cmd = os.system("pacman -S enum4linux")
							elif opcion2 == "21":
								cmd = os.system("pacman -S enumiax")
							elif opcion2 == "22":
								cmd = os.system("pacman -S exploitdb")
							elif opcion2 == "23":
								cmd = os.system("pacman -S fierce")
							elif opcion2 == "24":
								cmd = os.system("pacman -S firewalk")
							elif opcion2 == "25":
								cmd = os.system("pacman -S flashlight")
							elif opcion2 == "26":
								cmd = os.system("pacman -S forager")
							elif opcion2 == "27":
								cmd = os.system("pacman -S ghost-phisher")
							elif opcion2 == "28":
								cmd = os.system("pacman -S golismero")
							elif opcion2 == "29":
								cmd = os.system("pacman -S goofile")
							elif opcion2 == "30":
								cmd = os.system("pacman -S lbd")
							elif opcion2 == "31":
								cmd = os.system("pacman -S maltego")
							elif opcion2 == "32":
								cmd = os.system("pacman -S masscan")
							elif opcion2 == "33":
								cmd = os.system("pacman -S metagoofil")
							elif opcion2 == "34":
								cmd = os.system("pacman -S machinae")
							elif opcion2 == "35":
								cmd = os.system("pacman -S nmap")
							elif opcion2 == "36":
								cmd = os.system("pacman -S ntop")
							elif opcion2 == "37":
								cmd = os.system("pacman -S p0f")
							elif opcion2 == "38":
								cmd = os.system("pacman -S parsero")
							elif opcion2 == "39":
								cmd = os.system("pacman -S recon-ng")
							elif opcion2 == "40":
								cmd = os.system("pacman -S set")
							elif opcion2 == "41":
								cmd = os.system("pacman -S smtp-user-enum")
							elif opcion2 == "42":
								cmd = os.system("pacman -S snmpcheck")
							elif opcion2 == "43":
								cmd = os.system("pacman -S sslcaudit")
							elif opcion2 == "44":
								cmd = os.system("pacman -S sslsplit")
							elif opcion2 == "45":
								cmd = os.system("pacman -S sslstrip")
							elif opcion2 == "46":
								cmd = os.system("pacman -S sslyze")
							elif opcion2 == "47":
								cmd = os.system("pacman -S thc-ipv6")
							elif opcion2 == "48":
								cmd = os.system("pacman -S theharvester")
							elif opcion2 == "49":
								cmd = os.system("pacman -S tlssled")
							elif opcion2 == "50":
								cmd = os.system("pacman -S twofi")
							elif opcion2 == "51":
								cmd = os.system("pacman -S urlcrazy")
							elif opcion2 == "52":
								cmd = os.system("pacman -S wireshark-qt")
							elif opcion2 == "53":
								cmd = os.system("pacman -S wol-e")
							elif opcion2 == "54":
								cmd = os.system("pacman -S xplico")
							elif opcion2 == "55":
								cmd = os.system("pacman -S inundator")
							elif opcion2 == "56":
								cmd = os.system("pacman -S intrace")
							elif opcion2 == "57":
								cmd = os.system("pacman -S hping")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()		
							elif opcion2 == "0":
								cmd = os.system("pacman -S acccheck ace amap tekdefense-automater bing-ip2hosts braa casefile cdpsnarf cisco-torch cookie-cadger cisco-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk  r ghost-phisher golismero goofile lbd maltego masscan metagoofil machinae nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark-qt wol-e xplico inundator intrace hping && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")				
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")



						while opcion1 == "2":
							print ('''
\033[91m=+[ Vulnerability Analysis\033[1;m

 1) BBQSQL				18) Nmap
 2) BED					19) ohrwurm
 3) cisco-auditing-tool			20) openvas
 4) cisco-global-exploiter		21) Oscanner
 5) cisco-ocs				22) Powerfuzzer
 6) cisco-torch				23) sfuzz
 7) copy-router-config			24) SidGuesser
 8) commix				25) SIPArmyKnife
 9) DBPwAudit				26) sqlmap
10) DoonaDot				27) Sqlninja
11) DotPwn				28) sqlsus
12) Greenbone Security Assistant 	29) THC-IPV6
13) GSD					30) tnscmd
14) HexorBase				31) unix-privesc-check
15) Inguma				32) Yersinia
16) jSQL				
17) Lynis				
					

0) Install all Vulnerability Analysis tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S bbqsql")
							elif opcion2 == "2":
								cmd = os.system("pacman -S bed")
							elif opcion2 == "3":
								cmd = os.system("pacman -S cisco-auditing-tool")
							elif opcion2 == "4":
								cmd = os.system("pacman -S cisco-global-exploiter")
							elif opcion2 == "5":
								cmd = os.system("pacman -S cisco-ocs")
							elif opcion2 == "6":
								cmd = os.system("pacman -S cisco-torch")
							elif opcion2 == "7":
								cmd = os.system("pacman -S cisco-router-config")
							elif opcion2 == "8":
								cmd = os.system("pacman -S commix")
							elif opcion2 == "9":
								cmd = os.system("pacman -S dbpwaudit")
							elif opcion2 == "10":
								cmd = os.system("pacman -S doona")
							elif opcion2 == "11":
								cmd = os.system("pacman -S dotdotpwn")
							elif opcion2 == "12":
								cmd = os.system("pacman -S greenbone-security-assistant")
							elif opcion2 == "13":
								cmd = os.system("pacman -S gsd")
							elif opcion2 == "14":
								cmd = os.system("pacman -S hexorbase")
							elif opcion2 == "15":
								cmd = os.system("pacman -S inguma")
							elif opcion2 == "16":
								cmd = os.system("pacman -S jsql-injection")
							elif opcion2 == "17":
								cmd = os.system("pacman -S lynis")
							elif opcion2 == "18":
								cmd = os.system("pacman -S nmap")
							elif opcion2 == "19":
								cmd = os.system("pacman -S ohrwurm")
							elif opcion2 == "20":
								cmd = os.system("pacman -S openvas")
							elif opcion2 == "21":
								cmd = os.system("pacman -S oscanner")
							elif opcion2 == "22":
								cmd = os.system("pacman -S powerfuzzer")
							elif opcion2 == "23":
								cmd = os.system("pacman -S sfuzz")
							elif opcion2 == "24":
								cmd = os.system("pacman -S sidguesser")
							elif opcion2 == "25":
								cmd = os.system("pacman -S siparmyknife")
							elif opcion2 == "26":
								cmd = os.system("pacman -S sqlmap")
							elif opcion2 == "27":
								cmd = os.system("pacman -S sqlninja")
							elif opcion2 == "28":
								cmd = os.system("pacman -S sqlsus")
							elif opcion2 == "29":
								cmd = os.system("pacman -S thc-ipv6")
							elif opcion2 == "30":
								cmd = os.system("pacman -S tnscmd")
							elif opcion2 == "31":
								cmd = os.system("pacman -S unix-privesc-check")
							elif opcion2 == "32":
								cmd = os.system("pacman -S yersinia")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							elif opcion2 == "0":
								cmd = os.system("pacman -S bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch cisco-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql-injection lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd unix-privesc-check yersinia")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "3":
							print ('''
		\033[91m=+[ Wireless Attacks\033[1;m

 1) Aircrack-ng				17) KillerBee
 2) Asleap				18) Kismet
 3) Bluelog				19) mdk3
 4) BlueMaho				20) mfcuk
 5) Bluepot				21) mfoc
 6) BlueRanger				22) mitmap
 7) Bluesnarfer				23) Multimon-NG
 8) Bully				24) PixieWPS
 9) coWPAtty				25) Reaver
10) crackle				26) redfang
11) eapmd5pass				27) RTLSDR Scanner
12) Fern Wifi Cracker			28) Spooftooph
13) Ghost Phisher			29) Wifi Honey
14) GISKismet				30) Wifitap				
15) gr-scan				31) wifite
16) kalibrate-rtl			 

0) Install all Wireless Attacks tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S aircrack-ng")
							elif opcion2 == "2":
								cmd = os.system("pacman -S asleap")
							elif opcion2 == "3":
								cmd = os.system("pacman -S bluelog")
							elif opcion2 == "4":
								cmd = os.system("pacman -S bluemaho")
							elif opcion2 == "5":
								cmd = os.system("pacman -S bluepot")
							elif opcion2 == "6":
								cmd = os.system("pacman -S blueranger")
							elif opcion2 == "7":
								cmd = os.system("pacman -S bluesnarfer")
							elif opcion2 == "8":
								cmd = os.system("pacman -S bully")
							elif opcion2 == "9":
								cmd = os.system("pacman -S cowpatty")
							elif opcion2 == "10":
								cmd = os.system("pacman -S crackle")
							elif opcion2 == "11":
								cmd = os.system("pacman -S eapmd5pass")
							elif opcion2 == "12":
								cmd = os.system("pacman -S fern-wifi-cracker")
							elif opcion2 == "13":
								cmd = os.system("pacman -S ghost-phisher")
							elif opcion2 == "14":
								cmd = os.system("pacman -S giskismet")
							elif opcion2 == "15":
								cmd = os.system("pacman -S gr-scan")
							elif opcion2 == "16":
								cmd = os.system("pacman -S kalibrate-rtl")
							elif opcion2 == "17":
								cmd = os.system("pacman -S killerbee")
							elif opcion2 == "18":
								cmd = os.system("pacman -S kismet")
							elif opcion2 == "19":
								cmd = os.system("pacman -S mdk3")
							elif opcion2 == "20":
								cmd = os.system("pacman -S mfcuk")
							elif opcion2 == "21":
								cmd = os.system("pacman -S mfoc")
							elif opcion2 == "22":
								cmd = os.system("pacman -S mitmap")
							elif opcion2 == "23":
								cmd = os.system("pacman -S multimon-ng")
							elif opcion2 == "24":
								cmd = os.system("pacman -S pixiewps")
							elif opcion2 == "25":
								cmd = os.system("pacman -S reaver")
							elif opcion2 == "26":
								cmd = os.system("pacman -S redfang")
							elif opcion2 == "27":
								cmd = os.system("pacman -S rtlsdr-scanner")
							elif opcion2 == "28":
								cmd = os.system("pacman -S spooftooph")
							elif opcion2 == "29":
								cmd = os.system("pacman -S wifi-honey")
							elif opcion2 == "30":
								cmd = os.system("pacman -S wifitap")
							elif opcion2 == "31":
								cmd = os.system("pacman -S wifite")
							elif opcion2 == "0":
								cmd = os.system("pacman -S aircrack-ng asleap bluelog bluemaho bluepot blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mitmap multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "4":
							print ('''
\033[91m=+[ Web Applications\033[1;m

 1) apache-users			21) Parsero
 2) Arachni				22) plecost
 3) BBQSQL				23) Powerfuzzer
 4) BlindElephant			24) proxyscan
 5) Burp Suite				25) Recon-ng
 6) commix				26) Skipfish
 7) CutyCapt				27) sqlmap
 8) DAVTest				28) Sqlninja
 9) deblaze				29) sqlsus
10) DIRB				30) uatester
11) DirBuster				31) Uniscan
12) fimap				32) Vega
13) fuxploider				33) w3af
14) Grabber				34) WebScarab
15) jboss-autopwn			35) Webshag
16) joomscan				36) WebSlayer
17) jSQL				37) WebSploit
18) Maltego 				38) Wfuzz
19) PadBuster				39) WPScan
20) Paros				40) XSSer
					41) zaproxy

0) Install all Web Applications tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S apache-users")
							elif opcion2 == "2":
								cmd = os.system("pacman -S arachni")
							elif opcion2 == "3":
								cmd = os.system("pacman -S bbqsql")
							elif opcion2 == "4":
								cmd = os.system("pacman -S blindelephant")
							elif opcion2 == "5":
								cmd = os.system("pacman -S burpsuite")
							elif opcion2 == "6":
								cmd = os.system("pacman -S cutycapt")
							elif opcion2 == "7":
								cmd = os.system("pacman -S commix")
							elif opcion2 == "8":
								cmd = os.system("pacman -S davtest")
							elif opcion2 == "9":
								cmd = os.system("pacman -S deblaze")
							elif opcion2 == "10":
								cmd = os.system("pacman -S dirb")
							elif opcion2 == "11":
								cmd = os.system("pacman -S dirbuster")
							elif opcion2 == "12":
								cmd = os.system("pacman -S fimap")
							elif opcion2 == "13":
								cmd = os.system("pacman -S fuxploider")
							elif opcion2 == "14":
								cmd = os.system("pacman -S grabber")
							elif opcion2 == "15":
								cmd = os.system("pacman -S jboss-autopwn")
							elif opcion2 == "16":
								cmd = os.system("pacman -S joomscan")
							elif opcion2 == "17":
								cmd = os.system("pacman -S jsql-injection")
							elif opcion2 == "18":
								cmd = os.system("pacman -S maltego")
							elif opcion2 == "19":
								cmd = os.system("pacman -S padbuster")
							elif opcion2 == "20":
								cmd = os.system("pacman -S paros")
							elif opcion2 == "21":
								cmd = os.system("pacman -S parsero")
							elif opcion2 == "22":
								cmd = os.system("pacman -S plecost")
							elif opcion2 == "23":
								cmd = os.system("pacman -S powerfuzzer")
							elif opcion2 == "24":
								cmd = os.system("pacman -S proxyscan")
							elif opcion2 == "25":
								cmd = os.system("pacman -S recon-ng")
							elif opcion2 == "26":
								cmd = os.system("pacman -S skipfish")
							elif opcion2 == "27":
								cmd = os.system("pacman -S sqlmap")
							elif opcion2 == "28":
								cmd = os.system("pacman -S sqlninja")
							elif opcion2 == "29":
								cmd = os.system("pacman -S sqlsus")
							elif opcion2 == "30":
								cmd = os.system("pacman -S uatester")
							elif opcion2 == "31":
								cmd = os.system("pacman -S uniscan")
							elif opcion2 == "32":
								cmd = os.system("pacman -S vega")
							elif opcion2 == "33":
								cmd = os.system("pacman -S w3af")
							elif opcion2 == "34":
								cmd = os.system("pacman -S webscarab")
							elif opcion2 == "35":
								cmd = os.system("pacman -S webshag")
							elif opcion2 == "36":
								cmd = os.system("pacman -S webslayer")
							elif opcion2 == "37":
								cmd = os.system("pacman -S websploit")
							elif opcion2 == "38":
								cmd = os.system("pacman -S wfuzz")
							elif opcion2 == "39":
								cmd = os.system("pacman -S wpscan")
							elif opcion2 == "40":
								cmd = os.system("pacman -S xsser")
							elif opcion2 == "41":
								cmd = os.system("pacman -S zaproxy")										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()	
							elif opcion2 == "0":
								cmd = os.system("pacman -S apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap fuxploider grabber jboss-autopwn joomscan jsql-injection maltego padbuster paros parsero plecost powerfuzzer proxyscan recon-ng skipfish sqlmap sqlninja sqlsus uatester uniscan vega w3af webscarab webshag websploit webslayer wfuzz wpscan xsser zaproxy")												
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "5":
							print ('''
\033[91m=+[ Sniffing & Spoofing\033[1;m

 1) Burp Suite				17) snapception
 2) DNSChef				18) sctpscan
 3) fiked				19) SIPArmyKnife
 4) hamster				20) SIPp
 5) HexInject				21) SIPVicious
 6) iaxflood				22) SniffJoke
 7) inviteflood				23) SSLsplit
 8) inundator				24) sslstrip
 9) isr-evilgrade			25) THC-IPV6
10) mitmproxy				26) VoIPHopper
11) ohrwurm				27) WebScarab
12) protos-sip				28) Wifi Honey
13) rebind				29) Wireshark
14) responder				30) xspy
15) rtpbreak				31) Yersinia
16) sipffer				32) zaproxy 

0) Install all Sniffing & Spoofing tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S burpsuite")

							elif opcion2 == "2":
								cmd = os.system("pacman -S dnschef")

							elif opcion2 == "3":
								cmd = os.system("pacman -S fiked")
							elif opcion2 == "4":
								cmd = os.system("pacman -S hamster")
							elif opcion2 == "5":
								cmd = os.system("pacman -S hexinject")
							elif opcion2 == "6":
								cmd = os.system("pacman -S iaxflood")
							elif opcion2 == "7":
								cmd = os.system("pacman -S inviteflood")
							elif opcion2 == "8":
								cmd = os.system("pacman -S inundator")
							elif opcion2 == "9":
								cmd = os.system("pacman -S evilgrade")
							elif opcion2 == "10":
								cmd = os.system("pacman -S mitmproxy")
							elif opcion2 == "11":
								cmd = os.system("pacman -S ohrwurm")
							elif opcion2 == "12":
								cmd = os.system("pacman -S protos-sip")
							elif opcion2 == "13":
								cmd = os.system("pacman -S rebind")
							elif opcion2 == "14":
								cmd = os.system("pacman -S responder")
							elif opcion2 == "15":
								cmd = os.system("pacman -S rtpbreak")
							elif opcion2 == "16":
								cmd = os.system("pacman -S sipffer")
							elif opcion2 == "17":
								cmd = os.system("pacman -S snapception")
							elif opcion2 == "18":
								cmd = os.system("pacman -S sctpscan")
							elif opcion2 == "19":
								cmd = os.system("pacman -S siparmyknife")
							elif opcion2 == "20":
								cmd = os.system("pacman -S sipp")
							elif opcion2 == "21":
								cmd = os.system("pacman -S sipvicious")
							elif opcion2 == "22":
								cmd = os.system("pacman -S sniffjoke")
							elif opcion2 == "23":
								cmd = os.system("pacman -S sslsplit")
							elif opcion2 == "24":
								cmd = os.system("pacman -S sslstrip")
							elif opcion2 == "25":
								cmd = os.system("pacman -S thc-ipv6")
							elif opcion2 == "26":
								cmd = os.system("pacman -S voiphopper")
							elif opcion2 == "27":
								cmd = os.system("pacman -S webscarab")
							elif opcion2 == "28":
								cmd = os.system("pacman -S wifi-honey")
							elif opcion2 == "29":
								cmd = os.system("pacman -S wireshark-qt")
							elif opcion2 == "30":
								cmd = os.system("pacman -S xspy")
							elif opcion2 == "31":
								cmd = os.system("pacman -S yersinia")
							elif opcion2 == "32":
								cmd = os.system("pacman -S zaproxy")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()


							elif opcion2 == "0":
								cmd = os.system("pacman -S burpsuite dnschef fiked hamster hexinject iaxflood inviteflood inundator evilgrade mitmproxy ohrwurm protos-sip rebind responder rtpbreak sipffer snapception sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark-qt xspy yersinia zaproxy")  
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "6":
							print ('''
\033[91m=+[ Maintaining Access\033[1;m

 1) Cymothoa
 2) dbd
 3) dns2tcp
 4) httptunnel	
 5) Intersect
 6) Nishang
 7) polenum
 8) PowerSploit
 9) pwnat
 10) RidEnum
 11) sbd
 12) U3-Pwn
 13) Webshells
 14) Weevely

0) Install all Maintaining Access tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S cymothoa")
							elif opcion2 == "2":
								cmd = os.system("pacman -S dbd")
							elif opcion2 == "3":
								cmd = os.system("pacman -S dns2tcp")
							elif opcion2 == "4":
								cmd = os.system("pacman -S httptunnel")
							elif opcion2 == "5":
								cmd = os.system("pacman -S intersect")
							elif opcion2 == "6":
								cmd = os.system("pacman -S nishang")
							elif opcion2 == "7":
								cmd = os.system("pacman -S polenum")
							elif opcion2 == "8":
								cmd = os.system("pacman -S powersploit")
							elif opcion2 == "9":
								cmd = os.system("pacman -S pwnat")
							elif opcion2 == "10":
								cmd = os.system("pacman -S ridenum")
							elif opcion2 == "11":
								cmd = os.system("pacman -S sbd")
							elif opcion2 == "12":
								cmd = os.system("pacman -S u3-pwn")
							elif opcion2 == "13":
								cmd = os.system("pacman -S webshells")
							elif opcion2 == "14":
								cmd = os.system("pacman -S weevely")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S cymothoa dbd dns2tcp httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "7":
							print ('''
\033[91m=+[ Reporting Tools\033[1;m

1) CaseFile
2) CutyCapt
3) dos2unix
4) Dradis	
5) MagicTree
6) Metagoofil
7) Nipper
8) pipal

0) Install all Reporting Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S casefile")

							elif opcion2 == "2":
								cmd = os.system("pacman -S cutycapt")

							elif opcion2 == "3":
								cmd = os.system("pacman -S dos2unix")
							elif opcion2 == "4":
								cmd = os.system("pacman -S dradis-ce")
							elif opcion2 == "5":
								cmd = os.system("pacman -S magictree")
							elif opcion2 == "6":
								cmd = os.system("pacman -S metagoofil")
							elif opcion2 == "7":
								cmd = os.system("pacman -S nipper")
							elif opcion2 == "8":
								cmd = os.system("pacman -S pipal")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S casefile cutycapt dos2unix dradis-ce magictree metagoofil nipper pipal")  
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "8":
							print ('''
\033[91m=+[ Exploitation Tools\033[1;m

 1) Armitage
 2) Backdoor Factory
 3) BeEF
 4) cisco-auditing-tool
 5) cisco-global-exploiter	
 6) cisco-ocs
 7) cisco-torch
 8) commix
 9) crackle
10) jboss-autopwn
11) Linux Exploit Suggester
12) Maltego
13) SET
14) ShellNoob
15) sqlmap
16) THC-IPV6
17) Yersinia
18) Metasploit

0) Install all Exploitation Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							
							if opcion2 == "1":
								cmd = os.system("pacman -S armitage")

							elif opcion2 == "2":
								cmd = os.system("pacman -S backdoor-factory")

							elif opcion2 == "3":
								cmd = os.system("pacman -S beef")
							elif opcion2 == "4":
								cmd = os.system("pacman -S cisco-auditing-tool")
							elif opcion2 == "5":
								cmd = os.system("pacman -S cisco-global-exploiter")
							elif opcion2 == "6":
								cmd = os.system("pacman -S cisco-ocs")
							elif opcion2 == "7":
								cmd = os.system("pacman -S cisco-torch")
							elif opcion2 == "8":
								cmd = os.system("pacman -S commix")
							elif opcion2 == "9":
								cmd = os.system("pacman -S crackle")
							elif opcion2 == "10":
								cmd = os.system("pacman -S jboss-autopwn")
							elif opcion2 == "11":
								cmd = os.system("pacman -S linux-exploit-suggester")
							elif opcion2 == "12":
								cmd = os.system("pacman -S maltego")
							elif opcion2 == "13":
								cmd = os.system("pacman -S set")
							elif opcion2 == "14":
								cmd = os.system("pacman -S shellnoob")
							elif opcion2 == "15":
								cmd = os.system("pacman -S sqlmap")
							elif opcion2 == "16":
								cmd = os.system("pacman -S thc-ipv6")
							elif opcion2 == "17":
								cmd = os.system("pacman -S yersinia")
							elif opcion2 == "18":
								cmd = os.system("pacman -S metasploit")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch commix crackle jboss-autopwn linux-exploit-suggester maltego set shellnoob sqlmap thc-ipv6 yersinia beef metasploit")  						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "9":
							print ('''
\033[91m=+[ Forensics Tools\033[1;m

 1) Binwalk				11) extundelete
 2) bulk-extractor			12) Foremost
 3) Capstone				13) Galleta
 4) chntpw				14) Guymager
 5) Cuckoo				15) iPhone Backup Analyzer
 6) dc3dd				16) p0f
 7) ddrescue				17) pdf-parser
 8) DFF					18) pdfid
 9) disitool				19) pdgmail
10) Dumpzilla				20) peepdf
					21) RegRipper
					22) Volatility
					23) Xplico

0) Install all Forensics Tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")

							if opcion2 == "1":
								cmd = os.system("pacman -S binwalk")

							elif opcion2 == "2":
								cmd = os.system("pacman -S bulk-extractor")

							elif opcion2 == "3":
								cmd = os.system("pacman -S capstone")
							elif opcion2 == "4":
								cmd = os.system("pacman -S chntpw")
							elif opcion2 == "5":
								cmd = os.system("pacman -S cuckoo")
							elif opcion2 == "6":
								cmd = os.system("pacman -S dc3dd")
							elif opcion2 == "7":
								cmd = os.system("pacman -S ddrescue")
							elif opcion2 == "8":
								cmd = os.system("pacman -S dff")
							elif opcion2 == "9":
								cmd = os.system("pacman -S disitool")
							elif opcion2 == "10":
								cmd = os.system("pacman -S dumpzilla")
							elif opcion2 == "11":
								cmd = os.system("pacman -S extundelete")
							elif opcion2 == "12":
								cmd = os.system("pacman -S foremost")
							elif opcion2 == "13":
								cmd = os.system("pacman -S galleta")
							elif opcion2 == "14":
								cmd = os.system("pacman -S guymager")
							elif opcion2 == "15":
								cmd = os.system("pacman -S iphoneanalyzer")
							elif opcion2 == "16":
								cmd = os.system("pacman -S p0f")
							elif opcion2 == "17":
								cmd = os.system("pacman -S pdf-parser")
							elif opcion2 == "18":
								cmd = os.system("pacman -S pdfid")
							elif opcion2 == "19":
								cmd = os.system("pacman -S pdgmail")
							elif opcion2 == "20":
								cmd = os.system("pacman -S peepdf")
							elif opcion2 == "21":
								cmd = os.system("pacman -S regripper")
							elif opcion2 == "22":
								cmd = os.system("pacman -S volatility")
							elif opcion2 == "23":
								cmd = os.system("pacman -S xplico")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphoneanalyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "10":
							print ('''
\033[91m=+[ Stress Testing\033[1;m

 1) DHCPig
 2) fuxploider
 3) iaxflood
 4) Inundator
 5) inviteflood	
 6) ipv6toolkit
 7) mdk3
 8) Reaver
 9) rtp-flood
10) SlowHTTPTest
11) t50
12) Termineter
13) THC-IPV6
14) THC-SSL-DOS 		

0) Install all Stress Testing tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S dhcpig")

							elif opcion2 == "2":
								cmd = os.system("pacman -S fuxploider")

							elif opcion2 == "3":
								cmd = os.system("pacman -S iaxflood")
							elif opcion2 == "4":
								cmd = os.system("pacman -S inundator")
							elif opcion2 == "5":
								cmd = os.system("pacman -S inviteflood")
							elif opcion2 == "6":
								cmd = os.system("pacman -S ipv6toolkit")
							elif opcion2 == "7":
								cmd = os.system("pacman -S mdk3")
							elif opcion2 == "8":
								cmd = os.system("pacman -S reaver")
							elif opcion2 == "9":
								cmd = os.system("pacman -S rtp-flood")
							elif opcion2 == "10":
								cmd = os.system("pacman -S slowhttptest")
							elif opcion2 == "11":
								cmd = os.system("pacman -S t50")
							elif opcion2 == "12":
								cmd = os.system("pacman -S termineter")
							elif opcion2 == "13":
								cmd = os.system("pacman -S thc-ipv6")
							elif opcion2 == "14":
								cmd = os.system("pacman -S thc-ssl-dos ")    				             										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S dhcpig fuxploider iaxflood inviteflood ipv6toolkit mdk3 reaver rtp-flood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "11":
							print ('''
\033[91m=+[ Password Attacks\033[1;m

 1) acccheck				19) Maskprocessor
 2) Burp Suite				20) multiforcer
 3) CeWL				21) Ncrack
 4) chntpw				22) oclhashcat
 5) cisco-auditing-tool			23) PACK
 6) CmosPwd				24) patator
 7) creddump				25) phrasendrescher
 8) crunch				26) polenum
 9) DBPwAudit				27) RainbowCrack
10) findmyhash				28) rcracki-mt
11) hashcat				29) RSMangler
12) hashid				30) SQLdict
13) HexorBase				31) Statsprocessor
14) Hydra				32) THC-pptp-bruter
15) John the Ripper			33) TrueCrack
16) Johnny				34) WebScarab 
17) keimpx				35) wordbrutepress 
18) Maltego 				36) zaproxy 

0) Install all Password Attacks tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S acccheck")

							elif opcion2 == "2":
								cmd = os.system("pacman -S burpsuite")

							elif opcion2 == "3":
								cmd = os.system("pacman -S cewl")
							elif opcion2 == "4":
								cmd = os.system("pacman -S chntpw")
							elif opcion2 == "5":
								cmd = os.system("pacman -S cisco-auditing-tool")
							elif opcion2 == "6":
								cmd = os.system("pacman -S cmospwd")
							elif opcion2 == "7":
								cmd = os.system("pacman -S creddump")
							elif opcion2 == "8":
								cmd = os.system("pacman -S crunch")
							elif opcion2 == "9":
								cmd = os.system("pacman -S dbpwaudit")
							elif opcion2 == "10":
								cmd = os.system("pacman -S findmyhash")
							elif opcion2 == "11":
								cmd = os.system("pacman -S hashcat")
							elif opcion2 == "12":
								cmd = os.system("pacman -S hashid")
							elif opcion2 == "13":
								cmd = os.system("pacman -S hexorbase")
							elif opcion2 == "14":
								cmd = os.system("pacman -S hydra")
							elif opcion2 == "15":
								cmd = os.system("pacman -S john")
							elif opcion2 == "16":
								cmd = os.system("pacman -S johnny")
							elif opcion2 == "17":
								cmd = os.system("pacman -S keimpx")
							elif opcion2 == "18":
								cmd = os.system("pacman -S maltego")
							elif opcion2 == "19":
								cmd = os.system("pacman -S maskprocessor")
							elif opcion2 == "20":
								cmd = os.system("pacman -S cryptohazemultiforcer")
							elif opcion2 == "21":
								cmd = os.system("pacman -S ncrack")
							elif opcion2 == "22":
								cmd = os.system("pacman -S oclhashcat")
							elif opcion2 == "23":
								cmd = os.system("pacman -S pack")
							elif opcion2 == "24":
								cmd = os.system("pacman -S patator")
							elif opcion2 == "25":
								cmd = os.system("pacman -S phrasendrescher")
							elif opcion2 == "26":
								cmd = os.system("pacman -S polenum")
							elif opcion2 == "27":
								cmd = os.system("pacman -S rainbowcrack")
							elif opcion2 == "28":
								cmd = os.system("pacman -S rcracki-mt")
							elif opcion2 == "29":
								cmd = os.system("pacman -S rsmangler")
							elif opcion2 == "30":
								cmd = os.system("pacman -S sqldict")
							elif opcion2 == "31":
								cmd = os.system("pacman -S statsprocessor")
							elif opcion2 == "32":
								cmd = os.system("pacman -S thc-pptp-bruter")
							elif opcion2 == "33":
								cmd = os.system("pacman -S truecrack")
							elif opcion2 == "34":
								cmd = os.system("pacman -S webscarab")
							elif opcion2 == "35":
								cmd = os.system("pacman -S wordbrutepress")
							elif opcion2 == "36":
								cmd = os.system("pacman -S zaproxy")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash hashcat hashid hydra hexorbase john johnny keimpx maltego maskprocessor cryptohazemultiforcer ncrack oclhashcat pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordbrutepress zaproxy")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "12" :
							print ('''
\033[91m=+[ Reverse Engineering\033[1;m

 1) apktool
 2) dex2jar
 3) disitool
 4) edb-debugger
 5) jad	
 6) javasnoop
 7) radare2
 8) OllyDbg
 9) smali
10) Valgrind
11) YARA

0) Install all Reverse Engineering tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S android-apktool")

							elif opcion2 == "2":
								cmd = os.system("pacman -S dex2jar")

							elif opcion2 == "3":
								cmd = os.system("pacman -S disitool")
							elif opcion2 == "4":
								cmd = os.system("pacman -S edb-debugger")
							elif opcion2 == "5":
								cmd = os.system("pacman -S jad")
							elif opcion2 == "6":
								cmd = os.system("pacman -S javasnoop")
							elif opcion2 == "7":
								cmd = os.system("pacman -S radare2")
							elif opcion2 == "8":
								cmd = os.system("pacman -S OllyDbg")
							elif opcion2 == "9":
								cmd = os.system("pacman -S smali")
							elif opcion2 == "10":
								cmd = os.system("pacman -S Valgrind")
							elif opcion2 == "11":
								cmd = os.system("pacman -S YARA")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S android-apktool dex2jar disitool edb-debugger jad javasnoop radare2 OllyDbg smali Valgrind YARA")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "13" :
							print ('''
\033[91m=+[ Hardware Hacking\033[1;m

 1) android-sdk
 2) apktool
 3) Arduino
 4) dex2jar
 5) Sakis3G	
 6) smali

0) Install all Hardware Hacking tools
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("pacman -S android-sdk")

							elif opcion2 == "2":
								cmd = os.system("pacman -S android-apktool")

							elif opcion2 == "3":
								cmd = os.system("pacman -S arduino")
							elif opcion2 == "4":
								cmd = os.system("pacman -S dex2jar")
							elif opcion2 == "5":
								cmd = os.system("pacman -S sakis3g")
							elif opcion2 == "6":
								cmd = os.system("pacman -S smali")

							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("pacman -S android-sdk android-apktool arduino dex2jar sakis3g smali")
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
						while opcion1 == "14" :
							print ('''
\033[91m=+[ Extra\033[1;m

1) Wifresti
2) Squid3
				''')
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							if sys.version_info[0] < 3:
								opcion2 = raw_input("\033[91mbt > \033[1;m")
							else:
								opcion2 = input("\033[91mbt > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
								print (" ")
							elif opcion2 == "2":
								cmd = os.system("pacman -S squid3")
								print (" ")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()

				inicio()
		inicio1()
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
	if not os.geteuid() == 0:
		sys.exit("\n\033[91mOnly root can run this script\033[1;m\n")
	main()
