import requests

def get_traffic_data(api_key, location):
    url = f'https://maps.googleapis.com/maps/api/traffic/condition?location={location}&key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Example usage
api_key = "YOUR_GOOGLE_MAPS_API_KEY"
location = "latitude,longitude"  # Replace with user's location coordinates
traffic_data = get_traffic_data(api_key, location)

if traffic_data:
    print("Traffic Data:", traffic_data)
else:
    print("Failed to fetch traffic data.")
