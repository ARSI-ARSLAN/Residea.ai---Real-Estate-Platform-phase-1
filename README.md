# Residea.ai — AI-Powered Property Recommendation Platform

Residea.ai is a full-stack real estate platform that combines a React/TypeScript frontend with a Django REST API backend and trained ML models (XGBoost) to deliver personalized property recommendations, ROI predictions, and smart filtering for the Pakistani real estate market.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Environment Variables](#environment-variables)
- [ML Models](#ml-models)
- [API Endpoints](#api-endpoints)
- [Available Scripts](#available-scripts)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### 🏠 AI Property Recommendations
The core of the app. The main dashboard (`Dashboard.tsx`) shows personalised property recommendations powered by a trained XGBoost ranker model. Each property card shows an AI match percentage, society approvals (CDA/RDA/PHATA), and proximity scores for hospitals, schools, and security. Users can shortlist, compare (up to 3), and view full details.

### 🔮 ROI Predictions
Each recommended property includes 1-year, 3-year, and 5-year return-on-investment estimates from a dedicated XGBoost ROI predictor model. Risk-adjusted calculations account for safety scores and historical trends.

### 🛠️ AI Renovation Studio
A multi-step wizard (`RenovationDashboard.tsx`) where users upload a room photo, enter room metadata (type, dimensions, condition, age), and set renovation preferences (goal, budget tier, style). The AI backend generates renovation suggestions with impact/feasibility scores and a before/after visualisation via Stability AI or Replicate image generation.

### 🔐 User Authentication
JWT-based login, signup, forgot password, and session management via Django SimpleJWT.

### 🎯 Onboarding Flow
Collects user preferences (budget, location, bedrooms, facility priorities) on first login to personalise ML recommendations from the start.

### 🏗️ Property Management
- Add new property listings with photos and details
- My Listings view to manage your own submissions
- Admin dashboard for approving/rejecting submitted properties

### 📊 Property Comparison
Side-by-side comparison of up to 3 properties across key metrics.

### 💰 Mortgage Calculator
Built-in financing estimator to calculate monthly payments and affordability.

### 📅 Visit Scheduling & Notifications
Book property viewings and receive updates through the notifications panel.

---

## Tech Stack

### Frontend
| Technology | Version |
|---|---|
| React | 18.x |
| TypeScript | 5.x |
| Vite | 6.x |
| Tailwind CSS | 3.x |
| Radix UI | latest |
| Recharts | 2.x |
| Axios | 1.x |

### Backend
| Technology | Version |
|---|---|
| Python | 3.10+ |
| Django | 4.2.7 |
| Django REST Framework | 3.14.0 |
| SimpleJWT | 5.3.0 |
| django-cors-headers | 4.3.0 |
| XGBoost | 2.0.2 |
| scikit-learn | 1.3.2 |
| pandas | 2.1.3 |
| numpy | 1.26.2 |

### Database
- SQLite (development)
- PostgreSQL-ready via `psycopg2-binary`

---

## Project Structure

```
Residea.ai_Frontend/
├── README.md                        # This file
├── PROJECT_STATUS.md                # Current operational status
├── README_ML_SETUP.md               # ML model setup guide
├── TESTING_ML_RECOMMENDATIONS.md   # ML testing documentation
├── START_PROJECT.bat                # Start both servers (Windows)
├── start_backend.bat                # Start Django backend only
├── start_frontend.bat               # Start React frontend only
├── test_ml_recommendations.py       # ML system test script
│
└── Residea.ai_Frontend/             # Main application directory
    ├── index.html
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    ├── .env                         # Frontend environment variables (not committed)
    │
    ├── src/
    │   ├── App.tsx
    │   ├── main.tsx
    │   ├── index.css
    │   ├── components/
    │   │   ├── Homepage.tsx
    │   │   ├── LoginScreen.tsx
    │   │   ├── SignupScreen.tsx
    │   │   ├── ForgotPasswordScreen.tsx
    │   │   ├── Onboarding.tsx
    │   │   ├── Dashboard.tsx
    │   │   ├── AdminDashboard.tsx
    │   │   ├── PropertyDetails.tsx
    │   │   ├── PropertyComparison.tsx
    │   │   ├── AddPropertyListing.tsx
    │   │   ├── MyListings.tsx
    │   │   ├── MortgageCalculator.tsx
    │   │   ├── RenovationDashboard.tsx
    │   │   ├── ScheduleVisit.tsx
    │   │   ├── Notifications.tsx
    │   │   ├── UserProfile.tsx
    │   │   ├── Router.tsx
    │   │   ├── figma/               # Figma-exported components
    │   │   └── ui/                  # Radix UI-based design system
    │   ├── services/                # API service layer
    │   ├── config/                  # App configuration
    │   ├── styles/                  # Global styles
    │   ├── guidelines/              # Design guidelines
    │   └── assets/                  # Static assets
    │
    ├── Models Trained/              # Pre-trained ML model files (.pkl)
    │   ├── xgbr_ranker (2).pkl
    │   └── xgbr_roi (2).pkl
    │
    └── backend/
        ├── manage.py
        ├── requirements.txt
        ├── .env                     # Backend environment variables (not committed)
        ├── .env.example             # Environment variable template
        ├── db.sqlite3               # SQLite database (not committed)
        ├── setup.bat                # Windows setup script
        ├── setup.sh                 # Linux/macOS setup script
        │
        ├── residea_backend/         # Django project settings
        │   ├── settings.py
        │   ├── urls.py
        │   ├── wsgi.py
        │   └── asgi.py
        │
        ├── apps/
        │   ├── users/               # User auth & profiles
        │   ├── properties/          # Property listings & filtering
        │   ├── preferences/         # User preference storage
        │   └── ml_services/         # ML recommendation engine
        │       ├── model_loader.py
        │       ├── feature_engineering.py
        │       ├── ranker.py
        │       ├── roi_predictor.py
        │       ├── reference_recommendation_logic.py
        │       ├── views.py
        │       └── urls.py
        │
        ├── ml_models/               # Runtime ML model storage
        ├── media/                   # Uploaded property images
        └── logs/                    # Application logs
```

---

## Prerequisites

- **Node.js** v18+ and npm
- **Python** 3.10+
- **pip**
- Git

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/residea-ai.git
cd residea-ai
```

### Backend Setup

```bash
cd Residea.ai_Frontend/backend

# Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
copy .env.example .env   # Windows
cp .env.example .env     # macOS/Linux

# Edit .env with your configuration (see Environment Variables section)

# Run database migrations
python manage.py migrate

# (Optional) Load sample property data
python import_property_data.py

# Start the backend server
python manage.py runserver
```

Backend runs at: `http://localhost:8000`

### Frontend Setup

```bash
cd Residea.ai_Frontend

# Install dependencies
npm install

# Create environment file
copy .env.example .env   # Windows
cp .env.example .env     # macOS/Linux

# Start the development server
npm run dev
```

Frontend runs at: `http://localhost:5173`

### Quick Start (Windows only)

From the root directory, double-click or run:
```bash
START_PROJECT.bat
```

This starts both backend and frontend in separate terminal windows.

---

## Environment Variables

### Backend (`backend/.env`)

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
ML_MODELS_DIR=Models Trained
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

See `backend/.env.example` for the full list of available variables.

### Frontend (`.env`)

```env
VITE_API_BASE_URL=http://localhost:8000/api
```

---

## ML Models

The platform uses two pre-trained XGBoost models located in `Residea.ai_Frontend/Models Trained/`:

| Model | File | Purpose |
|---|---|---|
| Property Ranker | `xgbr_ranker (2).pkl` | Scores properties 0–10 based on user preferences |
| ROI Predictor | `xgbr_roi (2).pkl` | Estimates 1yr / 3yr / 5yr return on investment |

### How Recommendations Work

```
User Preferences → Property Filtering → Feature Engineering → ML Scoring → Ranked Results
```

The feature engineering pipeline extracts 11 features per property:
- `price_fit_score`, `bedroom_match`, `area_match_score`, `location_match_score`
- `school_score`, `hospital_score`, `metro_score`, `park_score`
- `facility_match_ratio`, `risk_adjusted_safety`, `risk_adjusted_roi`

See `README_ML_SETUP.md` for detailed ML configuration instructions.

### Test the ML System

```bash
# From the root directory
python test_ml_recommendations.py

# Or check the health endpoint
curl http://localhost:8000/api/ml/health/
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/ml/health/` | ML model health check |
| `GET` | `/api/properties/` | List all properties |
| `GET` | `/api/properties/recommendations/` | Personalised ML recommendations |
| `GET` | `/api/properties/{id}/roi_estimate/` | ROI estimate for a property |
| `POST` | `/api/users/register/` | User registration |
| `POST` | `/api/users/login/` | JWT login |
| `GET/PUT` | `/api/preferences/` | User preferences |

Full API documentation is available at `http://localhost:8000/api/docs/` (Swagger UI via drf-yasg) when the backend is running.

---

## Available Scripts

### Backend

```bash
python manage.py runserver        # Start development server
python manage.py migrate          # Apply database migrations
python manage.py createsuperuser  # Create admin user
python verify_system.py           # Verify full system health
python test_ml_recommendations.py # Test ML pipeline
```

### Frontend

```bash
npm run dev      # Start development server
npm run build    # Build for production
```

---

## Known Issues

- **XGBoost pickle warning**: A serialization version warning appears on model load. It does not affect functionality. Fix: re-save models using `model.save_model()`.
- **Default scores**: When no user preferences are set, all properties receive a base score of 5.0. This is expected fallback behaviour — users should complete onboarding for personalised results.

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> Built with ❤️ for the Pakistani real estate market
