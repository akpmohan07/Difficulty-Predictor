# Difficulty-Predictor
# About
This Project was one of the Interview Round by [Examly](https://examly.io/).
Project Time - **`7 days`**`
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

>  ** Difficulty ∝ Time _Taken ,Submission,Hints_Used,Wrong,Partial**

>  ** Difficulty  1/∝ Right,Partial**

From this, we infer that difficulty level is directly impacted by all the attributes except attended.

Generally, if a question is **easy** most of the students answered **correctly, fastly and accurately** and for **hard** question most of the students answered  **wrongly, slowly and inaccurately**.

With the help of decision-making attribute(**`Dependent attribute `**), we can predict the target attribute.

## 1.Data Collection
For collecting data ,first I framed the **Data Rules**.
`Here,Data rules is a data about data.`It define the each **attribute type and range.**

Finally I used Google form and google sheet to collect the data.