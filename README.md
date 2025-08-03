# 📚 Library Management System

## **🔐 Authentication Endpoints**

**These manage user registration, login, and JWT-based authentication.**

| **HTTP Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| POST | `/auth/register/` | Register a new user |
| POST | `/auth/login/` | Log in and obtain JWT token |
| POST | `/auth/logout/` | Log out the current user |
| POST | `/auth/token/refresh/` | Refresh an expired token |

## **🗂️ Category Endpoints**

Manage book categories like Fiction, Science, Biography, etc.

| **HTTP Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| GET | `/api/categories/` | List all categories |
| GET | `/api/categories/<id>/` | Retrieve a specific category |
| POST | `/api/categories/` | Create a new category (Admin) |
| PUT | `/api/categories/<id>/` | Update a category |
| DELETE | `/api/categories/<id>/` | Delete a category |

## **📘 Book Endpoints**

Manage and retrieve books

| **HTTP Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| GET | `/api/books/` | List all books |
| GET | `/api/books/<id>/` | Retrieve a specific book |
| GET | `/api/books/?search=` | Search books by title or author |
| POST | `/api/books/` | Add a new book to the system (Admin) |
| PUT | `/api/books/<id>/` | Update book details (Admin) |
| DELETE | `/api/books/<id>/` | Delete a book (Admin) |
| GET | `/api/books/?category=` | Filter books by category |

## **👥 Member Endpoints**

Allow viewing and managing member data.

| **HTTP Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| GET | `/api/members/` | List all members (Admin) |
| GET | `/api/members/<id>/` | Get a specific member |
| PUT | `/api/members/<id>/` | Update member profile (Admin) |
| DELETE | `/api/members/<id>/` | Delete a member (Admin) |

## **📚 Borrowing/Returning Endpoints**

Track when members borrow or return books.

| **HTTP Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| GET | `/api/borrow-records/` | List all books |
| GET | `/api/borrow-records/<id>/` | Retrieve a specific book |
| POST | `/api/borrow-records/` | Add a new book to the system (Admin) |
| PUT | `/api/borrow-records/<id>/return/` | Update book details (Admin) |
| DELETE | `/api/borrow-records/<id>/` | Delete a book (Admin) |

## **👤 User Profile Endpoints**

Allow users (members) to view and update their profile

| **HTTP Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| GET | `/api/profile/` | Retrieve the user's profile |
| PUT | `/api/profile/` | Update the user's profile |

## **📊 Dashboard  Endpoints (ADMIN only)**

Provide analytics for administrators.

| **HTTP Method** | **Endpoint** | **Description** |
| --- | --- | --- |
| GET | `/api/dashboard/total-books/` | Get total number of books |
| GET | `/api/dashboard/total-members/` | Get total number of registered members |
| GET | `/api/dashboard/total-borrows/` | Get total borrow transactions |
| GET | `/api/dashboard/overdue-books/` | Get list of overdue borrow records |

## **👤 User Model**

Represents library staff/admin users who manage the system (not members who borrow books).

| **Field Name** | **Data Type** | Description |
| --- | --- | --- |
| id | Primary Key | Unique identifier for the user. |
| first_name | Charfield | Required first name for the user. |
| last_name | Charfield | Required last name for the user. |
| email | Emailfield | Unique email for the user. |
| address | Textfield | Optional address of the user. |
| phone_number | Charfield | Optional phone number. |
| password | Charfield | Hashed password for authentication. |

## **🗂️ Category Model**

Groups books into categories or genres (e.g., Science Fiction, History).

| **Field Name** | **Data Type** | **Description** |
| --- | --- | --- |
| id | Primary Key | Unique identifier for the category. |
| name | Charfield | Name of the category. |
| description | Textfield | Optional description of the category. |

**Relationships**:

- Category to Book: **One-to-Many**
    
    (One category can have multiple books.)
    

## **📘 Book Model**

Contains details about books available in the library.

| **Field Name** | **Data Type** | **Description** |
| --- | --- | --- |
| id | Primary Key | Unique identifier for the book. |
| title | Charfield | Title of the book. |
| isbn | Charfield | Unique ISBN number of the book. |
| description | TextField | Optional detailed description. |
| availability_status | BooleanField | Whether the book is available for borrowing. |
| author | ForeignKey | Links to the Author model. |
| category | ForeignKey | Links to the Category model. |
| created_at | DateTimeField | Timestamp when the book was added. |
| updated_at | DateTimeField | Timestamp when the book details were updated. |

