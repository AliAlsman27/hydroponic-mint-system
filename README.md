# Smart Hydroponic Mint Farming System 🌿

A Raspberry Pi-based IoT system to automate and monitor mint farming in a hydroponic setup using environmental sensors and Blynk IoT platform.

## 🚀 Features
- Real-time monitoring of:
  - pH level (pH Sensor)
  - Total Dissolved Solids (TDS Sensor)
  - Water temperature (DS18B20)
  - Air temperature and humidity (DHT22)
  - Light intensity (LDR)
  - Water level (Water Level Sensor)
- Automated control of:
  - Water pump (based on schedule)
  - Nutrient pumps (based on pH and TDS values)
- Mobile dashboard and alerts using **Blynk**
- Manual override and threshold control via mobile

## 🛠️ Tech Stack
- **Raspberry Pi (Python)**
- **Blynk IoT platform**
- **Analog sensors with ADC**
- **Relay modules for pump control**

## 📦 Hardware Components
- Raspberry Pi
- PH Sensor
- TDS Sensor
- DS18B20 (Water temp)
- DHT22 (Air temp & humidity)
- LDR (Light)
- Water Level Sensor
- 3 Pumps (1 water, 2 nutrients)
- Relay Module
- ADC module (if analog sensors used)

## 📲 User Interface
- Built using Blynk:
  - Gauges for real-time data
  - SuperChart for trends
  - Buttons and sliders for control
  - Notifications for alerts

## ⚙️ Logic Flow
1. Read all sensor data periodically.
2. If pH or TDS out of range, activate appropriate nutrient pump.
3. If water level is too low, notify user and stop operations.
4. User can manually override via mobile dashboard.
5. Pump timings and thresholds are configurable from the app.

## 📸 Screenshots
![WhatsApp Image 2025-05-09 at 19 23 35_4107afe2](https://github.com/user-attachments/assets/1d6c7a47-07c5-4b0f-97e7-44d17eaa79a5)


---

## 📁 Project Status
✅ Functional prototype completed  
🔄 Future Work: Add camera for plant health monitoring using CV

---

## 🔗 License
MIT – Feel free to use and modify
