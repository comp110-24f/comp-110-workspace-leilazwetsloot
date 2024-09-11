def get_weather_report() -> str:
    """Helps determine what to wear based on weather"""
    weather: str = input("What is the weather?")
    if (weather == "rainy") or (weather == "cold"):
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather
