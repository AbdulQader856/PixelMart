# 🎮 **PixelMart - Game E-Commerce Platform**  

PixelMart is a **fully functional e-commerce website** for purchasing games online. Built with **Django, PostgreSQL, Stripe payments, and Bootstrap**, it provides a seamless shopping experience with **cart functionality, checkout, and order tracking**.  

---

## 📌 **Features**  

✅ **Game Listings & Categories** (Latest Releases, Top Selling, Upcoming)  
✅ **Game Detail Pages** with images, pricing, and descriptions  
✅ **Shopping Cart** with add/remove functionality  
✅ **Secure Checkout with Stripe** 💳  
✅ **Order History & User Authentication**  
✅ **Admin Dashboard** for managing games & orders  
✅ **Modern UI with Bootstrap 5** 🎨  
✅ **Optimized Performance & Security**

---

## 🛠️ **Tech Stack**

### **Backend:**  
- **Django** (Python Web Framework)  
- **PostgreSQL** (Relational Database)  
- **Stripe API** (Payment Integration)  

### **Frontend:**  
- **Bootstrap 5** (Responsive UI)  
- **HTML, CSS, JavaScript**  

### **Other Tools:**  
- **Gunicorn & Whitenoise** (Static file management & production readiness)  
- **Django Admin Panel** (For managing games & orders)  

---

## 📂 **Project Structure**  

```
PixelMart/
│── store/               # Main Django app
│   ├── migrations/      # Database migrations
│   ├── templates/store/ # HTML templates
│   ├── static/          # Static files (CSS, JS, Images)
│   ├── views.py         # Business logic
│   ├── models.py        # Database models
│   ├── urls.py          # URL routing
│   ├── admin.py         # Admin configurations
│
│── PixelMart/           # Django project settings
│   ├── settings.py      # Project settings
│   ├── urls.py          # Main URL configuration
│   ├── wsgi.py          # WSGI application for deployment
│
│── media/               # Uploaded images
│── staticfiles/         # Collected static files for deployment
│── db.sqlite3           # Database (if using SQLite for testing)
│── requirements.txt     # Python dependencies
│── manage.py            # Django management tool
```

---

## 🚀 **Installation**  

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/AbdulQader856/PixelMart.git
cd PixelMart
```

### 2️⃣ **Set Up a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 4️⃣ **Configure the Database (PostgreSQL)**  
Ensure **PostgreSQL is installed and running**. Update your `settings.py` with your database credentials:  
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pixelmart_db',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Apply migrations:  
```bash
python manage.py makemigrations store
python manage.py migrate
```

### 5️⃣ **Create a Superuser**  
```bash
python manage.py createsuperuser
```

### 6️⃣ **Run the Server**  
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** 🚀  

---

## 🤝 **Contributing**  
Contributions are welcome! If you'd like to improve **PixelMart**, follow these steps:  

1. **Fork the repository**  
2. **Create a feature branch** (`git checkout -b new-feature`)  
3. **Commit your changes** (`git commit -m "Added new feature"`)  
4. **Push to your fork** (`git push origin new-feature`)  
5. **Submit a Pull Request**  

---

## 📩 **Author**
### **Abdul Qader Kagzi**


🔗 **Connect with me:**
- 📧 **Email:** abdulqaderkagzi@gmail.com
- 🐙 **GitHub:** [github.com/AbdulQader856](https://github.com/AbdulQader856)

---

### **🌟 Star this repo if you found it useful!** ⭐🚀 