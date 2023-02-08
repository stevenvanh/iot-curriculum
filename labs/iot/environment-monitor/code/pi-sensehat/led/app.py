# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import asyncio
import json
import os
import random
from dotenv import load_dotenv
from azure.iot.device.aio import IoTHubDeviceClient, ProvisioningDeviceClient
from azure.iot.device import MethodResponse
from sense_hat import SenseHat 
sense = SenseHat()

# The connection details from IoT Central for the device
load_dotenv()
id_scope = os.getenv("ID_SCOPE")
primary_key = os.getenv("PRIMARY_KEY")
device_id = "pi-environment-monitor"


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

# The main function that runs the program in an async loop
async def main():
    # Connect to IoT Central and request the connection details for the device
    provisioning_device_client = ProvisioningDeviceClient.create_from_symmetric_key(
        provisioning_host="global.azure-devices-provisioning.net",
        registration_id=device_id,
        id_scope=id_scope,
        symmetric_key=primary_key)
    registration_result = await provisioning_device_client.register()

    # Build the connection string - this is used to connect to IoT Central
    conn_str="HostName=" + registration_result.registration_state.assigned_hub + \
                ";DeviceId=" + device_id + \
                ";SharedAccessKey=" + primary_key

    # The client object is used to interact with Azure IoT Central.
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the client.
    print("Connecting")
    await device_client.connect()
    print("Connected")

    # Asynchronously wait for commands from IoT Central
    # If the TooHot command is called, handle it and output to the console
    async def command_listener(device_client):
        # Loop forever waiting for commands
        while True:
            # Wait for commands from IoT Central
            method_request = await device_client.receive_method_request("TooHot")

            # Log that the command was received
            print("Too Hot Command received")

             # Show "TooLoud" on SenseHat Display
            sense.show_message("Too Hot", text_colour=[255, 0, 0])

            # IoT Central expects a response from a command, saying if the call
            # was successful or not, so send a success response
            payload = {"result": True}

            # Build the response
            method_response = MethodResponse.create_from_method_request(
                method_request, 200, payload
            )

            # Send the response to IoT Central
            await device_client.send_method_response(method_response)

    # async loop that sends the telemetry
    async def main_loop():
        while True:
            # Get the telemetry to send
            telemetry = await get_telemetry()
            print("Telemetry:", telemetry)

            # Send the telemetry to IoT Central
            await device_client.send_message(telemetry)

            # Wait for a minute so telemetry is not sent to often
            await asyncio.sleep(60)

    # Start the command listener
    command_listeners = asyncio.gather(command_listener(device_client))

    # Run the async main loop forever
    await main_loop()

    # Cancel listening
    command_listeners.cancel()

    # Finally, disconnect
    await device_client.disconnect()

# Start the program running
asyncio.run(main())
