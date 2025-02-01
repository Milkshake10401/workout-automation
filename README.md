# 🏋️ Workout Automation - Abhishek & Giselle

This repository automates workout logging using **Google Sheets** and is designed to integrate with a future **front-end dashboard on StarlightStrategies.io**. The goal is to streamline exercise tracking, reduce manual data entry, and provide valuable insights into workout progress.

## 🚀 Project Overview
### **Current Features**
- **Google Sheets Integration**: Automatically syncs exercises from the **Weekly Schedule** into the **Log Sheet** in the "Workout Tracker - Abhishek & Giselle".
- **Python Automation**: Uses `gspread` and `pandas` to pull and update workouts dynamically.
- **Cron Job Scheduling**: Allows daily automation without manual intervention.

### **Future Plans**
🔹 **Public Dashboard on StarlightStrategies.io**  
- A front-end UI to visualize workout progress.
- Personalized analytics & tracking for strength training and climbing.
- User authentication & multi-device support.

🔹 **Advanced Data Analytics**  
- AI-based performance insights & recovery recommendations.
- Periodization tracking for strength gains.
- Climbing grade progression analysis.

🔹 **Wearable Integration**  
- Potential integration with Apple Health, Fitbit, and Oura.
- Real-time biometrics tracking for workout optimization.

---

## 🛠️ Setup Instructions
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/workout-automation.git
cd workout-automation
```

### **2️⃣ Install Dependencies**
```bash
python3 -m venv venv
source venv/bin/activate  # (Mac/Linux)
pip install -r requirements.txt
```

### **3️⃣ Google Sheets API Setup**
1. Enable the [Google Sheets API](https://console.cloud.google.com/apis/library/sheets.googleapis.com).
2. Create a **Service Account** and download the `credentials.json` file.
3. Share your **Google Sheet** with the service account email.

### **4️⃣ Run the Automation**
```bash
python scripts/workout_sync.py
```

### **5️⃣ Automate with Cron (Mac/Linux)**
To schedule daily updates at 6 AM:
```bash
crontab -e
```
Add this line:
```
0 6 * * * /usr/bin/python3 /path/to/workout-automation/scripts/workout_sync.py
```

---

## 📈 Roadmap
- [x] Google Sheets integration
- [x] Automated daily workout sync
- [ ] **Front-end dashboard on StarlightStrategies.io**
- [ ] Data visualization (charts & graphs)
- [ ] Wearable & API integrations
- [ ] AI-based workout recommendations

---

## 📌 Contributing
🚀 If you're interested in contributing to this project, feel free to **submit pull requests** or **open issues**! Collaboration is welcome.

---

## 🛡️ License
This project is licensed under the **MIT License**.

---

## 👨‍💻 Maintainers
- **Abhishek Sriram**
- **Giselle Quevedo**
