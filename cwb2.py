#Filename: cwb2.py
#Author: Lee ying
#Centre No/Index No: 3024/
# Description: Read resource info from RESOURCE.DAT, get and validate extra details based on resource type, write to URESOURCE.DAT

from classes import *
def UPDATERESOURCE ():
    try:
        #open resource file for reading
        resource_file = open("RESOURCE.DAT","r")

        #open updated resource file for writing
        uresource_file = open("URESOURCE.DAT" , "w")

        #read heading line from resource file
        heading_line = resource_file.readline()
        heading_line = heading_line.rstrip("\n")
        
        #store creation date and number of records
        creation_date = heading_line[0:10]
        num_records = heading_line[10:]
        
        #write creation date and number of records to update resource file
        uresource_file.write(creation_date + num_records + "\n")

        #get resource details
        detail_lines = resource_file.readlines()

        #initialize resource list
        resource_list = [] 

        #loop through each resource
        for record_line in detail_lines:

            #clean each record line
            record_line = record_line.rstrip("\n")

         #get and store record details
            resource_no = record_line[0:5]
            title = record_line[5:35]
            date_acquired = record_line[35:41]
            resource_type = record_line[41:]

         #display resource info
            print("Resource no:" + resource_no)
            print("Title:" + title)
            print("Date Acquired:" + date_acquired)
            print("Resource type:" + resource_type)

         #if music CD
            if resource_type == "C":
                #get and validate music CD details
                #get and validate artist
                valid_artist = False
                while not valid_artist:
                    artist = input ("Enter artist:")
                    if len(artist) == 0:
                        print("Invalid. Empty input.")
                    elif len(artist) > 50 :
                        print("Invalid.Cannot exceed 50 character.")
                    else:
                        valid_artist = True
                #get and validate number of tracks
                valid_num_tracks = False
                while not valid_num_tracks:
                    num_tracks = input ("Enter number of tracks:")
                    if len(num_tracks) == 0:
                        print("Invalid. Empty input.")
                    elif not num_tracks.isdigit():
                        print("Invalid.Must be digit.")
                    elif not (0< int(num_tracks) <= 20):
                        print ( "Invalid! Range must be between 1 to 20.")
                    else:
                        valid_num_tracks = True

                #create music CD
                resource_list.append(MusicCD(resource_no, title, date_acquired , resource_type, artist, num_tracks))

            else:
                #get and validate film dvd details

                #get and validate director
                valid_director = False
                while not valid_director:
                    director = input ("Enter director:")
                    if len(director) == 0:
                        print("Invalid. Empty input.")
                    elif len(director) > 50 :
                        print("Invalid.Cannot exceed 50 character.")
                    else:
                        valid_director = True

                #get and validate running time
                valid_running_time = False
                while not valid_running_time:
                    running_time = input ("Enter running time:")
                    if len(running_time) == 0:
                        print("Invalid. Empty input.")
                    elif not running_time.isdigit():
                        print("Invalid.Must be digit")
                    elif not (30<=int(running_time) <= 180):
                        print("Invalid.Must be between 30 to 180 minutes.")
                    else:
                        valid_running_time = True

                resource_list.append(FilmDVD(resource_no, title, date_acquired,resource_type,director,running_time))

    
         #write full resource details to updated resource file
        for resource in resource_list:
            uresource_file.write(resource.display()+ "\n") #polymorphism 
       
        #close files
        resource_file.close()
        uresource_file.close()



    except IOError:
        #display file input/output errors( error: hard disk full, multi-user)
        print ( "Error! Cannot read from input file or to write to output file.")

#main
if __name__ == "__main__":
    UPDATERESOURCE()
