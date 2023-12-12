# Create an IoT Central command and trigger it from a rule

In the previous step you either [set up a Raspberry Pi with SenseHat](./rules-pi-led-sensehat.md), or [set up a virtual IoT device](./rules-virtual-led.md) to listen for an IoT Central command.

In this step you will create the IoT Central command and trigger it from a rule.

## Create a command

Commands are capabilities on an interface, so to add a command, a new version of the interface needs to be create on a new version of the device template.

1. Follow the steps in a previous part to create a new version of the `Environment Monitor v2` device template. Make sure it is named `Environment Monitor v3`.

1. Create a new version of the `Environment` interface

1. Add a new capability to the interface with the following settings:

    | Display Name | Name    | Capability Type | Command Type | Request | Response |
    | ------------ | ------- | --------------- | ------------ | ------- | -------- |
    | Too Loud     | TooLoud | Command         | Synchronous  | off     | off      |

    ![The new Too Loud capability](../images/iot-central-interface-new-too-loud-capability.png)

1. Save the interface, and publish the device template

1. Migrate the *Pi Environment Monitor* to the new *Environment Monitor v3* device template following the steps in the previous part. There is no need to migrate the simulated device over as this won't have an LED.

### Test the code

The code can be tested by manually calling the command from IoT Central.

1. From IoT Central, select the *Pi Environment Monitor* from the Devices

1. There will be a new tab called *Command*. This is created automatically whenever there is a command on a device template. Select this tab.

    ![The commands tab](../images/iot-central-device-commands-tab.png)

1. This tab shows the *Too Loud* command with a **Run** button to execute the command. Select the **Run** button.

    ![The run button](../images/iot-central-device-commands-tab-tooloud-run-button.png)

1. You will see the result of this command depending on if you are using a Pi or a virtual device

    * If you are using a Raspberry Pi, you will see the LED light for 10 seconds, then turn off
    * If you are using a virtual IoT device, you will see the following appear in the console:

        ```output
        #########################
        Too Loud Command received
        #########################
        ```
     * If you use the Raspberry Pi with Sense HAT you should see "Too Loud" on the display.


## This is the end of the IoT workshop ##



# End of IoT Workshop

This is where the IoT Workshop ends.
Under next steps you can find steps that allow you to build out your lab, this does require an Azure subscription.

## Next steps

In this step you created the IoT Central command and triggered it from a rule.

In the [next step](./anomaly-detection.md) you will perform more advanced analytics to detect anomalies in the data.
