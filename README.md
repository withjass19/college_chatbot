# 🎓 NLP-Based College Inquiry Chatbot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" />
  <img src="https://img.shields.io/badge/Flask-Backend-green" />
  <img src="https://img.shields.io/badge/NLP-ChatterBot-orange" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
</p>

## 📌 Overview

An **NLP-based intelligent chatbot** that automates student inquiries in a college environment. It delivers instant answers for admissions, courses, fees, exams, and more.

> 🔀 **Hybrid Approach**: Rule-based menu navigation + NLP similarity matching

---

## ❗ Problem

* Repetitive student queries overwhelm staff
* Slow/manual responses
* Limited support hours
* Hard-to-navigate websites

## 💡 Solution

A chatbot that:

* Understands queries using NLP
* Provides **instant responses (24/7)**
* Reduces administrative workload
* Improves student experience

---

## 🚀 Features

* 💬 Automated query handling
* 📋 Menu-driven FAQ system
* 🧠 NLP-based response generation (BestMatch)
* ⚡ Real-time responses
* 🕐 24/7 availability
* 📝 Query submission form

---

## 🛠️ Tech Stack

**Backend:** Python, Flask, ChatterBot
**Frontend:** HTML, CSS, JavaScript
**Data:** JSON (intents & menu)

---

## 🧠 How It Works

1. User sends a message from UI
2. Flask API receives the request
3. System checks:

   * Menu navigation (if option clicked)
   * Else → NLP similarity matching
4. ChatterBot computes similarity (BestMatch)
5. Best response returned

---

## 🏗️ Architecture

```
User → Frontend → Flask API → NLP Engine (ChatterBot)
                         ↓
                 JSON Knowledge Base
                         ↓
                     Response
```

---

## 📂 Project Structure

```
project/
│── data/
│   ├── intents.json
│   ├── menu.json
│
│── templates/
│   └── index.html
│
│── static/
│   ├── style.css
│   ├── main.js
│
│── run.py
│── README.md
```

---

## 📊 Dataset

Custom **JSON dataset** with:

* **Intents** → categories
* **Patterns** → user inputs
* **Responses** → bot replies

Example:

```json
{
  "tag": "fee_structure",
  "patterns": ["What is fee?", "Tell me fees"],
  "responses": ["Fee depends on course..."]
}
```

---

## 🤖 Model / Approach

This project **does NOT use traditional ML/DL models**.

It uses:

* NLP (Natural Language Processing)
* Similarity-based matching
* ChatterBot **BestMatch algorithm**

> 🧠 *Rule-based intelligent system enhanced with NLP*

---

## 📈 Comparison of Approaches

| Approach      | Used | Accuracy  | Complexity |
| ------------- | ---- | --------- | ---------- |
| Rule-Based    | ✅    | Medium    | Low        |
| ML Models     | ❌    | High      | Medium     |
| Deep Learning | ❌    | Very High | High       |

---

## ⚙️ Installation & Setup

```bash
git clone <repo-link>
cd project
pip install flask chatterbot chatterbot_corpus
python run.py
```

Open: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🖼️ Screenshots (Add yours)

```
/screenshots/chat-ui.png
```

---

## 📚 What I Learned

* Building REST APIs using Flask
* NLP basics & similarity matching
* Designing chatbot architecture
* Working with JSON datasets

---

## ⚠️ Limitations

* Limited to predefined dataset
* No deep learning
* Limited context understanding
* No voice support

---

## 🔮 Future Enhancements

* Deep Learning models (BERT, LSTM)
* Voice-based chatbot
* Real-time database integration
* Mobile app support
* Multilingual support

---

## 👨‍💻 Author

**Jaspreet Singh**
M.Sc. IT (Data Analytics)
Panjab University

---

## ⭐ Contribution

Feel free to fork, improve, and contribute.

---

## 📜 License

Educational purposes only.
