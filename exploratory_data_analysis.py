

import numpy as np
import pandas as pd

df = pd.read_csv('Social_media_impact_on_life.csv')

## Data Collection

# Data comes from 4500 high school-post docs

## summary statistics / exploration

df.columns # vars: gpa, sleep quality,
df.groupby(['Gender']).count() # mostly balanced but more men in most categories than females
df.groupby(['Gender']).count() # but more females in total in the survey
df['Academic_Level'].unique()

df.isna().sum() # very filled... this dataset might be ai generated

## visualizations

## research question
