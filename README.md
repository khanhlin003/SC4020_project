# SC4020_project

Here’s a sample `README.md` file for your project:

---

# **Human Mobility Sequential Pattern Mining Project**

## **Project Overview**

This project analyzes anonymized human mobility data from four metropolitan areas in Japan. The main objective is to uncover common movement patterns using **sequential pattern mining** techniques, specifically focusing on a 75-day period. We applied the **Generalized Sequential Pattern (GSP) algorithm** to identify frequent movement sequences in different cities.

## **Dataset Description**

The dataset consists of two types of data:

1. **Mobility Data**:
    - Spatial resolution: 500m x 500m grid cells.
    - Four cities: A, B, C, and D.
    - Each area is divided into a 200x200 grid.
    - Time span: 75 days, with 30-minute time intervals.
    - Data format includes:
      - `uid`: User ID
      - `d`: Date
      - `t`: Time
      - `x`, `y`: Grid coordinates representing user location.

2. **Points of Interest (POI) Data**:
    - POI categories and their corresponding counts for each grid cell.
    - Four CSV files provide POI distribution in each city.

## **Project Objectives**

The goal of this project is to:
- Preprocess the dataset to generate "triplegs" (movement segments).
- Mine frequent movement patterns using the GSP algorithm.
- Handle challenges such as missing data and large datasets efficiently.
- Analyze the patterns and interpret them to understand urban mobility.

## **How to Run the Project**

### **1. Requirements**

Make sure you have the following Python libraries installed:

```bash
pip install pandas numpy trackintel mlxtend matplotlib seaborn
```

### **2. Data Preprocessing**

- Load the CSV files for each city.
- Preprocess the mobility data to handle missing values (`x`, `y` = -999 for days 61–75 in cities B, C, and D).
- Use the `trackintel` library to generate "triplegs," which are the movement segments.

### **3. Sequential Pattern Mining**

- Convert triplegs into sequences of `(x, y)` coordinates.
- Use the **Generalized Sequential Pattern (GSP)** algorithm to mine frequent movement patterns from the sequences.
- Adjust parameters to optimize performance, especially when working with large datasets.

### **4. Code Structure**

- `preprocessing.py`: Contains functions to handle missing data and generate triplegs.
- `gsp_algorithm.py`: Implementation of the GSP algorithm for mining frequent movement patterns.
- `visualization.py`: Functions for visualizing the movement patterns using heatmaps or other relevant charts.

### **5. Running the Code**

- Use **Jupyter Notebook** for interactive development and data visualization.
- To run the entire process:
  1. Open `mobility_analysis.ipynb`.
  2. Follow the notebook cells to preprocess the data, apply the GSP algorithm, and analyze results.

### **6. Handling Large Datasets**

- The data for cities B, C, and D is large, and may need to be processed in chunks. The project includes code for chunk processing to optimize memory usage and performance.

## **Results and Analysis**

- The frequent movement patterns are saved in a CSV file named `frequent_patterns.csv`.
- The results include frequent sequences such as `<{2,4}, {1,2}>`, which highlight common routes taken by residents in the cities.

## **Challenges**

- **Missing Data**: Some datasets (B, C, and D) had missing coordinates for the last 15 days, handled by replacing `x` and `y` with NaN.
- **Large Datasets**: The project uses chunk processing and parameter optimization to handle large files efficiently.

## **Further Improvements**

- Consider extending the analysis to the full 75 days if computational resources permit.
- Explore advanced algorithms like **PrefixSpan** or **SPADE** for faster pattern mining.
  
