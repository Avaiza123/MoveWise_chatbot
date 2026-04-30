# Deployment Guide for Fitness Chatbot

This guide covers various deployment options for the Fitness Chatbot API.

## Table of Contents
1. [Local Development](#local-development)
2. [Docker Deployment](#docker-deployment)
3. [Heroku Deployment](#heroku-deployment)
4. [AWS Deployment](#aws-deployment)
5. [Production Checklist](#production-checklist)

## Local Development

### Windows Setup

1. **Prerequisites:**
   - Python 3.8+ installed
   - Git installed

2. **Setup:**
```bash
cd backend
run.bat
```

The batch script will:
- Create virtual environment
- Install dependencies
- Start the server

### Linux/Mac Setup

1. **Prerequisites:**
```bash
# Install Python
sudo apt-get install python3 python3-pip python3-venv
```

2. **Setup:**
```bash
cd backend
chmod +x run.sh
./run.sh
```

## Docker Deployment

### Build and Run with Docker

1. **Create Dockerfile** (if not exists):
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/health')"

# Run application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "app:app"]
```

2. **Create .dockerignore:**
```
venv/
__pycache__/
*.pyc
.env
.git
.gitignore
.DS_Store
```

3. **Build image:**
```bash
docker build -t fitness-chatbot:latest .
```

4. **Run container:**
```bash
docker run -p 5000:5000 \
  -e FLASK_ENV=production \
  -e PORT=5000 \
  fitness-chatbot:latest
```

### Docker Compose Setup

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - PORT=5000
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 5s
```

Run with:
```bash
docker-compose up -d
```

## Heroku Deployment

### Step 1: Prepare Files

Create `Procfile`:
```
web: gunicorn --bind 0.0.0.0:$PORT app:app
```

Create `runtime.txt`:
```
python-3.11.5
```

### Step 2: Deploy

1. **Install Heroku CLI:**
   ```bash
   # Windows: Download from https://devcenter.heroku.com/articles/heroku-cli
   # Linux/Mac:
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Login to Heroku:**
   ```bash
   heroku login
   ```

3. **Create app:**
   ```bash
   heroku create your-app-name
   ```

4. **Deploy:**
   ```bash
   git push heroku main
   ```

5. **View logs:**
   ```bash
   heroku logs --tail
   ```

### Environment Variables

Set via Heroku dashboard or CLI:
```bash
heroku config:set FLASK_ENV=production
heroku config:set DEBUG=False
```

## AWS Deployment

### Using Elastic Beanstalk

1. **Install EB CLI:**
```bash
pip install awsebcli
```

2. **Initialize EB:**
```bash
eb init -p python-3.11 fitness-chatbot --region us-east-1
```

3. **Create environment:**
```bash
eb create fitness-chatbot-env
```

4. **Deploy:**
```bash
eb deploy
```

### Using EC2

1. **Launch EC2 Instance:**
   - Choose Ubuntu 20.04 LTS
   - Security group: Allow HTTP (80), HTTPS (443), SSH (22)

2. **Connect and setup:**
```bash
ssh -i "key.pem" ubuntu@your-instance-ip

# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install dependencies
sudo apt-get install -y python3 python3-pip python3-venv nginx

# Clone repository
git clone your-repo-url
cd fitness-chatbot/backend

# Setup Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Setup Nginx reverse proxy:**

Create `/etc/nginx/sites-available/fitness-chatbot`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/fitness-chatbot /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

4. **Setup Systemd service:**

Create `/etc/systemd/system/fitness-chatbot.service`:
```ini
[Unit]
Description=Fitness Chatbot API
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/fitness-chatbot/backend
Environment="PATH=/home/ubuntu/fitness-chatbot/backend/venv/bin"
ExecStart=/home/ubuntu/fitness-chatbot/backend/venv/bin/gunicorn \
    --workers 4 \
    --bind 127.0.0.1:5000 \
    --timeout 120 \
    app:app

Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable fitness-chatbot
sudo systemctl start fitness-chatbot
```

### Using RDS (Optional - for future database integration)

```bash
# Create RDS PostgreSQL instance
aws rds create-db-instance \
    --db-instance-identifier fitness-chatbot-db \
    --db-instance-class db.t3.micro \
    --engine postgres \
    --master-username admin \
    --master-user-password your-password
```

## Production Checklist

### Security
- [ ] Use HTTPS/SSL certificate (Let's Encrypt)
- [ ] Enable CORS for your domain only
- [ ] Implement rate limiting (Flask-Limiter)
- [ ] Add API key authentication
- [ ] Use environment variables for secrets
- [ ] Enable security headers
- [ ] Regular security updates

### Performance
- [ ] Use Gunicorn with multiple workers
- [ ] Enable caching
- [ ] Optimize database queries
- [ ] Use CDN for static content
- [ ] Monitor response times
- [ ] Implement load balancing

### Monitoring & Logging
- [ ] Set up error tracking (Sentry)
- [ ] Configure centralized logging (ELK Stack)
- [ ] Monitor resource usage
- [ ] Set up alerts
- [ ] Track API metrics
- [ ] Monitor error rates

### Backup & Recovery
- [ ] Regular backups
- [ ] Disaster recovery plan
- [ ] Test backup restoration
- [ ] Document recovery procedures

### Deployment
- [ ] Automated CI/CD pipeline
- [ ] Blue-green deployment
- [ ] Rollback procedures
- [ ] Version control
- [ ] Release notes

## SSL/TLS Certificate Setup

### Using Let's Encrypt (Free)

```bash
# Install Certbot
sudo apt-get install certbot python3-certbot-nginx

# Generate certificate
sudo certbot certonly --nginx -d your-domain.com

# Update Nginx configuration
sudo certbot --nginx -d your-domain.com
```

### Using AWS Certificate Manager

```bash
# Create certificate in AWS ACM
# Attach to load balancer or CloudFront
```

## Monitoring with PM2 (Alternative to Systemd)

```bash
# Install PM2
npm install pm2 -g

# Create ecosystem config (ecosystem.config.js)
```

```javascript
module.exports = {
  apps: [{
    name: 'fitness-chatbot',
    script: './app.py',
    interpreter: 'python',
    instances: 4,
    exec_mode: 'cluster',
    watch: false,
    env: {
      FLASK_ENV: 'production'
    }
  }]
};
```

Run with:
```bash
pm2 start ecosystem.config.js
pm2 logs
pm2 save
pm2 startup
```

## Environment Variables Reference

```bash
# Core
FLASK_ENV=production
DEBUG=False
PORT=5000

# Server
HOST=0.0.0.0
WORKERS=4

# Logging
LOG_LEVEL=INFO

# API
API_TIMEOUT=30
RATE_LIMIT=1000/hour

# Database (future)
DATABASE_URL=postgresql://user:pass@localhost/db

# Monitoring
SENTRY_DSN=https://...

# API Keys (if needed)
API_KEY=your-secret-key
```

## Troubleshooting

### High Memory Usage
- Reduce number of Gunicorn workers
- Implement caching
- Check for memory leaks

### Slow Responses
- Monitor database queries
- Enable caching
- Check network latency
- Optimize intent classification

### Deployment Failures
- Check logs: `heroku logs --tail`
- Verify dependencies: `pip freeze`
- Test locally first
- Check environment variables

### SSL Certificate Issues
- Verify domain configuration
- Check certificate expiration
- Renew certificate if needed

## Performance Optimization Tips

1. **Caching:**
   - Cache intent classification results
   - Cache knowledge base lookups
   - Use Redis for distributed caching

2. **Database (future):**
   - Index frequently queried fields
   - Use connection pooling
   - Implement query optimization

3. **API:**
   - Implement pagination
   - Compress responses
   - Use CDN for static content

4. **Monitoring:**
   - Track API response times
   - Monitor error rates
   - Alert on anomalies

---

For questions or issues, refer to the main README.md file.
