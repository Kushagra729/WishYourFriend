from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Route to save the location data
@app.route('/save-location', methods=['POST'])
def save_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    # Save the data to a file
    with open('locations.txt', 'a') as f:
        f.write(f"Latitude: {latitude}, Longitude: {longitude}\n")
    
    return jsonify({'message': 'Location saved successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
