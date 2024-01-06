import requests


#Question 1. Create an assertion to verify the latitude is 51.51 and the longitude is -0.13

def test_openweathermap_api():
    # API endpoint URL
    url = "https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    # Parse the response JSON
    json_data = response.json()

    # Expected latitude and longitude values
    expected_latitude = 51.51
    expected_longitude = -0.13

    # Verify latitude
    assert json_data['coord']['lat'] == expected_latitude, f"Latitude is not as expected. Actual: {json_data['coord']['lat']}"
    	

    # Verify longitude
    assert json_data['coord']['lon'] == expected_longitude, f"Longitude is not as expected. Actual: {json_data['coord']['lon']}"

    print("Veriied latitude is 51.51 and the longitude is -0.13 passed successully.")

# Run the test case
test_openweathermap_api()