**Relationships**:

- Book to Author: **Many-to-One**
- Book to Category: **Many-to-One**

## **✍️ Author Model**

Stores information about authors of books.

| **Field Name** | **Data Type** | **Description** |
| --- | --- | --- |
| id | Primary Key | Unique identifier for the author. |
| name | Charfield | Full name of the author. |
| biography | Textfield | Short bio or background information.(Optional) |

**Relationships**:

- Author to Book: **One-to-Many**
    
    (One author can write multiple books.)
    

## **👥 Member Model**

Represents members (library users) who borrow books.

| **Field Name** | **Data Type** | Description |
| --- | --- | --- |
| id | Primary Key | Unique identifier for the member. |
| name | Charfield | Full name of the member. |
| email | Emailfield | Unique email address. |
| address | Textfield | Optional physical address of the member. |
| phone_number | Charfield | Optional phone number. |
| membership_date | DateField | Date when the membership was created. |

## **📚 BorrowRecord Model**

| **Field Name** | **Data Type** | Description |
| --- | --- | --- |
| id | Primary Key | Unique identifier for the record. |
| book | ForeignKey | Links to the Book model. |
| member | ForeignKey | Links to the Member model. |
| borrow_date | DateTimeField | When the book was borrowed. |
| return_date | DateTimeField | When the book was returned (nullable). |
| is_returned | DateTimeField | Whether the book has been returned. |

**Relationships**:

- BorrowRecord to Book: **Many-to-One**
- BorrowRecord to Member: **Many-to-One**



<img width="3819" height="2426" alt="LMS_(1)" src="https://github.com/user-attachments/assets/87dc834a-ae9e-4dbd-bc7f-a234430b8bda" />

## ⚙️ Model Relationships

**1. User**

- One-to-One or One-to-Many with `Member` (depending on design).
- Optional: Can be extended to handle login/admin roles.

**2. Member**

- One-to-One with `User` (if separated).
- One-to-Many with `BorrowRecord`.

**3. Author**

- One-to-Many with `Book` (One author can write multiple books).

**4. Category**

- One-to-Many with `Book` (One category includes multiple books).

**5. Book**

- Many-to-One with `Author`.
- Many-to-One with `Category`.
- One-to-Many with `BorrowRecord`.

**6. BorrowRecord**

- Many-to-One with `Member`.
- Many-to-One with `Book`.



# Steps to clone

## 🛠️ Getting Started – Clone & Run This Project

Follow the steps below to clone this repository and set up the project on a new machine (Linux/macOS/Windows).

### ✅ Requirements

- Python 3.10 or above
- Git
- Virtualenv (recommended)
- pip (Python package installer)

---

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

```

Replace `<your-username>` and `<your-repo-name>` with your actual GitHub details.

---

### 🧪 2. Create and Activate a Virtual Environment

### For Windows:

```bash
python -m venv venv
venv\Scripts\activate

```

### For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate

```

---

### 📦 3. Install Project Dependencies

```bash
pip install -r requirements.txt

```

If `requirements.txt` doesn't exist yet, you can generate it from your current environment:

```bash
pip freeze > requirements.txt

```

---

### ⚙️ 4. Apply Migrations

```bash
python manage.py migrate

```

---

### 👤 5. Create Superuser (Optional but Recommended)

```bash
python manage.py createsuperuser

```

---

### 🚀 6. Run the Development Server

```bash
python manage.py runserver

```

Then visit: [http://127.0.0.1:8000](http://127.0.0.1:8000/)

---

### 🗃️ 7. Environment Variables (Optional)

If you use `.env` file for secret keys or DB credentials:

- Make sure to include a sample file like `.env.example`.
- Add `.env` to `.gitignore` to avoid pushing sensitive data.

---

### 🌐 8. VS Code Dev Environment (Optional)

If you're using **VS Code**, install recommended extensions:

- Python
- Django
- Prettier
- Material Icon Theme (optional)
