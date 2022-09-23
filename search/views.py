from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.

def home(request):
    '''
    This is the function that defines the homepage
    '''
    return render(request, 'index.html')

def search(request):
    '''
    This method is where the user will be redirected once he/she
    feeds in the data he/she is looking up in the homepage
    It will in turn return the data the user is requesting
    '''
    if request.method == 'POST':
        search = request.POST['search']
        url = 'https://www.ask.com/web?q=' +search
        response = requests.get(url)
        soup = bs(response.text, 'lxml')

        result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item'})
        final_result = []

        for results in result_listings:
            result_title = results.find(class_ = 'PartialSearchResults-item-title').text
            result_url = results.find('a').get('href')
            result_description = results.find(class_ = 'PartialSearchResults-item-abstract').text
            final_result.append((result_title, result_url,  result_description))

            context = {
                'final_result': final_result
            }
        return render(request, 'search.html', context)
            
    return render(request, 'search.html')