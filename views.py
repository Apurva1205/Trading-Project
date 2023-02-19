from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .utils import process_csv, convert_candles
import json

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        timeframe = int(request.POST.get('timeframe'))
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.path(filename)
        candles = process_csv(file_path)
        converted_candles = convert_candles(candles, timeframe)
        converted_data = [candle.__dict__ for candle in converted_candles]
        with open('media/converted_data.json', 'w') as f:
            json.dump(converted_data, f)
        return redirect('download_json')
    return render(request, 'upload_form.html')
.
