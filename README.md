# Alx_Capstone_Project
# E-commerce Product API

This is a **Django REST Framework (DRF)** based API for managing users, products, and categories in an e-commerce system. It supports CRUD operations, product search, filtering, authentication, and error handling.

## Features

### **User Management**
- Users can create accounts
- Only authenticated users can modify user details.
- Admin users have full control over categories and product management.

### **Product Management**
- Users can create, update, and delete products.
- Products have attributes: **Name, Description, Price, Category, Stock Quantity, Image URL, and Created Date**.
- Users can filter and search for products.
- If a product is **out of stock**, an appropriate error message is returned.

### **Category Management**
- Categories are **predefined** and managed by admin users.
- Products must be assigned to an existing category.

### **Product Search & Filtering**
- Search for products by **name or category** (supports partial matches).
- Filter products by:
  - **Category**
  - **Price range**
  - **Stock availability**
- Supports **pagination** for better performance.

### **Error Handling**
- Returns appropriate HTTP status codes:
  - **404** when a product or category is not found.
  - **400** for bad requests (e.g., invalid data).
  - **403** for unauthorized access attempts.
- Custom error messages in JSON format for better API usability.

### **Authentication & Security**
- Implemented **user authentication** using Django’s built-in authentication system.
- Only authenticated users can manage products.

---

# Endpoints

## **User Endpoints**

| Method | Endpoint          | Description                |
|--------|------------------|----------------------------|
| GET    | `/api/users/`    | List all users            |
| POST   | `/api/users/`    | Create a new user         |
| GET    | `/api/users/{id}/` | Get user details        |
| PUT/PATCH/DELETE | `/api/users/{id}/` | Update/Delete a user |

## **Authentication Endpoints**

| Method | Endpoint          | Description               |
|--------|------------------|---------------------------|
| POST   | `/api/auth/login/`  | User login              |
| POST   | `/api/auth/register/` | User registration      |
| POST   | `/api/auth/logout/` | User logout            |

# *Example registration, login* 

# registration
{
    "username": "jack",
    "email": "jack@gmail.com",
    "password": "securepassword123"
}

# login
{
    "username": "jack",
    "password": "securepassword123"
}



## **Product Endpoints**

| Method | Endpoint          | Description                |
|--------|------------------|----------------------------|
| GET    | `/api/products/`  | List all products         |
| POST   | `/api/products/`  | Create a new product (Authenticated users) |
| GET    | `/api/products/{id}/` | Retrieve product details |
| PUT/PATCH/DELETE | `/api/products/{id}/` | Update/Delete a product (Authenticated users) |

# *Example product json body*
{
    "name": "Example Product",
    "description": "This is an example description of the product.",
    "price": 19.99,
    "category": 1, 
    "user": 2,
    "stock_quantity": 50,
    "image_url": "https://example.com/product-image.jpg",
    "created_at": "2025-04-08T10:00:00Z"
}



## **Category Endpoints**

| Method | Endpoint           | Description                 |
|--------|-------------------|-----------------------------|
| GET    | `/api/categories/` | List all categories        |
| POST   | `/api/categories/` | Create a new category (Admin only) |
| GET    | `/api/categories/{id}/` | Retrieve category details |
| PUT/PATCH/DELETE | `/api/categories/{id}/` | Update/Delete a category (Admin only) |

# *Example Category Json Body*
{
    "name": "Electronics",
    "description": "This is a description of the product.",
    "created_at": "2025-04-08T10:00:00Z"
}







