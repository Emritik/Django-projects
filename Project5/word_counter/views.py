from django.shortcuts import render

# Create your views here.
def counter(request): 
    if request.method == "POST":
        ''' Firstly store the text from the textarea to text variable!! '''
        text = request.POST.get('textcounter')
        '''Check  the weather a text is empty or not!!'''
        if text != "":
            '''If the text id not empty then executes the remaining code!!'''
            word_len = len(text.split())
            
            i = True
            
            return render(request, 'counter.html',{'word_len' : word_len, 'text' : text , 'i' : i , 'on' : 'active'})
        
        else:
            
            return render(request, 'counter.html', {'on' : 'active'})
        
    else:
        
        return render(request, 'counter.html', {'on' : 'active'})
            
            