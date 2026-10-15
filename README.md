 Myntra Product Analysis

Exploratory data analysis of **526,564 fashion products** listed on Myntra, an Indian e-commerce marketplace. The project answers practical pricing, discounting and ratings questions using Python (pandas), then reproduces the analysis in MongoDB and BI tools.

Dataset

- Source: https://www.kaggle.com/datasets/manishmathias/myntra-fashion-dataset
- Size: 526,564 rows, 13 original columns
- Key columns: 'BrandName`, `Category`, `Individual_category`, `category_by_Gender`, `OriginalPrice (in Rs)`, `DiscountPrice (in Rs)`, `DiscountOffer`, `SizeOption`, `Ratings`, `Reviews`
- The raw CSV is not included in this repo because of its size. Download it from the link above and place it in `data/`.

Tools used

Python: Pandas for Cleaning, exploration, 24 analysis questions
MongoDB (mongosh): RUD operations, aggregation pipelines, sort/limit queries 
Tableau Public: Interactive charts and dashboard 
Excel / Looker Studio : PivotTables and dashboards 
MySQL : SQL versions of the pandas questions (in progress)

Questions explored

The analysis is organized as 24 questions in four levels:

1. Basic exploration: unique brands, categories, most common size options, missing ratings
2. Filtering and grouping: average price per category, rating by sub-category, discount per brand, top-N products
3. Relationships: correlations between price, rating, reviews and discount; price-bucket analysis with 'pd.cut()`; brand pricing by gender
4. Data quality: missing-value handling, extracting numbers from text ("40% OFF" to 40), duplicate IDs, price consistency checks

Key findings

- Western wear is almost never discounted. Only 47 of 140,992 Western products (0.03%) have a discount price, while every other category sits between roughly 74% and 95%.
- Price barely predicts rating. The correlation is weakly negative (-0.076). Average rating drifts from 4.23 in the 0-500 rupee bucket to 3.96 in the 5000+ bucket.
- Reviews are not tied to rating or discount size. Correlations with rating (0.048) and discount percentage (0.055) are both near zero.
- Most brands that sell to both genders price women's items higher. Some exceptions exist, so the pattern is not universal.
- Steepest average discount: HRITIKA at about 88.8% across 134 products.
- Widest price range: lehenga-choli, with a gap of 88,375 rupees between its cheapest and most expensive product.
- Missing ratings are a natural state, not an error.** 336,152 products (64%) have no ratings or reviews, most likely because they haven't been reviewed yet. They are kept as `NaN` and filtered only where an analysis needs a rating.
- Data integrity checks passed. No duplicate Product_id values, and no product has a discount price higher than its original price.

MongoDB work

Using the same data loaded into a products collection:

- CRUD: insertOne, insertMany, find, findOne, updateOne, updateMany, deleteOne, deleteMany
- Aggregation:$match, $group, $sum, $avg, $min, $max, $count, plus $addFields to compute discount percentage inside the pipeline
- Sort and limit: ascending and descending sorts, combined filter + sort + limit queries

Queries are in (mongodb/queries.js).

Repository structure


myntra-product-analysis/

1. README.md
2. data/       # dataset download instructions
3. notebooks/  # pandas analysis (24 questions)
4. mongodb/    # mongosh queries
5. visuals/    # Tableau / Excel / Looker Studio screenshots


Dashboards

- Tableau Public: `<add link once published>`

How to reproduce

1. Download the dataset and place the CSV in data/.
2. Install dependencies: pip install pandas sqlalchemy pymysql pymongo
3. Open notebooks/ and run the notebook top to bottom.
4. For MongoDB, import the CSV into a products collection, then run the queries in mongodb/queries.js with mongosh.

What I learned

- Validating the same result across tools (pandas, Tableau, MongoDB) is a good check that an analysis is correct.
- Always check data types and real values before writing extraction or aggregation code.
- Unusual results, like the Western discount rate, deserve a sanity check before being reported as findings.
- Choose the aggregation (mean, sum, max) from the wording of the business question.
