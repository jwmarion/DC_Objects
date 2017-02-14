#ex6

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

    def print_contact_info(self):
        print "%s's email: %s %s's number: %s" % (self.name, self.email, self.name, self.phone)

    def add_friend(self, friend):
        self.friends.append(friend)

sonny = Person("Sonny","sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.add_friend(jordan)


print sonny.friends[0].name
print len(sonny.friends)
