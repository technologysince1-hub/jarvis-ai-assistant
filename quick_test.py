#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'engine'))

from dual_ai import DualAI

def test_features():
    """Test some key features of the dual_ai system"""
    
    print("Testing Dual AI Features\n")
    
    # Initialize the AI assistant
    try:
        ai = DualAI()
        print("AI Assistant initialized successfully")
    except Exception as e:
        print(f"Failed to initialize AI: {e}")
        return
    
    # Test cases with natural language
    test_cases = [
        "make it louder",           # volume_up
        "take a screenshot",        # screenshot  
        "what time is it",          # time
        "open calculator",          # calculator
        "show me my battery",       # battery
        "open chrome browser",      # chrome
        "tell me a joke",          # joke
        "what's the weather",      # weather
    ]
    
    print("\nTesting Natural Language Processing:")
    print("-" * 50)
    
    for i, test_query in enumerate(test_cases, 1):
        print(f"\n{i}. Testing: '{test_query}'")
        try:
            response = ai.execute(test_query)
            print(f"   Response: {response}")
        except Exception as e:
            print(f"   Error: {e}")
    
    print("\n" + "="*50)
    print("Test completed!")

if __name__ == "__main__":
    test_features()