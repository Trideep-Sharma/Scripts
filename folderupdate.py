import shutil,os,re
print('SOURCE')
source=input()
os.chdir(source)
print('DESTINATION')
destination=input()
folder=[]
file=[]
files=[]
folders=[]
def makesourcetree(s):
        global files,folders
        sourcedir=os.listdir()
        for i in sourcedir:
                try:
                        os.chdir(s+'\\'+i)
                        folders=folders+[s+'\\'+i]
                        makesourcetree(s+'\\'+i)
                except:
                        files=files+[s+'\\'+i]
def makedestinationtree(s):
        global file,folder
        sourcedir=os.listdir()
        for i in sourcedir:
                try:
                        os.chdir(s+'\\'+i)
                        folder=folder+[s+'\\'+i]
                        makedestinationtree(s+'\\'+i)
                except:
                        file=file+[s+'\\'+i]
makesourcetree(source)
os.chdir(destination)
makedestinationtree(destination)
sfile=[]
sfolder=[]
dfile=[]
dfolder=[]
for k in files:
        sfile=sfile+[re.sub(r'D:\\Trideep\\Books','',k,count=0)]
for k in folders:
        sfolder=sfolder+[re.sub(r'D:\\Trideep\\Books','',k,count=0)]
for k in file:
        dfile=dfile+[re.sub(r'Computer\\Lenovo K50a40\\Internal storage\\Books','',k,count=0)]
for k in folder:
        dfolder=dfolder+[re.sub(r'Computer\\Lenovo K50a40\\Internal storage\\Books','',k,count=0)]
lfolder=[]
lfile=[]
for k in sfolder:
        if k not in dfolder:
                lfolder=lfolder+[k]
for k in sfile:
        if k not in dfile:
                lfile=lfile+[k]
print('Enter')
input()
'''for k in lfolder:
        os.makedirs(destination+k)
for k in lfile:
        shutil.copy(source+k,destination+k)'''
        
