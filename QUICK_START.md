# 🚀 QUICK START - Fitness Chatbot

Start using the chatbot in 3 simple steps!

---

## Step 1: Start the Backend Server

### Windows
```bash
cd fitness-chatbot\backend
run.bat
```

### Linux/Mac
```bash
cd fitness-chatbot/backend
chmod +x run.sh
./run.sh
```

**Result:** Server starts at `http://localhost:5000`

---

## Step 2: Test the Chatbot (Optional)

```bash
# In a new terminal, from the backend directory
python test_chatbot.py
```

This runs comprehensive tests and shows example responses.

---

## Step 3: Integrate with Flutter (or Use API)

### Option A: Use the API Directly
```bash
# Test with curl
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"What is a good beginner workout?"}'
```

### Option B: Integrate with Flutter App
1. Copy `flutter_integration/chatbot_service.dart` to your Flutter project
2. Follow `flutter_integration/FLUTTER_INTEGRATION_GUIDE.md`
3. Update the base URL to your server

---

## 📡 API Endpoints

| Endpoint | Use |
|----------|-----|
| `POST /api/chat` | Any fitness question |
| `POST /api/fitness` | Workouts & exercises |
| `POST /api/health` | Health & wellness |
| `POST /api/diet` | Diet & nutrition |
| `POST /api/food` | Food information |
| `GET /api/greeting` | Get greeting message |
| `GET /health` | Check server status |

---

## 🎯 Example Questions

Ask about:
- "What is a good beginner workout?"
- "How many calories in chicken?"
- "How many hours of sleep do I need?"
- "What should I eat for weight loss?"
- "Best exercises for building muscle?"
- "How to do push-ups properly?"

---

## 📚 Documentation

- **Full Setup:** Read `README.md`
- **API Details:** Read `API_REFERENCE.md`
- **Flutter Guide:** Read `flutter_integration/FLUTTER_INTEGRATION_GUIDE.md`
- **Deployment:** Read `DEPLOYMENT_GUIDE.md`
- **Project Summary:** Read `PROJECT_SUMMARY.md`

---

## 🔧 Troubleshooting

### Port 5000 already in use?
```bash
# Windows: Change port in app.py or .env
# Linux/Mac: Kill process using port 5000
lsof -ti:5000 | xargs kill -9
```

### Python not found?
Install Python 3.8+: https://www.python.org/

### Dependencies failed to install?
```bash
# Upgrade pip first
pip install --upgrade pip

# Then try again
pip install -r requirements.txt
```

### Can't connect from Flutter app?
- Check server is running: `http://localhost:5000/health`
- Update baseUrl in Flutter: Change `localhost` to your server IP
- Check firewall settings allow port 5000

---

## 💡 Next Steps

1. ✅ Start the server (Step 1 above)
2. ✅ Test it works (Step 2 above)
3. ✅ Read full README.md for detailed setup
4. ✅ Follow Flutter guide for app integration
5. ✅ Configure for production (see DEPLOYMENT_GUIDE.md)

---

## ✨ What You Have

✅ Fully working fitness chatbot
✅ Knowledge base with fitness, health, diet, food
✅ REST API ready for any client
✅ Flutter integration ready
✅ Error-free, production-ready code
✅ Comprehensive documentation

---

## 🎉 You're Ready!

Your fitness chatbot is **production-ready** and can be:
- Used immediately via API
- Integrated with Flutter
- Deployed to cloud (Docker, Heroku, AWS)
- Extended with more knowledge
- Customized for your needs

**Questions?** Check the documentation files included in the project.

**Start now:** Run `run.bat` (Windows) or `run.sh` (Linux/Mac)

---

**Happy chatting! 🏋️‍♀️**
