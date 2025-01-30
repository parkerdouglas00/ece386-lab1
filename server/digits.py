"""
TODO: Insert what this program does here. Should start with
digits is a FastAPI app that...

This file should be compliant with Pyright.
The tensorflow import is ignored with # type: ignore[import]
because tensorflow doesn't support type hints appropriately.
"""

from tensorflow.keras.saving import load_model  # type: ignore[import]
from PIL import Image
from io import BytesIO
from fastapi import FastAPI, File, UploadFile
import numpy as np
from typing import Annotated

model_path: str = "digits.keras"
# TODO: Open saved Keras model as global variable. NO TYPE HINT REQUIRED!
model = load_model(model_path)

# TODO: Create FastAPI App as global variable
app = FastAPI()


def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    # First must use pillow to process bytes
    img = Image.open(BytesIO(image_bytes))
    # TODO: convert image to grayscale and resize
    img = img.convert("L")
    # # TODO: convert image to numpy array of shape model expects
    img = img.resize((28, 28))
    image_array = np.array(img)
    return image_array  # image_array


# TODO: Define predict POST function
@app.post("/predict")
def get_prediction(image: Annotated[bytes, File()]):
    processed_image = image_to_np(image)
    tensorflow.keras.input()
    return {"file_size": len(image)}


# def predict_post() -> int:
#     @app.post("/files/")
#     async def create_upload_file(file: Annotated[bytes, File()]):
#         return {"file_size": len(file)}
