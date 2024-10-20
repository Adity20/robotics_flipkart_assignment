# Ripeness of Fruit Detection 🍌🍍🍊
Welcome to the **Ripeness of Fruit Detection** project! This tool leverages the TensorFlow Object Detection API and Support Vector Classifiers to determine the ripeness of various fruits. Let’s dive into its setup and usage.

## 🌟 Features
- **Fruit Detection**: Identifies different fruits using a trained TensorFlow model.
- **Ripeness Classification**: Uses ensemble SVCs to assess ripeness levels.

## 🚀 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Mavrik-jnr/Ripeness-of-Fruit-Detection.git
   cd Ripeness-of-Fruit-Detection
   ```

2. **Set Up the Environment**
   Ensure you have Python 3.x and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Pretrained Models**
   Place the detection and classification models in the appropriate directories:
   - `assets/` for model files.
   - `variables/` for additional data.

## 📈 Usage

### Run the Detection

#### Image Detection
   ```bash
   python Image_Detection.py
   ```

#### Live Detection (for real-time video)
   ```bash
   python Live_Detection.py
   ```

## 🍇 Classes Detected
- Ripe Banana Bunch 🟡
- Unripe Banana Bunch 🍏
- Orange 🍊
- Banana 🍌
- Pineapple 🍍