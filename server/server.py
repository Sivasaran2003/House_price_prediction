from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/getLocations')

def getLocations() :
    response = jsonify({
        'locations':util.getLocations()
    })

    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predictHomePrice',method=['POST'])

def predictHomePrice() :
    total_sqft = float(request.form['total_sqft'])
    location = float(request.form['location'])
    bhk = float(request.form['bhk'])
    bath = float(request.form['bath'])

    response = jsonify({
        'estimated_price' : util.getEstimatedPrice(location,total_sqft,bhk,bath) })
    
    response.headers.add('Access-Control-Allow-Origin','*')

    return response


if __name__ == "__main__" :
    print("Starting python Flask server...")
    app.run()