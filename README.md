# Bear Image Classifier

Welcome to the Bear Image Classifier repository! This project showcases a sophisticated machine learning model capable of identifying four types of bears: Polar, Grizzly, Black, and Teddy. Using the FastAI library and a user-friendly Gradio web interface, this classifier stands out as a remarkable example of practical and accessible AI technology.

## Live Demo

Experience the classifier in action: [BearSpace - Hugging Face](https://huggingface.co/spaces/mattsankner/bearspace)

## Project Overview

The Bear Image Classifier is designed to demonstrate the capabilities of modern machine learning in a fun and interactive way. Users can upload images of bears, and the model will predict the type of bear present in the image.

### Key Features

- **Image Classification:** The model analyzes the image and accurately predicts the bear type.
- **FastAI Library:** Utilizes the powerful and efficient FastAI library, an abstraction layer over PyTorch, to train deep learning models effectively.
- **Gradio Web Interface:** Provides a simple, yet interactive interface for users to upload images and receive instant classification results.

### Technical Workflow

1. **Setup and Data Collection:** 
   - Import necessary libraries and modules, including FastAI and Gradio.
   - Use Bing Image Search API to gather images of different bear types.

2. **Model Development:**
   - Employ FastAI to create a DataBlock, facilitating dataset management.
   - Construct and train a deep learning model using the ResNet18 architecture.

3. **Deployment:**
   - Export the trained model for web integration.
   - Develop a Gradio web interface for real-time image classification.

4. **Execution:**
   - Launch the Gradio interface, enabling users to test the model via a web page.

### Getting Started

To replicate or build upon this project:
- Obtain a Bing Search API key from [Microsoft Bing Web Search API](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api).
- Follow the script in this repository to set up the environment, train the model, and deploy the Gradio interface.

## Use Case

This project serves as a practical example of creating an image classification system using deep learning. It illustrates the process from data collection to model deployment and can be adapted for various other classification tasks.
