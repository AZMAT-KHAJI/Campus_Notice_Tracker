# 📢 Campus Notice Tracker

> A centralized web platform for distributing campus notices and announcements - replacing scattered emails, posters, and WhatsApp messages with one clean digital hub.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🧩 About the Project

**Campus Notice Tracker** is a web-based application built to solve a real problem faced by students and faculty — the chaos of scattered announcements. Whether it's an exam schedule update, a holiday notice, or an event reminder, important information often gets lost across different channels.

This platform provides a **single, organized digital space** where:
- **Administrators** can post, manage, and categorize notices.
- **Students** can browse, search, and stay updated without switching between apps.

---

## ✨ Features

- 🔐 **User Authentication** — Secure login and registration for students and admins
- 📋 **Notice Board** — View all published notices in one place
- ✍️ **Admin Panel** — Create, edit, and delete notices with ease
- 🗂️ **Category-based Filtering** — Organize notices by type (Exam, Event, Holiday, General, etc.)
- 📅 **Date & Time Stamps** — Every notice shows when it was posted
- 📱 **Responsive Design** — Works seamlessly on desktop and mobile browsers
- 🔍 **Search Functionality** — Quickly find notices by keyword

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Django |
| Frontend | HTML5, CSS3 |
| Database | SQLite (default) |
| Admin | Django Admin Panel |
| Templating | Django Template Language (DTL) |

---

## 📁 Project Structure

```
Campus_Notice_Tracker/
│
├── config/                  # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── notices/                 # Core app — notices logic
│   ├── migrations/
│   ├── templates/
│   │   └── notices/
│   ├── models.py            # Notice data models
│   ├── views.py             # Request handling & rendering
│   ├── urls.py              # App-level URL routing
│   └── admin.py             # Admin configuration
│
├── static/
│   └── css/                 # Custom stylesheets
│
├── manage.py                # Django management utility
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/AZMAT-KHAJI/Campus_Notice_Tracker.git
   cd Campus_Notice_Tracker
   ```

2. **Create and activate a virtual environment**

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   > If `requirements.txt` is not present, install Django manually:
   > ```bash
   > pip install django
   > ```

4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Open in browser**

   ```
   http://127.0.0.1:8000/
   ```

   Admin panel:
   ```
   http://127.0.0.1:8000/admin/
   ```

---

## 📖 Usage

### For Administrators
1. Log in to the Django admin panel at `/admin/`
2. Navigate to **Notices** and click **Add Notice**
3. Fill in the title, content, category, and publication date
4. Save — the notice will appear live on the platform immediately

### For Students
1. Visit the homepage to see all published notices
2. Use the search bar or category filters to find relevant announcements
3. Click on any notice to read its full content

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add: your feature description"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please ensure your code follows Django best practices and is well-commented.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 📬 Developer

**Azmat Khaji**  
GitHub: [@AZMAT-KHAJI](https://github.com/AZMAT-KHAJI)

---
