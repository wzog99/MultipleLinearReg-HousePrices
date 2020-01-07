def Data_prep(DataFrame):
    drop_list = ['Utilities_NoSeWa', 'Exterior2nd', 'YearRemodAdd', 'LotShape', 'MSSubClass', 'TotalBsmtSF', 'Alley', 'GarageYrBlt', 'PoolQC', 'FireplaceQu', 'MiscFeature', 'MiscFeature']
    
    targetdf = traindf[['Id', 'SalePrice']]
    traindf.drop('SalePrice', axis=1, inplace=True)
    
    traindf = traindf.drop(drop_list, axis=1)
    
    traindf_cat = traindf[['Id', 'MSZoning']].copy()
    traindf.drop('MSZoning', axis=1, inplace=True)
    
    lotfront = traindf.LotFrontage.mean()
    traindf.LotFrontage.fillna(value=lotfront, inplace=True)
    
    traindf_cat['Street'] = traindf.Street
    traindf.drop('Street', axis=1, inplace=True)
    
    traindf_cat['LandContour'] = traindf.LandContour
    traindf.drop('LandContour', axis=1, inplace=True)
    
    traindf_cat['Utilities'] = traindf.Utilities
    traindf.drop('Utilities', axis=1, inplace=True)
    
    traindf_cat['LotConfig'] = traindf.LotConfig
    traindf.drop('LotConfig', axis=1, inplace=True)
    
    traindf_cat['LandSlope'] = traindf.LandSlope
    traindf.drop('LandSlope', axis=1, inplace=True)
    
    traindf_cat['Neighborhood'] = traindf.Neighborhood
    traindf.drop('Neighborhood', axis=1, inplace=True)
    
    traindf_cat['Condition1'] = traindf.Condition1
    traindf.drop('Condition1', axis=1, inplace=True)

    traindf_cat['Condition2'] = traindf.Condition2
    traindf.drop('Condition2', axis=1, inplace=True)
    
    traindf_cat['BldgType'] = traindf.BldgType
    traindf.drop('BldgType', axis=1, inplace=True)
    
    traindf_cat['HouseStyle'] = traindf.HouseStyle
    traindf.drop('HouseStyle', axis=1, inplace=True)
    
    traindf_cat['RoofStyle'] = traindf.RoofStyle
    traindf.drop('RoofStyle', axis=1, inplace=True)
    
    traindf_cat['RoofMatl'] = traindf.RoofMatl
    traindf.drop('RoofMatl', axis=1, inplace=True)
    
    traindf_cat['Exterior1st'] = traindf.Exterior1st
    traindf.drop('Exterior1st', axis=1, inplace=True)

    traindf.MasVnrType.fillna(value='None', inplace=True)
    traindf_cat['MasVnrType'] = traindf.MasVnrType
    traindf.drop('MasVnrType', axis=1, inplace=True)
    
    traindf.ExterQual = traindf.ExterQual.replace({'Ex': 10., 'Gd':7., 'TA':4., 'Fa':2, 'Po':1.}, value=None)
    
    traindf.ExterCond = traindf.ExterCond.replace({'Ex': 10., 'Gd':7., 'TA':4., 'Fa':2, 'Po':1.}, value=None)
    
    traindf_cat['Foundation'] = traindf.Foundation
    traindf.drop('Foundation', axis=1, inplace=True)
    
    traindf.MasVnrArea.fillna(value=0.00, inplace=True) 
    
    traindf.BsmtCond = traindf.BsmtCond.replace({'Ex': 10, 'Gd':7, 'TA':4, 'Fa':2, 'Po':1}, value=None)
    traindf.BsmtCond.fillna(value=0, inplace=True)
    
    traindf.BsmtFinType1 = traindf.BsmtFinType1.replace({'GLQ': 10, 'ALQ':7, 'BLQ':5, 'Rec':4, 'LwQ':2, 'Unf':1}, value=None)
    traindf.BsmtFinType1.fillna(value=0, inplace=True)
    
    traindf.BsmtExposure = traindf.BsmtExposure.replace({'Gd':10, 'Av': 7, 'Mn':2, 'No':1}, value=None)
    traindf.BsmtExposure.fillna(value=0, inplace=True)
    
    traindf.BsmtQual = traindf.BsmtQual.replace({'Ex':10, 'Gd':7, 'TA': 4, 'Fa':2, 'Po':1}, value=None)
    traindf.BsmtQual.fillna(value=0, inplace=True)
    
    traindf.BsmtFinType2 = traindf.BsmtFinType2.replace({'GLQ': 10, 'ALQ':7, 'BLQ':5, 'Rec':5, 'LwQ':2, 'Unf':1}, value=None)
    traindf.BsmtFinType2.fillna(value=0, inplace=True)
    
    traindf_cat['Heating'] = traindf.Heating
    traindf.drop('Heating', axis=1, inplace=True)
    
    traindf.HeatingQC = traindf.HeatingQC.replace({'Ex': 10, 'Gd':7, 'TA':4, 'Fa':2, 'Po':1}, value=None)
    traindf.HeatingQC.fillna(value=0, inplace=True)
    
    traindf_cat['CentralAir'] = traindf.CentralAir
    traindf.drop('CentralAir', axis=1, inplace=True)
    
    traindf_cat['Electrical'] = traindf.Electrical
    traindf.drop('Electrical', axis=1, inplace=True)
    traindf_cat.Electrical.fillna(value='SBrkr', inplace=True)
    
    traindf.KitchenQual = traindf.KitchenQual.replace({'Ex': 10, 'Gd':7, 'TA':5, 'Fa':3, 'Po':1}, value=None)
    traindf.KitchenQual.fillna(value=1, inplace=True)
    
    traindf_cat['Functional'] = traindf.Functional
    traindf.drop('Functional', axis=1, inplace=True)
    
    traindf_cat['GarageType'] = traindf.GarageType
    traindf.drop('GarageType', axis=1, inplace=True)
    traindf_cat.GarageType.fillna(value='NoGarage', inplace=True)
    
    traindf.GarageFinish = traindf.GarageFinish.replace({'Fin': 7, 'RFn':4, 'Unf':1}, value=None)
    traindf.GarageFinish.fillna(value=0., inplace=True)
    
    traindf.GarageQual = traindf.GarageQual.replace({'Ex': 10, 'Gd':7, 'TA':4, 'Fa':2, 'Po':1}, value=None)
    traindf.GarageQual.fillna(value=0, inplace=True)
    
    traindf.GarageCond = traindf.GarageCond.replace({'Ex': 10, 'Gd':7, 'TA':4, 'Fa':2, 'Po':1}, value=None)
    traindf.GarageCond.fillna(value=0, inplace=True)
    
    traindf_cat['PavedDrive'] = traindf.PavedDrive
    traindf.drop('PavedDrive', axis=1, inplace=True)
    
    traindf_cat['Fence'] = traindf.Fence
    traindf.drop('Fence', axis=1, inplace=True)
    traindf_cat.fillna(value='NoFence', inplace=True)
    
    traindf_cat['MoSold'] = traindf.MoSold
    traindf.drop('MoSold', axis=1, inplace=True)
    
    traindf_cat['SaleType'] = traindf.SaleType
    traindf.drop('SaleType', axis=1, inplace=True)
    
    traindf_cat['SaleCondition'] = traindf.SaleCondition
    traindf.drop('SaleCondition', axis=1, inplace=True)
    
    traindf['ExterQual'] = traindf.ExterQual.astype(int)
    traindf['ExterCond'] = traindf.ExterCond.astype(int)
    
    
    'Utilities_NoSeWa', 'Condition2_RRAe', 'Condition2_RRAn', 'RoofStyle_Shed', 'RoofStyle_Roll', 'Exterior1st_AsphShn', 'Exterior1st_CemntBd', 'Exterior1st_ImStucc', 'Exterior1st_Stone', 'Heating_OthW', 'SaleType_Oth'
    
    
    
# Check 