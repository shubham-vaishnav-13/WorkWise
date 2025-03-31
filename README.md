# 🚀 WorkWise - Home Services Marketplace

WorkWise is a **comprehensive online platform** that connects users with **trusted professionals** for a wide range of **home services**. The platform facilitates **easy service booking**, **secure payments**, and a **seamless user experience**. 🏡✨

---

## 🌟 Features

### 🔐 User Authentication
- ✅ **Traditional Login/Registration:** Email-based user registration with password validation.
- 🔗 **Google Authentication:** Sign in using Google account integration.
- 📧 **Email Verification:** Account activation through email verification links.
- 🔒 **Password Security:** Enforces strong password requirements with validation.

### 🔍 Service Browsing
- 📂 **Category-Based Services:** Browse services by categories (Plumber, Electrician, Carpenter, etc.).
- 📜 **Service Details:** View comprehensive information including:
  - 🏷️ Service title and description
  - 💰 Pricing information
  - ⏳ Service duration
  - 👨‍🔧 Service provider details
  - ⭐ User ratings and reviews
- 🛠️ **Search Functionality:** Easily find specific services using keywords.

### 🛒 Shopping Cart
- ➕ **Add/Remove Services:** Add services to the cart with a single click.
- 🔄 **Quantity Adjustment:** Increase or decrease service quantities.
- 🗂️ **Cart Management:** View all selected services with details.
- 🧮 **Price Calculation:** Automatic calculation of the total price.

### ✅ Checkout Process
- 📝 **Service Review:** Review selected services before proceeding.
- 📍 **Address Information:** Enter delivery/service address details.
- 📦 **Order Summary:** View a complete order summary before payment.
- 💳 **Secure Payment:** Integrated with **Razorpay** payment gateway.

### 👤 User Profile
- 🏠 **Personal Information:** Manage personal details and addresses.
- 📜 **Order History:** View all past orders with their status.
- 💵 **Payment Status:** Track payment status for each order.

### 💳 Payment Integration
- 🏦 **Razorpay Gateway:** Secure payment processing.
- ✅ **Payment Verification:** Server-side verification of payment status.
- 🎉 **Order Confirmation:** Immediate confirmation after successful payment.

### 📱 Responsive Design
- 📲 **Mobile-Friendly:** Fully responsive design works on all devices.
- 🎨 **Tailwind CSS:** Modern, clean user interface.
- 🔀 **Intuitive Navigation:** Easy-to-use interface for a seamless experience.

---

## ⚙️ Admin Features
- 🛠️ **Service Management:** Add, edit, and remove services.
- 📂 **Category Management:** Organize services into categories.
- 📦 **Order Management:** View and process customer orders.
- 👥 **User Management:** Manage user accounts and permissions.

---

## 🏗️ Technical Stack
- 🖥️ **Backend:** Django (Python web framework)
- 🎨 **Frontend:** HTML, Tailwind CSS, JavaScript
- 🗄️ **Database:** SQLite (development), configurable for **PostgreSQL** in production
- 🔑 **Authentication:** Django authentication system with social auth integration
- 💳 **Payment Processing:** Razorpay API integration
- 📂 **File Storage:** Django file storage for service images

---

## 🔒 Security Measures
- 🔐 **Password Encryption:** Secure storage of user credentials.
- 💳 **Payment Security:** Razorpay's built-in security mechanisms.
- 🚧 **Data Protection:** Role-based access control (**RBAC**) to prevent unauthorized access.

---

## ⚡ Setup Instructions

1. **Clone the repository:**  
   ```sh
   git clone https://github.com/your-repo/workwise.git
   cd workwise
   ```
2. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure environment variables:**  
   Create a `.venv` file and add credentials for **email, Razorpay, and database settings**.
4. **Run database migrations:**  
   ```sh
   python manage.py migrate
   ```
5. **Create a superuser for admin access:**  
   ```sh
   python manage.py createsuperuser
   ```
6. **Start the development server:**  
   ```sh
   python manage.py runserver
   ```

---

## 🔄 User Flow
1. 📝 Register or log in to your account.
2. 🔍 Browse available services by category.
3. 🛒 Add desired services to your cart.
4. ✅ Proceed to checkout and enter delivery details.
5. 💳 Complete payment through the Razorpay gateway.
6. 🎉 Receive order confirmation.
7. 📦 Track order status in your profile.

---

## 🚀 Future Enhancements
- 📍 **Real-time Order Tracking**
- 💬 **Chat Support for Customers and Service Providers**
- 🏆 **Subscription-Based Service Plans**

---

**WorkWise** aims to provide a **hassle-free experience** for booking home services, connecting customers with skilled professionals while ensuring **quality service and customer satisfaction**. 🏡💼✨
