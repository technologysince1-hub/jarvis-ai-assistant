from engine.new_features import new_features

print("Testing Flashcard Feature")
print("=" * 40)

# Test flashcard functionality
test_cases = [
    "add flashcard capital of india: new delhi",
    "add flashcard python: programming language", 
    "flashcard",
    "study flashcard"
]

for query in test_cases:
    print(f"\nTesting: '{query}'")
    print("-" * 30)
    
    try:
        result = new_features.execute(query)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

print("\nFlashcard test completed!")