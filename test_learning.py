from engine.new_features import new_features

print("Testing Learning Features")
print("=" * 50)

# Test cases for learning features
test_cases = [
    "translate hello to spanish",
    "define computer", 
    "wikipedia artificial intelligence",
    "calculate sin(45) + log(10)",
    "convert 100 meters to feet",
    "add flashcard capital of india: new delhi",
    "quiz on science"
]

for i, query in enumerate(test_cases, 1):
    print(f"\n{i}. Testing: '{query}'")
    print("-" * 40)
    
    try:
        result = new_features.execute(query)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

print("\n" + "=" * 50)
print("Learning features test completed!")