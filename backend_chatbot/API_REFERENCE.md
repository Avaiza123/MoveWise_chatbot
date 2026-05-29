# Fitness Chatbot API Reference

Complete API documentation for the Fitness Chatbot.

## Base URL
```
http://localhost:5000
```

## Authentication
Currently, no authentication is required. For production, implement API key authentication.

## Response Format

All responses are in JSON format with the following structure:

```json
{
  "success": true/false,
  "message": "Response message",
  "data": {},
  "type": "success|error|info|warning",
  "error_code": "error code if applicable"
}
```

## Endpoints

### 1. Main Chat Endpoint

**POST** `/api/chat`

Send a message to the chatbot and get a response.

**Request:**
```json
{
  "message": "What is a good beginner workout?",
  "user_id": "user_123"
}
```

**Parameters:**
- `message` (string, required): The user's question or message
- `user_id` (string, optional): Unique identifier for the user

**Response:**
```json
{
  "success": true,
  "message": "Here's a beginner-friendly workout routine...",
  "data": {
    "routine": ["Monday: 20 min cardio", "..."]
  },
  "type": "success",
  "error_code": null
}
```

**Status Codes:**
- `200`: Success
- `400`: Bad request or processing error
- `500`: Server error

---

### 2. Fitness Queries

**POST** `/api/fitness`

Send fitness-specific queries.

**Request:**
```json
{
  "message": "How to do push-ups?",
  "user_id": "user_123"
}
```

**Sample Queries:**
- "What is a good beginner workout?"
- "How to do a push-up?"
- "Best cardio exercises?"
- "How to build muscle?"
- "Best exercises for weight loss?"

---

### 3. Health Queries

**POST** `/api/health`

Send health-related queries.

**Request:**
```json
{
  "message": "How many hours of sleep do I need?",
  "user_id": "user_123"
}
```

**Sample Queries:**
- "How many hours of sleep?"
- "How to manage stress?"
- "How much water should I drink?"
- "Tips for immunity?"
- "What causes high blood pressure?"

---

### 4. Diet Queries

**POST** `/api/diet`

Send diet and nutrition queries.

**Request:**
```json
{
  "message": "What should I eat for weight loss?",
  "user_id": "user_123"
}
```

**Sample Queries:**
- "What should I eat for weight loss?"
- "How much protein do I need?"
- "What's a good meal plan?"
- "Best diet for muscle gain?"
- "Difference between macronutrients?"

---

### 5. Food Queries

**POST** `/api/food`

Get nutrition information about specific foods.

**Request:**
```json
{
  "message": "How many calories in chicken?",
  "user_id": "user_123"
}
```

**Sample Queries:**
- "How many calories in chicken?"
- "Tell me about salmon"
- "Breakfast ideas?"
- "High protein foods?"
- "Nutrition facts for banana?"

---

### 6. Get Greeting

**GET** `/api/greeting`

Get the initial greeting message.

**Response:**
```json
{
  "success": true,
  "message": "Hello! 👋 I'm your Fitness Chatbot...",
  "type": "info"
}
```

---

### 7. Health Check

**GET** `/health`

Check if the server is running and healthy.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "service": "Fitness Chatbot API"
}
```

**Status Codes:**
- `200`: Server is healthy
- `500`: Server error

---

## Request Examples

### Using cURL

```bash
# Chat endpoint
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"What is a good beginner workout?"}'

# Fitness endpoint
curl -X POST http://localhost:5000/api/fitness \
  -H "Content-Type: application/json" \
  -d '{"message":"How to do push-ups?"}'

# Greeting
curl -X GET http://localhost:5000/api/greeting

# Health check
curl -X GET http://localhost:5000/health
```

### Using Python

```python
import requests

# Chat query
response = requests.post(
    'http://localhost:5000/api/chat',
    json={'message': 'What is a good beginner workout?'}
)
print(response.json())

# Fitness query
response = requests.post(
    'http://localhost:5000/api/fitness',
    json={'message': 'How to do push-ups?'}
)
print(response.json())
```

### Using JavaScript/Node.js

```javascript
// Chat query
fetch('http://localhost:5000/api/chat', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    message: 'What is a good beginner workout?'
  })
})
.then(response => response.json())
.then(data => console.log(data));

