#ex8

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greet = 0

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greet += 1

    def print_contact_info(self):
        print "%s's email: %s %s's number: %s" % (self.name, self.email, self.name, self.phone)

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        print len(self.friends)

    def greet_count(self):
        print self.greet

sonny = Person("Sonny","sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.add_friend(jordan)

sonny.num_friends()
