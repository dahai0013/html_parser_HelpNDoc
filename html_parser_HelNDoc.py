from bs4 import BeautifulSoup

# Fetch the html file
#response = urllib.request.urlopen('http://jlk0013.ihostfull.com/latest_7750_HTML/Howto_7750_SR.html?MacandIPv4Multicastaddressmappin.html')
path = 'C:\\Users\jkriker\Google Drive\FTUwebsite\O0O000OOO00O\latest_General_HTML'
filename = '3CreateanlocalISOrepository.html'
response = open(path+'\\'+filename, 'r')
# Parse the html file
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')
#print( soup)

# create and yaml file from filename , the file name is provided!
print ('\n'+"will print the name of the yaml file")
yfilename = filename.strip('.hmtl')+'.yaml'
print ('\t'+yfilename)

#print only the "<div>" tag match "topic_breadcrumb"
print('\n'+ "This is the list of directory where this page : ")
for listtag in soup.find_all("div"):
    if listtag.get('id') == "topic_breadcrumb":
        #print (listtag)
        #print the "<a>" tag underthe "<div>" tag
        for atag in listtag.find_all("a"):
            #print (atag.string , )
            #print (atag.get('href'))
            print('\t'+atag.text)

#images = soup.find_all('img')

print('\n'+ "This is the list of images in this page : ")
for listtag in soup.find_all("div"):
    if listtag.get('id') == "topic_content":
        print ('\t'+ "The Topic Content is :",listtag.get('id'))
        for image in listtag.find_all('img'):
            print ('\t\t'+ image.get('src'))
            #print alternate text
            #print (image(['alt']))