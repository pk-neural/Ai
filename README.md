# AI-Detection

AI-Detection is a unified **AI-powered multi-model image verification system** built using **FastAPI** and **ONNX Runtime**.  
It detects **deepfake images, fake Aadhaar documents, spoiled fruits, and manipulated food images** using custom-trained deep learning models.

This project is designed for **local testing, experimentation, academic use, and hackathon demos**, with a lightweight frontend and fast CPU-based inference.

---

## ✨ Features

- 🧠 **Deepfake Detection** – Detects AI-generated human face images  
- 🪪 **Document (Aadhaar) Verification** – Classifies documents as fake or authentic  
- 🍔 **Fast-Food Image Fraud Detection** – Detects AI-generated or manipulated food images  
- 🍎 **Fruit Spoilage Detection** – Identifies spoiled vs real fruits  
- ⚡ Fast inference using **ONNX Runtime**  
- 🌐 Minimal frontend for image upload  
- 🔁 Multiple scans without page reload  

---

## 🧰 Tech Stack

### Backend
- FastAPI  
- ONNX Runtime  
- NumPy  
- OpenCV  

### Frontend
- HTML  
- CSS  
- Vanilla JavaScript (Fetch API)  

### Models
- CNN / ResNet-based models  
- Exported to **ONNX** for efficient CPU inference  

---

## 📁 Project Structure

