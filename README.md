# Factory Hazard Mitigation System

## Human Movement Detection-Based Control System

A comprehensive system utilizing YOLO (You Only Look Once) V8 object detection technology, ultrasonic sensor, and Arduino Uno microcontrollers to enhance factory safety by detecting and alerting workers of their proximity to operating machinery. The primary goal is to prevent accidents by providing timely warnings to workers and initiating machine shutdown mechanisms when individuals approach hazardous areas within the factory floor. The system aims to minimize the risk of workplace injuries and fatalities, thereby fostering a safer working environment and promoting operational efficiency within industrial settings.

## Introduction

Ensuring workplace safety is a paramount societal concern, with industrial accidents posing significant risks to workers' well-being and economic stability. According to the International Labour Organization (ILO), approximately 2.78 million fatal accidents occur annually in workplaces worldwide, equating to over 7,600 deaths every day. Additionally, non-fatal accidents and occupational diseases further contribute to the burden of workplace injuries, leading to prolonged disabilities and decreased productivity.

## Purpose

In this context, the implementation of advanced safety measures, such as the integration of YOLO object detection, ultrasonic sensors, and Arduino Uno microcontrollers, addresses a critical societal need for improved industrial safety standards. By proactively identifying and mitigating potential hazards associated with machine-worker interactions, this technology-driven solution aims to reduce the incidence of workplace accidents and safeguard the physical and mental well-being of workers.

## Benefits

Moreover, enhancing workplace safety not only protects individual workers but also benefits society as a whole by minimizing the socio-economic costs associated with injuries, medical expenses, lost productivity, and legal liabilities. By prioritizing the development and deployment of innovative safety systems, industries can contribute to creating safer, more sustainable working environments, thereby fostering societal progress and economic development.

## How it works

- **Camera distance:** YOLOv8 detects people (class 0) in the webcam feed, and the distance is
  estimated from the bounding-box width using a pinhole-camera approximation.
- **Ultrasonic distance:** an HC-SR04 sensor on an Arduino Uno (`arduino.ino`, trig pin 11,
  echo pin 12) streams distance in cm over serial.
- **Zones:** both readings must agree. Over 500 cm is out of range; 200–500 cm is safe;
  100–200 cm plays `warning.mp3`; under 100 cm plays `alert.mp3` and signals machine shutdown.

## Run

1. Flash `arduino.ino` to the Arduino Uno and connect the ultrasonic sensor.
2. Install dependencies: `pip install -r requirements.txt`
3. Set the Arduino's serial port if it isn't `COM7`, e.g. `SERIAL_PORT=/dev/ttyACM0`.
4. Run `python main.py` and press `q` to quit. The YOLOv8n weights download on first run.
