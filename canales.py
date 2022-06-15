import wget
import os
import shutil
import webbrowser
import requests

def reqweb(url):
	try:
		r = requests.get(url, timeout=2)
		if r.status_code == 401:
			return True
	except:
		return False

def Wordlist():
	words = []
	with open("C:/Users/JesusV/Documents/python/mx.m3u") as file:
		for lines in file:
			words.extend(lines.split())
		return words

def Zip_():
	if os.path.isfile("C:/Users/JesusV/Desktop/LATINOMX/LATINOMX.zip"):
		os.remove("C:/Users/JesusV/Desktop/LATINOMX/LATINOMX.zip")
		return Zip_()
	else:
		print("CREANDO ZIP...")
		file_zip = shutil.make_archive("C:/Users/JesusV/Desktop/LATINOMX","zip","C:/Users/JesusV/Desktop/LATINOMX")
		print("ZIP CREADO.")


def main():
	a=0
	urlchannel = []
	namechannel = []
	temp = []
	urls =['http://192.168.1.61/','http://192.168.1.62/','http://192.168.1.63/','http://192.168.1.64/','http://192.168.1.65/','http://192.168.1.66/','http://192.168.1.67/','http://192.168.1.68/','http://192.168.1.69/']

	if os.path.isfile("C:/Users/JesusV/Documents/python/mx.m3u"):
		print("\t\t" + "***************************************************")
		print("\t\t" + "*" + "\t" + "\t" + "COFIGURATION MAKER" + "\t\t  " + "*")
		print("\t\t" + "***************************************************")
		print ("ARCHIVO ENCONTRADO\nBORRANDO...")
		os.remove("C:/Users/JesusV/Documents/python/mx.m3u")
		return main()
	else:
		print("\n"+"DESCARGANDO...")
		url = "http://regioplay.xyz/s21/mx.m3u"
		wget.download(url,'c:/Users/JesusV/Documents/python')
		print("\n" + "DESCARGA COMPLETA.\n")
		print("CREANDO CONFIGURACION...")
		w = Wordlist()
		form = open("C:/Users/JesusV/Desktop/LATINOMX/components/Config.brs","w")
		total=len(w)

		for url in w:
			if "SR_REGIO" in url and "tp.php" in url:
				urlchannel.append(url)

		for z in range(0,total):
			if "NACIONALES" in w[z]:
				y=z
				break
				
		for i in range(y,total):
			if "-1" in w[i]:
				for j in range(1,4):
					if "http" in w[i+j]:
						break
					else:
						temp.append(w[i+j])
				temp.append('*')

		namelong = ' '.join(temp)
		namechannel = namelong.split(sep='*')

		namechannel.pop()

		form.write("Function loadConfig() as Object\narr=[\n")
		form.close()
		form1 = open("C:/Users/JesusV/Desktop/LATINOMX/components/Config.brs","a")

		for h in range(len(urlchannel)):
			form1.write("\n{\n\tTitle:\"" + namechannel[h] + "\"\n\tstreamFormat: \"hls\"" + "\n\tLogo: \" \"" + "\n\tStream: \"" + urlchannel[h] + "\"\n}")

		form1.write("\n]\nreturn arr\nend Function")
		form1.close()
		print("CONFIGURACION CREADA.\n")
		Zip_()
		print("\nUSUARIO: rokudev")
		print("PASSWORD: abcde\n")
		
		for url in urls:
			print("PROBANDO " + url + "...")
			z = reqweb(url)
			if z == True:
				webbrowser.open(url)
				break

		input("\n" + "PRESIONA ENTER PARA CONTINUAR...")
main()