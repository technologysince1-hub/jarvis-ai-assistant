# JARVIS AI Assistant - API Documentation

## Overview

This document provides comprehensive API documentation for JARVIS AI Assistant, including internal APIs, external integrations, and usage examples.

## Core APIs

### 1. Voice Command API

#### `allCommands(message)`
Processes voice or text commands and executes appropriate actions.

**Parameters:**
- `message` (str|int): Command text or 1 for voice input

**Returns:**
- Executes command and provides voice/text response

**Example:**
```python
# Voice input
allCommands(1)

# Text input
allCommands("open calculator")
```

#### `takecommand()`
Captures voice input and converts to text.

**Returns:**
- `str`: Recognized speech text

**Example:**
```python
query = takecommand()
print(f"User said: {query}")
```

### 2. AI Integration API

#### `dual_ai.execute(query)`
Processes queries using dual AI system (Groq + Gemini).

**Parameters:**
- `query` (str): User query or command

**Returns:**
- `str`: AI-generated response

**Example:**
```python
from engine.dual_ai import dual_ai
response = dual_ai.execute("What's the weather like?")
```

#### `get_simple_response(query)`
Gets quick AI response for simple queries.

**Parameters:**
- `query` (str): Simple query

**Returns:**
- `str`: AI response

### 3. Authentication API

#### `AuthenticateFace()`
Performs face recognition authentication.

**Returns:**
- `tuple`: (success_flag, user_id) or `int`: success_flag

**Example:**
```python
from engine.auth.recoganize import AuthenticateFace
result = AuthenticateFace()
if result == 1:
    print("Face authentication successful")
```

#### `AuthenticateFingerprint()`
Performs fingerprint authentication via ADB.

**Returns:**
- `bool`: Authentication success status

### 4. System Control API

#### `speak(text)`
Converts text to speech with emotion adaptation.

**Parameters:**
- `text` (str): Text to speak

**Example:**
```python
from engine.command import speak
speak("Hello, how can I help you?")
```

#### `openCommand(query)`
Opens applications or websites based on query.

**Parameters:**
- `query` (str): Application or website name

### 5. Phone Integration API

#### `whatsApp(mobile_no, message, flag, name, schedule_time=None)`
Sends WhatsApp messages or makes calls.

**Parameters:**
- `mobile_no` (str): Phone number
- `message` (str): Message content
- `flag` (str): 'message', 'call', or 'video call'
- `name` (str): Contact name
- `schedule_time` (str, optional): Schedule time

#### `sendMessage(message, mobile_no, name)`
Sends SMS via ADB.

**Parameters:**
- `message` (str): SMS content
- `mobile_no` (str): Phone number
- `name` (str): Contact name

#### `makeCall(name, mobile_no)`
Makes phone call via ADB.

**Parameters:**
- `name` (str): Contact name
- `mobile_no` (str): Phone number

### 6. Health Tracking API

#### `mood_tracker.track_mood(mood, description="")`
Tracks user mood with AI analysis.

**Parameters:**
- `mood` (str): Mood description
- `description` (str, optional): Additional context

#### `health_monitor.log_health_data(data_type, value, unit="")`
Logs health data (heart rate, weight, etc.).

**Parameters:**
- `data_type` (str): Type of health data
- `value` (float): Measurement value
- `unit` (str, optional): Unit of measurement

## External API Integrations

### 1. Groq AI API

**Base URL:** `https://api.groq.com/openai/v1/`

**Authentication:** Bearer token

**Usage:**
```python
from groq import Groq
client = Groq(api_key="your-api-key")

response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Hello"}],
    model="llama-3.1-8b-instant"
)
```

### 2. Google Gemini API

**Base URL:** `https://generativelanguage.googleapis.com/v1beta/`

**Authentication:** API key

**Usage:**
```python
import google.generativeai as genai
genai.configure(api_key="your-api-key")

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Hello")
```

### 3. Weather API Integration

**Provider:** OpenWeatherMap

**Endpoint:** `https://api.openweathermap.org/data/2.5/weather`

**Usage:**
```python
import requests

def get_weather(city):
    api_key = "your-api-key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()
```

## Configuration APIs

### 1. Settings Management

#### `get_ui_config()`
Retrieves UI configuration settings.

**Returns:**
- `dict`: Configuration dictionary

#### `save_ui_config(config)`
Saves UI configuration settings.

**Parameters:**
- `config` (dict): Configuration dictionary

### 2. Voice Control

#### `setVoiceGender(gender)`
Sets voice gender (male/female).

