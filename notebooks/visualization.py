import streamlit as st
import pandas as pd

import plotly.express as px
import altair as alt

from datetime import date, datetime


data = pd.read_csv("../data/train.csv")


# Function used to generate plotly chart that displays all sales for all stores
def generate_sales_plot(data, date, sales):
	data = data.groupby(date, as_index = False)[sales].sum()
	fig = px.line(data, x = date, y = sales)
	return fig

# Function used to generate plotly chart that displays sales by item or store
def generate_sales_store_item_plot(data, date, sales, store_item, store_item_list):
	data = data[data[store_item].isin(store_item_list)]
	data = data.groupby([date,store_item], as_index = False)[sales].sum()
	fig = px.line(data, x=date, y=sales, color = store_item)
	return fig

# Function used to return the data given a start and end date
def generate_data_date(data, start_date, end_date):
	start_date = start_date.strftime("%Y-%m-%d")
	end_date = end_date.strftime("%Y-%m-%d")
	date_mask = (data['date'] >= start_date) & (data['date'] <= end_date)
	data = data.loc[date_mask]
	return data

# Function used to generate plotly chart that display histogram of sales by store and item
def generate_bar_charts(data, sales, store_item):
	data = data.groupby(store_item, as_index = False)[sales].sum()
	fig = px.bar(data, x= store_item, y= sales)
	return fig


def main():

	# NUMBER OF SALES PLOT
	st.header("Number of Sales")
	st.plotly_chart(generate_sales_plot(data, 'date', 'sales'), use_container_width = True)

	# Two columns, one for the start date input and one for the end date input
	date_1, date_2 = st.columns(2)

	with date_1:
		start_date = st.date_input("Start Date")

	with date_2:
		end_date = st.date_input("End Date")


	# Histogram of sales by store and by item
	st.plotly_chart(generate_bar_charts(generate_data_date(data, start_date, end_date), 'sales', 'store'))
	st.plotly_chart(generate_bar_charts(generate_data_date(data, start_date, end_date), 'sales', 'item'))


	# SALES BY STORE
	st.header("Number of Sales by Store")

	# Multiselect tool that allows you to look at sales for selected stores
	stores = st.multiselect("Select Store", data['store'].unique(), default = [1])

	st.plotly_chart(generate_sales_store_item_plot(data, 'date', 'sales', 'store',  stores), 
		use_container_width = True)

	# SALES BY ITEM
	st.header("Number of Sales by Item")

	# Multiselect tool that allows you to look at sales for selected items
	items = st.multiselect("Select Item", data['item'].unique(), default = [1])

	st.plotly_chart(generate_sales_store_item_plot(data, 'date', 'sales', 'item',  items), 
		use_container_width = True)

main()



