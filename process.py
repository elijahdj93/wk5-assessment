log_file = open("um-server-01.txt")


def sales_reports(log_file):  # creating a function that takes in the file from log_file
    for line in log_file:     # looping through each line in the file
        line = line.rstrip()  # removing the ending white space
        day = line[0:3]       # selecting the 0 index day out of the file
        if day == "Mon":      # if the day is Tue
            print(line)       # print out that entire row


sales_reports(log_file)       # invokes the function made above
