from bs4 import BeautifulSoup

"""usage: test.py  <directory> """
""" this class will take one parameter:
1- directory
it will list all the files and go thru them and create 2 files:
I- an yaml per file with:
a- filename
b- directory
c- list of images 
II- an content file: simple html file ( with courier font ) """

# Fetch the html file
#response = urllib.request.urlopen('http://jlk0013.ihostfull.com/latest_7750_HTML/Howto_7750_SR.html?MacandIPv4Multicastaddressmappin.html')
path = 'C:\\Users\jkriker\Google Drive\FTUwebsite\O0O000OOO00O\latest_General_HTML'
filename = '3CreateanlocalISOrepository.html'
response = open(path+'\\'+filename, 'r')
# Parse the html file
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')
#print( soup)

""" create and yaml file from filename , the file name is provided! """
print ('\n'+"will print the name of the yaml file")
yfilename = filename.strip('.hmtl')+'.yaml'
print ('\t'+"filename = " + yfilename)


"""" list all the directory to get ot this file """
print('\n'+ "This is the list of directory where this page : ")
for listtag in soup.find_all("div"):
    if listtag.get('id') == "topic_breadcrumb":
        #print the "<a>" tag underthe "<div>" tag
        id = 0
        for atag in listtag.find_all("a"):#
            id = id + 1
            output = {id:atag.text}
            print ('\t\t'+'' + str(id),' = ',output[id])


""" list all the images attach to this file """
print('\n'+ "This is the list of images in this page : ")
for listtag in soup.find_all("div"):
    if listtag.get('id') == "topic_content":
        print ('\t'+ "The Topic Content is :",listtag.get('id'))
        id = 0
        for image in listtag.find_all('img'):
            id = id + 1
            output = {id:image.get('src')}
            print ('\t\t'+'' + str(id),' = ',output[id])
            #print alternate text
            #print (image(['alt']))


if __name__ == "__main__":
   main(sys.argv[1:])