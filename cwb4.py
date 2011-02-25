#Author: Lee ying
#Filename: cwb4.py
#Centre No/Index No: 3024/
#Description:Displaying resource


import datetime

#read in resource no, title, resource type into list of list

#open file
def RESOURCELIST():
    
    try:
        #open LOAN.DAT to read
        loan_file = open("LOAN.DAT","r")

        #read record details
        detail_lines = loan_file.readlines()

        # loop through all records
        for resource_line in detail_lines:

            #get and store record details
            resource_no = record_line[0:5]
            student_id = record_line[5:10]

        #compute date due
        #get current date
        DateLoaned = datetime.date.today()

        #add 7 days to get date due back
        DateDueBack = DateLoaned + datetime.timedelta(days=7)
        DateLoaned = DateLoaned[8:] + "-" + DateLoaned[5:7]+"-" +DateLoaned[:4]
        DateDueBack = DateDueBack.strftime("%d-%m-%y")

        print("Date:" + DateDueBack)

        #set up data structure to hold merged record
        final_rec = []
        #compare resource no in loan_list with resource no in resource list
        for loan in loan_list:
            for resource in resource_list:
                if (loan[0] == resource[0]): #check if resource numbers coincide
                    if resource[2] == "C":
                        resource_type = "CD"
                    else:
                        resource_type = "DVD"
                        if loan[4] == (" " * 50):
                            final_rec.append([resource[0], resource[1], resource_type, loan[1], loan[2]])

        print (final_red)

#close files
        loan_file.close()


    except IOError:
        # I/O message
        print("Error! Cannot read from input or append to output file.")

#main
if __name__=="__main__":
    RESOURCELIST()
