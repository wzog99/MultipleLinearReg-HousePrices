# MultipleLinearReg-HousePrices
Kaggle dataset on housing data for Ames Iowa

### Purpose 
Create a multiple linear regression model for home price data for a rural town Iowa.

### Goal
Creating a linear model will enable future price prediction on houses, given the same features. Being able to predict the house sale price and the current asking price, I'll be able to see whether the house is overprice, or underpriced, compared to the prediction. 

### Process
- Data cleaning; replacing/removing NaNs, and columns that have too many NaNs to be considered viable features.
- Seperating catagorical and continuous features
- Feature Scaling numerical features to standardize the features and eliminate outliers
- Test for intercorrelation amongst features using created function
- Try using Linear Regression inspite of large amount of features
    - Overfitting, and getting poor results for R^2 on the testing data
- Now going to use Lasso regression that'll zero out unneeded terms
    - The test set scored an R^2 of approximately .7 and the train scored about .87
    - 
    - Lasso regression scored an R^2 around .902 with an adjusted R^2 around .75, which is permissable
    - Optimizing alpha based on adjusted alpha will achive a more generalized model and remove unneeded terms
    - Best alpha ~ 1.34 (But this bound to change with adjustments to code)
- 




