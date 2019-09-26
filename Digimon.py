from flask import Flask, render_template, jsonify, request, redirect
import requests,json,pickle
import numpy as np
import pandas as pd

app=Flask(__name__)

df = pd.read_json('digimon.json')
df['target'] = df.apply(
    lambda row : row['Stage'] + '|' + row['Type'] + '|' + row['Attribute'],axis=1
)

@app.route('/')
def home():
    return render_template('home.html')

def loadModel():
    global model
    with open('modelDG.pkl','rb') as mymodel:
        model = pickle.load(mymodel)

@app.route('/digimon',methods = ['POST'])
def digimon():
    request.method == 'POST'
    body = request.form
    digi = body["digi"].capitalize()
    if digi not in list(df['Nama']):
        return render_template('error.html')
    else:
    # fav = digimon
        indexFav = df[df['Nama']==digi].index.values[0]
        digimon = list(enumerate(model[indexFav]))
        sortDigi = sorted(digimon, key=lambda i : i[1], reverse=True)
        recommend = []
        for i in sortDigi[:6]:
            lists=[]
            lists.append(df.iloc[i[0]])
            recommend.append(lists)
        stage = df[df['Nama']==digi]['Stage'].to_numpy()[0]
        url = df[df['Nama'] == digi]['Gambar'].to_numpy()[0]
        types = df[df['Nama'] == digi]['Type'].to_numpy()[0]
        attribute = df[df['Nama']==digi]['Attribute'].to_numpy()[0]

        return render_template('hasil.html', insert1='{}'.format(body['digi'].capitalize()),insert2='{}'.format(stage), insert3='{}'.format(url),insert4='{}'.format(types), insert5='{}'.format(attribute), recom1='{}'.format(recommend[0][0]['Nama']),recom2='{}'.format(recommend[0][0]['Gambar']),recom3='{}'.format(recommend[0][0]['Stage']),recom4='{}'.format(recommend[0][0]['Type']),recom5='{}'.format(recommend[0][0]['Attribute']),recom6='{}'.format(recommend[1][0]['Nama']),recom7='{}'.format(recommend[1][0]['Gambar']),recom8='{}'.format(recommend[1][0]['Stage']),recom9='{}'.format(recommend[1][0]['Type']),recom10='{}'.format(recommend[1][0]['Attribute']),recom11='{}'.format(recommend[2][0]['Nama']),recom12='{}'.format(recommend[2][0]['Gambar']),recom13='{}'.format(recommend[2][0]['Stage']),recom14='{}'.format(recommend[2][0]['Type']),recom15='{}'.format(recommend[2][0]['Attribute']),recom16='{}'.format(recommend[3][0]['Nama']),recom17='{}'.format(recommend[3][0]['Gambar']),recom18='{}'.format(recommend[3][0]['Stage']),recom19='{}'.format(recommend[3][0]['Type']),recom20='{}'.format(recommend[3][0]['Attribute']),recom21='{}'.format(recommend[4][0]['Nama']),recom22='{}'.format(recommend[4][0]['Gambar']),recom23='{}'.format(recommend[4][0]['Stage']),recom24='{}'.format(recommend[4][0]['Type']),recom25='{}'.format(recommend[4][0]['Attribute']),recom26='{}'.format(recommend[5][0]['Nama']),recom27='{}'.format(recommend[5][0]['Gambar']),recom28='{}'.format(recommend[5][0]['Stage']),recom29='{}'.format(recommend[5][0]['Type']),recom30='{}'.format(recommend[5][0]['Attribute']))

if (__name__) == '__main__':
    loadModel()
    app.run(
        debug=True,
        host='localhost',
        port=5000
        )