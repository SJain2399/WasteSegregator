import wastemodule as wm
import uvicorn
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO

app = FastAPI()

def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

@app.get('/index')
def hello_world():
    return "Hello_World"

@app.post("/predict")
def predict_waste(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(file.file.read())
    prediction = wm.predict_waste_class(image)
    return 2

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')