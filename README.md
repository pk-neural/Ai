# AI-Detect

AI-Detect is a FastAPI-based multi-model image verification system. It serves multiple ONNX deep learning models and a lightweight frontend for uploading images and running different detection modes.

## ✨ Features

- 🧠 **Deepfake Detection** – Detects AI-generated face images
- 🪪 **Document (Aadhaar) Verification** – Classifies documents as fake or authentic
- 🍔 **Fast-Food Image Analysis** – Detects AI-generated vs real rotten food images
- 🍎 **Fruit Spoilage Detection** – Identifies spoiled vs real fruit images
- ⚡ Fast inference using ONNX Runtime
- 🌐 Modern frontend with real-time confidence display
- 🔁 Multiple scans supported without page reload

## 🧰 Tech Stack

### Backend
- FastAPI
- ONNX Runtime
- NumPy
- OpenCV

### Frontend
- HTML5
- CSS3
- Vanilla JavaScript (Fetch API)

### Models
- CNN / ResNet-based models
- Exported to ONNX for efficient CPU inference

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/pk-neural/Ai.git
cd Ai
```

2. Navigate to backend directory:
```bash
cd backend
```

3. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Ensure model files are in `backend/models/` directory:
   - `fruit_model-2.onnx`
   - `resnet18_aadhaar.onnx`
   - `food_detection_model.onnx`
   - `rvf10k_resnet18.onnx`

### Running the Application

1. Start the FastAPI backend:
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. Open the frontend:
   - For local development: Open `frontend/index.html` in your browser
   - For GitHub Pages: The frontend is automatically served from the `frontend/` directory

3. The frontend will connect to `http://127.0.0.1:8000` by default.

## 📁 Project Structure

```
Ai/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── models/             # ONNX model files
│       ├── fruit_model-2.onnx
│       ├── resnet18_aadhaar.onnx
│       ├── food_detection_model.onnx
│       └── rvf10k_resnet18.onnx
├── frontend/
│   ├── index.html          # Main frontend file
│   └── .nojekyll          # GitHub Pages configuration
└── README.md
```

## 🔌 API Endpoints

- `POST /scan-deepfake` - Deepfake detection
- `POST /scan-document` - Document verification
- `POST /scan-fastfood` - Fast food image analysis
- `POST /scan-fruit` - Fruit spoilage detection

All endpoints accept `multipart/form-data` with a `file` field containing an image file.

### Response Format
```json
{
  "prediction": "fake" | "real" | "authentic" | "fake spoiled" | "real spoiled" | "fake rotton" | "real rotton",
  "confidence": 91.23
}
```

## 🌐 GitHub Pages

The frontend is configured for GitHub Pages. To enable:

1. Go to repository Settings → Pages
2. Select source: `Deploy from a branch`
3. Select branch: `main`
4. Select folder: `/frontend`
5. Save

The frontend will be available at: `https://pk-neural.github.io/Ai/`

**Note:** Update the `API_BASE` in `frontend/index.html` if your backend is hosted elsewhere.

## 📝 License

This project is open source and available for educational and research purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

<<<<<<< HEAD
=======
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



 

 ////////////////////////////////////////////////////////////////////////////////
 # Go to project root folder
cd ~/Downloads/AI

# Activate virtual environment
source .venv/bin/activate

# Install all required packages (run once or after changes)
pip install fastapi uvicorn onnxruntime numpy opencv-python pillow python-multipart

# Save installed packages for future use
pip freeze > requirements.txt

# Go to backend folder
cd backend

# Run FastAPI backend server (auto-reload on changes)
uvicorn main:app --reload

# ================================
# OPEN A NEW TERMINAL AFTER THIS
# ================================

# Go to frontend folder
cd ~/Downloads/AI/frontend

# Run frontend server for HTML/CSS/JS
python -m http.server 5500

# Open in browser:
# Backend → http://127.0.0.1:8000/docs
# Frontend → http://localhost:5500
>>>>>>> 0f28073 (Clean repository and update gitignore)
