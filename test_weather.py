from engine.new_features import new_features

print("Testing Weather Feature")
print("=" * 50)

# Test weather for different locations
test_cases = [
    "weather belagavi",
    "weather mumbai", 
    "weather new york",
    "weather"
]

for query in test_cases:
    print(f"\nTesting: '{query}'")
    print("-" * 40)
    
    try:
        result = new_features.weather_forecast(query)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

print("\nWeather test completed!")