# LoadProfiling
This repository contains: 
* code used for the webapp (demo.py), inside the map DemoWebApp
* code which uses preprocessed data from Jakob's masters degree and turns them into webapp ready data (DemoCode.ipynb) _{use the newer version}_
* dataset that contains processed data (ElderlyCareDemoResults.pkl)
## Docker
This webapp is accesible in a [docker container](https://hub.docker.com/repository/docker/anzepirnat/ecdemo). _{updated to latest version!}_
## About the app
Elderly care dahsboard is a webapp developed as a demo to showcase usability of anomaly detection on NILM datasets.

It works by studying the routine of the elders' electric device usage and then comparing current state to routine state. If current state deviates by the usual routine state enough on two devices at a time, it is recognised as an anomaly.

It is designed to give user an insight into the last anomaly detected, its accuracy and date+time of it as it could mean an elder is unconscious and his life in danger. Accuracy provides the probability of said medical state or other causes for the described outcome.

To provide help to the elderly there is a phone number, location and some basic personal information that a caregiver can use to aid.

Beside that the webapp provides the quality of routine, on which the accuracy of our prediction depends on. It also features the most and least descriptive 3 devices by their impact on the quality of routine. We suggest the elders try to improve on their routine having the most descriptive 3 as an example. We give our feedback on devices in a user friendly manner, describing them with easily understandable graphics.

## Acknowledgement
This research was funded by Comsensus
