# Bear-Classifier-with-Gradio-and-FastAI(PyTorch)
Link To Deployed Version: https://huggingface.co/spaces/mattsankner/bearspace

This repository contains a machine learning model that classifies images of bears. The types of bears it can identify are Polar, Grizzly, Black, and Teddy bears. When faced with an image that is not one of the four, it will pick one of the four. The model is trained using the FastAI library, and a simple web interface is built using Gradio for users to upload and classify their images. Feel free to download a bear image of your choice from the internet and test it on the above deployed space. 

Key Features
Image Classification: The model takes an image as input and predicts the type of bear in the image.

FastAI: The model is built using the FastAI library, which is an abstraction over PyTorch, making it easier to train high-performing deep learning models.

Gradio: A user-friendly web interface is created with Gradio, enabling users to upload their images and see the classification results.

How It Works
The script starts by importing necessary libraries and modules including FastAI and Gradio.

It uses Bing Image Search API to download images of different types of bears. To make your own, go to Azure's Bing Search API page and create/use your own API key. You will need to create an account. It is free: https://www.microsoft.com/en-us/bing/apis/bing-web-search-api

FastAI is used to create a DataBlock for the dataset and a deep learning model based on the ResNet18 architecture, which is trained with the images. The trained model is then exported for later use.

Gradio is used to create a web interface where users can upload images. This interface calls a function that uses the trained model to classify the uploaded image and display the results. The script then launches the Gradio interface which can be used to classify images through a web page.

Use Case
This project is an example of how you can build a simple image classification system using deep learning and can be extended for other classification tasks.








