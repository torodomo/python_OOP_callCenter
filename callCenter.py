#Call Center
# You're creating a program for a call center. Every time a call comes in you need a way to track that call. 
# One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

# You will create two classes. One class should be Call, the other CallCenter.


class call(object):
    def __init__(self, unique_id, caller_name, phone_number, time, reason):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.phone_number = phone_number
        self.time = time
        self.reason = reason

    def display(self):
        print self.unique_id
        print self.caller_name
        print self.phone_number
        print self.time
        print self.reason
        return self

# Jason = call(01,"Json",1234567890,"10:00", "free style")
# Jason.display()

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self, caller):
        self.calls.append(caller)
        self.queue_size += 1
        return self
    
    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self

    def info(self):
        print "list size", self.queue_size
        for count in self.calls:
            print " "
            print "caller:", count.caller_name
            print "number:", count.phone_number
            print "call time:", count.time
            print "reason to call:", count.reason
            print " "

        return self

caller1 = call(1,"Juan","831-840-7899","7:00 pm","Juan solo")
caller2 = call(2,"Jose","831-840-7780","12:00 am","I am a God")
caller3 = call(3,"Grant","309-222-7777","6:00 AM","morning call")
callcenter1 = CallCenter()
callcenter1.add(caller1).add(caller2).add(caller3).info().remove().info()