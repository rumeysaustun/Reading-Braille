import torch
import shutil
from time import sleep
import os

def tespitEt(filename):
    
    model = torch.hub.load('yolov5', 'custom', path='yolov5/210DatasetModel-s.pt', source='local') 
    img = 'uploads/' +filename
    a = os.path.isdir("runs/detect/exp")
    if a:
        shutil.rmtree("runs/detect/exp", ignore_errors=False, onerror=None)
    results = model(img)
    results.save()
    sleep(4)