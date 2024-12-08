import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Set up the page configuration
st.set_page_config(page_title="Data Insights Dashboard", layout="wide")

# File uploader for CSV files
st.sidebar.header("Upload CSV Files")
uploaded_files = st.sidebar.file_uploader(
    "Upload up to 3 CSV files", type="csv", accept_multiple_files=True
)

# Load datasets
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

dataframes = {}
if uploaded_files:
    for uploaded_file in uploaded_files:
        name = uploaded_file.name.split(".")[0]
        dataframes[name] = load_data(uploaded_file)

# Tabs for navigation
if not dataframes:
    st.warning("Please upload CSV files to proceed.")
else:
    tab1, tab2, tab3 = st.tabs(["Overview", "Visualizations", "Advanced Analysis"])

    # Tab 1: Data Overview
    with tab1:
        st.header("Data Overview")
        dataset_name = st.selectbox("Select a dataset to preview", list(dataframes.keys()))

        if dataset_name:
            df = dataframes[dataset_name]
            st.subheader(f"Preview of {dataset_name} dataset")
            st.dataframe(df.head())

            st.subheader("Summary Statistics")
            st.write(df.describe().T)

            st.subheader("Missing Values")
            st.write(df.isnull().sum())

    # Tab 2: Visualizations
    with tab2:
        st.header("Visualizations")
        dataset_name = st.selectbox("Select a dataset for visualizations", list(dataframes.keys()))

        if dataset_name:
            df = dataframes[dataset_name]

            # Line Chart for Time Series
            if "Date" in df.columns:
                df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
                if df["Date"].isnull().all():
                    st.warning("Date column could not be parsed. Please check the format.")
                else:
                    time_cols = [col for col in ["GHI", "DNI", "DHI", "Tamb"] if col in df.columns]
                    if time_cols:
                        st.subheader("Time Series Analysis")
                        selected_col = st.selectbox("Select a column to plot", time_cols)

                        if selected_col:
                            fig, ax = plt.subplots(figsize=(10, 6))
                            sns.lineplot(data=df, x="Date", y=selected_col, ax=ax)
                            ax.set_title(f"{selected_col} Over Time")
                            st.pyplot(fig)
                    else:
                        st.warning("No suitable columns found for time series plotting.")

            # Correlation Matrix
            st.subheader("Correlation Matrix")
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if not numeric_cols.empty:
                corr = df[numeric_cols].corr()
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
                ax.set_title("Correlation Matrix")
                st.pyplot(fig)
            else:
                st.warning("No numeric columns available for correlation matrix.")

    # Tab 3: Advanced Analysis
    with tab3:
        st.header("Advanced Analysis")
        dataset_name = st.selectbox("Select a dataset for advanced analysis", list(dataframes.keys()))

        if dataset_name:
            df = dataframes[dataset_name]

            # Outlier Analysis using Z-Score
            st.subheader("Outlier Detection")
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            if not numeric_cols.empty:
                selected_col = st.selectbox("Select a column for Z-Score Analysis", numeric_cols)

                if selected_col:
                    zscore_df = df.copy()
                    zscore_df["Z-Score"] = zscore(zscore_df[selected_col])
                    st.write(zscore_df[[selected_col, "Z-Score"]].sort_values(by="Z-Score", ascending=False).head(10))
            else:
                st.warning("No numeric columns available for Z-Score analysis.")

            # Wind Analysis (Wind Speed and Direction)
            if "WS" in df.columns and "WD" in df.columns:
                st.subheader("Wind Analysis")
                fig, ax = plt.subplots(figsize=(8, 8))
                sns.scatterplot(data=df, x="WS", y="WD", ax=ax)
                ax.set_title("Wind Speed vs Direction")
                st.pyplot(fig)

# Sidebar footer
st.sidebar.markdown("---")
st.sidebar.write("Developed by Amen Zelealem.")
