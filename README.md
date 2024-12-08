# Moonlight EDA Dashboard

A comprehensive **Exploratory Data Analysis (EDA)** script designed to automate the analysis of raw datasets, generate statistical summaries, visualize data, and save cleaned outputs in an organized manner.

---

## 📁 Project Structure
Moonlight-EDA-Dashboard/ 
├── data/ # Folder containing raw input data │ 
    ├── benin-malanville.csv │ 
    ├── sierraleone-bumbuna.csv 
    │ └── togo-dapaong_qc.csv 
├── notebooks/ # notebooks for detailed analysis 
    │ └── eda_analysis.ipynb 
├── scripts/ # Python scripts for automating EDA 
    │ └── eda_analysis.py 
├── output/ # Generated output files (plots, summaries, cleaned data) 

├── tests/ # Placeholder for test scripts 
├── requirements.txt # Python dependencies 
└── README.md # Project documentation


---

## 🚀 Features
- **Input Directory**: Reads raw CSV files from the `data/` folder.
- **Automated EDA**:
  - Descriptive statistics
  - Missing value checks
  - Outlier detection
  - Time-series analysis
  - Correlation heatmaps
  - Histogram generation
- **Output Directory**:
  - Cleaned datasets
  - Statistical summaries in CSV
  - Visualizations (time-series plots, heatmaps, histograms, etc.)
- **Extensible**: Easily adaptable to different datasets and analysis requirements.

---

## 🛠️ Getting Started

### Prerequisites
Ensure you have Python 3.8+ and `pip` installed on your system.

### Installation
1. Clone the repository:
   git clone https://github.com/amen-zelealem/moonlight-eda-dashboard.git

2. Navigate to the project directory:
   cd moonlight-eda-dashboard

3. Create a virtual environment:
    python -m venv myvenv
    source myvenv/bin/activate   # Linux/macOS
    myvenv\Scripts\activate  

4. Install dependencies:
   pip install -r requirements.txt

## ⚙️ Usage
Place your raw CSV files in the data/ folder.

Run the eda_analysis.py script:
    python scripts/eda_analysis.py

View the outputs in the output/ folder:
    Plots (saved in output/plots/)
    Summary statistics (saved in output/summaries/)
    Cleaned data (saved in output/cleaned/)

## 📊 Example Output
Summary Statistics: A CSV file detailing mean, median, standard deviation, and missing values for each column.
Visualizations:
Time-series plots
Heatmaps for correlation
Histograms for numerical columns
Bubble charts (if applicable)

## 🧩 Customization
Modify scripts/eda_analysis.py to include additional analyses.
Adjust visualization styles and parameters using matplotlib and seaborn.

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch
   git checkout -b feature-name
3. Commit your changes
   git commit -m "Add your message here"
4. Push to the branch:
   git push origin feature-name
5. Open a pull request.
   
## 📧 Contact
For questions or support, please reach out to amenzelealem@gmail.com