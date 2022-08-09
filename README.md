# LoadProfiling
This repository contains: 
* code used for the webapp (demo.py) 
* code which uses preprocessed data from Jakob's masters degree and turns them into webapp ready data (DemoCode.ipynb)
## About the app
Elderly care dahsboard is a webapp developed as a demo to showcase usability of anomaly detection on NILM datasets.

It works by studying the routine of the elders' electric device usage and then comparing current state to routine state. If current state deviates by the usual routine state enough on two devices at a time, it is recognised as an anomaly.

It is designed to give user an insight into the last anomaly detected, its accuracy and date+time of it as it could mean an elder is unconscious and his life in danger. Accuracy provides the probability of said medical state.

To provide help to the elderly there is a phone number, location and some basic personal information that a caregiver can use to aid.

Beside that the webapp provides the quality of routine, on which the accuracy of our prediction depends on. It also features the best and worst 3 devices by their impact on the quality of routine. We suggest the elser tries to improve on the worst 3. We give our feedback about them in a user friendly manner, describing them with: excellent, very good, good, quite good, decent, usable, almost usable, useless (adjectives are listed descending by their desirability).

## Lore
This research was funded by Comsensus

