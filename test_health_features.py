from engine.new_features import new_features

def test_health_features():
    print("Testing Health Features")
    print("=" * 50)
    
    # Test cases for new health features
    test_cases = [
        "feeling happy today",
        "mood 8",
        "heart rate 72 bpm", 
        "add vitamin D at 9am",
        "weight 70 height 175"
    ]
    
    for i, query in enumerate(test_cases, 1):
        print(f"\n{i}. Testing: '{query}'")
        print("-" * 40)
        
        try:
            result = new_features.execute(query)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
    
    print("\n" + "=" * 50)
    print("Health features test completed!")

if __name__ == "__main__":
    test_health_features()