# Test Script for Fitness Chatbot
import requests
import json

# Configuration
BASE_URL = "http://localhost:5000"
ENDPOINTS = {
    "chat": "/api/chat",
    "fitness": "/api/fitness",
    "health": "/api/health",
    "diet": "/api/diet",
    "food": "/api/food",
    "greeting": "/api/greeting"
}

test_queries = {
    "fitness": [
        "What is a good beginner workout?",
        "How do I do a push-up?",
        "Best cardio exercises?",
        "How to build muscle?"
    ],
    "health": [
        "How many hours of sleep do I need?",
        "How to manage stress?",
        "How much water should I drink daily?",
        "What is good for immunity?"
    ],
    "diet": [
        "What should I eat for weight loss?",
        "How much protein do I need?",
        "What's a good meal plan?",
        "Difference between macros?"
    ],
    "food": [
        "How many calories in chicken?",
        "Tell me about salmon",
        "Breakfast ideas?",
        "High protein foods?"
    ]
}

def test_health_check():
    """Test server health check"""
    print("\n" + "="*50)
    print("Testing Server Health")
    print("="*50)
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        print(f"✓ Server is healthy: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"✗ Server health check failed: {str(e)}")

def test_greeting():
    """Test greeting endpoint"""
    print("\n" + "="*50)
    print("Testing Greeting Endpoint")
    print("="*50)
    try:
        response = requests.get(f"{BASE_URL}{ENDPOINTS['greeting']}", timeout=5)
        print(f"✓ Greeting retrieved: {response.status_code}")
        print(f"Message: {response.json()['message'][:100]}...")
    except Exception as e:
        print(f"✗ Greeting test failed: {str(e)}")

def test_queries():
    """Test chat queries"""
    print("\n" + "="*50)
    print("Testing Chat Queries")
    print("="*50)
    
    for category, queries in test_queries.items():
        endpoint = ENDPOINTS.get(category, ENDPOINTS["chat"])
        print(f"\n--- Testing {category.upper()} ---")
        
        for query in queries[:2]:  # Test first 2 queries per category
            try:
                response = requests.post(
                    f"{BASE_URL}{endpoint}",
                    json={"message": query},
                    timeout=10
                )
                
                result = response.json()
                status = "✓" if result.get("success") else "✗"
                print(f"\n{status} Q: {query}")
                print(f"   Message: {result.get('message', 'No response')[:100]}...")
                if result.get("error_code"):
                    print(f"   Error Code: {result.get('error_code')}")
                    
            except Exception as e:
                print(f"✗ Error: {str(e)}")

def test_error_cases():
    """Test error handling"""
    print("\n" + "="*50)
    print("Testing Error Handling")
    print("="*50)
    
    error_tests = [
        ("Empty message", {}),
        ("No message field", {"user_id": "test"}),
        ("Invalid endpoint", "/api/invalid"),
    ]
    
    for description, payload in error_tests:
        print(f"\nTesting: {description}")
        try:
            if isinstance(payload, dict):
                response = requests.post(
                    f"{BASE_URL}{ENDPOINTS['chat']}",
                    json=payload,
                    timeout=5
                )
            else:
                response = requests.get(f"{BASE_URL}{payload}", timeout=5)
            
            print(f"Status: {response.status_code}")
            result = response.json()
            print(f"Success: {result.get('success')}")
            print(f"Error Code: {result.get('error_code', 'N/A')}")
            
        except Exception as e:
            print(f"Error: {str(e)}")

def main():
    """Run all tests"""
    print("\n" + "#"*50)
    print("# Fitness Chatbot - Comprehensive Test Suite")
    print("#"*50)
    
    try:
        # Check if server is running
        print("Checking server connection...")
        requests.get(f"{BASE_URL}/health", timeout=2)
        print("✓ Server is running!\n")
    except:
        print("✗ Server is not running. Please start it first.")
        print(f"  Run: python app.py")
        return
    
    # Run tests
    test_health_check()
    test_greeting()
    test_queries()
    test_error_cases()
    
    print("\n" + "#"*50)
    print("# Test Suite Completed")
    print("#"*50 + "\n")

if __name__ == "__main__":
    main()
