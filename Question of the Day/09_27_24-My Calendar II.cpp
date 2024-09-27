//https://leetcode.com/problems/my-calendar-ii/?envType=daily-question&envId=2024-09-27
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