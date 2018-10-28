from jinja2 import Environment, FileSystemLoader

""" this class will write a yaml file
it will take:
1- name of the file
2- path of the file??
3- dictionary ( with values to be replace in the template """

mydict = { 'filename1':"myfilename1", 'name1' : "myname1",'location1' : "mylocation1", 'dir1' : "mydir1",'dir2' : "mydir2" }

#This line uses the current directory
file_loader = FileSystemLoader('.')

env = Environment(loader=file_loader)
template = env.get_template('template.j2')
output = template.render(mydict)

#write to an yaml file
try:
    f = open ('myfile.yaml','w+')
    f.write(output)
except IOError:
    print ( "Error: can\'t find file data" )
else:
    print ( "Written content in the file successfully" )
f.close()




