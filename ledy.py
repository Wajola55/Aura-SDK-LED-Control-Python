import requests

# Initialize SDK
initialize_url = "http://127.0.0.1:27339/AuraSDK"
initialize_payload = {"category": "SDK"}
initialize_response = requests.post(initialize_url, json=initialize_payload)

# Check if SDK was initialized successfully
if initialize_response.status_code == 200:
    print("SDK initialized successfully")
else:
    print("Failed to initialize SDK")
    exit()

# Send PUT request to change LED color
led_url = "http://127.0.0.1:27339/AuraSDK/AuraDevice"
led_payload = {
    "data": [
        {
            "device": "Motherboard_LED_Strip",
            "range": "all",
            "color": "5000",
            "apply": "true"
        }
    ]
}

led_response = requests.put(led_url, json=led_payload)

# Check if LED color was changed successfully
if led_response.status_code == 200:
    print("LED color changed successfully")
else:
    print("Failed to change LED color")


