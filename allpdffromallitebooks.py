import requests,bs4,os
for j in range(1,12):
        for i in range(1,31):
                if(i<10)and(j<10):
                        f='2016'+'0'+str(j)+'0'+str(i)
                        a=requests.get('http://google.com/search?q=' + ' '+'filetype:pdf+http:%2F%2Ffile.allitebooks.com%2F'+f+'%2F')
                        b=bs4.BeautifulSoup(a.text)
                        c=b.select('.r a')
                        print(f)
                        os.makedirs('Location to be saved'+f)
                        for k in range(len(c)):             
                                t=c[k].get('href')[44:c[k].get('href').find('.pdf')+4]
                                t=t.replace('%2520',' ')
                                d=open('Location to be saved'+f+'/'+t, 'wb')
                                q=requests.get('http://google.com' + c[k].get('href'))
                                for chunk in q.iter_content(100000):
                                        d.write(chunk)
                                d.close()
                                print('Done')
                elif(i<10)and(j>10):
                        f='2016'+str(j)+'0'+str(i)
                        a=requests.get('http://google.com/search?q=' + ' '+'filetype:pdf+http:%2F%2Ffile.allitebooks.com%2F'+f+'%2F')
                        b=bs4.BeautifulSoup(a.text)
                        c=b.select('.r a')
                        print(f)
                        os.makedirs('Location to be saved'+f)
                        for k in range(len(c)):
                                t=c[k].get('href')[44:c[k].get('href').find('.pdf')+4]
                                t=t.replace('%2520',' ')
                                d=open('Location to be saved'+f+'/'+t, 'wb')
                                q=requests.get('http://google.com' + c[k].get('href'))
                                for chunk in q.iter_content(100000):
                                        d.write(chunk)
                                d.close()
                                print('Done')
                elif(i>10)and(j<10):
                        f='2016'+'0'+str(j)+str(i)
                        a=requests.get('http://google.com/search?q=' + ' '+'filetype:pdf+http:%2F%2Ffile.allitebooks.com%2F'+f+'%2F')
                        b=bs4.BeautifulSoup(a.text)
                        c=b.select('.r a')
                        print(f)
                        os.makedirs('Location to be saved'+f)
                        for k in range(len(c)): 
                                t=c[k].get('href')[44:c[k].get('href').find('.pdf')+4]
                                t=t.replace('%2520',' ')
                                d=open('Location to be saved'+f+'/'+t, 'wb')
                                q=requests.get('http://google.com' + c[k].get('href'))
                                for chunk in q.iter_content(100000):
                                        d.write(chunk)
                                d.close()
                                print('Done')
                elif(i>10)and(j>10):
                        f='2016'+str(j)+str(i)
                        a=requests.get('http://google.com/search?q=' + ' '+'filetype:pdf+http:%2F%2Ffile.allitebooks.com%2F'+f+'%2F')
                        b=bs4.BeautifulSoup(a.text)
                        c=b.select('.r a')
                        print(f)
                        os.makedirs('Location to be saved'+f)
                        for k in range(len(c)):
                                t=c[k].get('href')[44:c[k].get('href').find('.pdf')+4]
                                t=t.replace('%2520',' ')
                                d=open('Location to be saved'+f+'/'+t, 'wb')
                                q=requests.get('http://google.com' + c[k].get('href'))
                                for chunk in q.iter_content(100000):
                                        d.write(chunk)
                                d.close()
                                print('Done')

