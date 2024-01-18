import json
import pickle
import numpy  # Make sure to import numpy

locations = None
data_columns = None
model = None

def getEstimatedPrice(location, sqft, bhk, bath):
    try:
        loc_index = data_columns.index(location.lower())
    except ValueError:
        loc_index = -1
    global model
    x = numpy.zeros(len(data_columns))
    if loc_index >= 0:
        x[loc_index] = 1
    x[1] = sqft
    x[2] = bhk
    x[3] = bath

    return round(model.predict([x])[0], 2)

def getLocations():
    return locations

def load_saved_artifacts():
    print('loading artifacts...')
    global data_columns
    global locations
    try :
        with open('E:/ml/House_price_prediction/server/artifacts/columns.json', 'r') as f:
            data_columns = json.load(f)['data_columns']
            locations = data_columns[3:]

        global model

        print('locations loaded')
        with open('E:\ml\House_price_prediction\model\house_price_prediction_model.pickle', 'rb') as f:
            model = pickle.load(f)

        print('all the artifacts are loaded...')
    except :
        print('artifacts cant be loaded...')

if __name__ == '__main__':
    load_saved_artifacts()
    estimated_price = getEstimatedPrice('Hebbal', 1, 1, 1)
    print(f"Estimated Price: {estimated_price} lakhs")

    locations_list = getLocations()
    print(locations_list)
