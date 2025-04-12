# She Connects

**She Connects** is an AI-powered platform where women can anonymously share their stories and connect with others based on shared experiences. The platform leverages natural language processing (NLP) to match users based on keywords and sentiment analysis.

## Features

- **Anonymous Story Submission**: Users can share their stories without revealing their identity.
- **AI-Powered Matching**: Stories are matched based on keyword overlap and sentiment proximity.
- **Modern UI**: Built with React and Material-UI for a clean and responsive design.

## Architecture

The project is divided into two main parts:

1. **Frontend**: A React application for user interaction.
2. **Backend**: A Flask REST API for story submission and matching, with an AI layer for NLP processing.

### Directory Structure

```
she-connects/
├── frontend/        # React app
│   ├── public/      # Static files (index.html, favicon, etc.)
│   ├── src/         # React components, services, and pages
│   └── package.json # Frontend dependencies
├── backend/         # Flask API
│   ├── ai/          # NLP utilities and matching logic
│   ├── data/        # Temporary JSON storage for stories
│   ├── app.py       # API routes
│   └── requirements.txt # Backend dependencies
└── README.md        # Project documentation
```

## Installation

### Prerequisites

- Node.js (v16 or later)
- Python (v3.8 or later)
- pip (Python package manager)

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hibakhalidm/SheConnects.git
   cd she-connects
   ```

2. **Frontend Setup**:
   ```bash
   cd frontend
   npm install
   ```

3. **Backend Setup**:
   ```bash
   cd ../backend
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

## Running the Application

1. **Start the Frontend**:
   ```bash
   cd frontend
   npm start
   ```

2. **Start the Backend**:
   ```bash
   cd ../backend
   flask run
   ```

3. **Run Both Simultaneously**:
   From the root directory:
   ```bash
   npm run start:dev
   ```

## Technologies Used

- **Frontend**:
  - React
  - Material-UI
  - Axios

- **Backend**:
  - Flask
  - Flask-CORS
  - spaCy
  - TextBlob

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
