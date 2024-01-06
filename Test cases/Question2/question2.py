import requests

#Question 2. In addition to asserting the latitude and longitude, please develop 3 more test cases you can test using the open weather map API using Postman


def test_openweathermap_api():
    # API endpoint URL
    url = "https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    # Parse the response JSON
    json_data = response.json()

    # Test Case 1: Verify Latitude and Longitude
    assert json_data['coord']['lat'] == 51.51, f"Latitude is not as expected. Actual: {json_data['coord']['lat']}"
    assert json_data['coord']['lon'] == -0.13, f"Longitude is not as expected. Actual: {json_data['coord']['lon']}"
    print("Test Case 1: Verify Latitude and Longitude passed successfully.")

    # Test Case 2: Verify Temperature Unit is Kelvin
    assert json_data['main']['temp'] >= 0 and json_data['main']['temp'] <= 373.15, "Temperature unit is not in Celsius."
    print("Test Case 2: Verify Temperature Unit is Kelvin passed successfully.")

    # Test Case 3: Verify City Name
    assert json_data['name'] == "London", f"City name is not as expected. Actual: {json_data['name']}"
    print("Test Case 3: Verify City Name passed successfully.")

    # Test Case 4: Verify Humidity is within Range
    assert json_data['main']['humidity'] >= 0 and json_data['main']['humidity'] <= 100, "Humidity is not within the acceptable range."
    print("Test Case 4: Verify Humidity is within Range passed successfully.")


# Run the test case
test_openweathermap_api()

