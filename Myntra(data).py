import pandas as pd
df=pd.read_csv('D:\Myntra(data)\Myntra Fasion Clothing.csv')
print('to gather the info the data sheet',df.info())
print(df.head())
BrandName_unique=df['BrandName'].nunique()
print(BrandName_unique)#To get the count of brands
Category_unique=df['Category'].unique()
print(Category_unique)#to get the list of distinct values
category_by_Gender_unique=df['category_by_Gender'].unique()
print(category_by_Gender_unique)#to get the list of distinct values
BrandName_list=df['BrandName'].value_counts()
BrandName_list=BrandName_list.rename_axis('BrandName').reset_index(name='count')
BrandName_list.to_csv('BrandName_list.csv',index=False)
print(BrandName_list)
Avg_OriginalPrice=df['OriginalPrice (in Rs)'].mean()
print(Avg_OriginalPrice)
SizeOption=df['SizeOption'].str.contains('S').sum()
print(SizeOption)
Ratings_null=df['Ratings'].isnull().sum()
print(Ratings_null)
Category=df['Category'].value_counts()
print(Category)
avg_price_by_category=df.groupby('Category')['OriginalPrice (in Rs)'].mean()
print(avg_price_by_category)
highest_rating_individual_category=df.groupby('Individual_category')['Ratings'].mean().sort_values(ascending=False)
print(highest_rating_individual_category)
Category_by_gender=df['category_by_Gender'].value_counts()
print(Category_by_gender)
OriginalPrice=df['OriginalPrice (in Rs)']
DiscountPrice=df['DiscountPrice (in Rs)']
df['discount_pct']=((df['OriginalPrice (in Rs)']-df['DiscountPrice (in Rs)'])/df['OriginalPrice (in Rs)'])*100
dis_per_by_brandname=df.groupby('BrandName')['discount_pct'].mean().sort_values(ascending=False)
print(dis_per_by_brandname)
expensive=df.sort_values('OriginalPrice (in Rs)', ascending=False).head(10)
print(expensive[['BrandName','OriginalPrice (in Rs)']])
filter=df[df['Reviews']>=100]
highest_rated=filter.sort_values('Ratings',ascending=False).head(10)
print(highest_rated[['BrandName','Category','Ratings','Reviews']])
df['discount']=df['DiscountPrice (in Rs)'].notnull()
per_of_dis=df.groupby('Category')['discount'].mean()*100
print(per_of_dis)
western_null=df[df['Category'] == 'Western']['DiscountPrice (in Rs)'].isnull().sum()
western=df[df['Category'] == 'Western'].shape[0]
print("Total=",western)
print("Null=",western_null)
corr_review_ratings=df['Ratings'].corr(df['Reviews'])
print(corr_review_ratings)
corr_disper_review=df['discount_pct'].corr(df['Reviews'])
print(corr_disper_review)
steepest_dis=df.groupby('BrandName')['discount_pct'].mean().sort_values(ascending=False).head(10)
print(steepest_dis)
print(df[df['BrandName']=='HRITIKA'].shape[0])
high_price=df['OriginalPrice (in Rs)'].corr(df['Ratings'])
print(high_price)
max_individual_category=df.groupby('Individual_category')['OriginalPrice (in Rs)'].max()
min_individual_category=df.groupby('Individual_category')['OriginalPrice (in Rs)'].min()
price_range=max_individual_category-min_individual_category
print(price_range.sort_values(ascending=False))
std=df.groupby('Individual_category')['OriginalPrice (in Rs)'].std().sort_values(ascending=False)
print(std)
price=[0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000, float('inf')]
range=['0-500','500-1000','1000-1500','1500-2000','2000-2500','2500-3000','3000-3500','3500-4000','4000-4500','4500-5000','5000+']
df['Price_Range']=pd.cut(df['OriginalPrice (in Rs)'],bins=price,labels=range)
range_rating=df.groupby('Price_Range')['Ratings'].mean().sort_index()
print(range_rating)
uni_brands=df.groupby('BrandName')['category_by_Gender'].nunique()
uni_brands=uni_brands[uni_brands>=2].index.tolist()
print(uni_brands)
filter=df[df['BrandName'].isin(uni_brands)]
price_compare=filter.groupby(['BrandName','category_by_Gender'])['OriginalPrice (in Rs)'].mean()
print(price_compare)
price_pivot = price_compare.unstack()
price_pivot['diff'] = price_pivot['Women'] - price_pivot['Men']
print(price_pivot.sort_values('diff', ascending=False))
print(df['DiscountOffer'].unique()[:10])
percent_40_only=df[df['DiscountOffer']=='40% OFF']
print(percent_40_only)
print(df['DiscountOffer'].dtype)
df['discount_num'] = df['DiscountOffer'].str.extract(r'(\d+)').astype(float)
print(df['discount_num'])
same_product_id=df[df.duplicated(['Product_id'])]
print('number of same product id = ',same_product_id.shape[0])
last=df[df['DiscountPrice (in Rs)'] > df['OriginalPrice (in Rs)']]
print(last.shape[0])
print(last.head())
print(df.info())