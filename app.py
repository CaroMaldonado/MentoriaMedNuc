import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py
import numpy as np 
import pydicom as dicom
import os
import cv2
import SimpleITK as sitk

# Definimos el path en donde están las imágenes
BASE='C:/Users/joaco/Desktop/Mentoría/Imágenes Pedro'
path_1hr = (BASE + '/1h')
path_15hr = (BASE +'/15h')
path_40hr = (BASE +'/40h')
path_64hr = (BASE +'/64h')
# Enlistamos y ordenamos los archivos dicom de cada carpeta
imgs_1hr = os.listdir(path_1hr)
imgs_15hr = os.listdir(path_15hr)
imgs_40hr = os.listdir(path_40hr)
imgs_64hr = os.listdir(path_64hr)
imgs_1hr.sort()
imgs_15hr.sort()
imgs_40hr.sort()
imgs_64hr.sort()
# Cargamos las imágenes de cada tiempo (sólo se usan las post_sc.dcm, que nos parecieron las mejores):
img1_dcm =  dicom.read_file(path_1hr + '/' + imgs_1hr[2])
img1 = img1_dcm.pixel_array
img2_dcm =  dicom.read_file(path_15hr + '/' + imgs_15hr[2])
img2 = img2_dcm.pixel_array
img3_dcm =  dicom.read_file(path_40hr + '/' + imgs_40hr[2])
img3 = img3_dcm.pixel_array
img4_dcm =  dicom.read_file(path_64hr + '/' + imgs_64hr[2])
img4 = img4_dcm.pixel_array

# Graficamos las imágenes seteando el mismo rango de valores en la escala de grises para las tres imágenes
plt.figure(figsize=(16,10))
plt.subplot(141)
plt.imshow(img1, cmap=plt.cm.gray, vmin=0,vmax=553)
plt.title('1 hora')
plt.axis('off')
plt.subplot(142)
plt.imshow(img2, cmap=plt.cm.gray, vmin=0,vmax=553)
plt.title('15 horas')
plt.axis('off')
plt.subplot(143)
plt.imshow(img3, cmap=plt.cm.gray, vmin=0,vmax=553)
plt.title('40 horas')
plt.axis('off')
plt.subplot(144)
plt.imshow(img4, cmap=plt.cm.gray, vmin=0,vmax=553)
plt.title('60 horas')
plt.axis('off')
plt.show()



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')

trace1= go.Scatter(x=[0,0.5,1,2,2.2],y=[1.23,2.5,0.42,3,1])
layout= go.Layout(images= [dict(
                  source= "https://images.plot.ly/language-icons/api-home/python-logo.png",
                  xref= "x",
                  yref= "y",
                  x= 0,
                  y= 3,
                  sizex= 2,
                  sizey= 2,
                  sizing= "stretch",
                  opacity= 0.5,
                  layer= "below")])

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={data=[trace1],layout=layout
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)