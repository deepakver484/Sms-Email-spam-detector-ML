# Description

#### SMS/Email Spam Detector using Machine Learning is a powerful project designed to identify and classify spam messages in SMS and email communications. Leveraging various data cleaning techniques, this project ensures data quality and performs Exploratory Data Analysis (EDA) to gain insights into the dataset's characteristics. The textual messages are transformed into numerical feature vectors using vectorization techniques and the Natural Language Toolkit (NLTK) for text processing and analysis.

# Key Features
* Data Cleaning Techniques: This project employs robust data cleaning techniques to preprocess the raw SMS and email data, ensuring high-quality data for precise and accurate predictions.

* Exploratory Data Analysis (EDA): Gain insights into the dataset's characteristics with EDA techniques, enhancing the understanding of underlying patterns and trends.

* Vectorization and NLTK: Transform textual messages into numerical feature vectors using vectorization techniques, coupled with the powerful Natural Language Toolkit (NLTK) for text processing and analysis.

* Machine Learning Models: Several machine learning models are implemented and evaluated to predict whether a given message is spam or not. The project includes popular classifiers like Support Vector Machines (SVM), Random Forest, and Naive Bayes, providing a comparative analysis of their performance.

* Streamlit Deployment: The trained machine learning model is deployed using Streamlit, offering a user-friendly web application where users can interact with the spam detector seamlessly.

# Tech Stack Used
- Python
- Pandas
- Scikit-learn (Sklearn)
- Natural Language Toolkit (NLTK)
- Streamlit


# Insights
![](https://github.com/Harsh9174/Sms-Email-spam-detector-ML/blob/main/Data/Insights.png?raw=true)
![](https://github.com/Harsh9174/Sms-Email-spam-detector-ML/blob/main/Data/spam%20or%20ham.png?raw=true)

# Model 
![](https://github.com/Harsh9174/Sms-Email-spam-detector-ML/blob/main/Data/Screenshot%20(15).png?raw=true)

# Challenges Faced

- Data Imbalance: Dealing with an imbalanced dataset where the number of legitimate messages far outweighs the number of spam messages could have impacted the model's ability to distinguish between classes.

- Feature Extraction: Identifying relevant features from raw text data, such as email or SMS content, and converting them into suitable formats for machine learning models could have required advanced natural language processing (NLP) techniques.

- Model Generalization: Building a machine learning model that effectively generalizes across different types of spam messages, considering the variety of tactics used by spammers, might have posed challenges.

- Model Selection: Choosing the most appropriate machine learning algorithm for your specific task, whether it's a classic classifier like Naive Bayes or a more complex algorithm like Support Vector Machines (SVM), required experimentation and evaluation.

- Model Evaluation: Properly evaluating model performance, especially in the context of spam detection where false positives and false negatives have different consequences, demanded selecting appropriate evaluation metrics.

- Tuning Hyperparameters: Fine-tuning model hyperparameters to achieve optimal performance and prevent issues like underfitting or overfitting required a combination of domain knowledge and experimentation.

- Deployment Challenges: Integrating the trained model into a user-friendly application, such as a web interface, and ensuring real-time predictions while maintaining model accuracy demanded effective deployment strategies.






