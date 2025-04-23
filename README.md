# 🧠 MNIST Digit Classifier with CNN + Gradio App

This project demonstrates handwritten digit classification using the [MNIST dataset](http://yann.lecun.com/exdb/mnist/), powered by a Convolutional Neural Network (CNN). It includes data preprocessing, EDA, model building with training optimizations, evaluation metrics, and an interactive Gradio app deployed on Hugging Face Spaces.

---

## 🚀 Features

- 📊 Exploratory Data Analysis (EDA)
- 🖼️ Data Augmentation using `ImageDataGenerator`
- 🧠 CNN model for digit classification
- 🛑 Early Stopping to avoid overfitting
- 📈 Evaluation using Accuracy, Confusion Matrix, and Classification Report
- 🖌️ Interactive Gradio Sketchpad for digit prediction
- 🌐 Deployed on Hugging Face Spaces



# ✍️ MNIST Digit Recognizer – Sketch Your Digits!

Welcome to the **MNIST Digit Recognizer**! This app allows you to draw a digit (0–9) directly in your browser and predicts what digit you sketched using a trained deep learning model.

## 🚀 How to Use


1. **Open the link for the running server on a huggingface space**
  - [Try the app here!](https://ahmed-amer-mnist-gradio.hf.space/?__theme=light)

2. **Sketch Your Digit**
   - Click on the **🖌️ Brush icon** located on the **left side** of the sketchpad.
   - Use your mouse or touchscreen to **draw a digit** (0 through 9) inside the sketch area.
   - Make sure to draw clearly, using most of the canvas for better recognition.

3. **Submit Your Drawing**
   - After drawing, simply **wait a moment** and the model will automatically predict your digit.
   - You'll see the prediction results below the canvas with the probabilities for each digit.

4. **Clear the Sketchpad**
   - To erase your sketch and start over, **click the trash can 🗑️ icon** on the **top-right corner** of the canvas.
   - ⚠️ Do **not** use any additional "Clear" button — just the one on the canvas!

## 🧠 Behind the Scenes

This app uses a TensorFlow-trained neural network to classify handwritten digits. The drawing is preprocessed into a 28x28 grayscale image before being fed to the model.
