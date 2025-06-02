# WhatsApp Webhook with Flask

This is a simple and secure Flask-based webhook handler for integrating with the WhatsApp Cloud API from Meta.

## 🚀 Features
- Webhook verification via a `VERIFY_TOKEN`
- Basic setup to handle POST requests from WhatsApp
- Ready to extend with message handling logic

---

## 🛠️ Requirements

- Python 3.8+
- Flask
- Requests
- (Optional) python-dotenv

---

## 🔧 Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/whatsapp-flask-webhook.git
cd whatsapp-flask-webhook
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file:
```env
VERIFY_TOKEN=your_custom_verify_token
ACCESS_TOKEN=your_meta_access_token
```

Or directly replace them in `app.py`.

---

## 🚦 Running the Webhook Server
```bash
python app.py
```

The app will be available at: `http://localhost:5000/webhook`

---

## 🌍 Webhook Deployment

Use [ngrok](https://ngrok.com/) to expose your local server to the public:

```bash
ngrok http 5000
```

Copy the generated HTTPS URL and configure it in the WhatsApp Webhook setup in Meta Developer Console.

---

## 📬 Respond to Messages

Add your message-handling logic inside the POST section of the webhook.

---

## 🛡️ Security Tips

- Store sensitive tokens in `.env` or a secure vault
- Use HTTPS for production deployments
- Validate incoming request signatures from Meta (optional advanced step)

---

## 📄 License

MIT License