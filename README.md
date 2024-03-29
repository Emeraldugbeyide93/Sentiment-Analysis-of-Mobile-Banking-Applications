
# Sentiment Analysis of Mobile Bank Applications
## Overall Description
This repository contains files used for a course project on sentiment analysis of Mobile Banking Applications with focus on 10 UK Banks(mainly inolved in retail banking). This project is focused only on banks in the UK.
## Dataset
The data for this project was primarily sourced. The dataset contains reviews of customers of specific banks on how satisfied they are with the service provided by their banks through its mobile banking application. The key platforms for scrapping the reviews used for this project were Playstore and Appstore. 
The datasets are in two parts. The non-labelled dataset(i.e the scrapped one with no sentiment or data cleansing) and the sentiment labelled dataset.
Each dataset was analyzed individually because of the size and in order to achieve optimal results and no merging of datasets was done.

The variables found in each dataset upon scrapping are;

GOOGLE PLAY: ReviewId,	UserName,	UserImage, Content,	Score, ThumbsUpCount,	ReviewCreatedVersion,	At,	ReplyContent,	RepliedAt.

APPSTORE: Review,	UserName,	Date,	IsEdited,	Rating,	Title,	DeveloperResponse.

NOTE: The variables did not remain constant till the end of the project as some were deemed irrelevant for the project hence were deleted and some were renamed.

NOTE: Only the dataset of one bank per platform will be uploaded(BARCLAYS). This is because the datasets pretty much has the same variables across the banks and the analysis codes are pretty much the same.
## Code
The codes used for each step of the project can be found in the code folder. The codes are broken into 3 parts;

*Scrapping codes(Codes used for scrapping all the data used for this project per bank).

*Sentiment Labelling Codes(This stage inolved cleansing and labelling the dataset using the lexicon-based sentiment labeller VADER).

*Sentiment Analysis(This Stage involved different analysis of the dataset, wordcloud visualizations, k-fold cross validation etc)

I tried to simplify the codes as best as I could by adding description in order to aid better understanding.

## Classifiers
The Classification models used in this project are(in no particular order);

*SVM(Support Vector Machine)

*GB(Gradient Boosting)

*RF(Random Forest)

*Logistic Regression

*XGBoost

## Requirements
The classifiers work for python 2.7, 3.0 and above
To use these algorithms you should install : sklearn 0.14 version (http://scikit-learn.org/dev/index.html) , numpy (http://www.numpy.org/), nltk 3 with full packages using nltk.download() instruction in python. A full list of packages used on this project are found in the code used for the sentiment analysis.

## Further Analysis
A statistical Analysis was carried out on the results gotten using the two way ANOVA without replication and this was done using Microsoft Excel.

## NOTE
This is my first ever project on sentiment analysis and it was an interesting one. I hope these codes help someone out there as well.

THANK YOU!

DESCRIPTION
A sentiment Analysis Project of mobile banking applications with focus on 10 UK Retail focused Banks using customer reviews on Google Play Store and Apple Store.
