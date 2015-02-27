import urllib 
url = 'www.themoneyconverter.com/rss-feed/EUR/rss.xml'
websitepath = 'http://' + url
website = urllib.urlopen(websitepath)
utext = website.readlines()
EuroExchangeconfigfile = open('C:/Users/peter/Documents/GitHub/TravelBudget/config.txt','w')
firstdescrip = False
firstitle = 0
for line in utext:
    if '<lastBuildDate>' in line:
      string = ('LAST UPDATED: ' + line[line.index('<lastBuildDate>') + 15:line.rindex('</lastBuildDate>')] + '\n')
      EuroExchangeconfigfile.write(string)
    # Skip the first two '<title>' headings
    if '<title>' in line:
      if  firstitle < 2:
          firstitle += 1
      else:
        string = ('TITLE: ' + line[line.index('<title>') + 7:line.rindex('</title>')]  + '\n' )
        EuroExchangeconfigfile.write(string)
    #Skip the first <description>
    if '<description>' in line:
      if not firstdescrip:
          firstdescrip = True
      else:
        string = ('DESCRIPTION: ' +line[line.index('<description>') + 13:line.rindex('</description>')]  + '\n')
        EuroExchangeconfigfile.write(string)
    if '<category>' in line:
      string = ('CATEGORY: ' +line[line.index('<category>') + 10:line.rindex('</category>')] + '\n' + '\n' )
      EuroExchangeconfigfile.write(string)
    
    

website.close()
EuroExchangeconfigfile.close()