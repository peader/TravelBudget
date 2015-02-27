import urllib 
url = 'www.themoneyconverter.com/rss-feed/EUR/rss.xml'
websitepath = 'http://' + url
website = urllib.urlopen(websitepath)
utext = website.readlines()
for line in utext:
    print line
#print utext
#websiteholder = open('C:/Users/peter/Documents/600.1xFiles/Messing/Urltext.txt','w')
#l = utext.find('Login')
#websiteholder.write(utext[l:l+6])
#website.close()