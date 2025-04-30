# Raspberry Pi Lidar Alert System - Architecture

This system is designed to detect the distance of nearby objects using a UART-connected lidar sensor and respond with visual, auditory, and mechanical outputs. It runs on a Raspberry Pi and uses GPIO control for a warning LED, a sound alert, and a pump relay.

## 📊 System Overview

- **Sensor Input**: UART lidar distance sensor.
- **Outputs**:
  - LED alert when an object is within 4 meters.
  - Audio alert (bear growl) when within 3 meters.
  - Pump relay turns on when within 2 meters.

## 🧩 Component Diagram

```plaintext
+------------------+       +---------------------+
| Lidar (UART)     | ----> | Raspberry Pi        |
+------------------+       |                     |
                           |  +---------------+  |
                           |  | GPIO: LED     |--|--> LED
                           |  | GPIO: Relay   |--|--> Pump
                           |  | Audio via ALSA|--|--> Speaker
                           +---------------------+
