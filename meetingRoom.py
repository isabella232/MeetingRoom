def main():
    times = [[20,45],[10,55],[10,30],[30,50],[50,55],[5,15],[30,45],[0,10]] # N elements in input array
    times.sort() 
    print(checkAvailability(times))
    print(numRooms(times))

def checkAvailability(times = []):

    for i in range(0,len(times)-1):			# N elements in for loop
    	if(times[i][1] > times[i+1][0]): 	# because we sorted it we only have to look at 
    		return False					#if i'th end time overlaps with the next start time
            
    return True
    
def numRooms(times = []):

	starts, ends = [], [] 					# list for storing all start and end times respectively 
	for i in range(len(times)):				# N elements in for loop
		starts.append(times[i][0])
		ends.append(times[i][1])

	starts.sort()							# list containg all sorted start times
	ends.sort()	
	print(starts)
	print(ends)							# list containg all sorted end times
	s_time, e_time = 0, 0

	rooms = 0
	min_rooms = 0

	while s_time < len(starts):
		if starts[s_time] < ends[e_time]:
			#rooms += 1  					# update the number of rooms if start time smaller than end time
			s_time += 1                                     # iterate to the next start time
			rooms +=1
			min_rooms = max(min_rooms, rooms)
		else:
			rooms -= 1						# decrement the num rooms because start time > end time 
			e_time += 1						# because that means they only need one room

	return min_rooms


main()
    
