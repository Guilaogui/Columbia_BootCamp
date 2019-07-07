# Dependencies and Setup
import pandas as pd

# File to Load
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
print(school_data_complete)

#Calculate the total number of schools
total_number_schools = len(school_data_complete["School ID"].unique())
print(total_number_schools)

#Calculate the total number of students
total_number_students = len(school_data_complete["Student ID"].unique())
print(total_number_students)


#Calculate the total budget
total_budget = school_data["budget"].sum()
print(total_budget)


#Calculate the average math score
average_math_score = student_data["math_score"].mean()
print(average_math_score)


#Calculate the average reading score
average_reading_score = student_data["reading_score"].mean()
print(average_reading_score)


#Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
overall_average_score = (average_math_score + average_reading_score)/2
print(overall_average_score)


#Calculate the percentage of students with a passing math score (70 or greater)
#But First let's create the passing student data in math or reading
student_data["#passing_math"] = student_data["math_score"] >= 70
student_data["#passing_reading"] = student_data["reading_score"] >= 70
percent_passing_math = ((student_data["#passing_math"]).mean())*100
print(percent_passing_math)


#Calculate the percentage of students with a passing reading score (70 or greater)
percent_passing_reading = ((student_data["#passing_reading"]).mean())*100
print(percent_passing_reading)


#Calculate overall percentage
overall_passing_rate = (percent_passing_math + percent_passing_reading)/2
print(overall_passing_rate)


#Create a dataframe to hold the above results
#Optional: give the displayed data cleaner formatting
district_results = [{"Total Schools": total_number_schools, 
            "Total Students": total_number_students, 
            "Total Budget": total_budget, 
            "Average Math Score":  round(average_math_score,2), 
            "Average Reading Score":  round(average_reading_score,2), 
           "% Passing Math": round(percent_passing_math,2),
           "% Passing Reading": round(percent_passing_reading,2),
            "% Overall Passing Rate": round(overall_passing_rate,2)}]
district_summary_table = pd.DataFrame(district_results)

#Formatting
district_summary_table["% Passing Math"] = district_summary_table["% Passing Math"].map("{:,.2f}%".format)
district_summary_table["% Passing Reading"] = district_summary_table["% Passing Reading"].map("{:,.2f}%".format)
district_summary_table["% Overall Passing Rate"] = district_summary_table["% Overall Passing Rate"].map("{:,.2f}%".format)
district_summary_table["Total Budget"] = district_summary_table["Total Budget"].map("${:,.2f}".format)
district_summary_table["Total Students"] = district_summary_table["Total Students"].map("{:,}".format)

print(district_summary_table)


#For this part, school_data_complete

school_data_complete["passing_math"] = school_data_complete["math_score"] >= 70
school_data_complete["passing_reading"] = school_data_complete["reading_score"] >= 70

print(school_data_complete)

# Use groupby by school_name

school_group = school_data_complete.groupby(["school_name"]).mean()
school_group["Per Student Budget"] = school_group["budget"]/school_group["size"]
school_group["% Passing Math"] = round(school_group["passing_math"]*100,2)
school_group["% Passing Reading"] = round(school_group["passing_reading"]*100,2)
school_group["% Overall Passing Rate"] = round(((school_group["passing_math"] + school_group["passing_reading"])/2)*100,3)

#Merge with school_data to collect information about the type, size and budget
school_data_summary = pd.merge(school_group, school_data, how="left", on=["school_name", "school_name"])
del school_data_summary['size_y']
del school_data_summary['budget_y']
del school_data_summary['Student ID']
del school_data_summary['School ID_x']

#Create a dataframe to store the results
school_summary_dataframe = pd.DataFrame({"School Name":  school_data_summary["school_name"],
                                "School Type": school_data_summary["type"],
                               "Total Students":school_data_summary["size_x"],
                               "Total School Budget": school_data_summary["budget_x"],
                               "Per Student Budget":school_data_summary["Per Student Budget"], 
                               "Average Math Score":round(school_data_summary["math_score"],2),
                               "Average Reading Score":round(school_data_summary["reading_score"],2), 
                               "% Passing Math": school_data_summary["% Passing Math"],
                               "% Passing Reading": school_data_summary["% Passing Reading"],
                               "% Overall Passing Rate": school_data_summary["% Overall Passing Rate"]}) 

#Formatting
school_summary_dataframe["Total Students"] = school_summary_dataframe["Total Students"].map("{:,.0f}".format)
school_summary_dataframe["Total School Budget"] = school_summary_dataframe["Total School Budget"].map("${:,.2f}".format)
school_summary_dataframe["Per Student Budget"] = school_summary_dataframe["Per Student Budget"].map("${:,.2f}".format)
#Display
print(school_summary_dataframe)

