# E-Commerce Django Project

A full-featured Django-based e-commerce application for browsing products, managing a shopping cart, creating wishlists, placing orders, and supporting seller-specific workflows.

This project is currently in active development and already includes core e-commerce functionality with a clean Bootstrap-based interface, custom user roles, and order management.

---

## 1. Project Overview

This repository contains a Django e-commerce platform with multiple apps for:

- Product catalog and search
- User authentication and profile management
- Seller approval and seller-specific product controls
- Wishlist and cart management
- Checkout and order placement
- Order tracking and seller status updates

The application is designed with a modular structure, making it easy to extend as the project grows.

---

## 2. Key Features

### Customer Features
- Browse products from the home page
- Search products by name
- Filter products by category and sub-category
- View detailed product pages
- Add products to wishlist
- Add products to cart
- Increase or decrease cart quantity
- Apply a coupon code during cart flow
- Checkout with payment method selection
- View placed orders
- Track order status

### Seller Features
- Register as a seller
- Approve seller access through custom user flags
- Add new products
- Edit existing products
- Delete products owned by the seller
- View and manage customer orders related to their products
- Update order status for fulfillment tracking

### User & Account Features
- Custom user model with profile information
- Signup and seller signup forms
- Profile viewing, editing, and deletion
- Password change support
- Login/logout integration with Django auth

---

## 3. Tech Stack

### Core Technologies
- Python 3
- Django 6.0.4
- SQLite (default development database)

### UI / Frontend
- Bootstrap 5
- Bootstrap Icons
- Custom CSS in static/css/style.css
- Django templates

### Supporting Libraries
- crispy-forms
- crispy-bootstrap5
- Pillow (for image upload handling)

### Development Tools
- Django Admin
- Python virtual environment
- Git and GitHub workflow

---

## 4. Current Project Structure

```text
D:\Project\ecommerce
├── .env
├── .gitignore
├── reqirements.txt
├── django_project/
│   ├── accounts/
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── migrations/
│   │   └── templates/
│   ├── commerce/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   └── migrations/
│   ├── orders/
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   └── migrations/
│   ├── product/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   └── migrations/
│   ├── users/
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   ├── templates/
│   │   ├── base.html
│   │   ├── decorator/
│   │   └── registration/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── media/
│   │   └── product_images/
│   ├── django_project/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── db.sqlite3
│   └── manage.py
└── .venv/
```

---

## 5. App Responsibilities

### accounts
Handles authentication, user registration, profile management, seller approval status, password changes, and custom user fields such as:
- age
- gender
- mobile number
- address information
- category and sub-category preferences

### product
Manages the product catalog:
- product listing
- search and filters
- product details
- seller product creation
- update and deletion
- discount and actual price calculation

### commerce
Controls the shopping experience:
- wishlist
- cart
- quantity management
- coupon application
- checkout and order creation

### orders
Handles order lifecycle and fulfillment:
- viewing orders
- tracking order items
- seller status updates
- order visibility for sellers

### users
Provides dashboard-style views for user-specific sections and account interaction.

---

## 6. Main Functional Flow

### Customer Journey
1. User visits the homepage and browses products.
2. User can search or filter products.
3. User adds desired products to the cart or wishlist.
4. User proceeds to checkout.
5. Order is created and appears in the user’s order history.
6. User can track the status of the order.

### Seller Journey
1. Seller signs up and is marked as an approved seller.
2. Seller creates products for sale.
3. Orders for their products are visible in the seller dashboard.
4. Seller updates order status as the order moves through fulfillment.

---

## 7. Installation & Setup

### Prerequisites
- Python 3.10+
- pip
- virtual environment support

### Steps

1. Clone the repository
   ```bash
   git clone <your-repo-url>
   cd ecommerce
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r reqirements.txt
   ```

4. Navigate to the Django project folder
   ```bash
   cd django_project
   ```

5. Apply database migrations
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server
   ```bash
   python manage.py runserver
   ```

8. Open the application in your browser
   ```text
   http://127.0.0.1:8000/
   ```

---

## 8. Environment Notes

- The project currently uses SQLite for local development.
- Media files are stored in the media/product_images folder.
- Static files are managed from the django_project/static directory.
- The application uses Django’s built-in authentication system and a custom user model.

---

## 9. Current Status

This project is already functional for the following areas:
- product browsing and search
- seller product management
- cart and wishlist logic
- checkout and order placement
- order status tracking

It is still an ongoing project, and future improvements can include:
- payment gateway integration
- real email verification
- advanced filters and sorting
- inventory validation
- analytics dashboards
- admin reports
- responsive enhancements

---

## 10. Suggested Next Improvements

To take this project to the next level, the following enhancements are recommended:

- Add real payment integration (Stripe / PayPal / SSLCommerz)
- Add review and rating system for products
- Add inventory stock validation before checkout
- Improve search with advanced filters
- Add order history analytics for sellers and buyers
- Add email notifications for order updates
- Improve security for production deployment
- Add deployment support for Azure / Render / Railway / Vercel

---

## 11. Summary

This repository is a solid Django e-commerce project with:
- a modern modular app structure
- custom seller and buyer workflows
- product and order management
- Bootstrap-based frontend
- flexible extension points for future enhancements

It is a strong foundation for building a production-grade online shopping platform.

---

## 12. Quick Start Command Reference

```bash
cd D:\Project\ecommerce
python -m venv .venv
.\.venv\Scripts\activate
pip install -r reqirements.txt
cd django_project
python manage.py migrate
python manage.py runserver
```

If you want, I can also help you improve this README further with screenshots, badges, deployment instructions, or a professional project summary section.
