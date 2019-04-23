---
theme: jekyll-theme-modernist
title: InsulCalc
description: Marguerite Dube's Data Science Capstone for the Center of Information Technology at Deep Run High School
logo: InsulCalcLogoOpaque.png
background-image: InsulCalcBG.jpg
---

## [About](https://dubemc.github.io/DubeCapstone2019/) - [Data](https://dubemc.github.io/DubeCapstone2019/data) - [Calculate](https://dubemc.github.io/DubeCapstone2019/calculate) - [Resources](https://dubemc.github.io/DubeCapstone2019/resources) - [Contact](https://dubemc.github.io/DubeCapstone2019/contact)

# Data Used
For this project, I specifically used my mother's data that she kept logged in a journal. I had to input this data by hand into a spreadsheet. All the data was validated (and cross-validated) and calculations were made from that data in order to make a more accurate prediction for the Insulin intake. The data I used from her journal includes the date, time, glucose, insulin intake, menstrual data, and sick days. 
My mother is a Type 1 diabetic, so I'm not sure that the calculator would work the same for Type 2 diabetics. (Huge thank you to my mother for her help!)

### DISCLAIMER
```markdown
NOTICE OF RISK. InsulCalc can at times involve substantial risk of 
injury- such as hypoglycemia (low blood sugar) and hyperglycemia 
(high blood sugar) - and other dangers when used as a medicinal 
tool to calculate insulin dosage. Dangers peculiar to such 
activities include, but are not limited to, uncontrollable 
fluctuation of glucose levels, fainting, nausea, and death. DO 
NOT USE AS A REPLACEMENT FOR DOCTOR'S ORDERS. While the InsulCalc 
strives to make the information on this website as timely and 
accurate as possible, InsulCalc makes no claims, promises, or 
guarantees about the accuracy, completeness, or adequacy of the 
contents of this site, and expressly disclaims liability for errors 
and omissions in the contents of this site. InsulCalc is not 
responsible if you decide to use to calculate insulin dosage and 
cause personal injury. All data inputted into this system is entirely 
anonymous. By clicking the "Calculate Now" button, you agree to 
InsulCalc's disclaimer. 
```
# Graphs of the Data
Before we get into this, all graphs displayed below show the Original Insulin Intake vs. the Predicted Insulin Intake for the different models. The Mean Squared Error is the potential error of the model; the closer the model's predictions are to a line, the more accurate the model is. 

## Linear Regression
![LinearReg](https://github.com/dubemc/DubeCapstone2019/blob/master/Screen%20Shot%202019-04-23%20at%2010.28.58%20AM.png)

Learn more about Linear Regression [here.](http://www.stat.yale.edu/Courses/1997-98/101/linreg.htm)

## Multilayer Perceptron
![MLP](https://github.com/dubemc/DubeCapstone2019/blob/master/Screen%20Shot%202019-04-23%20at%2010.29.12%20AM.png)

Learn more about Multilayer Perceptron [here.](http://deeplearning.net/tutorial/mlp.html)

## Random Forest Regressor
![RandForReg](https://github.com/dubemc/DubeCapstone2019/blob/master/Screen%20Shot%202019-04-23%20at%2010.29.24%20AM.png)

Learn more about Random Forest Regression [here.](https://turi.com/learn/userguide/supervised-learning/random_forest_regression.html)
