# WeatherCLI - City Weather Checker

## Overview

**WeatherCLI** is a simple and lightweight command-line application that fetches real-time weather data for any city using the [OpenWeatherMap API](https://openweathermap.org/api).
Designed for quick access to current weather conditions directly from your terminal, it’s ideal for developers, students, and hobbyists looking to work with APIs and environment-based security.

---

## Features

* Real-time weather data for any city
* Displays:

  * Weather condition and description
  * Temperature and "feels like" in Celsius
  * Humidity level
  * Wind speed
* Uses `.env` file to securely load your API key
* Minimal dependencies

---

## Installation Guide

### Clone the Repository

```bash
git clone https://github.com/Rnaveennithyakalyan/weatherCLI.git
cd weatherCLI
```

### Set Up Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure API Key

Create a `.env` file in the root directory and add your OpenWeatherMap API key:

```
api_key=your-openweathermap-api-key
```

You can obtain a free API key from: [https://openweathermap.org/api](https://openweathermap.org/api)

---

## Running WeatherCLI

```bash
python main.py
```

You’ll be prompted to enter the city name, and the app will display:

```
Enter the city: London
Weather in London:
Condition: Clouds - broken clouds
Temperature: 17.82°C
Feels Like: 16.30°C
Humidity: 76%
Wind Speed: 4.5 m/s
```

---

## Project Structure

```
weather-cli/
├── main.py           # Main script for weather retrieval
├── .env              # Contains your OpenWeatherMap API key
├── requirements.txt  # Required Python packages
└── README.md         # Project documentation
```

---

## Future Enhancements

* Add 5-day weather forecast
* Convert to GUI or web version using Flask or Streamlit
* Add error logs and retry mechanism
* Support for multiple units (Fahrenheit, Kelvin)

---

## License

This project is licensed under the MIT License.

---

## Contact

GitHub: [https://github.com/Rnaveennithyakalyan](https://github.com/Rnaveennithyakalyan)
Email: [naveennithyakalyan@gmail.com](mailto:naveennithyakalyan@gmail.com)

---
