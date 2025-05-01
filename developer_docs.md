
---

### `developer_docs.md`

```markdown
# Developer Documentation

## System Overview

- Reads distance from a UART lidar sensor.
- LED turns on below 4m (GPIO 23).
- Audio plays below 3m (`bearscare.wav` using `aplay`).
- Relay (GPIO 17) activates pump below 2m.

## Key Functions

- `read_uart_distance()`: Reads 9-byte UART packet and returns distance in meters.
- Uses `RPi.GPIO` for hardware control.
- `subprocess.Popen` handles audio playback.
- Supports graceful shutdown via `KeyboardInterrupt`.

## Hardware Requirements

- Lidar sensor connected via UART (`/dev/serial0`)
- LED on GPIO 23
- Relay pump on GPIO 17
- `.wav` file for audio alert
