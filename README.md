# 🏡 Housing Price Analysis and Prediction – Bengaluru

## 📌 Overview
Bengaluru's real estate market is **rapidly evolving**, making it challenging for buyers, sellers, and investors to make informed decisions. This project leverages **Big Data Analytics and Machine Learning** to predict housing prices based on key property attributes.  

Through **Exploratory Data Analysis (EDA)** and **predictive modeling**, we aim to identify critical factors influencing property prices and provide **accurate, data-driven insights** to users.

---

## 🚀 Approach & Technologies Used

### 🏗 Data Pipeline:
1. **Data Collection** 📊  
   - Source: **[Kaggle - Bengaluru House Price Dataset](https://www.kaggle.com/datasets/anitakataria/bengaluru-house-dataset/data)**
   - Features include **location, size, total sqft, number of bedrooms, price per sqft, and amenities.**

2. **Data Preprocessing** 🛠  
   - Handled **missing values**, **outliers**, and **feature encoding.**
   - Applied **one-hot encoding for categorical variables** (e.g., location).
   - Standardized numerical features using **StandardScaler**.

3. **Exploratory Data Analysis (EDA)** 📈  
   - **Correlation analysis** to identify price-impacting factors.
   - **Location-based price variations** using **visualizations in Power BI**.
   - **Outlier detection** using **Z-scores and Box Plots**.

---

## 🔍 Machine Learning Models Implemented:
| Model | Accuracy (%) |
|--------|-------------|
| **Linear Regression** | 65.70% |
| **Lasso Regression** | 65.73% |
| **Ridge Regression** | 65.70% |
| **Random Forest Regression** | **66.50% (Best Model)** |

**Final Model Chosen:** ✅ **Random Forest Regression** (Highest Accuracy)

---

## 🛠 Tech Stack
- **Programming Language:** Python  
- **Libraries Used:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn  
- **Modeling:** Linear Regression, Ridge, Lasso, Random Forest  
- **Visualization:** Power BI, Matplotlib, Seaborn  
- **Deployment:** Flask Web App  

---

## 🔬 Methodology

### 📌 Data Cleaning & Feature Engineering:
- **Removed irrelevant features** (e.g., area type) to focus on key attributes.
- **Converted categorical variables** (e.g., "2 BHK" → numerical encoding).
- **Applied feature scaling** to normalize numerical values.
- **Removed extreme outliers** to improve prediction accuracy.

### 📊 Price Prediction Models:
1. **Linear Regression** - Baseline model assuming a linear relationship.
2. **Lasso Regression** - Shrinks less important features to zero.
3. **Ridge Regression** - Prevents overfitting by limiting coefficient size.
4. **Random Forest Regression** 🌲 - Captures **non-linear relationships** and provides the **best results**.

### 📈 Model Evaluation:
- **Mean Absolute Error (MAE)**
- **Root Mean Square Error (RMSE)**
- **R² Score for accuracy assessment**

---

## 🎯 Key Insights
- **Location plays a crucial role in pricing** – Prime areas like **Indiranagar and Koramangala** have significantly higher prices.
- **Number of bedrooms does not always correlate with price** – Instead, **total sqft and location are stronger indicators**.
- **Outliers (extremely high or low prices) affect model performance** – Removing these significantly improved accuracy.

---

## 💻 Web Application
The trained model is deployed using **Flask**, providing a **user-friendly interface** where users can:
- **Enter property details** (location, sqft, bedrooms, etc.).
- **Receive real-time price predictions**.
- **View interactive charts & analysis**.

### 🔽 Installation:
```bash
# Clone the repository
git clone https://github.com/HousePricePrediction.git
cd housing-price-prediction

# Install dependencies
pip install -r requirements.txt
