# Demand Forecasting
This repository is used to learn about different time series techniques for store-item product forecasting using Kaggle dataset.

## Business Use Case
- Demand Forecasting is a field of predictive analytics used to predict customer demands to optimize supply decisions.
- How many products should the company have in stock? How often should they be restocked?
- Incorrect inventory management can lead to the following problems:
  - Customer wants to purchase a product, however not available. This leads to loss in potential profit and customer dissatisfaction.
  - Too many products are stocked and remain unsold. This is a problem for products with short shelf life.
- The task is to use historical sales records to estimate future demand.

## Challenges
- There are a lot of external factors that directly affect the number of purchases:
  - Seasonality
  - Weather
  - Events
  - Promotions
  - Weird customer behaviour

## Dataset
- Kaggle dataset
  - sales_train.csv: Daily historical data from January 2013 to October 2015
  - test.csv: Need to forecast the sales for these shops and products for future.
  - items.csv: Supplemental information about the items/products
  - item_categories.csv: Supplemental information about the items categories.
  - shops.csv: Supplemental information about the shops.
