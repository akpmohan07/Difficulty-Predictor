# About
This Project was one of the Interview Round by [Examly](https://examly.io/).
Project Time - ***`7 days`***
## Problem Statement
Derive an algorithm to find the difficulty of a question.
For more [Details](https://github.com/akpmohan07/Difficulty-Predictor/blob/master/static/Readme%20Files/Campus%20Hiring%20Dev%20Role%20Tasks-1.pdf)
## Task
1. Data Collection
2. Model Building
3. UI Development
4. Deployment
5. Documentation
## Attribute Description
|Attribute| Description |
|--|--|
|Question_Type |Type of the Question|
|Question_Difficulty |Difficuty of the Question |
|Attended|Total number of students Attended|
|Time_Taken| Time is taken by the Student to solve the Question  |
|Submission| Number of times student submitted the answer|
|Hints_Used|Number of hints used by the student|
|Right| Number of students Correctly answered |
|Partial| Number of students Partially Answered |
|Wrong|Number of students Wrongly Answered|

## Solution

 ***` Difficulty ∝ Time _Taken ,Submission,Hints_Used,Wrong,Partial`***

 ***`Difficulty  1/∝ Right, Partial`***

From this, we infer that difficulty level is directly impacted by all the attributes except attended.

Generally, if a question is ***easy*** most of the students answer ***correctly, fastly and accurately*** and for ***hard*** question most of the students answer  ***wrongly, slowly and inaccurately***.

With the help of decision-making attribute(**`Dependent attribute `**), we can predict the target attribute.

## Application Structure
![flow](https://github.com/akpmohan07/Difficulty-Predictor/blob/master/static/Readme%20Files/Difficulty_Predictor_Struct.png?raw=)

## 1.Data Collection
For collecting data, first I framed the **Data Rules**.
`Here, Data rules is data about data.` It defines the each **attribute type and range based on given Metrics from the given given metrics.**

Finally, I used Google form and google sheet to collect the data.
Sample Data Rule is here!
![1](https://github.com/akpmohan07/Difficulty-Predictor/blob/master/static/Readme%20Files/Data_Rule_1.PNG?raw=)
For more [Details.](https://github.com/akpmohan07/Difficulty-Predictor/blob/master/static/Readme%20Files/Data_Rule.PNG)
## 2.Model Building
[***Source Code is Here!***](https://github.com/akpmohan07/Difficulty-Predictor/blob/master/static/Notebook/Difficulty_Predict.ipynb)

The model can be defined as ***representation*** of something. The model represents the ***Mathematical relation and Logical relation*** of the Training data.
### 1.Cleaning Data
- Before building the model we need to do some process like ***Data cleaning, Feature Extraction***.

- As our data is self-created it does not have any issues. But in our data have ***Categorical attribute***. To handle this, we use **Label encoding Technique** which means assigning a numerical value to the category.

		[Easy,Medium,Hard] => [0,1,2]
### 2.Model Selection
For building the model we use ***`Python Scikit-Learn`*** Library.
From that we select one of the  ***Classification Algorithm*** called 
***DecisionTreeClassifier***.

### DecisionTreeClassifier:
 - As the name says, it creates the ***Tree Structure*** by *** Decision-Making Rule*** as its Node.
 - Almost every computer engineer should come across this basic [question](https://www.geeksforgeeks.org/program-to-assign-grades-to-a-student-using-nested-if-else/), ***`Assign the grade for a student based on their marks!`***
 - The key concept of Decision Tree classifier is the above question. Butt he only thing is it makes ***decision based on multiple atrribute***.
 - For easy understanding, it is like a ***nested if-else Condition***.
 - 
 Image Describes Nested if-else Loop.
---
![loop](https://github.com/akpmohan07/Difficulty-Predictor/blob/master/static/Readme%20Files/nested-if-else-flowchart.png?raw=)

## Algorithm

[Source code is here!](https://github.com/akpmohan07/Difficulty-Predictor/blob/master/static/Notebook/Decision_Tree.ipynb)
|  ![enter image description here](https://github.com/akpmohan07/Difficulty-Predictor/blob/master/static/Readme%20Files/dtc_1.png?raw=)|  ![](https://github.com/akpmohan07/Difficulty-Predictor/blob/master/static/Readme%20Files/dtc_2.png?raw=)|
|--|--|
|  ![enter image description here](https://github.com/akpmohan07/Difficulty-Predictor/blob/master/static/Readme%20Files/dtc_3.png?raw=)|  ![enter image description here](https://github.com/akpmohan07/Difficulty-Predictor/blob/master/static/Readme%20Files/dtc_4.png?raw=)|
---
## Algorithm Sample:

    if (Hints_Used<3.5)
    {
	    Class->Easy
    }
    else 
    {
	    if(wrong<641925)
	    {
		    class->Medium
		}
		else
		{
			class->Hard
		}	
	}

### 3.Creating Model and Testing
 - The input data is splited into ***train and test data***.
 - The model is created with training data.
 - Finally the Model is tested with test data.
 
The Below graph is an Boundary analysis of Decision Tree Classifier.Ploted as ***Time_Taken vs Submission***.

![Analysis](https://github.com/akpmohan07/Difficulty-Predictor/blob/master/static/Readme%20Files/dtc_boundary_analysis.png?raw=)

 - ![List item](https://via.placeholder.com/15/9a21fc/?text=%20) Easy
 - ![enter image description here](https://via.placeholder.com/15/f3ff4f/?text=%20) Medium
 - ![enter image description here](https://via.placeholder.com/15/59b7ff/?text=%20) Hard

From this graph we can conclude that  ***increases in Time_Taken and Submission increases  the Difficulty Level***.
 
 
 ## 3.UI Development
For the UI Development I use ***Python Flask Framework***.
The input can be in two form,
 - File as ***URL***
 - ***Feature*** as input
 ## 4.Deloyment
 For Deployment I used Heroku Cloud Platform.
## 5.Documentation
The is an Documentation
## Technology Stack
 -  Python
 - HTML
 - CSS
 - Flask
 
## Library Used
 - Pandas
 - Numpy
 - Scikit-Learn
 - Pickle
 - Matplotlib
## Tools Used
 - Google Colab
 - Jupyter Notebook
 - Heroku
 - Github
 - Bootstrap
 - Google Form
 - Google Sheet


                             ***Thank You***
