'''
731. My Calendar II

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

Implement the MyCalendarTwo class:
MyCalendarTwo() Initializes the calendar object.
boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.


Example 1:
Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]

Output
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked. 
myCalendarTwo.book(50, 60); // return True, The event can be booked. 
myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
 

Constraints:

0 <= start < end <= 10^9
At most 1000 calls will be made to book.
'''

'''
Gives TLE when using prefix sum - since it creates a large sparse array - not efficient.
'''
class MyCalendarTwo1:

    def __init__(self):
        self.events = []        
        

    def book(self, startTime: int, endTime: int) -> bool:
        end = 1
        
        self.events.append([startTime, endTime])
        max_length = max(x[end] for x in self.events)

        prefix_sum = [0] * (max_length + 1)
        for s,e in self.events:
            prefix_sum[s] += 1
            prefix_sum[e] -= 1
        
        for index in range(1, max_length+1):
            prefix_sum[index] += prefix_sum[index - 1]
        
        for index, value in enumerate(prefix_sum):
            if value > 2:
                self.events.pop()
                return False
        
        return True


'''
very similar to prefix sum but with 1 slight change. attach +1 and -1 to start end values and store in sorted order.
'''
class MyCalendarTwo2:
    def __init__(self):
        self.events = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        self.events.append([start, end])
        timeline = []
        for s, e in self.events:
            timeline.append((s, 1))
            timeline.append((e, -1))
        
        timeline.sort()
        count = 0
        for _, delta in timeline:
            count += delta
            if count >= 3:
                # More than two overlaps, can't book
                self.events.pop()
                return False
        return True


'''
found on leetcode
'''
class MyCalendarTwo:

    def __init__(self):
        self.single = []  
        self.double_booked = []  

    def book(self, start: int, end: int) -> bool:
        # Triple booking?
        for s, e in self.double_booked:
            inter_s = max(start, s)
            inter_e = min(end, e)
            if inter_s < inter_e:
                return False  
        
        # Add the overlapping parts to double bookings
        for s, e in self.single:
            inter_s = max(start, s)
            inter_e = min(end, e)
            if inter_s < inter_e:
                self.double_booked.append([inter_s, inter_e])
        
        # Add the event to single bookings
        self.single.append([start, end])
        return True
        

obj = MyCalendarTwo()

times = [[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]



for startTime , endTime in times:
    print(obj.book(startTime,endTime))

