 

AI-Detect

AI-Detect is a local FastAPI-based multi-model image verification system.
It serves multiple ONNX deep learning models and a lightweight frontend for uploading images and running different detection modes.

The project is designed for local testing, experimentation, and hackathon demos.


---

✨ Features

🧠 Deepfake Detection – Detects AI-generated face images

🪪 Document (Aadhaar) Verification – Classifies documents as fake or authentic

🍔 Fast-Food Image Analysis – Detects AI-generated vs real rotten food images

🍎 Fruit Spoilage Detection – Identifies spoiled vs real fruit images

⚡ Fast inference using ONNX Runtime

🌐 Minimal frontend for uploading images

🔁 Multiple scans supported without page reload



---

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



---

📁 Project Layout

AI-Detect/
│
├── backend/
│   ├── main.py              # FastAPI application
│   ├── models/
│   │   ├── rvf10k_resnet18.onnx        # Deepfake model
│   │   ├── rvf10k_resnet18.onnx.data
│   │   ├── resnet18_aadhaar.onnx       # Document model
│   │   ├── fastfood_detection_model.onnx
│   │   └── fruit_model-2.onnx
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md


---

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



---

📦 Setup (Backend)

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install fastapi uvicorn onnxruntime numpy opencv-python pillow


---

▶️ Run the Backend

cd backend
source ../.venv/bin/activate
uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000

API documentation (Swagger UI):

http://127.0.0.1:8000/docs


---

🌐 Run the Frontend

You can open frontend/index.html directly,
or serve it via a local server (recommended):

cd frontend
python -m http.server 8001

Open in browser:

http://127.0.0.1:8001

The frontend communicates with the backend using Fetch API.
CORS is enabled on the backend for local development.


---

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


---

🧪 Test Using curl

Example:

curl -F "file=@/path/to/image.jpg" http://127.0.0.1:8000/scan-deepfake


---

🍔 Fast-Food Model Notes

Model file: backend/models/fastfood_detection_model.onnx

Optional label file: backend/models/fastfood_labels.txt

One label per line


Supports both:

Single-logit (sigmoid) models

Multi-class (softmax) models


Debug information (preprocessing stats) may be returned in the API response for troubleshooting.



---

🧠 Model Preprocessing

All models currently use:

Image resize: 224 × 224

RGB format

Normalization: 0–1 range

Channel order: NCHW


If a model expects NHWC, the backend attempts to auto-detect and transpose inputs.


---

🛠️ Troubleshooting

Model input shape errors:
Ensure the ONNX model input size matches preprocessing in backend/main.py.

Dependency issues:
Verify the correct virtualenv is activated.

Unexpected predictions:
Check model output shape (1 logit vs multi-class) and adjust inference logic.



---

🔮 Future Improvements

Video-based deepfake detection

Cloud deployment (Render / Railway)

Authentication and user history

Better UI visualizations for confidence scores



 

 