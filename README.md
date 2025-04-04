# EasyPay Hub API Documentation

Introduction

EasyPay Hub is a Django-based RESTful API that acts as a third-party payment gateway for online transactions. It enables merchants to securely process payments, verify transactions, and update payment statuses in real time. The system ensures seamless integration with shopping applications, providing a robust, scalable, and efficient payment processing solution.

Why Use EasyPay Hub?

Seamless Payment Integration: Helps businesses process online transactions securely and efficiently.

Real-time Updates: Ensures merchants and customers receive immediate transaction status updates.

Security & Authentication: Uses Django's authentication system for secure API access.

Scalability: Built with Django REST Framework (DRF), allowing easy scaling for high transaction volumes.

Merchant & Transaction Management: Provides structured data storage and tracking of all transactions.

Customizable & Extendable: Can be enhanced with additional features like fraud detection, multiple payment options, and analytics.

Technologies Used

Programming Language: Python

Framework: Django, Django REST Framework (DRF)

Database: MySQL

Authentication: Django's built-in authentication (username/password-based)

API Testing: Postman

Version Control: Git, GitHub

Deployment: AWS (optional for cloud hosting)

Challenges Overcome by EasyPay Hub

Traditional Payment Processing Complexity: Simplifies online payment handling for merchants.

Lack of Transaction Transparency: Provides detailed transaction tracking and status updates.

Security Concerns: Implements authentication and secure data storage mechanisms.

Scalability Issues: Supports multiple merchants and transactions simultaneously.

High Integration Costs: Offers a cost-effective, open-source payment gateway alternative.

Advantages

Efficient Payment Processing: Streamlined transaction handling.

Enhanced Security: Uses authentication and secure database practices.

Real-time Transaction Status: Merchants can track payments instantly.

Customizable API Endpoints: Allows businesses to tailor payment flows.

Open-Source & Cost-Effective: Avoids expensive third-party payment gateway fees.

Easy Integration: Works seamlessly with existing shopping platforms.

Features

Merchant Management

Register merchants

Track transactions linked to merchants

Transaction Processing

Initiate payments

Verify payment status

Update transactions

Secure Authentication

Username and password-based authentication for API access

Database Storage

Merchant Table: Stores merchant and transaction details

Transaction Table: Tracks payment history and status

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Django (>=4.0)
- Django REST Framework

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/easypay_hub.git
   cd easypay_hub
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for authentication:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### Authentication
The API uses **Basic Authentication**. Include the following header in your requests:
```
Authorization: Basic <base64_encoded_username:password>
Content-Type: application/json
```

---

### Merchant API

#### 1. List All Merchants
**GET** `/api/merchants/`

#### 2. Create a Merchant
**POST** `/api/merchants/`
```json
{
  "name": "Merchant A",
  "status": "Active"
}
```

#### 3. Retrieve a Merchant
**GET** `/api/merchants/{mid}/`

#### 4. Update a Merchant
**PUT** `/api/merchants/{mid}/`

#### 5. Delete a Merchant
**DELETE** `/api/merchants/{mid}/`

---

### Transaction API

#### 1. List All Transactions
**GET** `/api/transactions/`

#### 2. Create a Transaction
**POST** `/api/transactions/`
```json
{
  "merchant": 1,
  "product_name": "Laptop",
  "product_cost": 1500.00,
  "status": "Pending"
}
```

#### 3. Retrieve a Transaction
**GET** `/api/transactions/{transaction_id}/`

#### 4. Update a Transaction
**PUT** `/api/transactions/{transaction_id}/`

#### 5. Delete a Transaction
**DELETE** `/api/transactions/{transaction_id}/`

---

### Payment API

#### 1. Initiate Payment
**POST** `/api/initiate-payment/`
```json
{
  "merchant_name": "Merchant A",
  "product_name": "Smartphone",
  "product_cost": 999.99
}
```

#### 2. Verify Payment
**POST** `/api/verify-payment/`
```json
{
  "transaction_id": 1
}
```

#### 3. Payment Webhook (Real-time Updates)
**POST** `/api/payment-webhook/`
```json
{
  "transaction_id": 1,
  "status": "Completed"
}
```

---

## Testing the API

### Using `cURL`
#### Initiate Payment
```bash
curl -X POST http://127.0.0.1:8000/api/initiate-payment/ \
  -H "Authorization: Basic <base64_encoded_username:password>" \
  -H "Content-Type: application/json" \
  -d '{"merchant_name": "Merchant A", "product_name": "Smartphone", "product_cost": 999.99}'
```

### Using Postman
1. Open Postman.
2. Set the request type to **POST**.
3. Enter the API URL (e.g., `http://127.0.0.1:8000/api/initiate-payment/`).
4. In **Authorization**, select `Basic Auth` and enter your username and password.
5. In **Headers**, add:
   ```
   Content-Type: application/json
   ```
6. In **Body**, select `raw` and enter the JSON payload.
7. Click **Send**.

---

## Logging
All API calls and errors are logged for debugging purposes. Logs are stored in:
```
/logs/easypay.log
```

---

## Conclusion
This API provides secure and efficient payment processing for merchants. Future improvements can include JWT authentication, enhanced security, and third-party payment gateway integrations.



