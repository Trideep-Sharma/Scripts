import PyPDF2,os,re,shelve
os.chdir('e:\Trideep\Python')
file=os.listdir()
d={}
try:
    for i in file:
        d[i]=''
    for i in file:
        print(i)
        pdffile=open('E:\Trideep\Python\\'+i,'rb')
        pdfreader=PyPDF2.PdfFileReader(pdffile)
        for j in range(pdfreader.numPages):
            page=pdfreader.getPage(j)
            s=page.extractText()
            d[i]=d[i]+s
except:
    pass
l=shelve.open('e:/trideep/list')
for t in d:
    l[t]=d[t]
l.close()
l=shelve.open('e:/trideep/list')
for k in l:
    if(len(re.findall('python',l[k],re.I))>0):
        print(k)
l.close()
