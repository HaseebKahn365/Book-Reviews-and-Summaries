#!/usr/bin/env python3
"""
Online Courses Dataset - EDA and Data Cleaning
File: online_courses_eda.py
Purpose: Comprehensive exploratory data analysis and data cleaning
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', None)

# File path
file_path = '/Users/apple/Downloads/ML & AI/Book-Reviews-and-Summaries/Hands on ML O\'riele/Online_Courses.csv'

print("="*80)
print("ONLINE COURSES DATASET - EXPLORATORY DATA ANALYSIS & DATA CLEANING")
print("="*80)
print(f"\nAnalysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# ============================================================================
# STEP 1: DATA LOADING
# ============================================================================
print("\n" + "="*80)
print("STEP 1: DATA LOADING")
print("="*80)

try:
    df = pd.read_csv(file_path, encoding='utf-8')
    print(f"✓ Data loaded successfully!")
    print(f"  - Shape: {df.shape[0]} rows × {df.shape[1]} columns")
except Exception as e:
    print(f"✗ Error loading data: {e}")
    exit(1)

# ============================================================================
# STEP 2: COLUMN IDENTIFICATION
# ============================================================================
print("\n" + "="*80)
print("STEP 2: DATA COLUMNS IDENTIFICATION")
print("="*80)

print(f"\nTotal Columns: {len(df.columns)}\n")
print("Column Names and Data Types:")
print("-" * 80)
for idx, (col, dtype) in enumerate(zip(df.columns, df.dtypes), 1):
    print(f"{idx:3d}. {col:40s} | {str(dtype):15s}")

# ============================================================================
# STEP 3: BASIC INFORMATION
# ============================================================================
print("\n" + "="*80)
print("STEP 3: BASIC DATASET INFORMATION")
print("="*80)

print("\nDataset Info:")
df.info()

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

# ============================================================================
# STEP 4: MISSING VALUES ANALYSIS
# ============================================================================
print("\n" + "="*80)
print("STEP 4: MISSING VALUES ANALYSIS")
print("="*80)

missing_data = pd.DataFrame({
    'Column': df.columns,
    'Missing_Count': df.isnull().sum(),
    'Missing_Percentage': (df.isnull().sum() / len(df) * 100).round(2)
})
missing_data = missing_data[missing_data['Missing_Count'] > 0].sort_values('Missing_Count', ascending=False)

if len(missing_data) > 0:
    print(f"\nColumns with Missing Values: {len(missing_data)}")
    print("-" * 80)
    print(missing_data.to_string(index=False))
else:
    print("\n✓ No missing values found!")

# ============================================================================
# STEP 5: DUPLICATE ANALYSIS
# ============================================================================
print("\n" + "="*80)
print("STEP 5: DUPLICATE RECORDS ANALYSIS")
print("="*80)

duplicates = df.duplicated().sum()
print(f"\nTotal Duplicate Rows: {duplicates}")

if duplicates > 0:
    print(f"  - Percentage: {(duplicates/len(df)*100):.2f}%")
    print("\nDuplicate rows:")
    print(df[df.duplicated(keep=False)])

# ============================================================================
# STEP 6: STATISTICAL SUMMARY
# ============================================================================
print("\n" + "="*80)
print("STEP 6: STATISTICAL SUMMARY")
print("="*80)

print("\nNumerical Columns Summary:")
print(df.describe())

print("\nCategorical Columns Summary:")
print(df.describe(include=['object']))

# ============================================================================
# STEP 7: CATEGORICAL COLUMNS ANALYSIS
# ============================================================================
print("\n" + "="*80)
print("STEP 7: CATEGORICAL COLUMNS ANALYSIS")
print("="*80)

categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols[:10]:  # Show first 10 categorical columns
    unique_count = df[col].nunique()
    print(f"\n{col}:")
    print(f"  - Unique values: {unique_count}")
    if unique_count <= 20:
        print(f"  - Value counts:")
        print(df[col].value_counts().head(10))

# ============================================================================
# STEP 8: NUMERICAL COLUMNS ANALYSIS
# ============================================================================
print("\n" + "="*80)
print("STEP 8: NUMERICAL COLUMNS ANALYSIS")
print("="*80)

numerical_cols = df.select_dtypes(include=[np.number]).columns
print(f"\nNumerical Columns: {list(numerical_cols)}")

for col in numerical_cols:
    print(f"\n{col}:")
    print(f"  - Min: {df[col].min()}")
    print(f"  - Max: {df[col].max()}")
    print(f"  - Mean: {df[col].mean():.2f}")
    print(f"  - Median: {df[col].median():.2f}")
    print(f"  - Std Dev: {df[col].std():.2f}")

# ============================================================================
# STEP 9: DATA CLEANING
# ============================================================================
print("\n" + "="*80)
print("STEP 9: DATA CLEANING")
print("="*80)

# Create a copy for cleaning
df_clean = df.copy()

print("\nCleaning Steps:")
print("-" * 80)

# 1. Remove duplicates
initial_rows = len(df_clean)
df_clean = df_clean.drop_duplicates()
removed_duplicates = initial_rows - len(df_clean)
print(f"1. Removed {removed_duplicates} duplicate rows")

# 2. Handle missing values in key columns
# For this dataset, we'll identify key columns first
key_columns = ['Title', 'Category', 'Sub-Category', 'Course Type', 'Site']

for col in key_columns:
    if col in df_clean.columns:
        missing_before = df_clean[col].isnull().sum()
        if missing_before > 0:
            # For categorical, fill with 'Unknown'
            df_clean[col].fillna('Unknown', inplace=True)
            print(f"2. Filled {missing_before} missing values in '{col}' with 'Unknown'")

# 3. Clean Rating column (extract numeric value)
if 'Rating' in df_clean.columns:
    print("\n3. Cleaning 'Rating' column:")
    # Extract numeric rating from strings like "4.9stars"
    df_clean['Rating_Numeric'] = df_clean['Rating'].str.extract(r'(\d+\.?\d*)')[0].astype(float)
    print(f"   - Created 'Rating_Numeric' column")
    print(f"   - Range: {df_clean['Rating_Numeric'].min()} to {df_clean['Rating_Numeric'].max()}")

# 4. Clean Number of viewers column
if 'Number of viewers' in df_clean.columns:
    print("\n4. Cleaning 'Number of viewers' column:")
    # Remove commas and convert to numeric with error handling
    df_clean['Number_of_viewers_Numeric'] = pd.to_numeric(
        df_clean['Number of viewers'].str.replace(',', '').str.replace(' ', '').str.extract(r'(\d+)')[0],
        errors='coerce'
    )
    print(f"   - Created 'Number_of_viewers_Numeric' column")
    valid_viewers = df_clean['Number_of_viewers_Numeric'].dropna()
    if len(valid_viewers) > 0:
        print(f"   - Range: {valid_viewers.min():.0f} to {valid_viewers.max():.0f}")
        print(f"   - Valid values: {len(valid_viewers)}/{len(df_clean)}")

# 5. Clean Duration column
if 'Duration' in df_clean.columns:
    print("\n5. Cleaning 'Duration' column:")
    # Extract months from strings like "Approximately 3 months to complete"
    df_clean['Duration_Months'] = pd.to_numeric(
        df_clean['Duration'].str.extract(r'(\d+)\s*month')[0],
        errors='coerce'
    )
    print(f"   - Created 'Duration_Months' column")
    valid_duration = df_clean['Duration_Months'].dropna()
    if len(valid_duration) > 0:
        print(f"   - Range: {valid_duration.min():.0f} to {valid_duration.max():.0f} months")
        print(f"   - Valid values: {len(valid_duration)}/{len(df_clean)}")

# ============================================================================
# STEP 10: SAVE CLEANED DATA
# ============================================================================
print("\n" + "="*80)
print("STEP 10: SAVE CLEANED DATA")
print("="*80)

output_file = '/Users/apple/Downloads/ML & AI/Book-Reviews-and-Summaries/Hands on ML O\'riele/Online_Courses_Cleaned.csv'
df_clean.to_csv(output_file, index=False)
print(f"\n✓ Cleaned data saved to: {output_file}")
print(f"  - Final shape: {df_clean.shape[0]} rows × {df_clean.shape[1]} columns")

# ============================================================================
# STEP 11: VISUALIZATION
# ============================================================================
print("\n" + "="*80)
print("STEP 11: CREATING VISUALIZATIONS")
print("="*80)

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (15, 10)

# Create figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Online Courses Dataset - Exploratory Data Analysis', fontsize=16, fontweight='bold')

# Plot 1: Top 10 Categories
if 'Category' in df_clean.columns:
    top_categories = df_clean['Category'].value_counts().head(10)
    axes[0, 0].barh(range(len(top_categories)), top_categories.values, color='steelblue')
    axes[0, 0].set_yticks(range(len(top_categories)))
    axes[0, 0].set_yticklabels(top_categories.index)
    axes[0, 0].set_xlabel('Count')
    axes[0, 0].set_title('Top 10 Course Categories')
    axes[0, 0].invert_yaxis()

# Plot 2: Rating Distribution
if 'Rating_Numeric' in df_clean.columns:
    axes[0, 1].hist(df_clean['Rating_Numeric'].dropna(), bins=20, color='coral', edgecolor='black')
    axes[0, 1].set_xlabel('Rating')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].set_title('Distribution of Course Ratings')
    axes[0, 1].axvline(df_clean['Rating_Numeric'].mean(), color='red', linestyle='--', label=f'Mean: {df_clean["Rating_Numeric"].mean():.2f}')
    axes[0, 1].legend()

# Plot 3: Duration Distribution
if 'Duration_Months' in df_clean.columns:
    axes[1, 0].hist(df_clean['Duration_Months'].dropna(), bins=15, color='lightgreen', edgecolor='black')
    axes[1, 0].set_xlabel('Duration (Months)')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].set_title('Distribution of Course Duration')

# Plot 4: Top 10 Sites
if 'Site' in df_clean.columns:
    top_sites = df_clean['Site'].value_counts().head(10)
    axes[1, 1].bar(range(len(top_sites)), top_sites.values, color='mediumpurple')
    axes[1, 1].set_xticks(range(len(top_sites)))
    axes[1, 1].set_xticklabels(top_sites.index, rotation=45, ha='right')
    axes[1, 1].set_ylabel('Count')
    axes[1, 1].set_title('Top 10 Course Sites')

plt.tight_layout()
viz_file = '/Users/apple/Downloads/ML & AI/Book-Reviews-and-Summaries/Hands on ML O\'riele/Online_Courses_EDA.png'
plt.savefig(viz_file, dpi=300, bbox_inches='tight')
print(f"\n✓ Visualizations saved to: {viz_file}")

# ============================================================================
# STEP 12: SUMMARY REPORT
# ============================================================================
print("\n" + "="*80)
print("STEP 12: SUMMARY REPORT")
print("="*80)

summary_report = f"""
ONLINE COURSES DATASET - ANALYSIS SUMMARY
{'='*80}

