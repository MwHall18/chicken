# User Guide

## Setup Instructions
1. Place the `main.py` script and `bearscare.wav` file on your Raspberry Pi.
2. Connect the lidar sensor via UART, an LED to GPIO 23, and a relay to GPIO 17.
3. Ensure `aplay` is installed for audio playback:
   ```bash
   sudo apt-get install alsa-utils
