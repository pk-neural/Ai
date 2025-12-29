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

