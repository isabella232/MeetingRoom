
def main(): 
    times = [[20,45],[10,55],[10,30],[30,50],[50,55],[5,15],[30,45],[0,10]] # N elements in input array
    # sort times to pass into functions
    
    # print and call functions
    print(checkAvailability(times))
    print(numRooms(times))

def checkAvailability(times = []):	# returns True if times are available
	# check through array of times
	
		# returns False if i'th end time overlaps with the next start time
    
def numRooms(times = []):	# returns number of rooms needed for times
	# initializing lists for start and end times
	
	# checking through array of times
	
		# appending start times to start list and end times to end list
		
		
	# sorting lists
	
	
	
	# initializing number of rooms, minimum rooms, indexes for respective lists
	
	
	# while loop for checking start times
	
		# checking if start time is smaller than end time
		
			# update index for start times to go to next time
			
			# update number of rooms and minimum
			
			
		# otherwise decrement the num rooms because start time > end time 
		
			# increment index for end times because that means they only need one room

	# return the minimum number of rooms


main()
    
