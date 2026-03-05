<div align="center">

# 🚀 Business Strategy Generator

### AI-powered business strategy reports using Google Gemini & Flask

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Google Cloud](https://img.shields.io/badge/Google_Cloud-Vertex_AI-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)](https://cloud.google.com/vertex-ai)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

<br/>

![Business Strategy Generator Screenshot](https://raw.githubusercontent.com/Divyanshi88/genai-BA-chatbot/main/img/Screenshot%202026-03-04%20at%209.26.12%E2%80%AFAM.png)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **AI Strategy Generation** | Powered by Google Gemini via Vertex AI |
| 📊 **Structured Reports** | Strategy · Marketing · Revenue · Risk · Competitors |
| 💾 **SQLite Persistence** | Save, view, and manage all generated reports |
| 📥 **Report Download** | Export any report as a `.txt` file |
| ✅ **Input Validation** | Clean error handling throughout |
| 📱 **Responsive UI** | Works on desktop and mobile |

---

## 📁 Project Structure

```
business-strategy-generator/
├── app/
│   ├── __init__.py           # Flask app initialization
│   ├── models.py             # Database models
│   ├── routes.py             # API endpoints
│   ├── validators.py         # Input validation
│   ├── gemini_service.py     # Gemini API integration
│   ├── templates/
│   │   └── index.html        # Main UI
│   └── static/
│       ├── css/style.css     # Styling
│       └── js/app.js         # Frontend logic
├── instance/                 # Database storage
├── run.py                    # Application entry point
├── config.py                 # Configuration
├── requirements.txt          # Dependencies
├── .env.example              # Environment variables template
└── setup.sh                  # Setup script
```

---

## ⚙️ Prerequisites

Before you begin, ensure you have:

- ✅ **Python 3.8+** and `pip` installed
- ✅ **Google Cloud Project** with Vertex AI API enabled
- ✅ **Google Cloud credentials** configured (service account or ADC)

---

## 🛠️ Setup & Installation

### Step 1 — Clone / Navigate to Project

```bash
cd /path/to/business-strategy-generator
```

### Step 2 — Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure Google Cloud

```bash
# Copy the example env file
cp .env.example .env
```

Open `.env` and set your project ID:

```env
GOOGLE_CLOUD_PROJECT_ID=your-project-id
```

Then set up credentials — choose one method:

```bash
# Option A: Service Account JSON
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json

# Option B: Application Default Credentials
gcloud auth application-default login
```

### Step 5 — Run the Application

```bash
python3 run.py
```

> 🌐 Open **http://localhost:5000** in your browser
> 
> Press `Ctrl+C` to stop the server

---

## 🎯 How to Use

1. **Fill in the form** with your business details:
   - **Business Type** — e.g. *"AI-Powered Analytics Platform"*
   - **Target Audience** — e.g. *"Enterprise data analysts"*
   - **Problem Statement** — e.g. *"Complex data analysis takes too long"*
   - **Budget** — e.g. *"$100,000 – $500,000"*

2. Click **"Generate Strategy"**

3. View your AI-generated report with these sections:
   - 📌 Business Strategy
   - 📣 Marketing Plan
   - 💰 Revenue Model
   - ⚠️ Risk Analysis
   - 🏆 Competitor Insights
   - 📄 Full Report

4. **Download** the report as a `.pdf` file or browse previous reports

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/generate-strategy` | Generate a new business strategy |
| `GET` | `/api/reports` | Fetch all saved reports |
| `GET` | `/api/reports/<id>` | Fetch a specific report |
| `DELETE` | `/api/reports/<id>` | Delete a report |

---

## 🌍 Environment Variables

Edit your `.env` file to customize behaviour:

```env
FLASK_ENV=development          # development or production
FLASK_PORT=5000                # Port number (default: 5000)
GOOGLE_CLOUD_PROJECT_ID=...    # Your GCP project ID
```

---

## 🗄️ Database

The app uses **SQLite** for local persistence.

**Database location:** `instance/business_strategy.db`

To reset the database:

```bash
# Stop the app first, then:
rm instance/business_strategy.db
python3 run.py
```

---

## 🔧 Troubleshooting

<details>
<summary><b>❌ ModuleNotFoundError: No module named 'google'</b></summary>

```bash
pip install -r requirements.txt
```
</details>

<details>
<summary><b>❌ Error calling Gemini API</b></summary>

- Verify your credentials are set correctly
- Ensure **Vertex AI API** is enabled in the [GCP Console](https://console.cloud.google.com/)
</details>

<details>
<summary><b>❌ Port already in use</b></summary>

Change `FLASK_PORT` in your `.env` file, or kill the existing process:

```bash
lsof -i :5000
kill -9 <PID>
```
</details>

<details>
<summary><b>❌ Database errors</b></summary>

```bash
rm instance/business_strategy.db
python3 run.py
```
</details>

---

## 🚢 Production Deployment

For production use:

1. Set `FLASK_ENV=production` in `.env`
2. Use a production WSGI server like **Gunicorn**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 run:app
   ```
3. Switch to a production database (PostgreSQL recommended)
4. Configure HTTPS/SSL
5. Use environment-specific credentials

---

## 📚 Documentation & Links

- 🔵 [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai)
- 🌶️ [Flask Documentation](https://flask.palletsprojects.com)
- 🗄️ [SQLAlchemy](https://www.sqlalchemy.org)

---

<div align="center">

Made with ❤️ using Flask & Google Gemini

</div>
