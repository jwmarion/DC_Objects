#objects 1

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)

#1
sonny = Person("Sonny","sonny@hotmail.com", "483-485-4948")

#2

jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

#3
sonny.greet(jordan)

#4
jordan.greet(sonny)

#5

print("%s, %s, %s" % (sonny.name, sonny.email, sonny.phone))

#6

print("%s, %s, %s" % (jordan.name, jordan.email, jordan.phone))
