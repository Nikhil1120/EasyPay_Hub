# EasyPay_Hub
## Problem Statement
In modern e-commerce, multiple shopping applications require seamless and secure payment processing. However, integrating multiple payment gateways directly into each shopping app can be complex, time-consuming, and expensive. Additionally, merchants need a streamlined way to track transactions and manage their sales efficiently.

## Solution: EasyPay HUB
**EasyPay HUB** is a third-party payment gateway that acts as a bridge between shopping apps and payment processing. It simplifies the payment process by allowing merchants to register and process transactions securely through a centralized system. The platform maintains two core tables:
- **Merchant Table**: Stores merchant details and records the purchases made.
- **Transaction Table**: Keeps track of transaction details, including product name, timestamp, status, and cost.

## Problems Overcome by EasyPay HUB
1. **Simplified Payment Integration**: Shopping apps no longer need to build individual payment solutions; they can integrate EasyPay HUB for seamless transactions.
2. **Centralized Transaction Management**: Merchants can track their transactions in one place, reducing complexity.
3. **Improved Security & Reliability**: Transactions are stored in a structured database with status tracking to prevent fraud or errors.
4. **Real-time Transaction Updates**: The system records transaction statuses and amounts in real-time, ensuring transparency.
5. **Scalability**: EasyPay HUB can be used by multiple merchants without affecting performance, making it a scalable solution.

## Advantages of EasyPay HUB
✔ **Efficient Payment Processing** – Automates transaction recording and merchant payments.
✔ **Cost-Effective** – Reduces the need for shopping apps to develop custom payment gateways.
✔ **Easy Integration** – RESTful API ensures seamless integration with various shopping apps.
✔ **Secure & Reliable** – Reduces transaction failures and provides clear transaction history.
✔ **Merchant-Friendly** – Allows merchants to focus on business growth instead of payment complexities.

---

## Installation
### **1. Clone the Repository:**
```
git clone https://github.com/yourusername/easypay-hub.git
cd easypay-hub
```

### **2. Set Up a Virtual Environment:**
```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

```

### **3. Install Dependencies:** 
```
pip install -r requirements.txt

```

### **4. Apply Migrations:**
```python
python manage.py makemigrations
python manage.py migrate

```

### **5. Run the Development Server:**
```python
python manage.py runserver

```


## API Endpoints
1. **Merchant Endpoints:** – GET /merchants/: List all merchants.
 - POST /merchants/: Create a new merchant.
 - GET /merchants/{id}/: Retrieve a specific merchant.
 - PUT /merchants/{id}/: Update a merchant's details.
 - DELETE /merchants/{id}/: Delete a merchant.

2. **Transaction Endpoints:** – GET /transactions/: List all transactions.
 - POST /transactions/: Create a new transaction.
 - GET /transactions/{id}/: Retrieve a specific transaction.
 - PUT /transactions/{id}/: Update a transaction's details.
 - DELETE /transactions/{id}/: Delete a transaction.
4. **Transaction Status Endpoint:t** – GET /transaction-status/{transaction_id}/: Retrieve the status of a specific transaction.

## Testing with Postman
--To ensure the API functions as expected, you can use Postman, a popular API testing tool.
1. **Install Postman:**  Download and install Postman from the official website.
2. **Import the API Collection:** - Open Postman and click on the "Import" button.
   - Import the provided Postman collection file (EasyPay_HUB.postman_collection.json) located in the repository.
3. **Set Up Environment:** - Create a new environment in Postman with the following variable:
 - base_url: Set this to http://127.0.0.1:8000/ or your deployed API URL.
4. **Testing Endpoints:** -Use the imported collection to test various endpoints.
 - Ensure to provide necessary headers and body data as required by each endpoint.
