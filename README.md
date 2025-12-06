# MQTT Basic Operations

A simple Python project demonstrating the fundamentals of MQTT (Message Queuing Telemetry Transport) protocol using the Eclipse Paho library.

## What is MQTT?

**MQTT** is a lightweight, publish-subscribe messaging protocol designed for constrained devices and low-bandwidth, high-latency networks. It's widely used in:

- 🏠 **IoT (Internet of Things)** - Smart home devices, sensors
- 🏭 **Industrial automation** - Machine-to-machine communication
- 📱 **Mobile applications** - Push notifications, real-time updates
- 🚗 **Connected vehicles** - Telemetry data transmission

## Core Concepts

### 1. Broker

The **broker** is the central server that receives all messages from publishers and routes them to the appropriate subscribers. In this project, we use the public test broker `test.mosquitto.org`.

```
Publisher → [BROKER] → Subscriber
```

### 2. Topics

**Topics** are hierarchical strings that act as message channels. They use `/` as a level separator.

```
home/livingroom/temperature
home/kitchen/light
factory/machine1/status
```

### 3. Publish/Subscribe Pattern

- **Publisher**: Sends messages to a specific topic
- **Subscriber**: Listens to one or more topics to receive messages

Publishers and subscribers are **decoupled** - they don't need to know about each other.

### 4. Wildcards

MQTT supports two wildcard characters for subscribing to multiple topics:

| Wildcard | Description | Example |
|----------|-------------|---------|
| `+` | Single-level wildcard | `home/+/temperature` matches `home/kitchen/temperature` and `home/bedroom/temperature` |
| `#` | Multi-level wildcard | `home/#` matches `home/kitchen/light`, `home/bedroom/temperature`, etc. |

### 5. QoS (Quality of Service)

MQTT provides three levels of message delivery guarantee:

| Level | Name | Description |
|-------|------|-------------|
| 0 | At most once | Fire and forget - no acknowledgment |
| 1 | At least once | Message is delivered at least once (may have duplicates) |
| 2 | Exactly once | Message is delivered exactly once |

## Project Structure

```
mqtt_basic_operations/
├── MqttSub.py       # Subscriber - Listens for messages
├── MqttPub.py       # Publisher - Sends messages
├── README.md        # This file
└── requirements.txt # Python dependencies
```

## Prerequisites

- Python 3.x
- Internet connection (to reach the public broker)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mqtt_basic_operations.git
cd mqtt_basic_operations
```

2. Install dependencies:
```bash
pip install paho-mqtt
```

## Usage

### Step 1: Start the Subscriber

Open a terminal and run:

```bash
python MqttSub.py
```

This will:
- Connect to `test.mosquitto.org` broker
- Subscribe to all topics under `Asgard/#`
- Print incoming messages

Expected output:
```
Connected with result code Success
```

### Step 2: Publish Messages

Open another terminal and run:

```bash
python MqttPub.py
```

This will publish sample messages to various topics:
- `Asgard/power` → "100W"
- `Asgard/temperature` → "20C"
- `Asgard/humidity` → "50%"
- `Asgard/pressure` → "1013hPa"

### Expected Result

The subscriber terminal will display:
```
Connected with result code Success
Power: b'100W'
Temperature: b'20C'
Humidity: b'50%'
Pressure: b'1013hPa'
```

## Code Explanation

### Subscriber (MqttSub.py)

```python
import paho.mqtt.client as mqtt

# Callback when connected to broker
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("Asgard/#")  # Subscribe to all Asgard topics

# Callback when message is received
def on_message(client, userdata, msg):
    # Handle different topics
    if msg.topic == "Asgard/power":
        print("Power: " + str(msg.payload))
    # ... more topic handlers

# Create client and set callbacks
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# Connect and start listening
mqttc.connect("test.mosquitto.org", 1883, 60)
mqttc.loop_forever()  # Blocking loop
```

### Publisher (MqttPub.py)

```python
import paho.mqtt.client as mqtt

# Create client and connect
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

# Publish messages to different topics
client.publish("Asgard/power", "100W")
client.publish("Asgard/temperature", "20C")

# Disconnect when done
client.disconnect()
```

## Common MQTT Brokers

| Broker | URL | Port | Description |
|--------|-----|------|-------------|
| Eclipse Mosquitto (Test) | test.mosquitto.org | 1883 | Public test broker |
| HiveMQ | broker.hivemq.com | 1883 | Public test broker |
| EMQX | broker.emqx.io | 1883 | Public test broker |

> ⚠️ **Note**: Public brokers are for testing only. For production, use a private broker or a managed service.

## Useful Commands (with Mosquitto CLI)

### Installing Mosquitto CLI

**Windows (using winget):**
```powershell
winget install EclipseFoundation.Mosquitto
```

**Linux (Debian/Ubuntu):**
```bash
sudo apt install mosquitto-clients
```

**macOS (using Homebrew):**
```bash
brew install mosquitto
```

### Adding Mosquitto to PATH (Windows)

After installing on Windows, add Mosquitto to your PATH:

**Temporary (current session only):**
```powershell
$env:Path += ";C:\Program Files\mosquitto"
```

**Permanent (run as Administrator):**
```powershell
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\mosquitto", "Machine")
```

Then restart your terminal.

### Using Mosquitto CLI

```bash
# Subscribe to a topic
mosquitto_sub -h test.mosquitto.org -t "Asgard/#"

# Publish a message
mosquitto_pub -h test.mosquitto.org -t "Asgard/power" -m "200W"
```

> ⚠️ **PowerShell Note**: If using topics with `$`, use single quotes to prevent variable interpolation:
> ```powershell
> mosquitto_pub -t '$SYS/broker/version' -h test.mosquitto.org -m "test"
> ```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Connection timeout | Check your internet connection and firewall settings |
| Messages not received | Ensure subscriber is running before publishing |
| `$` topics not working | Topics starting with `$` are reserved for system use |

## Resources

- [MQTT Official Specification](https://mqtt.org/mqtt-specification/)
- [Eclipse Paho Python Client](https://www.eclipse.org/paho/index.php?page=clients/python/index.php)
- [HiveMQ MQTT Essentials](https://www.hivemq.com/mqtt-essentials/)
- [Mosquitto Broker](https://mosquitto.org/)

## License

This project is open source and available under the [MIT License](LICENSE).
