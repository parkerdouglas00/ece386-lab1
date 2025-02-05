# Digits Server

The server opens the keras model, accepts a post request from the client to predict, adjust the image to meet model parameters, then runs the image through the model to make a prediction, and returns the prediction as an integer to the client.

## Usage

Open Fast API and run the server in a virtual environment, moting that the displayed IP address is the IP address that should be passed to the client.

## Documentation:

Used ChatGPT to know how to convert an image to a numpy array.
Prompt: In python how to convert pillow image to numpy array
Link: https://chatgpt.com/share/679a74da-ab14-8005-be42-53c5cab91b7b