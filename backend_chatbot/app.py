# Main Flask Application - API Endpoints
import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import traceback

from app.chatbot_engine import FitnessChatbot
from app.models.response_model import ResponseType, ERROR_CODES

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for Flutter app

# Initialize chatbot
chatbot = FitnessChatbot()

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for server status"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Fitness Chatbot API"
    }), 200

# Main chat endpoint
@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Main chat endpoint
    
    Request format:
    {
        "message": "user's question",
        "user_id": "optional_user_id"
    }
    
    Response format:
    {
        "success": true/false,
        "message": "response message",
        "data": {...},
        "type": "success/error/info/warning",
        "error_code": "error code if any"
    }
    """
    try:
        # Get request data
        data = request.get_json()
        
        # Validate input
        if not data or 'message' not in data:
            logger.warning("Invalid request: missing 'message' field")
            return jsonify({
                "success": False,
                "message": "Please provide a 'message' field in your request",
                "type": "error",
                "error_code": ERROR_CODES["INVALID_INPUT"]
            }), 400
        
        user_message = data.get('message', '').strip()
        user_id = data.get('user_id')
        
        if not user_message:
            logger.warning("Empty message received")
            return jsonify({
                "success": False,
                "message": "Message cannot be empty",
                "type": "error",
                "error_code": ERROR_CODES["INVALID_INPUT"]
            }), 400
        
        logger.info(f"Processing message from user {user_id}: {user_message[:100]}")
        
        # Process query
        response = chatbot.process_query(user_message, user_id)
        
        # Return response
        return jsonify(response.to_dict()), 200 if response.success else 400
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({
            "success": False,
            "message": "An error occurred processing your request",
            "type": "error",
            "error_code": ERROR_CODES["INTERNAL_ERROR"]
        }), 500

# Get greeting
@app.route('/api/greeting', methods=['GET'])
def greeting():
    """Get initial greeting message"""
    try:
        greeting_msg = chatbot.get_greeting()
        return jsonify({
            "success": True,
            "message": greeting_msg,
            "type": "info"
        }), 200
    except Exception as e:
        logger.error(f"Error getting greeting: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error getting greeting",
            "type": "error"
        }), 500

@app.route('/api/knowledge/stats', methods=['GET'])
def knowledge_stats():
    """Return learned knowledge memory statistics."""
    try:
        stats = chatbot.knowledge_store.stats()
        return jsonify({
            "success": True,
            "message": "Knowledge stats retrieved",
            "data": stats,
            "type": "info"
        }), 200
    except Exception as e:
        logger.error(f"Error getting knowledge stats: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error retrieving knowledge stats",
            "type": "error",
            "error_code": ERROR_CODES["INTERNAL_ERROR"]
        }), 500

# Backward-compatible category endpoints now reuse the same chat flow
@app.route('/api/fitness', methods=['POST'])
def fitness_query():
    """Endpoint for fitness-specific queries"""
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({
                "success": False,
                "message": "Please provide a 'message' field",
                "type": "error"
            }), 400
        
        user_message = data['message'].strip()
        user_id = data.get('user_id')
        response = chatbot.process_query(user_message, user_id)
        
        return jsonify(response.to_dict()), 200 if response.success else 400
    except Exception as e:
        logger.error(f"Error in fitness endpoint: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error processing fitness query",
            "type": "error"
        }), 500

@app.route('/api/health', methods=['POST'])
def health_query():
    """Endpoint for health-specific queries"""
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({
                "success": False,
                "message": "Please provide a 'message' field",
                "type": "error"
            }), 400
        
        user_message = data['message'].strip()
        user_id = data.get('user_id')
        response = chatbot.process_query(user_message, user_id)
        
        return jsonify(response.to_dict()), 200 if response.success else 400
    except Exception as e:
        logger.error(f"Error in health endpoint: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error processing health query",
            "type": "error"
        }), 500

@app.route('/api/diet', methods=['POST'])
def diet_query():
    """Endpoint for diet-specific queries"""
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({
                "success": False,
                "message": "Please provide a 'message' field",
                "type": "error"
            }), 400
        
        user_message = data['message'].strip()
        user_id = data.get('user_id')
        response = chatbot.process_query(user_message, user_id)
        
        return jsonify(response.to_dict()), 200 if response.success else 400
    except Exception as e:
        logger.error(f"Error in diet endpoint: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error processing diet query",
            "type": "error"
        }), 500

@app.route('/api/food', methods=['POST'])
def food_query():
    """Endpoint for food-specific queries"""
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({
                "success": False,
                "message": "Please provide a 'message' field",
                "type": "error"
            }), 400
        
        user_message = data['message'].strip()
        user_id = data.get('user_id')
        response = chatbot.process_query(user_message, user_id)
        
        return jsonify(response.to_dict()), 200 if response.success else 400
    except Exception as e:
        logger.error(f"Error in food endpoint: {str(e)}")
        return jsonify({
            "success": False,
            "message": "Error processing food query",
            "type": "error"
        }), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "success": False,
        "message": "Endpoint not found",
        "type": "error",
        "error_code": "ERR_404"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        "success": False,
        "message": "Internal server error",
        "type": "error",
        "error_code": ERROR_CODES["INTERNAL_ERROR"]
    }), 500

if __name__ == '__main__':
    logger.info("Starting Fitness Chatbot API Server")
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False') == 'True'
    app.run(host='0.0.0.0', port=port, debug=debug)
