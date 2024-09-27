//https://leetcode.com/problems/my-calendar-ii/?envType=daily-question&envId=2024-09-27

/*
    Time Complexity = O(nlogn)
    Line sweep Algorithm 
    -   The Line Sweeping Algorithm is an efficient method for solving interval problems, such as booking conflict finding. 
        The core idea behind this algorithm is to treat the problem like scanning across a timeline and "sweeping" 
        through events to detect overlaps or conflicts in real time.

    The Line Sweep algorithm works by marking when bookings start and end. 
    For each booking (start, end), we mark the start point by increasing its count by 1 (indicating a booking begins), 
    nd we mark the end point by decreasing its count by 1 (indicating a booking ends). These marks are stored in a map, 
    which keeps track of the number of bookings starting or ending at each point.

    Once all bookings are processed, we compute the prefix sum over the map. The prefix sum at any point tells us how many 
    active bookings overlap at that moment. If the sum at any point exceeds 2, it means we have a triple booking. 
    At this point, the function should return false to prevent adding a new booking. If no triple booking is found, 
    the function returns true, and the booking is allowed.

    This approach is easily extendible. If we wanted to check for four or more bookings instead of three, we would simply 
    adjust the threshold from 2 to 3 when calculating the prefix sum. 
    This flexibility makes the Line Sweep method a more robust solution for variations of the problem.


*/

class MyCalendarTwo {
public:

    // because i want to loop in sorted manner so map instead of unordered_map
    map<int,int> bookingCount;
    int maxBooking=2;

    MyCalendarTwo() {
        
    }
    
    bool book(int start, int end) {
        
        // increment start time and deccrement end time
        bookingCount[start]++;
        bookingCount[end]--;

        int overlap = 0;

        for(auto x:bookingCount){
            overlap += x.second;
            // check if the overlap is greater than maxOverlap allowed 
            if(maxBooking < overlap){

                // as overlap > maxBooking , we need to return false, 
                // but we need to undo the increment and decrement we did above
                bookingCount[start]--;
                bookingCount[end]++;
                // Remove the entries from the map to avoid unnecessary, counting it in the timeline
                if(bookingCount[start]==0){
                    bookingCount.erase(start);
                }
                if(bookingCount[end]==0){
                    bookingCount.erase(end);
                }

                return false;
            }
        }

        return true;

    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(start,end);
 */

