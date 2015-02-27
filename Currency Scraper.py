import urllib 
url = 'www.themoneyconverter.com/rss-feed/EUR/rss.xml'
websitepath = 'http://' + url
website = urllib.urlopen(websitepath)
utext = website.readlines()
EuroExchangeconfigfile = open('C:/Users/peter/Documents/GitHub/TravelBudget/config.txt','w')
for line in utext:
    if '<lastBuildDate>' in line:
      string = ('LAST UPDATED: ' + line[line.index('<lastBuildDate>') + 15:line.rindex('</lastBuildDate>')])
      EuroExchangeconfigfile.write(string)
      #print line.index('<lastBuildDate>') + 15
    #print line
#print utext
#websiteholder = open('C:/Users/peter/Documents/600.1xFiles/Messing/Urltext.txt','w')
#l = utext.find('Login')
#websiteholder.write(utext[l:l+6])
website.close()
EuroExchangeconfigfile.close()