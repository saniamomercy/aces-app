import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

import pickle

# load model
model = pickle.load(open('model.pkl','rb'))

# app
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


# routes
@app.route("/api/v1/http://localhost:3000/", methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
