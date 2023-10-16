# Real-Estate-Prediction-Model
Small project for practicing the creation and training of machine learning models.


This project was undertaken to showcase the ability to scrape, clean, manipulate, and organize data effectively. With the curated data, visualizations were crafted to analyze the patterns and insights within. Using this data, a linear regression model was implemented to predict real estate prices based on geocode location and the month of the year.

Project Highlights
Data Scraping: Developed custom scraping scripts to gather real estate sales data directly from the Whatcom County Assessor's Office website.
Data Cleaning: Managed missing data, outliers, and errors to prepare the dataset for analysis and modeling.
Data Visualization: Developed informative graphs to extract and visualize insights from the data.
Machine Learning: Created a linear regression model to predict real estate prices.
Results & Limitations
The current model has a Mean Absolute Error (MAE) of $500,000. This means that, on average, the model's predictions are off by a margin of $500k. This limitation arises primarily due to the constraints in the available data features. Attributes such as bedroom count, bathroom count, living square footage, and acreage were not available in the dataset, which are pivotal in predicting real estate prices more accurately.

Future Directions
The current project serves as a demonstration of foundational data science and machine learning skills. With access to richer and more detailed data, the prediction accuracy can be substantially improved. Future iterations of this project may expand on incorporating more features, refining the model, and potentially exploring more advanced machine learning techniques to better predict real estate prices.

Project Structure
data/: Contains datasets used in this project.
src/: Main codebase, with scripts for scraping, preprocessing, and modeling.
notebooks/: Jupyter notebooks used for exploratory data analysis.
models/: Trained linear regression model.
output/: Graphs and visualizations generated from the dataset.
Acknowledgements
Special thanks to the following tools and libraries that made this project possible:

ChatGPT by OpenAI: Assisted in various aspects of the project, from conceptualization to completion.
BeautifulSoup: Used for parsing HTML and extracting data from the Whatcom County Assessor's Office website.
Requests: Enabled HTTP requests for the data scraping process.
Pandas: Facilitated data manipulation and analysis.
Scikit-learn (sklearn): The main library behind the machine learning model, linear regression in this case.
Matplotlib: Assisted in creating visualizations and graphs for data analysis.
