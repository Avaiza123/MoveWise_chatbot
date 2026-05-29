# Fitness Chatbot - Configuration
import os

class Config:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False
    
class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    ENV = 'development'
    
class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    ENV = 'production'
    
class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True

# Get config based on environment
config = os.environ.get('FLASK_ENV', 'development')
if config == 'production':
    app_config = ProductionConfig()
elif config == 'testing':
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