1. DATASET OVERVIEW
   - Total Records: {df.shape[0]:,}
   - Total Columns: {df.shape[1]}
   - Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB

2. DATA QUALITY
   - Duplicate Rows: {duplicates}
   - Columns with Missing Values: {len(missing_data)}
   - Total Missing Values: {df.isnull().sum().sum():,}

3. CLEANED DATASET
   - Final Records: {df_clean.shape[0]:,}
   - Final Columns: {df_clean.shape[1]}
   - Records Removed: {df.shape[0] - df_clean.shape[0]}

4. KEY INSIGHTS
   - Most Common Category: {df_clean['Category'].mode()[0] if 'Category' in df_clean.columns else 'N/A'}
   - Average Rating: {df_clean['Rating_Numeric'].mean():.2f if 'Rating_Numeric' in df_clean.columns else 'N/A'}
   - Average Duration: {df_clean['Duration_Months'].mean():.1f} months (if 'Duration_Months' in df_clean.columns else 'N/A')
   - Most Popular Site: {df_clean['Site'].mode()[0] if 'Site' in df_clean.columns else 'N/A'}

5. OUTPUT FILES
   - Cleaned Data: Online_Courses_Cleaned.csv
   - Visualizations: Online_Courses_EDA.png
   - Analysis Script: online_courses_eda.py

{'='*80}
Analysis completed successfully!
"""

print(summary_report)

# Save summary report
report_file = '/Users/apple/Downloads/ML & AI/Book-Reviews-and-Summaries/Hands on ML O\'riele/EDA_Summary_Report.txt'
with open(report_file, 'w') as f:
    f.write(summary_report)
print(f"\n✓ Summary report saved to: {report_file}")

print("\n" + "="*80)
print("ANALYSIS COMPLETE!")
print("="*80)
