#### API FLASK RETOURNE LE SCORE CLIENT
import flask 
import pandas as pd
from joblib import load#,dump 
import numpy as np
#from dash import Dash, dcc, html, Input, Output
#import io
#from flask import request
#import json
#from plotly.subplots import make_subplots

app = flask.Flask(__name__, template_folder='templates')

model = load('model/model_lgb_clf_light.sav')
df1 = pd.read_csv('dfXL_for_prod.csv')
df2 = df1.drop(['TARGET','SK_ID_CURR','PRED','PREDproba','cluster'],axis=1, inplace=False)
#TARGET 	SK_ID_CURR 	PRED 	PREDproba 	cluster
print('df2_columns',df2.columns)

 
print(df2.shape)
#↨print(np.round(model.predict_proba(df2.loc[df2.index==3].values)[0][0],decimals=2))

@app.route('/predict', methods=['GET', 'POST'])
def main():

    if flask.request.method == 'POST':
        SK_ID_CURR = int(flask.request.form['SK_ID_CURR'])
        print(SK_ID_CURR)
        predictions = np.round(model.predict_proba(df2.loc[df1['SK_ID_CURR']==SK_ID_CURR].values)[0][0],decimals=2)
         
        print(predictions)
 
        idc=SK_ID_CURR
        print('idc=',idc)
        # Add trace with large marker

        #return flask.render_template('clientidscorefordev.html', original_input={'ID_Client': ID_Client}, result=predictions)
        return flask.jsonify({'id':SK_ID_CURR,'prediction':predictions,'df2':df2.shape})

if __name__ == '__main__':
    app.run(debug=True)
    
