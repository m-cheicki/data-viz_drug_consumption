# Python for data analysis : Drug consumption case

<a href="https://github.com/m-cheicki/data-viz_drug_consumption/raw/main/CELIE_CHEICKISMAIL_Drug_Consumption.pdf" download>Download the presentation</a>

## Dataset information

Database contains records for 1885 respondents. <br/>
For each respondent 12 attributes are known: <br/>
Personality measurements which include :

-   NEO-FFI-R (neuroticism, extraversion, openness to experience, agreeableness, and conscientiousness),
-   BIS-11 (impulsivity),
-   and ImpSS (sensation seeking),
-   level of education,
-   age,
-   gender,
-   country of residence and
-   ethnicity.

All input attributes are originally categorical and are quantified. After quantification values of all input features can be considered as real-valued. <br/>
In addition, participants were questioned concerning their use of 18 legal and illegal drugs :

-   alcohol,
-   amphetamines,
-   amyl nitrite,
-   benzodiazepine,
-   cannabis,
-   chocolate,
-   cocaine,
-   caffeine,
-   crack,
-   ecstasy,
-   heroin,
-   ketamine,
-   legal highs,
-   LSD,
-   methadone,
-   mushrooms,
-   nicotine and
-   volatile substance abuse (VSA)
-   and one fictitious drug (Semeron) which was introduced to identify over-claimers.

For each drug they have to select one of the answers:

-   never used the drug,
-   used it over a decade ago,
-   or in the last decade,
-   year,
-   month,
-   week, or
-   day.

Database contains 18 classification problems. <br/>
Each of independent label variables contains seven classes: "Never Used", "Used over a Decade Ago", "Used in Last Decade", "Used in Last Year", "Used in Last Month", "Used in Last Week", and "Used in Last Day".

Problem which can be solved:

-   Seven class classifications for each drug separately.
-   Problem can be transformed to binary classification by union of part of classes into one new class. For example, "Never Used", "Used over a Decade Ago" form class "Non-user" and all other classes form class "User".
-   The best binarization of classes for each attribute.
-   Evaluation of risk to be drug consumer for each drug.

Detailed description of database and process of data quantification are presented in <br/>
E. Fehrman, A. K. Muhammad, E. M. Mirkes, V. Egan and A. N. Gorban,
["The Five Factor Model of personality and evaluation of drug consumption risk.,"](https://arxiv.org/abs/1506.06297), 2015

Paper above solve binary classification problem for all drugs. For most of drugs sensitivity and specificity are greater than 75%.

## Purpose of the project

Different possibilities of prediction were available to us, we chose to predict for a person when that person used a specific drug for the last time. We tried several methods of machine learning, SVC, Decision Tree, Random Forest and deep learning. Out of the first three, SVC and Random Forest showed better results than Decision Tree, without any tuning. So we focused on finding the best hyperparameters using gridSearch. After the use of gridSearch, the model chosen for the API was the Random Forest.

The deep learning was used under another approach. With it, we tried to predict which drugs have been consumed in the last 24 hours for a person. To do so, it was necessary to process and transform the prediction columns to show 1's instead of CL6 and 0's otherwise. However, we did not manage to have an accuracy of more than 50% on the training data. The keras tuner was then used to try to get better parameters but without success.

<a href="https://github.com/m-cheicki/data-viz_drug_consumption/raw/main/CELIE_CHEICKISMAIL_Drug_Consumption.pdf" download>Download the presentation</a>
