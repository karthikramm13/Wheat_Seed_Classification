import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Area':15.26, 'Perimeter':14.84, 'Compactness':0.871, 'Length of Kernel':5.763, 'Width of Kernel':3.312, 'Asymmetry Coefficient':2.221, 'Length of Kernel groove':5.22})

print(r.json())