from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import onnxruntime as ort
import numpy as np
import cv2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fruit_session = ort.InferenceSession("models/fruit_model-2.onnx", providers=["CPUExecutionProvider"])
document_session = ort.InferenceSession("models/resnet18_aadhaar.onnx", providers=["CPUExecutionProvider"])
fastfood_session = ort.InferenceSession("models/food_detection_model.onnx", providers=["CPUExecutionProvider"])
deepfake_session = ort.InferenceSession("models/rvf10k_resnet18.onnx", providers=["CPUExecutionProvider"])

FRUIT_CLASSES = ["fake spoiled", "real spoiled"]
DOCUMENT_CLASSES = ["fake", "authentic"]
FASTFOOD_CLASSES = ["fake rotton", "real rotton"]
DEEPFAKE_CLASSES = ["fake", "real"]

def preprocess_image(image_bytes):
    img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img.astype(np.float32) / 255.0
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0)
    return img

def softmax(x):
    e = np.exp(x - np.max(x))
    return e / np.sum(e)

@app.post("/scan-fruit")
async def scan_fruit(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img_tensor = preprocess_image(image_bytes)
    input_name = fruit_session.get_inputs()[0].name
    output = fruit_session.run(None, {input_name: img_tensor})[0]
    out = np.array(output)

    if out.ndim == 2 and out.shape[1] == 1:
        logits = out[:, 0]
        prob = 1 / (1 + np.exp(-logits))
        pred_class = int(prob[0] >= 0.5)
        confidence = float(prob[0] * 100)
    else:
        probs = softmax(out[0])
        pred_class = int(np.argmax(probs))
        confidence = float(np.max(probs) * 100)

    return {"prediction": FRUIT_CLASSES[pred_class], "confidence": round(confidence, 2)}

@app.post("/scan-document")
async def scan_document(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img_tensor = preprocess_image(image_bytes)
    input_name = document_session.get_inputs()[0].name
    output = document_session.run(None, {input_name: img_tensor})[0]
    probs = softmax(output[0])
    pred_class = int(np.argmax(probs))
    confidence = float(np.max(probs) * 100)
    return {"prediction": DOCUMENT_CLASSES[pred_class], "confidence": round(confidence, 2)}

@app.post("/scan-fastfood")
async def scan_fastfood(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img_tensor = preprocess_image(image_bytes)
    inp = fastfood_session.get_inputs()[0]
    inp_shape = inp.shape
    if len(inp_shape) == 4 and inp_shape[-1] == 3:
        img_tensor = np.transpose(img_tensor, (0, 2, 3, 1))

    output = fastfood_session.run(None, {inp.name: img_tensor})[0]
    out = np.array(output)

    if out.ndim == 2 and out.shape[1] == 1:
        logits = out[:, 0]
        prob = 1 / (1 + np.exp(-logits))
        pred_class = int(prob[0] >= 0.5)
        confidence = float(prob[0] * 100)
    else:
        probs = softmax(out[0])
        pred_class = int(np.argmax(probs))
        confidence = float(np.max(probs) * 100)

    return {"prediction": FASTFOOD_CLASSES[pred_class], "confidence": round(confidence, 2)}

@app.post("/scan-deepfake")
async def scan_deepfake(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img_tensor = preprocess_image(image_bytes)
    input_name = deepfake_session.get_inputs()[0].name
    output = deepfake_session.run(None, {input_name: img_tensor})[0]
    out = np.array(output)

    if out.ndim == 2 and out.shape[1] == 1:
        score = float(1 / (1 + np.exp(-out[0][0])))
        pred_class = int(score >= 0.5)
        confidence = score if pred_class == 1 else (1 - score)
        confidence *= 100.0
    else:
        probs = softmax(out[0])
        pred_class = int(np.argmax(probs))
        confidence = float(np.max(probs) * 100)

    return {"prediction": DEEPFAKE_CLASSES[pred_class], "confidence": round(confidence, 2)}
