import requests

api_url = 'http://34.141.243.146:8080/api/v1/static'

def send_text_to_speech_request(text):
    # Parameters to send to the API
    data = {
        'text': text,
        'voice': "m-us-1"
    }
    
    # Send POST request to the API
    response = requests.post(api_url, data=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Save the audio response
        with open('output.wav', 'wb') as f:
            f.write(response.content)
        print("Audio file has been saved as 'output.wav'")
    else:
        # Print the error response
        print("Error:", response.json()['error'])

# URL of the API


# Example usage of the function
send_text_to_speech_request('Hello, this is a test.')
