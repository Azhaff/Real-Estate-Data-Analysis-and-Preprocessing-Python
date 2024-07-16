### Real Estate Data Analysis and Preprocessing

This project focuses on the analysis and preprocessing of a real estate dataset using various data science libraries in Python. The goal is to clean, standardize, and extract meaningful insights from the data. The dataset includes various features such as price, location, agent details, and property specifics.

### Features and Workflow

1. **Data Import and Initial Setup**:
   - The dataset is imported from a CSV file using Pandas.
   - Display settings are configured to enhance readability of floating-point numbers.

2. **Data Cleaning**:
   - Removal of rows with missing values.
   - Filling any remaining missing values with zeros.
   - Conversion of the `price` column to numeric format to handle inconsistencies.

3. **Outlier Detection and Removal**:
   - Identification of outliers in the `price` column using Z-scores.
   - Removal of rows where the `price` column has Z-scores beyond a threshold of 3, indicating potential outliers.

4. **Correlation Analysis**:
   - Calculation of the correlation matrix for numeric columns including `price`, `latitude`, `longitude`, `baths`, and `bedrooms`.
   - Visualization of the correlation matrix using a heatmap.

5. **Agent Analysis**:
   - Calculation of the correlation between the number of properties listed by an agent and the average property price.
   - Visualization of this correlation using a scatter plot.

6. **Price per Square Meter**:
   - Creation of a new column `price_per_sqm` to indicate the price per square meter of each property.
   - Handling of numeric conversion for the `area` column.

7. **Temporal Features**:
   - Extraction of additional temporal features such as month, quarter, and day of the week from the `date_added` column.

8. **Standardization**:
   - Standardization of numerical variables using `StandardScaler` to ensure they have a mean of 0 and a standard deviation of 1.

9. **Categorical Encoding**:
   - Encoding of categorical variables using `LabelEncoder` to convert them into a numeric format suitable for machine learning algorithms.

### How to Use

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/real-estate-data-analysis.git
   cd real-estate-data-analysis
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Install the required libraries using:
   ```sh
   pip install pandas numpy matplotlib seaborn scipy scikit-learn
   ```

3. **Run the Script**:
   Execute the script to perform the data analysis and preprocessing:
   ```sh
   python analysis_script.py
   ```

### Dependencies

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- scikit-learn

### Dataset

The dataset used in this project should be a CSV file named `Q1_property.csv` with the following columns:
- `property_id`
- `price`
- `latitude`
- `longitude`
- `baths`
- `bedrooms`
- `agent`
- `date_added`
- `area`
- `page_url`
- `property_type`
- `location`
- `city`
- `province_name`
- `purpose`
- `agency`

### Future Enhancements

- **Advanced Outlier Detection**: Implement more sophisticated outlier detection methods.
- **Feature Engineering**: Create additional features to improve the analysis.
- **Machine Learning Models**: Build and evaluate machine learning models for property price prediction.
- **Dashboard**: Develop an interactive dashboard for real-time data visualization and analysis.

This project provides a comprehensive approach to data cleaning, preprocessing, and initial analysis, forming a solid foundation for further exploration and model development in the real estate domain.
