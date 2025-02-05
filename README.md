# ece386-lab01

Serving handwritten digit inference with FastAPI.

See [USAFA ECE 386: AI Hardware Applications - Lab 1](https://usafa-ece.github.io/ece386-book/b1-prediction/lab-digits-api.html)

**GitHub Actions are enabled in this repository!** The workflow currently:

- Runs [Black](https://black.readthedocs.io/en/stable/index.html) format checker against client and server
- Runs [Pyright](https://microsoft.github.io/pyright/#/) type checker against client and server

## Writeup

*Answer the following questions. Strive to be articulate.*

### What strategies did you use to ensure that your client and server were communicating with the same schema?

We continually cross-referenced what the client and server requires as arguments throughout the client-server communication process to ensure that we were passing the correct type of data. For example, we initially attempted to pass an image to the server, but the server required a numpy array, so we needed to modify our client code. Additionally, when testing our client-server architecture, we examined error codes to identify the source of the problem. For example, when we had a 422 error, we knew the error was related to the post command.

### In regard to preprocessing your digit images, how well do you think your server would scale to *any* picture of a digit?

It would likely work much of the time given the performance observed during testing. However, in an environment in which the server could be passed any image, it may not work as well because the keras model was trained only on white numbers and a black background. As such, the model likely will not perform as well when the image is not white numbers on a black background.

### Does the client/server architecture make sense for this problem? Why or why not?

This architecture works properly for the problem at hand, but it may be more complicated than necessary depending on requirements. If the keras model is intended to be run on a computer other than the client, then this model is an adequate fit. However, in the way in which we were using this architecture, it would be simpler and more streamlined to pass data only as function arguments on one system to avoid errors passing data from the client to the server, and vice versa. This would also simplify the overall architecture.

## Documentation

Used ChatGPT to know how to convert an image to a numpy array.
Prompt: In python how to convert pillow image to numpy array
Link: https://chatgpt.com/share/679a74da-ab14-8005-be42-53c5cab91b7b

Met with Captain Yarbrough on 30 January to review code already written and better understand how the client-server architecture operates.