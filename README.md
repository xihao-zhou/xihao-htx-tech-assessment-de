# HTX xCode Technical Assessment - Data

## 🧾 Overview

This repository provides a simple Python-based Command-line interface (CLI) application for analyzing and querying mock international passenger flight data.

It contains four core analytics functionalities:
1. **Monthly Unique Flight Count** – Calculates the number of unique flights operated in each month.
2. **Frequent Flyer Analysis** – Identifies the top passengers by number of flights taken.
3. **Longest Non-SG Travel Run** – Determines, for each passenger, the longest continuous sequence of flights without returning to Singapore.
4. **Travel Pair Detection** – Finds pairs of passengers who have flown together more than a user-specified number of times, with optional date range filtering.

### 🧰 Features

- ✅ Intuitive CLI for running all analyses 
- ✅ Supports user input for flexible companion analysis (number of flights, date range)  
- ✅ Mock data uses realistic, chronologically-linked flight and passenger data  
- ✅ Uses pandas for efficient, reliable data wrangling

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