from engine.new_features import new_features

print("Testing Creative Tools")
print("=" * 50)

# Test cases for creative features
test_cases = [
    "create meme programming joke",
    "logo for TechCorp blue and white", 
    "color palette ocean sunset",
    "ascii art HELLO",
    "barcode 123456789",
    "mind map learning python"
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
print("Creative tools test completed!")