
import pandas as pd
import matplotlib.pyplot as plt


####################################################
# By: Fady Elgohary
# Date: December 30, 2025
#
# This program extracts all values of Moncton
# and inserts it into a new csv file.
# The csv file is then melted and data is
# presented on a line graph
#
####################################################

# Read the file and extract data
df = pd.read_csv("Canada_3_Bed_rent.csv")

target = "Moncton"

new_df = df[df["City"] == target]

new_df.to_csv("Moncton_data.csv", index=False)

# Melt the data for better handling
df = pd.read_csv("Moncton_data.csv")

melted = pd.melt(df, id_vars=('City', 'Province'), var_name='Year', value_name='Rent')

melted.to_csv("Moncton_data_melted.csv", index=False)

# Plot the Graph

plt.plot(melted['Year'], melted['Rent'])

plt.show()


