import requests , time ,os

import save

try:

	os.system("color a")

except:

	pass



o = input("link - ")

rest = requests.get(o)

result = rest.text

sData = []

Data = []

result = result.split("\n")

print('''

< RESULTS >

''')

time.sleep(3)

for line in result:

	

	if "href=" in line and "https:"  not in line:

		print(line) 

		time.sleep(.2)

		link = line.split('href=')

		link2 = link[1]

		DATA = link2.split()

		m_link = DATA[0]

		if ">" in m_link:

			m_link = m_link.split(">")

			m_link = m_link[0]

		sData.append(m_link)

	

	elif "href=" in line and "https:" in line:

		print(line) 

		time.sleep(.2)

		link = line.split('href=')

		link2 = link[1]

		DATA = link2.split()

		m_link = DATA[0]

		if ">" in m_link:

			m_link = m_link.split(">")

			m_link = m_link[0]

		Data.append(m_link)

time.sleep(3)

print('''



< PROCESS COMPLETED >



''')

time.sleep(2)

length = len(Data + sData)

print('''

          <LINKS>

          ''')

for  link in Data:
 index = Data.index(link)

 print(index,link + "\n")

 time.sleep(.3)



print('''

IN SITE LINKS

''')

o = o.replace('https://','')

o = o.replace('http://','')



domain = o.split("/",maxsplit=1)

domain = domain[0].replace("'",'')

domain = domain.replace('"','')



for link in sData:
	#g
    if '/' not in link[1] :
   # 	g
        link = '/'+link
        k= "https://"+domain+ link + "\n"
        k = k.replace('"','')
        k = k.replace("'",'')
        print(k)
        time.sleep(.3)



print(f'''

<TOTAL LINK FOUND - {length}>

''')



		
