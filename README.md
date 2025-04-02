# Go to your project folder

cd /c/Projects/repositories/sensor_data_logic

# Create README.md file

touch README.md

# Open README.md in VS Code (or any editor) and paste the following content:

echo "# Sensor Data Logger (C++ + Python)

This project simulates sensor data using C++ and visualizes it in real time using Python.

## 🛠 How it works

- \`sensor_simulator.cpp\`: Generates random sensor values and writes them to \`sensor_data.txt\`
- \`plot_sensor_data.py\`: Reads and plots the values from that file live using Matplotlib

## 💻 Requirements

- Python 3 + matplotlib
- g++ (via MSYS2)

## 🚀 Run the project

### 1. Compile and run the C++ simulator

\`\`\`bash
g++ -std=c++11 sensor_simulator.cpp -o sensor_simulator
./sensor_simulator
\`\`\`

### 2. Run the Python live plot

\`\`\`bash
python plot_sensor_data.py
\`\`\`

## 📂 File Structure

\`\`\`
sensor_data_logic/
├── sensor_simulator.cpp
├── plot_sensor_data.py
├── sensor_data.txt (generated)
└── README.md
\`\`\`
" > README.md

# Initialize Git if needed

git init

# Add all files

git add .

# Commit your changes

git commit -m "Initial commit: sensor data logger with C++ and Python"

# Add GitHub remote (replace with your repo URL)

git remote add origin https://github.com/SerhiiMis/sensor_data_logger.git
git branch -M main

# Push to GitHub

git push -u origin main
