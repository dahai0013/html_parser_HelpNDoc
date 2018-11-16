from bs4 import BeautifulSoup
import yaml
import sys, os

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
    """ Fetch the filename.html file and create a soup
    :param filename:  a file name
    :return: soup from BeautifulSoup 
    """
    #response = urllib.request.urlopen('http://jlk0013.ihostfull.com/latest_7750_HTML/Howto_7750_SR.html?MacandIPv4Multicastaddressmappin.html')
    # must run where the file is
    # path is a global variable now:   path = 'C:\\Users\jkriker\Google Drive\FTUwebsite\O0O000OOO00O\migrate framed to unframed'
    # this is for testing:  filename = 'Enablestats_Original.html'
    response = open(path+'\\'+filename, 'r')
    # Parse the html file
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    #print( soup)
    return(soup)

def listdir(soup):
    """ list all the directory inside this .html file to get to this html page
    :param soup:   soup from beautifulSoup module
    :return: dictionary of the structure where the .html live
    """
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
    """  List all the images attach to this html page
    :param soup:   soup
    :return:   dictionary of the images used in the .html live
    """
    #print('\n'+ "This is the list of images in this page : ")
    dtoyamlimag = {}
    for listtag in soup.find_all("div"):
        if listtag.get('id') == "topic_content":
            #print ('\t'+ "The Topic Content is :",listtag.get('id'))
            id = 0
            for image in listtag.find_all('img'):
                id = id + 1
                output = {id:image.get('src')}
                # and strip the folder name 'lib'
                dtoyamlimag["imag" + str(id)] = output[id].strip('lib/')
                #print ('\t\t'+'' + str(id),' = ',output[id])
                #print alternate text
                #print (image(['alt']))
    #print (dtoyamlimag)
    return (dtoyamlimag)

def createyaml(dtoyamltier,dtoyamlimag,filename):
    """  Create an new .yaml file or over write the old one and
    also extract the file name from html file
    This new yaml file will be pit in the 'yaml' folder
    :param dtoyamltier:    dictionary of folder/structure
    :param dtoyamlimag:   dictionany of images
    :param filename:   filename.html use to create filename.yaml
    :return:
    """
    # create an yaml directory to put all the new .yaml files
    yamlpath = path+r'\yaml'
    #print (yamlpath)
    if not os.path.exists(yamlpath):
        os.makedirs(yamlpath)
    #print ('\n'+"will print the name of the yaml file")
    yfilename = yamlpath+'\\'+filename.strip('hmtl')+'yaml'
    print ('\t'+"filename = " + yfilename)

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


def cleanMe(filename):
    """     Strip many tag from the .html file
    :param filename:   filename.html
    :return:   return a clean .html file
    """
    # create an cleaned directory to put all the new cleaned .html files
    cleanedpath = path+r'\cleaned'
    print (cleanedpath)
    if not os.path.exists(cleanedpath):
        os.makedirs(cleanedpath)

    # the clean up section
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
    # remove the folder lib
    for x in soup.find_all('img'):
        x['src'] = x.get('src').strip('lib/')
    # replace the header image name
    for x in soup.find_all('img') :
        if x['src']=='header1.jpg':
            x['src'] = 'headerFTU.jpg'
    # replace the link to the new website: thefreetelecomuni
    for x in soup.find_all('a'):
        if x['href']=="www.freetelecomuni.co.uk":
            x['href']="www.thefreetelecomuni.uk"
    # Very good for testing
    #for x in soup.find_all('a'):
    #    if x['href']=="www.freetelecomuni.co.uk":
    #        x['href']="www.thefreetelecomuni.uk"
    #        print(x)
    #    x['src'] = x.get('src').strip('lib/')
    #    print(x['src'])
    #    print(x.attrs)


    #
    #[x.extract() for x in soup.find_all('noscript')]
    #[x.extract() for x in soup.find_all(text=lambda text:isinstance(text, Comment))]
    #
    # last is to replace the image file with another name header.jpg2 ?
    #
    # write it to the cleaned folder
    cleaned_html = cleanedpath+'\\'+filename
    with open(cleaned_html, 'w') as cleaned_file:
        #remove the lost information with the same: &nbsp
        nonBreakSpace = u'\xa0'
        cleaned_file.write(str(soup).replace(nonBreakSpace, r'&nbsp'))
    cleaned_file.close()
    return (cleaned_html)


def main(argv):
    #print("argv:"+argv[0])
    filename = argv[0]
    soup = getfile(filename)
    dtoyamltier = listdir(soup)
    dtoyamlimag = listimag(soup)
    yfilename = createyaml(dtoyamltier,dtoyamlimag,filename)
    #print ("The end. yaml filename is:"+yfilename)
    cleaned_html = cleanMe(filename)
    #print ("filename:"+cleaned_html)


if __name__ == "__main__":
    # 1: will strip the first argument, the script.py itself
    main(sys.argv[1:])