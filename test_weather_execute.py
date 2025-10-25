from engine.new_features import new_features

print("Testing Weather via Execute Function")
print("=" * 50)

# Test through main execute function
test_cases = [
    "weather belagavi",
    "weather bangalore", 
    "weather delhi"
]

for query in test_cases:
    print(f"\nTesting: '{query}'")
    print("-" * 40)
    
    try:
        result = new_features.execute(query)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

print("\nWeather execute test completed!")