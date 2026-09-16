 # PROJECT 5: Food Delivery Order Analysis (Swiggy/Zomato style)
# ------------------------------------------------------------------
# Analyze order data across restaurants and cities. Complete each TODO.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------
# STEP 1 (Day 24): Load data
# -----------------------------------------------------
# TODO: Read 'food_orders.csv' into df
 
df=read_csv("food_orders.csv")
print(df)


# -----------------------------------------------------
# STEP 2 (Day 25): Explore
# -----------------------------------------------------
# TODO: head, tail, info, describe, isnull().sum()


# -----------------------------------------------------
# STEP 3 (Day 26): Clean
# -----------------------------------------------------
# TODO: Drop duplicate rows
# TODO: Fill missing 'OrderAmount' with the mean OrderAmount FOR THAT
#       FoodCategory (hint: groupby('FoodCategory')['OrderAmount'].transform('mean'))
# TODO: Fill missing 'Rating' with the overall average rating

##OrderAmount         3
##Rating              2

# -----------------------------------------------------
# STEP 4 (Day 22 + 21): Function with if-elif
# -----------------------------------------------------
# TODO: Write function delivery_speed(minutes) that returns:
#       'Fast' if minutes <= 25, 'Normal' if minutes <= 40, else 'Slow'
# TODO: Create column 'DeliverySpeed' using this function


# -----------------------------------------------------
# STEP 5 (Day 27): Filter, sort, rename
# -----------------------------------------------------
# TODO: Filter all orders where DeliverySpeed == 'Slow'
# TODO: Sort by OrderAmount descending, print top 5 biggest orders
# TODO: Rename column 'DeliveryTime_min' to 'DeliveryMinutes'


# -----------------------------------------------------
# STEP 6 (Day 28): GroupBy
# -----------------------------------------------------
# TODO: Group by 'Restaurant' -> total OrderAmount (this is restaurant revenue)
# TODO: Group by 'FoodCategory' -> average Rating
# TODO: Group by ['City', 'FoodCategory'] -> total OrderAmount (multi-level)


# -----------------------------------------------------
# STEP 7 (Day 23): NumPy
# -----------------------------------------------------
# TODO: Convert 'DeliveryMinutes' to NumPy array
# TODO: Print np.mean(), np.median(), np.max() of the array

# -----------------------------------------------------
# STEP 8 (Day 20 + 21): Dict + loop + condition
# -----------------------------------------------------
# TODO: Build a dict restaurant_revenue mapping Restaurant -> total revenue
# TODO: Loop through it; print "<Restaurant> is a TOP performer" if
#       revenue > 1500, else "<Restaurant> needs promotion"


# -----------------------------------------------------
# STEP 9 (Day 30): File handling
# -----------------------------------------------------
# TODO: Export cleaned df to 'orders_cleaned.csv'


# -----------------------------------------------------
# STEP 10 (Day 31): Matplotlib
# -----------------------------------------------------
# TODO: Histogram -> distribution of DeliveryMinutes
# TODO: Bar chart -> revenue by restaurant




# -----------------------------------------------------
# STEP 11 (Day 32): Seaborn
# -----------------------------------------------------
# TODO: sns.boxplot of Rating grouped by FoodCategory
# TODO: sns.heatmap correlation between OrderAmount, DeliveryMinutes, Rating


# -----------------------------------------------------
# STEP 12: Conclusion
# -----------------------------------------------------
# TODO: Print the top restaurant by revenue, the slowest delivery category,
#       and one operational recommendation
