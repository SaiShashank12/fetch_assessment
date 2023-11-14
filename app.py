from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from fetch_assessment.pipeline.predict import PredictionPipleline
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
import uvicorn
import os

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return {"message": "Welcome to the Receipt Count Prediction API"}

@app.get("/train")
async def training():
    try:
        # Assuming 'python main.py' generates an image at 'output/training_image.png'
        os.system("python main.py")
        image_path = os.path.join(PredictionPipleline().config.root_dir,"training_image.png")
        return JSONResponse(content={"message": "Training successful !!", "image_path": image_path})
    except Exception as e:
        return JSONResponse(content={"message": f"Error Occurred! {e}"})

@app.post("/predict")
async def predict_route(n_days: int):
    try:

        obj = PredictionPipleline()
        predict = obj.predict(int(n_days))

        return Response(str(predict))
    except Exception as e:
        raise e
    
@app.get("/training_image")
async def get_training_image():
    image_path = os.path.join(PredictionPipleline().config.root_dir,"training_image.png")
    return FileResponse(image_path)

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
