# PrepMate AI 🎯

An AI-powered mock interview platform that reads your resume and conducts a personalized technical interview, then gives you a performance score and detailed feedback.

**Live Demo → [prep-mate-ai-taupe.vercel.app](https://prep-mate-ai-taupe.vercel.app)**

---

## Features

- **Resume-aware interviews** — Upload your PDF resume and the AI reads it to ask questions specific to your actual experience
- **Real-time AI interviewer** — Powered by Groq LLaMA 3.3 70B for fast, intelligent responses
- **Performance scoring** — Get a score out of 10 with detailed strengths and areas for improvement
- **Session history** — All past interviews saved so you can review them anytime
- **Secure auth** — JWT-based authentication with bcrypt password hashing

---

## Tech Stack

**Backend**
- Python + FastAPI
- PostgreSQL + SQLAlchemy + Alembic
- JWT authentication (python-jose)
- Groq API (LLaMA 3.3 70B)
- pypdf for resume parsing

**Frontend**
- React + Vite
- React Router
- Axios

**Deployment**
- Backend → Render
- Frontend → Vercel

---

## How It Works

1. Register and log in
2. Upload your resume PDF
3. The AI reads your resume and starts asking personalized interview questions
4. Answer as many questions as you like
5. End the interview to get your score (out of 10) and a detailed performance summary
6. Review all past sessions from the History page

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and get JWT token |
| POST | `/resume/upload` | Upload resume PDF |
| POST | `/interview/start` | Start a new interview session |
| POST | `/interview/answer` | Submit an answer, get next question |
| GET | `/interview/history` | Get messages for current session |
| POST | `/interview/end` | End session and get AI summary + score |
| GET | `/interview/sessions` | List all past sessions |
| GET | `/interview/sessions/{id}` | Get full detail of a session |

---

## Local Setup

### Prerequisites
- Python 3.10+
- PostgreSQL
- Node.js 18+

### Backend

```bash
# Clone the repo
git clone https://github.com/vaishali-codes/PrepMate-AI.git
cd PrepMate-AI

# Create and activate virtual environment
python -m venv venv
venv\Scripts\Activate.ps1  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Fill in your values in .env

# Run database migrations
alembic upgrade head

# Start the server
uvicorn main:app --reload
```

### Environment Variables

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/prepmate
SECRET_KEY=your-secret-key
GROQ_API_KEY=your-groq-api-key
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`  
Backend runs at `http://localhost:8000`

---

## Project Structure

```
PrepMate-AI/
├── main.py                  # FastAPI app entry point
├── app/
│   ├── auth.py              # JWT authentication
│   ├── config.py            # Settings
│   ├── database.py          # Database connection
│   ├── models/
│   │   ├── user.py          # User model
│   │   └── interview.py     # InterviewSession + InterviewMessage models
│   ├── routers/
│   │   ├── auth.py          # Auth endpoints
│   │   ├── resume.py        # Resume upload endpoint
│   │   └── interview.py     # Interview endpoints
│   └── services/
│       └── interview.py     # Groq AI integration
├── frontend/                # React frontend
│   └── src/
│       ├── pages/           # Login, Upload, Interview, Summary, History
│       ├── components/      # Navbar
│       └── api.js           # Axios API calls
├── alembic/                 # Database migrations
├── requirements.txt
└── .env.example
```

---

## Built By

**Vaishali Singh** — Python/FastAPI Developer  
[GitHub](https://github.com/vaishali-codes) · [LinkedIn](https://linkedin.com/in/vaishali-singh)
