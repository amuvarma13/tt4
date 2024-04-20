import requests
import time

api_url = 'http://34.141.243.146:8080/api/v1/static'
ping_url = 'http://34.141.243.146:8080/ping'

def send_text_to_speech_request(text):
    # Parameters to send to the API
    data = {
        'text': text,
        'voice': "m-us-1"
    }
    
    # Send POST request to the API
    startTime = time.time()
    response = requests.post(api_url, data=data)
    endTime = time.time()

    # Measure ping
    ping_start = time.time()
    response_ping = requests.post(api_url, data=data)
    ping_end = time.time()
    ping_dur = ping_end - ping_start
    print(f"Time taken: {endTime - startTime - ping_dur} seconds")


    
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
