# HTX xCode Technical Assessment - Data

## 🧾 Overview

## 🛠 Prerequisites

Ensure you have the following installed:

- Python 3.10+
- Git

## 📦 Setup

1. **Clone or download the repo as zip file:**

   ```bash
   git clone https://github.com/xihao-zhou/xihao-htx-tech-assessment-de.git
   cd xihao-htx-tech-assessment-de
   ```

2. **Create and activate a virtual environment:**

   **Linux/MacOs**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate

   deactivate #command to deactivate virtual environment
   ```

   **Windows**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate

   deactivate #command to deactivate virtual environment
   ```
   
3. **Install dependencies:**
   
   **Linux/MacOs**
   ```bash
   pip3 install -r requirements.txt
   ```

   **Windows**
   ```bash
   pip install -r requirements.txt
   ```


## 🚀 Running the App

   **Linux/MacOs**
   ```bash
   python3 app/main.py
   ```
   
   **Windows**
   ```bash
   python .\app\main.py
   ```

## 📁 Project Struture

```plaintext
xihao-htx-tech-assessment-de/
├── app/
│   ├── __init__.py
│   ├── analysis.py
│   └── main.py
├── data/
│   ├── flightData.csv
│   └── passengers.csv
├── requirements.txt
└── README.md
```