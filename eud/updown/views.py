from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from tablib import Dataset
import requests
import csv

# Create your views here.


def upload_file(request):
    if request.method == 'POST':
        new_file = request.FILES['myfile']
        if not new_file.name.endswith('xlsx'):
            messages.info(request, 'Sorry, wrong file format! Please upload only xlsx files.')
            return render(request, 'upload.html')
        else:
            dataset = Dataset()
            imported_data = dataset.load(new_file.read(), format='xlsx')
            r = HttpResponse(content_type='text/csv')
            r['Content-Disposition'] = 'attachment; filename="download_address_file.csv"'
            for data in imported_data:
                url = 'https://maps.googleapis.com/maps/api/geocode/json'
                parameters = {'address': data[0].split('\n')[0],
                              'key': 'api_key'}  # google API is paid, hence no API key
                response = requests.get(url, params=parameters)
                if response.ok:
                    lat= response.json()['results'][0]['geometry']['location']['lat']
                    long = response.json()['results'][0]['geometry']['location']['lng']
                    writer = csv.writer(r)
                    row_list = []
                    for i in data:
                        row_list.append(i)
                    row_list.append(lat)
                    row_list.append(long)
                    writer.writerow(row_list)
                else:
                    print("Failed to connect to API, please check!.")
                    print(response)
            return r
    return render(request, 'upload.html')





