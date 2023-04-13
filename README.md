### Aura SDK LED Control Python

This is a Python script that uses the requests library to communicate with an Aura SDK running on the local machine.

The script first initializes the SDK by sending a POST request to the http://127.0.0.1:27339/AuraSDK endpoint with a JSON payload that
includes a category key with the value "SDK". 
If the initialization is successful (HTTP status code 200), the script then sends a PUT request to the http://127.0.0.1:27339/AuraSDK/AuraDevice endpoint with a JSON payload that specifies a
device (Motherboard_LED_Strip), a range (all), and a color (5000). 

The apply key is set to "true", indicating that the change should be applied. 
If the LED color change is successful (HTTP status code 200), 
the script outputs a message to the console. If not, it outputs an error message and exits.
