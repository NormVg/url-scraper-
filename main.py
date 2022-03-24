import requests , time


o = input("link - ")
rest = requests.get(o)
result = rest.text
Data = []
result = result.split("\n")
print('''
< RESULTS >
''')
time.sleep(3)
for line in result:
	if "href=" in line and "https:" in line:
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
length = len(Data)
for link in Data:
	print(link + "\n")
	time.sleep(.3)
print(f'''
<TOTAL LINK FOUND - {length}>
''')

		