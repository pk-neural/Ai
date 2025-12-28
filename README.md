AI-Detect
AI-Detect is a local FastAPI-based multi-model image verification system.
It serves multiple ONNX deep learning models and a lightweight frontend for uploading images and running different detection modes.
The project is designed for local testing, experimentation, and hackathon demos.
📦 Complete Project ZIP (Google Drive)
Due to GitHub file size limitations, the complete project folder (including all files and resources) is hosted on Google Drive.
🔗 Google Drive Link:
https://drive.google.com/drive/folders/1Edb4RAHBmL9UqthOiJDai4DwZQ0p6EL0?usp=share_link
⚠️ Note: Large files are hosted externally to comply with GitHub upload limits.
✨ Features
🧠 Deepfake Detection – Detects AI-generated face images
🪪 Document (Aadhaar) Verification – Classifies documents as fake or authentic
🍔 Fast-Food Image Analysis – Detects AI-generated vs real rotten food images
🍎 Fruit Spoilage Detection – Identifies spoiled vs real fruit images
⚡ Fast inference using ONNX Runtime
🌐 Minimal frontend for uploading images
🔁 Multiple scans supported without page reload
🧰 Tech Stack
Backend
FastAPI
ONNX Runtime
NumPy
OpenCV
Frontend
HTML
CSS
Vanilla JavaScript (Fetch API)
Models
CNN / ResNet-based models
Exported to ONNX for efficient CPU inference
📁 Project Layout
AI-Detect/
│
├── backend/
│   ├── main.py
│   ├── models/
│   │   ├── rvf10k_resnet18.onnx
│   │   ├── rvf10k_resnet18.onnx.data
│   │   ├── resnet18_aadhaar.onnx
│   │   ├── fastfood_detection_model.onnx
│   │   └── fruit_model-2.onnx
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
⚙️ Requirements
macOS / Linux
Python 3.9+
Virtual environment recommended (.venv)
Python Packages
fastapi
uvicorn
onnxruntime
numpy
opencv-python
pillow
📦 Setup (Backend)
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install fastapi uvicorn onnxruntime numpy opencv-python pillow
▶️ Run the Backend
cd backend
source ../.venv/bin/activate
uvicorn main:app --reload
Backend URL:
http://127.0.0.1:8000
Swagger UI:
http://127.0.0.1:8000/docs
🌐 Run the Frontend
cd frontend
python -m http.server 8001
Open in browser:
http://127.0.0.1:8001
The frontend communicates with the backend using Fetch API.
CORS is enabled for local development.
🔌 API Endpoints
Feature	Endpoint
Fruit Spoilage Detection	/scan-fruit
Document Verification	/scan-document
Fast-Food Detection	/scan-fastfood
Deepfake Detection	/scan-deepfake
Example Response
{
  "prediction": "FAKE",
  "confidence": 91.87
}
🧪 Test Using curl
curl -F "file=@/path/to/image.jpg" http://127.0.0.1:8000/scan-deepfake
🍔 Fast-Food Model Notes
Model file: backend/models/fastfood_detection_model.onnx
Optional labels file: backend/models/fastfood_labels.txt
Supports:
Single-logit (sigmoid) models
Multi-class (softmax) models
Debug preprocessing info may be returned in API response.
🧠 Model Preprocessing
Image size: 224 × 224
Color format: RGB
Normalization: 0–1 range
Channel order: NCHW
If a model expects NHWC, input is auto-transposed.
🛠️ Troubleshooting
Model input shape errors: Ensure ONNX input size matches preprocessing
Dependency issues: Activate correct virtual environment
Unexpected predictions: Verify output shape (binary vs multi-class)
🔮 Future Improvements
Video-based deepfake detection
Cloud deployment (Render / Railway)
Authentication and user history
Better UI visualizations for confidence scores
