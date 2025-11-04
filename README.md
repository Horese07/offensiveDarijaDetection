
# 🧠 Offensive Darija Detection

*A Django-based web application for detecting offensive or toxic language in Darija (Moroccan Arabic dialect) using BERT.*

---

## 📘 Overview

**Offensive Darija Detection** is an AI-powered web platform that combines **natural language processing** and **content moderation** within a blog system.
Built on **Django** and leveraging a **BERT model fine-tuned for Darija**, it automatically identifies toxic or abusive expressions in user-generated content — helping moderators keep discussions safe and respectful.

---

## 🚀 Key Features

* 📝 **Blog Platform** — Users can register, create, and publish articles.
* 💬 **Comment Moderation** — Every comment is automatically analyzed for offensiveness. Toxic comments are flagged before publication.
* 🤖 **AI Toxicity Detection** — Integrates the **[`Abdelaaziz/toxic-darija-bert-classification`](https://huggingface.co/Abdelaaziz/toxic-darija-bert-classification)** model from HuggingFace.
* 🔒 **Admin Control Panel** — Admins can review, approve, or delete flagged comments and manage articles.
* 🖼️ **Media & UI** — Supports article images and provides a responsive **Bootstrap-based interface**.

---

## 🧩 Tech Stack

| Layer           | Technology                                     |
| :-------------- | :--------------------------------------------- |
| **Backend**     | Django (Python)                                |
| **AI Model**    | HuggingFace BERT for Darija Toxicity Detection |
| **Database**    | SQLite (default)                               |
| **Frontend**    | HTML • Bootstrap • CSS                         |
| **Integration** | HuggingFace API via `requests`                 |
| **Environment** | `.env` configuration for API keys and secrets  |

---

## 🏗️ Project Structure

```
OffensiveDarijaDetection/
│
├── login/                # Authentication, blog, and comment logic
├── media/                # Uploaded article images
├── projet_blog/          # Main Django project settings
├── static/               # CSS, JS, and image files
├── templates/            # HTML templates and UI pages
├── utils/
│   └── toxic_filter.py   # HuggingFace API integration and toxicity logic
│
└── requirements.txt
```

---

## ⚙️ How It Works

1. Users publish an article and post comments.
2. Each comment is sent to the **HuggingFace API**, which returns a **toxicity score**.
3. If the score exceeds a threshold, the comment is **flagged** and hidden pending admin approval.
4. Administrators can **approve, edit, or delete** flagged content directly from the Django admin panel.

---

## 🧠 Model Reference

* **Model Name:** [`Abdelaaziz/toxic-darija-bert-classification`](https://huggingface.co/Abdelaaziz/toxic-darija-bert-classification)
* **Architecture:** BERT-based text classification
* **Goal:** Detect and classify toxic or offensive expressions in Moroccan Arabic (Darija).

---

## 🧰 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/offensive-darija-detection.git
cd offensive-darija-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root and add your HuggingFace API key:

```
HUGGINGFACE_API_KEY=your_api_key_here
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Then visit:
👉 [http://localhost:8000](http://localhost:8000)

---

## 🧑‍💻 Example Use Case

> **Scenario:** A user posts a comment containing a potentially offensive phrase in Darija.
>
> * The app automatically sends the comment text to the BERT model.
> * If it’s detected as toxic, the comment is flagged and hidden.
> * The admin receives a notification and decides whether to approve or delete it.

---

## 📈 Future Improvements

* Add multilingual support (Arabic, French).
* Implement real-time moderation with WebSockets.
* Include visual analytics dashboards for toxicity reports.
* Expand dataset and fine-tune model for better accuracy.

---

## 🧑‍🤝‍🧑 Contributors

| Name                  | Role                       |
| --------------------- | -------------------------- |
| **Elhoucine Lachgar** | Developer / AI Integration |
| **[Your Teammates]**  | Backend & UI Design        |

---

## 📜 License

This project is distributed under the **MIT License**.

