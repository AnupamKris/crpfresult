from django.shortcuts import render
import pandas as pd
# Create your views here.

def showresult(request):
    x = ''
    if request.method == 'POST':
        try:
            data = request.POST
            dl = list(data.values())
            context = {'uid': dl[1], 'dob':dl[2]}
            temp = dl[2].split('-')[::-1]
            dob = ''
            for i in temp:
            	dob+=i+'-'
            dob = dob[:-1]
            context['dob'] = dob.replace('-','/')
            df = pd.read_excel('/home/resultkvhvf/schoolresult/resultdata.xlsx')
            df.columns = ['sno','uid','name','nan','class','section','dob','x','res',]
            x = df.loc[(df['uid']==int(context['uid'])) & (df['dob']==context['dob'])]
            x = x.values[0]
            if x[8] != 'PASS':
                otc = '#fc0000'
                if len(x[8]) > 25:
                    ots = '17px'
                else:
                    ots = '20px'
            else:
                otc = '#00fc00'
                ots = '30px'
            cont = {'name' : x[2],'class': x[4],'sec'  : x[5],'res'  : x[8], 'outcolor': otc, 'outsize': ots}
            return render(request,'result.html',cont)
        except:
            try:
                x = str([context['dob'],cont['dob']])
            except:
                x = 'Invalid Details\n Please Re-Enter Details and Click "Submit"'
                return render(request,'index.html',{'x':x})
    else:
    	return render(request,'index.html',{'x':x})

