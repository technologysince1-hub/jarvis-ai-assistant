from engine.new_features import new_features

# Simple test without emojis
print("Testing Health Features")

# Test mood tracker
try:
    result = new_features.mood_tracker("feeling happy")
    print("Mood tracker:", result)
except Exception as e:
    print("Mood error:", e)

# Test heart rate
try:
    result = new_features.heart_rate_monitor("heart rate 75 bpm")
    print("Heart rate:", result)
except Exception as e:
    print("Heart rate error:", e)

# Test BMI
try:
    result = new_features.bmi_calculator("weight 70 height 175")
    print("BMI:", result)
except Exception as e:
    print("BMI error:", e)

print("Test completed!")