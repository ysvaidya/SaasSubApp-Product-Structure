# 📦 SaaS SubApp – Product Structure

## 📌 Overview

The **Product App** is a modular and scalable backend component designed for a SaaS-based Inventory & Sales Management System.

It provides structured product management functionality including:

- Product creation and updates
- SKU management
- Soft deletion logic
- Stock validation rules
- Service-layer based architecture
- API-ready structure for scalable integration

This module follows clean backend architecture principles and separates concerns using a service layer.

---

## 🏗️ Architecture Design

The app is structured using a layered approach:

```
Product App
│
├── models.py        → Database schema
├── services/        → Business logic layer
├── serializers/     → Data validation layer
├── views/           → API endpoints
└── urls.py          → Route definitions
```

### Design Principles Used

- Separation of Concerns
- Service Layer Pattern
- Clean API Validation via Serializers
- Soft Delete Implementation
- Business Rule Enforcement at Service Level

---

## ⚙️ Core Features

### 1️⃣ Product Management
- Create products with SKU and stock tracking
- Update product details
- Prevent invalid state transitions

### 2️⃣ Soft Delete System
Instead of permanently deleting records:
- Products are marked as `is_deleted = True`
- Deletion blocked if stock exists
- Prevents accidental data loss

### 3️⃣ Stock Validation Rules
- Products with remaining stock cannot be deleted
- Business logic handled in service layer
- Validation errors raised properly

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite (development)
- Git (Version Control)

---

## 🚀 Setup Instructions

### Clone Repository

```bash
git clone https://github.com/ysvaidya/SaasSubApp-Product-Structure.git
cd SaasSubApp-Product-Structure
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

---

## 📂 Business Logic Philosophy

All critical logic is implemented inside the **service layer**, not directly in views.

This ensures:

- Better maintainability
- Easier testing
- Clear separation between HTTP logic and business rules
- Production-ready structure

---

## 📘 Author

Yash Vaidya  
Backend Developer | Django | SaaS Architecture | AI Systems