// Fitness query
fetch('http://localhost:5000/api/fitness', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    message: 'How to do push-ups?'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

### Using Dart/Flutter

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

// Chat query
Future<void> sendChatMessage() async {
  final response = await http.post(
    Uri.parse('http://localhost:5000/api/chat'),
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({
      'message': 'What is a good beginner workout?'
    }),
  );
  
  print(jsonDecode(response.body));
}

// Fitness query
Future<void> sendFitnessQuery() async {
  final response = await http.post(
    Uri.parse('http://localhost:5000/api/fitness'),
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({
      'message': 'How to do push-ups?'
    }),
  );
  
  print(jsonDecode(response.body));
}
```

---

## Response Examples

### Successful Fitness Query

```json
{
  "success": true,
  "message": "**Strength Training Guide**\n\nDescription: Exercises using weights or resistance to build muscle\n\n**Examples:** Weightlifting, Bodyweight exercises, Resistance bands, Dumbbells\n\n**Benefits:**\n• Builds muscle\n• Increases metabolism\n• Stronger bones\n• Improves posture\n\n**Duration:** 30-60 minutes\n**Frequency:** 3-4 times per week\n**Rest Days:** 48 hours between same muscle group training",
  "data": {
    "description": "Exercises using weights or resistance to build muscle",
    "examples": ["Weightlifting", "Bodyweight exercises", "Resistance bands", "Dumbbells"],
    "benefits": ["Builds muscle", "Increases metabolism", "Stronger bones", "Improves posture"],
    "duration": "30-60 minutes",
    "frequency": "3-4 times per week",
    "rest_days": "48 hours between same muscle group training"
  },
  "type": "success",
  "error_code": null
}
```

### Successful Food Query

```json
{
  "success": true,
  "message": "**Chicken Breast Nutrition Info**\n\n**Category:** Protein\n**Serving Size:** 100g (cooked)\n\n**Nutrition Per Serving:**\n• Calories: 165\n• Protein: 31g\n• Carbs: 0g\n• Fat: 3.6g\n• Fiber: 0g\n\n**Benefits:**\n• Lean protein\n• Low fat\n• Versatile\n\n**Preparation:** Grill, bake, or boil",
  "data": {
    "category": "Protein",
    "serving_size": "100g (cooked)",
    "calories": 165,
    "protein": 31,
    "carbs": 0,
    "fat": 3.6,
    "fiber": 0,
    "benefits": ["Lean protein", "Low fat", "Versatile"],
    "preparation": "Grill, bake, or boil"
  },
  "type": "success",
  "error_code": null
}
```

### Error Response

```json
{
  "success": false,
  "message": "Invalid query. Please ask a meaningful question.",
  "data": null,
  "type": "error",
  "error_code": "ERR_005"
}
```

---

## Error Codes

| Code | Message | Description |
|------|---------|-------------|
| ERR_001 | Invalid Input | Missing or invalid request parameters |
| ERR_002 | Intent Not Found | Could not determine query intent |
| ERR_003 | Knowledge Base Error | Error accessing knowledge base |
| ERR_004 | Database Error | Database operation failed |
| ERR_005 | Invalid Query | Query format or content invalid |
| ERR_006 | Internal Error | Unexpected server error |
| ERR_404 | Not Found | Endpoint does not exist |

---

## Rate Limiting

Currently no rate limiting is implemented. For production, it's recommended to add:

```
Rate Limit: 1000 requests/hour per user
Burst Limit: 50 requests/minute
```

---

## CORS Headers

The API returns the following CORS headers:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: Content-Type, Accept
```

---

## Best Practices

1. **Always include `message` field** in POST requests
2. **Use appropriate endpoint** for better intent classification
3. **Include `user_id`** for context tracking
4. **Handle errors gracefully** with proper error codes
5. **Check `success` field** before processing response
6. **Cache responses** for identical queries
7. **Implement retry logic** for failed requests
8. **Set appropriate timeouts** (recommended: 30 seconds)

---

## Response Time

- Average response time: **100-200ms**
- Maximum response time: **5 seconds** (with timeout)
- Network latency: Not included in response time

---

## Limits

- **Message length:** No limit (but shorter is better)
- **Response size:** Typically 1-5 KB
- **Concurrent requests:** Limited by server resources
- **History:** Maintained in memory per session

---

## Pagination

Not applicable for current version.

## Versioning

Current API Version: **1.0.0**

---

## Support

For API issues or questions, refer to:
- Main README.md
- Flutter Integration Guide
- Deployment Guide
- Test script (test_chatbot.py)

---

**Last Updated:** 2024
**Status:** Production Ready ✅
