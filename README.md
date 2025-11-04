Offensive Darija Detection
A Django-based web application to detect offensive/toxic language in Darija (Moroccan Arabic dialect) using a BERT model.

Overview
This project implements a blog platform with integrated AI-powered toxicity detection for user comments and articles written in Darija. Leveraging the HuggingFace BERT model, it automatically identifies abusive content and assists administrators in moderating discussions.

Features
Blog System: Users can register, log in, and publish articles.

Comment Moderation: Comments posted on articles are automatically scanned for offensiveness. Toxic comments are flagged and require admin approval.

AI Toxicity Detection: Integrates HuggingFace’s Abdelaaziz/toxic-darija-bert-classification model to classify and filter toxic Darija text.

Admin Tools: Administrators can review, approve, or delete flagged comments.

Media and Static Content: Supports article images and a Bootstrap-based user interface.

Tech Stack
Backend: Django (Python)

AI Model: HuggingFace API for BERT-based Darija toxicity detection

Database: SQLite (default)

Frontend: Bootstrap, HTML templates

Utilities: REST API integration via requests in Python

Project Structure
login/ — Contains authentication, blog, and comment logic

media/ — Stores uploaded images

projet_blog/ — Django project settings and configuration

static/ — Static files (CSS, JS, images)

templates/ — HTML files, UI templates

utils/toxic_filter.py — Toxicity detection API calls and logic

How It Works
Users publish articles and post comments.

Each comment is automatically submitted to the HuggingFace API, which returns a toxicity score.

Offensive comments are flagged, showing a warning message to users and remaining hidden unless approved by an admin.

Administrators can log in to moderate the flagged content and manage articles.

Installation and Setup
Clone this repository.

Install required dependencies:

bash
pip install -r requirements.txt
Create and configure your .env file with your HuggingFace API key.

Run migrations:

bash
python manage.py migrate
Start the development server:

bash
python manage.py runserver
Model Reference
HuggingFace Model: Abdelaaziz/toxic-darija-bert-classification
