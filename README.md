# OpenOA Deployment – Assignment

This project demonstrates deployment of the OpenOA repository in two forms:

1. JupyterLab (original workflow)  
2. FastAPI (API-based access to core analysis)  

---

## 🔧 Overview

The original OpenOA repository is designed as a Jupyter-based analytical toolkit rather than a production-ready application.

To make it deployable and usable in a SaaS-like environment, I implemented:

- A FastAPI service exposing core analysis logic  
- Docker-based deployment for reproducibility  
- Cloud deployment using Render  

---

## 🚀 Live Deployments

- FastAPI (Swagger UI):  
  https://openoa-idaa.onrender.com/docs  

- JupyterLab:  
  https://openoa-1-12ew.onrender.com/lab  

---

## ⚙️ Local Setup

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd OpenOA
```

---

## 🐍 Running Locally (Without Docker)

### Step 1: Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

---

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

> `pip install -e .` installs the project in editable mode, allowing local modules to be imported correctly.

---

### Step 3: Run JupyterLab

```bash
jupyter lab
```

Open:
```
http://localhost:8888
```

---

### Step 4: Run FastAPI

```bash
uvicorn main:app --reload
```

Open:
```
http://127.0.0.1:8000/docs
```

---

## 🐳 Running with Docker

### FastAPI

```bash
docker build -t openoa-api .
docker run -p 8000:8000 openoa-api
```

Open:
```
http://localhost:8000/docs
```

---

### JupyterLab

```bash
docker build -f Dockerfile.jupyter -t openoa-jupyter .
docker run -p 8001:8000 openoa-jupyter
```

Open:
```
http://localhost:8001
```

---

## 🧠 Implementation Details

- Extracted core analysis logic from Jupyter notebooks  
- Built REST API using FastAPI  
- Resolved module import issues using editable install (`pip install -e .`)  
- Fixed path handling for Docker/cloud environments  
- Dockerized both FastAPI and JupyterLab  
- Deployed both services on Render  

---

## ⚠️ Notes

- Some notebook cells may produce errors due to deprecated functions or dataset dependencies.  
- The FastAPI endpoint performs computationally intensive analysis and may fail on Render free tier due to memory constraints.  
- The Jupyter deployment fully supports the original workflow.  

---

## 📌 Conclusion

This project demonstrates:

- Converting research-oriented notebook code into a deployable API  
- Handling real-world issues like dependency mismatches and file paths  
- Using Docker for consistent environments  
- Deploying services to cloud platforms  
- Making analytical workflows accessible via APIs  
