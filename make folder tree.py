import shutil,os,re
print('SOURCE')
source=input()
os.chdir(source)
folder=[]
file=[]
def maketree(s):
        global file,folder
        sourcedir=os.listdir()
        for i in sourcedir:
                try:
                        os.chdir(s+'\\'+i)
                        folder=folder+[s+'\\'+i]
                        maketree(s+'\\'+i)
                except:
                        file=file+[s+'\\'+i]
maketree(source)
