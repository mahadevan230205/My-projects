
# # PROJECT 5: Food Delivery Order Analysis (Swiggy/Zomato style)
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

df=pd.read_csv("food_orders.csv")

print(df)
print(df.columns.tolist())  ###['OrderID', 'Customer', 'Restaurant', 'FoodCategory', 'OrderAmount', 'DeliveryTime_min', 'Rating', 'City']

# -----------------------------------------------------
# STEP 2 (Day 25): Explore
# -----------------------------------------------------
# TODO: head, tail, info, describe, isnull().sum()

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# -----------------------------------------------------
# STEP 3 (Day 26): Clean
# -----------------------------------------------------
# TODO: Drop duplicate rows
# TODO: Fill missing 'OrderAmount' with the mean OrderAmount FOR THAT
#       FoodCategory (hint: groupby('FoodCategory')['OrderAmount'].transform('mean'))
# TODO: Fill missing 'Rating' with the overall average rating

##OrderAmount         3
##Rating              2

print(df.duplicated().sum())  ## no duplicate values
print(df)

mean_df=df.groupby("FoodCategory")["OrderAmount"].transform("mean")
print("mean:",mean_df)
df["OrderAmount"]=mean_df


df['Rating'] = df['Rating'].fillna(df['Rating'].mean())
print(df["Rating"])
print(df.isnull().sum())

# -----------------------------------------------------
# STEP 4 (Day 22 + 21): Function with if-elif
# -----------------------------------------------------
# TODO: Write function delivery_speed(minutes) that returns:
#       'Fast' if minutes <= 25, 'Normal' if minutes <= 40, else 'Slow'
# TODO: Create column 'DeliverySpeed' using this function

def DeliverySpeed(minutes):
 if minutes <= 25:
   return("Fast")
 elif minutes <= 40:
   return("Normal")
 else:
   return("Slow")

df["DeliverySpeed"]= df["DeliveryTime_min"].apply(DeliverySpeed)
print(df)
print(df.columns.tolist())

# -----------------------------------------------------
# STEP 5 (Day 27): Filter, sort, rename
# -----------------------------------------------------
# TODO: Filter all orders where DeliverySpeed == 'Slow'
# TODO: Sort by OrderAmount descending, print top 5 biggest orders
# TODO: Rename column 'DeliveryTime_min' to 'DeliveryMinutes'

orders=df[df["DeliverySpeed"]=="Slow"]
print("\n---- Slow deliveries ----")
print("orders:",orders)
top_5=df.sort_values("OrderAmount",ascending=False).head()
print("\n---- Top 5 biggest orders ----")
print(top_5)

df=df.rename(columns={"DeliveryTime_min":"DeliveryMinutes"})
print("column renamed:",df)

# -----------------------------------------------------
# STEP 6 (Day 28): GroupBy
# -----------------------------------------------------
# TODO: Group by 'Restaurant' -> total OrderAmount (this is restaurant revenue)
# TODO: Group by 'FoodCategory' -> average Rating
# TODO: Group by ['City', 'FoodCategory'] -> total OrderAmount (multi-level)

restaurant_revenue = df.groupby('Restaurant')['OrderAmount'].sum().sort_values(ascending=False)
print("\n---- Revenue by restaurant ----")
print(restaurant_revenue)

rating=df.groupby("FoodCategory")["Rating"].mean()
print(rating)

multi_lev=df.groupby(['City', 'FoodCategory'])["OrderAmount"].sum()
print(multi_lev)

# # -----------------------------------------------------
# # STEP 7 (Day 23): NumPy
# # -----------------------------------------------------
# # TODO: Convert 'DeliveryMinutes' to NumPy array
# # TODO: Print np.mean(), np.median(), np.max() of the array

delivery_array = df['DeliveryMinutes'].to_numpy()
print(f"\nMean delivery time: {np.mean(delivery_array):.1f} min, "
      f"Median: {np.median(delivery_array):.1f}, Max: {np.max(delivery_array)}")

# # -----------------------------------------------------
# # STEP 8 (Day 20 + 21): Dict + loop + condition
# # -----------------------------------------------------
# # TODO: Build a dict restaurant_revenue mapping Restaurant -> total revenue
# # TODO: Loop through it; print "<Restaurant> is a TOP performer" if
# #       revenue > 1500, else "<Restaurant> needs promotion"

restaurant_revenue_dict = restaurant_revenue.to_dict()
print("\n---- Restaurant performance ----")
for restaurant, revenue in restaurant_revenue_dict.items():
    if revenue > 1500:
        print(f"{restaurant} is a TOP performer (Revenue: {revenue:.0f})")
    else:
        print(f"{restaurant} needs promotion (Revenue: {revenue:.0f})")


# # -----------------------------------------------------
# # STEP 9 (Day 30): File handling
# # -----------------------------------------------------
# # TODO: Export cleaned df to 'orders_cleaned.csv'

df.to_csv('orders_cleaned.csv')
print('file saved:orders_cleaned.csv')

# # -----------------------------------------------------
# # STEP 10 (Day 31): Matplotlib
# # -----------------------------------------------------
# # TODO: Histogram -> distribution of DeliveryMinutes
# # TODO: Bar chart -> revenue by restaurant


plt.hist(df["DeliveryMinutes"], bins=6, color="mediumpurple", edgecolor="black")
plt.title("Distribution of DeliveryMinutes")
plt.xlabel("DeliveryMinutes")
plt.ylabel("Number of Deliveries")
plt.savefig("chart_delivery_time_dist.png")
plt.show()

plt.figure(figsize=(6, 4))
plt.bar(restaurant_revenue.index, restaurant_revenue.values, color='mediumseagreen')
plt.title("Revenue by Restaurant")
plt.xlabel("Restaurant")
plt.ylabel("Revenue (Rs)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("chart_revenue_by_restaurant.png")
plt.close()
plt.show()

# # -----------------------------------------------------
# # STEP 11 (Day 32): Seaborn
# # -----------------------------------------------------
# # TODO: sns.boxplot of Rating grouped by FoodCategory
# # TODO: sns.heatmap correlation between OrderAmount, DeliveryMinutes, Rating
 #### Distribution plot 

rate = df.groupby("FoodCategory")["Rating"].mean().sort_values(ascending=False)
print(rate)

sns.histplot(rate.values, bins=6, kde=True, color="teal")
plt.title("Distribution of Rating")
plt.xlabel("Rating")
plt.ylabel("FoodCategory")    
plt.show()
plt.savefig("dist.png")

sns.kdeplot(rate.values, color="darkorange", fill=True)
plt.title("Density Curve of Rating")
plt.xlabel("Rating")
plt.show()
plt.savefig("kde.png")

correlation= df[["OrderAmount","DeliveryMinutes","Rating"]].corr()
print(correlation)

sns.heatmap(correlation, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation between OrderAmount, DeliveryMinutes and Rating")
plt.savefig("heatmap.png")
plt.show()

# # -----------------------------------------------------
# # STEP 12: Conclusion
# # -----------------------------------------------------
# # TODO: Print the top restaurant by revenue, the slowest delivery category,
# #       and one operational recommendation

slowest= df[df["DeliverySpeed"] == "Slow"]
top_restaurant = restaurant_revenue.idxmax()
slowest_category = df.groupby('FoodCategory')['DeliveryMinutes'].mean().idxmax()

print("\n---- CONCLUSION ----")
print(f"Top restaurant by revenue: {top_restaurant}")

print(f"Slowest delivery category on average: {slowest_category}")


# ### create own delivery app to improve the delivery speed