#Name: Colton Matthews
#Class: MCS-394
#Date: 9/15/2022

def Monica(m, l, M, L, time_m, time_l):
    #finds the displacement of m
    total_time_m = abs(m) + abs(m-M) 
    #finding the final time for t_l
    final_time_l = total_time_m + abs(M-l) + abs(l-L)
    #return a boolean if the displacement is less than or equal t_m
    #and if the final_t_l is less than or equal t_l
    return total_time_m <= time_m and final_time_l <= time_l

def Lydia(m, l, M, L, time_m, time_l):
    #finds the displacement of l
    total_time_l = abs(l) + abs(l-L)
    #finds the final time for t_m
    final_time_m = total_time_l + abs(L-m) + abs(m-M)
    #returns a boolean if the displacement is less than equal t_l
    #and if the final_t_l is less than or equal t_l 
    return total_time_l <= time_l and final_time_m <= time_m

#This function go through different possibility that if m is in different order. 
def onTime(m, l, M, L, time_m, time_l):
    #Using the if statement for all different order of who is going to move first
    if any((Monica(m, l, M, L, time_m, time_l), Lydia(m, l, M, L, time_m, time_l))):
        return True
    elif m < l <= 0:
        return Monica(m, m, M, L, time_m, time_l)
    elif 0 <= l < m:
        return Monica(m, m, M, L, time_m, time_l)
    elif l < m <= 0: 
        return Lydia(l, l, M, L, time_m, time_l)
    elif 0 <= m < l:
        return Lydia(l, l, M, L, time_m, time_l)
    else:
        return False #return False if any cases of the meal will not be enough time. 

def main():
    #the input will be in-pairs that need to be split for m and l for initial position, final position, and time for their meal and
    # map the input into the function onTime.
    #The function will return a boolean if the statement is true, then print "possible"
    # else print "impossible"
    if onTime(*map(int,input().split()),*map(int,input().split()),*map(int,input().split())):
        print("possible")
    else:
        print("impossible")

if __name__ == "__main__":
    main()