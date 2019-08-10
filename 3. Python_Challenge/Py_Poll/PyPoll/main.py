import csv

inputfile = '\\Users\\guila\\PycharmProjects\\python_poll\\election_data.csv'
outputfile = '\\Users\\guila\\PycharmProjects\\python_poll\\election_output.txt'
# Create empty list for csv file
polls = []
# Create empty dictionary to record only candidate names
dict_polls = {}
# Create empty dictionaty to summarize the total number votes per candidate name
dict_summary = {}
# Open file and assign to csvfile object name
with open(inputfile, newline='') as csvfile:
    # read and split the data on commas assign to pollreader string variable
    pollreader = csv.reader(csvfile, delimiter=',')
    # Skip header row
    next(pollreader)
    text_file = open(outputfile, "w")
    # Output to text file
    text_file.write("Election Results")

    # Terminal output
    print("Election Results.....By Serge Guilao")
    # Output to text file
    text_file.write("\n-------------------------")
    # Terminal Output
    print("-------------------------")
    # Converting string to list
    for line in pollreader:
        polls.append(line)
    # Output to text file
    text_file.write("\nTotal Votes: " + str(len(polls)))
    # Terminal Output
    print("Total Votes: " + str(len(polls)))
    # Text file Output
    text_file.write("\n-------------------------")
    # Terminal Output
    print("-------------------------")
    # Converting to dictionary for counting and grouping candidate names
    for line in polls:
        name_key = line[2]
        if name_key not in dict_polls:
            # insert name_key into dictionary and initialize to 0
            dict_polls[name_key] = 0
        # count the name key inside dictionary
        dict_polls[name_key] += 1

    # Dictionary_summary
    total_polls = len(polls)
    for name in dict_polls:
        dict_summary[name] = round((dict_polls[name] / total_polls) * 100)
        # Output to text file
        text_file.write("\n" + str(name) + ": " + str(dict_summary[name]) + "% " + "(" + str(dict_polls[name]) + ")")
        # Output to console
        print(str(name) + ": " + str(dict_summary[name]) + "% " + "(" + str(dict_polls[name]) + ")")

    # The highest value
    highest = 0
    # Find larget value of the key/value pair inside dictionary and place the key name inside winner
    for name in dict_summary:
        if highest < dict_summary[name]:
            highest = dict_summary[name]
            winner = name

    # Output to text file
    text_file.write("\n-------------------------")
    # Output to console
    print("-------------------------")
    # Output to text file
    text_file.write("\nWinner: " + winner)
    # Output to console
    print("Winner: " + winner)
    # Output to text file
    text_file.write("\n-------------------------")
    # Output to console
    print("-------------------------")

# Close text file
text_file.close()