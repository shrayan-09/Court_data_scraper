# Delhi High Court — Court Data Fetcher & Mini-Dashboard

##  Court Chosen
**Delhi High Court** — Official public search portal: [https://delhihighcourt.nic.in/case.asp](https://delhihighcourt.nic.in/case.asp)

---

##  Objective
A small Flask web app that allows users to:
- Select **Case Type**, **Case Number**, and **Filing Year**
- Fetch **case metadata** and **latest orders/judgments**
- Download the **latest order PDF**
- Log all queries in a PostgreSQL database

---

##  Setup Steps

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/delhi-hc-case-fetcher.git
cd delhi-hc-case-fetcher
```

### 2. Create Virtual Environment & Install Requirements
```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

### 3. Set Environment Variables  
Create a `.env` file in the project root:
```
DATABASE_URL=postgresql://username:password@localhost:5432/court_db
SECRET_KEY=your-very-secure-random-string
```

Generate a secure key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 4. Create PostgreSQL Database
```bash
psql -U postgres
CREATE DATABASE court_db;
CREATE USER court_user WITH PASSWORD 'strongpassword';
GRANT ALL PRIVILEGES ON DATABASE court_db TO court_user;
\q
```

If you want to use the **`postgres`** default user instead of creating a new one, just adjust your `.env`:
```
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/court_db
```

### 5. Install Playwright Browsers
```bash
playwright install
```

### 6. Run the App
```bash
flask run
```

---

##  CAPTCHA Strategy
The Delhi HC search page uses a simple HTML form **without visual CAPTCHA** for most queries.  
Our Playwright script directly:
1. Navigates to the search page
2. Selects the **Case Type**
3. Fills the **Case Number** and **Filing Year**
4. Clicks **Search** and parses results

If CAPTCHA ever appears, we plan to:
- Prompt the user to manually enter the displayed CAPTCHA in a form field
- Submit it along with the request

This approach stays **legal** and **non-invasive**, respecting court site terms.



##  Sample `.env` File
```
DATABASE_URL=postgresql://court_user:strongpassword@localhost:5432/court_db
SECRET_KEY=be9c6d3f782f48a78b4f7d8e8f8a9c9a7c0e5c6d4f2e1b7a8c4d9f0a3b5d6e7f
```



##  Item Details
  
 Item   Details 

 **Code Repo**  Public GitHub with MIT License 
 **Court**      Delhi High Court 
 **Setup Steps**  See above 
 **CAPTCHA Strategy**  Manual fallback input if CAPTCHA appears 
 **Sample Env Vars**  See above `.env` example 
 **Demo Video**  ≤ 5 min screen capture (to be recorded) 
 **Extras**  Dockerfile, pagination for multiple orders, unit tests (optional) 






