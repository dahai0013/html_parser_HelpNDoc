from bs4 import BeautifulSoup
import yaml
import sys, getopt
from bs4 import Comment

"""usage: html_parser_HelNDoc.py  <directory> """
""" this class will take one parameter:  the directory

It will list all the files and go thru them and create 2 files:

I- an yaml per file with:
    a- filename
    b- list of directories / structure
    c- list of images 
    d- 
II- an content file: simple html file ( with courier font ) """

path = 'C:\\Users\jkriker\Google Drive\FTUwebsite\O0O000OOO00O\migrate framed to unframed'

def getfile(filename):
    # Fetch the html file
    #response = urllib.request.urlopen('http://jlk0013.ihostfull.com/latest_7750_HTML/Howto_7750_SR.html?MacandIPv4Multicastaddressmappin.html')
    # must run where the file is
    path = 'C:\\Users\jkriker\Google Drive\FTUwebsite\O0O000OOO00O\migrate framed to unframed'
    #filename = 'Enablestats_Original.html'
    response = open(path+'\\'+filename, 'r')
    # Parse the html file
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    #print( soup)
    return(soup)

def listdir(soup):
    """" list all the directory to get ot this file """
    #print('\n'+ "This is the list of directory where this page : ")
    dtoyamltier = {}
    for listtag in soup.find_all("div"):
        if listtag.get('id') == "topic_breadcrumb":
            #print the "<a>" tag underthe "<div>" tag
            id = 0
            for atag in listtag.find_all("a"):#
                id = id + 1
                output = {id:atag.text}
                dtoyamltier ["tier"+str(id)]= output[id]
                #print ('\t\t'+'' + 'Tier'+str(id),' = ','"'+output[id]+'"')
    #print (dtoyamltier)
    return(dtoyamltier)

def listimag (soup):
    """ list all the images attach to this file """
    #print('\n'+ "This is the list of images in this page : ")
    dtoyamlimag = {}
    for listtag in soup.find_all("div"):
        if listtag.get('id') == "topic_content":
            #print ('\t'+ "The Topic Content is :",listtag.get('id'))
            id = 0
            for image in listtag.find_all('img'):
                id = id + 1
                output = {id:image.get('src')}
                dtoyamlimag["imag" + str(id)] = output[id]
                #print ('\t\t'+'' + str(id),' = ',output[id])
                #print alternate text
                #print (image(['alt']))
    #print (dtoyamlimag)
    return (dtoyamlimag)

def createyaml(dtoyamltier,dtoyamlimag,filename):
    """"Create an new .yaml file or over write the old one and """
    """ also extract the file name from html file """
    #print ('\n'+"will print the name of the yaml file")
    yfilename = filename.strip('hmtl')+'yaml'
    #print ('\t'+"filename = " + yfilename)

    dfile = {'filename':filename}
    dTier = {'Tier':dtoyamltier }
    dImag = {'Image': dtoyamlimag}
    with open(yfilename, 'w') as yaml_file:
        yaml_file.write('---\n')
        yaml_file.write('# Original filename \n')
        yaml.dump(dfile, yaml_file, default_flow_style=False)
        yaml_file.write('# Directory structure in this html file\n')
        yaml.dump(dTier, yaml_file, default_flow_style=False)
        yaml_file.write('# Image in this html file\n')
        yaml.dump(dImag, yaml_file, default_flow_style=False)
    yaml_file.close()
    return (yfilename)

"""Strip many tag from the html file"""
def cleanMe(filename):
    #soup = BeautifulSoup(html)
    response = open(path+'\\'+filename, 'r')
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    [x.extract() for x in soup.find_all('script')]
    [x.extract() for x in soup.find_all('style')]
    [x.extract() for x in soup.find_all('meta')]
    [x.extract() for x in soup.find_all(id="topic_header")]
    [x.extract() for x in soup.find_all(id="topic_footer")]
    [x.extract() for x in soup.find_all(id='Otitle')]
    [x.extract() for x in soup.find_all(attrs={'class': 'rvts9'})]
    [x.extract() for x in soup.find_all(attrs={'class': 'rvts10'})]
    [x.extract() for x in soup.find_all(attrs={'rel': 'stylesheet'})]
    # Very good for testing
    #for x in soup.find_all(attrs={'rel': 'stylesheet'}) :
    #    print (x)
    #
    #[x.extract() for x in soup.find_all('noscript')]
    #[x.extract() for x in soup.find_all(text=lambda text:isinstance(text, Comment))]
    #
    # last is to replace the image file with another name header.jpg2 ?
    #

    cleaned_html = path+'\\'+filename + ".cleaned.html"
    with open(cleaned_html, 'w') as cleaned_file:
        #remove the lost information with the same: &nbsp
        nonBreakSpace = u'\xa0'
        cleaned_file.write(str(soup).replace(nonBreakSpace, r'&nbsp'))
    cleaned_file.close()
    return (cleaned_html)


def main(argv):
    print("argv:"+argv[0])
    filename = argv[0]
    soup = getfile(filename)
    dtoyamltier = listdir(soup)
    dtoyamlimag = listimag(soup)
    yfilename = createyaml(dtoyamltier,dtoyamlimag,filename)
    print ("The end. yaml filename is:"+yfilename)
    cleaned_html = cleanMe(filename)
    print ("filename:"+cleaned_html)


if __name__ == "__main__":
    # 1: will strip the first argument, the script.py itself
    main(sys.argv[1:])