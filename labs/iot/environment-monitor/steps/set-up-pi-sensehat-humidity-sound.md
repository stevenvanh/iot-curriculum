# Set up the Raspberry Pi with SenseHAT to send humidity data

In the [previous step](./set-up-humidity-sound.md) you set up IoT Central to receive humidity data.

In this step you will set up the Raspberry Pi to send humidity data.


### Update the code

In this section you will be adding code to the Python file. If you haven't used Python before, be aware it is very specific about how the lines are indented, so make sure the code is indented the same as the code around it. You can find the full code in the [app.py](../code/pi-sensehat/humidity/app.py) file in the [code/pi-sensehat/humidity](../code/pi-sensehat/humidity) folder to check your code against if you get errors.

1. Connect to the Pi using Visual Studio Code, open the `Environment Monitor` folder, and open the `app.py` file.

   Head to the `get_telemetry` function and replace the code of this function with the following:

    ```python
    
    # Gets telemetry from SenseHat
    # Telemetry needs to be sent as JSON data
    async def get_telemetry() -> str:
        # Get temperature, rounded to 0 decimals
        temperature = round(sense.get_temperature())

        # Get humidity, rounded to 0 decimals
        humidity = round(sense.get_humidity())

        # Build a dictionary of data
        # The items in the dictionary need names that match the
        # telemetry values expected by IoT Central
        dict = {
            "Temperature" : temperature,  # The temperature value
            "Humidity" : humidity,        # The humidity value
        }

        # Convert the dictionary to JSON
        return json.dumps(dict)
    ```

    This code makes the following changes:

    * The humidity value is now read, and is added to the telemetry dictionary


1. Save the file

1. Run the code from the VS Code terminal using the following command:

    ```sh
    python3 app.py
    ```

1. The app will start up, connect to Azure IoT Central, then send temperature and humidity values:

    ```output
    pi@jim-iot-pi:~/EnvironmentMonitor $ python3 app.py
    RegistrationStage(RequestAndResponseOperation): Op will transition into polling after interval 2.  Setting timer.
    Connecting
    Connected
    Telemetry: {"Temperature": 27.0, "Humidity": 44.0, "Sound": 304}
    Telemetry: {"Temperature": 26.0, "Humidity": 45.0, "Sound": 326}
    Telemetry: {"Temperature": 26.0, "Humidity": 45.0, "Sound": 400}
    Telemetry: {"Temperature": 26.0, "Humidity": 45.0, "Sound": 361}
    ```

    Try adjusting humidity level by breathing on the sensor, and see the values change both in the output of the Python code, and in IoT Central.


## Next steps

In this step you set up the Raspberry Pi to send humidity data.

In the [next step](./rules.md) you will perform simple analytics and create alerts on the data using IoT Central rules.
