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
	with open("C:/Users/IsMerk/Desktop/mx.m3u") as file:
		for lines in file:
			words.extend(lines.split())
		return words

def Zip_():
	if os.path.isfile("C:/Users/IsMerk/Desktop/LATINOMX.zip"):
		os.remove("C:/Users/IsMerk/Desktop/LATINOMX.zip")
		return Zip_()
	else:
		print("CREANDO ZIP...")
		file_zip = shutil.make_archive("C:/Users/IsMerk/Desktop/LATINOMX","zip","C:/Users/IsMerk/Desktop/LATINOMX")
		print("ZIP CREADO.")


def main():
	a=0
	urlchannel = []
	namechannel = []
	temp = []
	urls =['http://192.168.1.61/','http://192.168.1.62/','http://192.168.1.63/','http://192.168.1.64/','http://192.168.1.65/','http://192.168.1.66/','http://192.168.1.67/','http://192.168.1.68/','http://192.168.1.69/']

	if os.path.isfile("C:/Users/IsMerk/Desktop/mx.m3u"):
		print("\t\t" + "***************************************************")
		print("\t\t" + "*" + "\t" + "\t" + "COFIGURATION MAKER" + "\t\t  " + "*")
		print("\t\t" + "***************************************************")
		print ("ARCHIVO ENCONTRADO\nBORRANDO...")
		os.remove("C:/Users/IsMerk/Desktop/mx.m3u")
		return main()
	else:
		print("\n"+"DESCARGANDO...")
		url = "http://regioplay.xyz/j21/mx.m3u"
		wget.download(url,"C:/Users/IsMerk/Desktop")
		print("\n" + "DESCARGA COMPLETA.\n")
		print("CREANDO CONFIGURACION...")
		w = Wordlist()
		form = open("C:/Users/IsMerk/Desktop/LATINOMX/components/Config.brs","w")

		for z in range(0,len(w)):
			if "EVENTOS" in w[z]:
				y=z-10
			if "Vix" in w[z]:
				total=z
				break

		for z in range(y+10, total):
			if "logo" in w[z]:
				pass
			elif "http" in w[z]:
				urlchannel.append(w[z])

		for i in range(y,total):
			if "#EXTINF:-1" in w[i]:
				for j in range(3,10):
					if "http" in w[i+j]:
						break
					elif "tvg-id" in w[i+j] or '"' in w[i+j]:
						pass
					else:
						temp.append(w[i+j])
				temp.append('*')

		namelong = ' '.join(temp)
		namechannel = namelong.split(sep='*')

		for m in range(len(namechannel)):
			for n in range(len(namechannel)):
				if namechannel[n] == ' ':
					namechannel.pop(n)
					break
		m,n=0,0
		for m in range(len(urlchannel)):
			for n in range(len(urlchannel)):
				if ".m3u8" in urlchannel[n]:
					pass
				else:
					urlchannel.pop(n)
					namechannel.pop(n)
					break
		
		form.write("Function loadConfig() as Object\narr=[\n")
		form.close()
		form1 = open("C:/Users/IsMerk/Desktop/LATINOMX/components/Config.brs","a")

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