**Parameters:**
- `gender` (str): "male" or "female"

**Returns:**
- `str`: Status message

#### `setLanguage(language)`
Sets system language.

**Parameters:**
- `language` (str): Language name

**Returns:**
- `str`: Status message

## Database APIs

### 1. Contact Management

#### `findContact(query)`
Searches for contact in database.

**Parameters:**
- `query` (str): Contact name or partial name

**Returns:**
- `tuple`: (mobile_number, contact_name) or (0, 0) if not found

#### SQL Operations:
```sql
-- Add contact
INSERT INTO contacts (name, mobile_no) VALUES (?, ?)

-- Search contact
SELECT name, mobile_no FROM contacts WHERE LOWER(name) LIKE ?

-- Delete contact
DELETE FROM contacts WHERE LOWER(name) LIKE ?
```

### 2. Memory System

#### `context_memory_store(information)`
Stores information in long-term memory.

**Parameters:**
- `information` (str): Information to store

#### `context_memory_recall(query="")`
Recalls stored memories.

**Parameters:**
- `query` (str, optional): Search query

**Returns:**
- `list`: Matching memories

## Error Handling

### Standard Error Responses

```python
# API Error Response Format
{
    "success": False,
    "error": "Error description",
    "error_code": "ERROR_CODE",
    "timestamp": "2024-11-11T10:30:00Z"
}

# Success Response Format
{
    "success": True,
    "data": {...},
    "message": "Operation completed successfully",
    "timestamp": "2024-11-11T10:30:00Z"
}
```

### Common Error Codes

- `AUTH_FAILED`: Authentication failure
- `COMMAND_NOT_FOUND`: Unknown command
- `API_LIMIT_EXCEEDED`: Rate limit exceeded
- `NETWORK_ERROR`: Network connectivity issue
- `PERMISSION_DENIED`: Insufficient permissions

## Rate Limits

### AI API Limits
- **Groq API**: 30 requests/minute
- **Gemini API**: 60 requests/minute
- **Weather API**: 1000 requests/day

### Internal Limits
- **Voice Commands**: No limit
- **Database Operations**: No limit
- **File Operations**: System dependent

## Authentication & Security

### API Key Management
```python
# Environment variables
GROQ_API_KEY=your_groq_key
GEMINI_API_KEY=your_gemini_key
WEATHER_API_KEY=your_weather_key

# Configuration files
groq_config.py
gemini_config.py
```

### Security Headers
```python
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "User-Agent": "JARVIS-AI-Assistant/2.0"
}
```

## WebSocket APIs (Future)

### Real-time Communication
```javascript
// WebSocket connection for real-time updates
const ws = new WebSocket('ws://localhost:8080/jarvis');

ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    console.log('Received:', data);
};

// Send command
ws.send(JSON.stringify({
    type: 'command',
    data: 'open calculator'
}));
```

## SDK Usage Examples

### Python SDK
```python
from jarvis_sdk import JARVIS

# Initialize
jarvis = JARVIS(api_key="your-key")

# Execute command
result = jarvis.execute("What's the weather?")

# Voice command
jarvis.listen_and_execute()

# Health tracking
jarvis.health.track_mood("happy", "Great day at work!")
```

### JavaScript SDK (Future)
```javascript
import { JARVIS } from 'jarvis-sdk';

const jarvis = new JARVIS({
    apiKey: 'your-key',
    baseUrl: 'http://localhost:8000'
});

// Execute command
const result = await jarvis.execute('open calculator');
```

## Testing APIs

### Unit Test Examples
```python
import unittest
from engine.command import allCommands

class TestJARVIS(unittest.TestCase):
    def test_calculator_command(self):
        result = allCommands("open calculator")
        self.assertTrue(result)
    
    def test_voice_recognition(self):
        # Mock voice input
        result = takecommand()
        self.assertIsInstance(result, str)
```

### API Testing
```bash
# Test voice command endpoint
curl -X POST http://localhost:8000/api/command \
  -H "Content-Type: application/json" \
  -d '{"command": "open calculator"}'

# Test health tracking
curl -X POST http://localhost:8000/api/health/mood \
  -H "Content-Type: application/json" \
  -d '{"mood": "happy", "description": "Great day!"}'
```

## Monitoring & Analytics

### Performance Metrics
- Response time tracking
- Command success rates
- AI model performance
- System resource usage

### Logging
```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('jarvis.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('JARVIS')
logger.info('Command executed successfully')
```

This API documentation provides comprehensive coverage of all JARVIS AI Assistant APIs and integration points.