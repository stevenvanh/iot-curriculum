# Perform simple analytics and create an email alert on the data using rules

In the [previous step](./set-up-pi-sensehat-humidity-sound.md) you set up IoT Central and the Raspberry Pi to send humidity data.

In this step you will perform simple analytics and create an email alert on the data using IoT Central rules.

## IoT Central rules

IoT Central can run rules - actions that are executed when a condition is met, such as a telemetry value exceeding a threshold. These rules can be based off individual values, or an aggregation over time.

The actions that can be run include sending emails, calling webhooks (Web addresses that you call to run a task, such as [sending a message to Microsoft Teams](https://docs.microsoft.com/microsoftteams/platform/webhooks-and-connectors/what-are-webhooks-and-connectors?WT.mc_id=academic-7372-jabenn)), or calling [Power Automate](https://flow.microsoft.com/?WT.mc_id=academic-7372-jabenn) or [Logic Apps](https://azure.microsoft.com/services/logic-apps/?WT.mc_id=academic-7372-jabenn).

The rule you will be creating will be an alert when the temperature level breaks a threshold. This kind of setup can be used in the real world to monitor equipment in factories or industry to ensure it doesn't exceed safe levels. The concept can also be used for things like temperature monitoring of machinery to ensure it doesn't overheat, or vibration monitoring to ensure a machine isn't breaking. In most situations you would either want an alert through a notification such as an email, or through direct control of a machine.

This part will cover sending an email alert. In a later step, you will enhance this rule to show a message on the SenseHat Display, or showing a message on the console of the virtual IoT device.


## Create an IoT Central rule

### Create the rule

To create an IoT Central rule

1. From the IoT Central app, select the **Rules** tab from the side bar menu

    ![The rules menu](../../../images/iot-central-menu-rules.png)

1. Select the **+ New** button to create a new rule

    ![The new rules button](../images/iot-central-rules-new-rule-button.png)

1. Name the rule `Temperature Alert`

    ![The named rule](../images/iot-central-rules-name-rule-temp.png)

1. Drop down the **Device Template** box in the **Target Devices** section and select `Environment Monitor v2`

    ![Selecting the target devices](../images/iot-central-rules-select-rule-target-devices-v2.png)

1. For the condition, select the `Temperature` *Telemetry* value, the `Is greater than` *Operator*, and set the *Value* to something like 40

    ![The temperature conditions](../images/iot-central-rules-set-rule-conditions-temperature.png)

    This value needs to be higher than your measured temperature, so check the output of the app running on the Pi to see what your temperature is, and adjust if necessary.

1. In the *Actions* section, select the **+ Email** button

    ![The add email button](../images/iot-central-rules-rule-actions-add-email-button.png)

1. Name the email action `Send email` and put your email address in the *To* box. Then select the **Done** button.

    ![The email configure dialog](../images/iot-central-rules-rule-actions-email-dialog-temperature.png)

1. Select the **Save** button to save the rule


### Test the rule

To test the rule, the temperature sensor needs to receive a higher value than expected.

1. Trigger the rule:

    * Increase the temperature, for example by putting the cover on the SenseHat.

1. Check your email for an alert. The Email will include the value that caused the rule to trigger. It may take a few minutes for the email to arrive.

    ![An email showing a sound measurement of 1008](../images/email-sound-check-rule-breach.jpg)


### Disable the rule

To stop receiving email alerts, you need to disable the rule.
Disable the rule by adjusting the slider next to it
[The disable rule slider](../images/iot-central-rules-rule-actions-email-disable.png)


## Next steps

In this step you performed simple analytics and created an alert on the data using IoT Central rules.

In the next step you will Set up an IoT device to listen for an IoT Central command. Select the relevant next step from the list below depending on if you have a Pi or want to set up a virtual IoT device.

* [Set up the command on a Raspberry Pi with Sense HAT](./rules-pi-led-sensehat.md)
* [Set up the command on a virtual device using your PC or Mac](./rules-virtual-led.md)
