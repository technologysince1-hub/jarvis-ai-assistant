from engine.new_features import new_features

def test_dual_ai_features():
    test_cases = [
        "feeling overwhelmed with work",
        "anxious about presentation", 
        "stressed about deadlines"
    ]
    
    print("Testing Dual AI Features")
    print("=" * 50)
    
    for i, query in enumerate(test_cases, 1):
        print(f"\n{i}. Testing: '{query}'")
        print("-" * 40)
        
        try:
            result = new_features.execute(query)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
    
    print("\n" + "=" * 50)
    print("Test completed!")

if __name__ == "__main__":
    test_dual_ai_features()