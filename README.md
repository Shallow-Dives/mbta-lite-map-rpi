# MBTA Lite Map

The MBTA Lite Map is a Raspberry Pi powered LED map of the MBTA Red Line in Boston. It was inspired by the LED maps from [Traintrackr](https://www.traintrackr.io/). 

Each train contributes a scaled value to the brightness of individual station LEDs based on whether they are at, 
incoming to, or departing from the station.  The map updates with live MBTA data every 5 seconds, so you can watch 
trains move through the system.

This project is split into two components:

* **RPi Map Interface** - This repository contains the Raspberry Pi interface to display the trains on the Red Line as 
  station LEDs with variable brightness based on the state of trains at and between stations.


* **MBTA Lite Map API** - The map interface depends on the [mbta-lite-map-api](https://github.com/Shallow-Dives/mbta-lite-map-api), deployed at [ADD: Lite Map API link](). This service accesses train data from the MBTA API, converts it to an LED representation, and serves it to be displayed - avoiding compute on the RPi.

![Image of a Boston MBTA map with bright LEDs representing red line stations with trains](https://github.com/Shallow-Dives/mbta-lite-map-rpi/blob/main/assets/map.jpg)

## Hardware

## Deployment Workflow


## Todos

* Cache computed LED overlays to standardize response time

## Resources

* [Adafruit LED Tutorial](https://learn.adafruit.com/adafruit-neopixel-uberguide/the-magic-of-neopixels)
* [MBTA Map](https://cdn.mbta.com/sites/default/files/2022-12/2022-12-12-subway-map-v37f.pdf)
