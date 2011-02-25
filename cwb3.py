#Filename: cwb3.py
#Author: Lee ying
#Centre No/Index No: 3024/
#Description: Enter validated load record to load file


import datetime
#open file
def LOANRESOURCE():
    
    try:
        #open load file to append
        loan_file= open("LOAN.DAT", "a")
        
        #open URESOURCE.DAT to read
        uresource_file = open("URESOURCE.DAT","r")

        #skip heading lines
        heading_line = uresource_file.readline()

        #initialize Resource number list
        resourceno_list = []

        #read record details
        detail_lines = uresource_file.readlines()

        # loop through all records
        for resource_line in detail_lines:

            #get resource number
            resourceno = resource_line[0:5]

            #append Resource number to list
            resourceno_list.append(resourceno)

        #get and validate resource number
        valid_resourceno = False
        while not valid_resourceno:
        resourceno = input("Enter resource number:")
            if len(resourceno) == 0:
                print ("Error!Resource number cannot be empty.")
            elif len(resourceno) != 5:
                print("Error! Resource number must be 5 digits.")
            elif not resourceno.isdigit():
                print("Error! Resource number must be dgits.")
            elif resourceno not in resourceno_list:
                print("Error! Resource number does not exist.")
            else:
                valid_resourceno = True
            #assume resource is not loaned

        #get and validate student id
        valid_studentid=False
        while not valid_studentid:
        studentid = input("Enter studentid:")
            if len(studentid) == 0:
                print ("Error!Resource number cannot be empty.")
            elif len(studentid) != 5:
                print("Error! Student ID must be 5 digits.")
            elif not studentid[0:1].upper() == "S":
                print("Error! Student ID must start with S.")
            elif not studentid[1:5].isdigit():
                print("Error! last 4 character must be digit.")
            elif not 0 < int(studentid[1:5]) < 10000:
                print("Error.student id must be from S0001 to S9999.")
            else:
                valid_studentid = True

        #get and validate student name
        valid_studentname=False
        while not valid_studentid:
        studentname = input("Enter student name:")
            if len(studentname) == 0:
                print ("Error!Student name cannot be empty.")
            elif len(studentname) > 30:
                print("Error,student name must be less than 30 character.")
            else:
                valid_studentname = True

        #compute date due
        #get current date
        DateLoaned = datetime.date.today()
        
        #add 7 days to get date due back
        DateDueBack = DateLoaned + datetime.timedelta(days=7)
        DateDueBack = DateDueBack.strftime("%d-%m-%y")

        #validate evaluation
        valid_evaluation=False
        while not valid_evaluation:
        evaluation = input("Enter evaluation:")
            if len(evaluation) == 0:
                print ("Error!Evaluation cannot be empty.")
            elif len(evaluation) > 50:
                print("Error,Evaluation must be less than 50 character.")
            else:
                valid_evaluation = True

        #write validated record to loan file
        loan_file.write(resourceno + studentid + studentname + DateDueBack + evaluation + "\n")

        

        #close files
        loan_file.close()
        uresource_file.close()

    except IOError:
        # I/O message
        print("Error! Cannot read from input or append to output file.")

#main
if __name__=="__main__":
    LOANRESOURCE()
