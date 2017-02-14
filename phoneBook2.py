#Phonebook
import os, pickle


class phone_book(object):

    def __init__(self):
        if os.path.exists("pb.pickle"):
            with open("pb.pickle") as f1:
                self.db = pickle.load(f1)
        else:
            self.db = {}

    def mainMenu(self):
        self.header("Welcome")
        print "1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit"

        inp = raw_input("What do you want to do? (1-5): ")

        if inp == "1":
            self.lookup()
        elif inp == "2":
            self.sentry()
        elif inp == "3":
            self.dentry()
        elif inp == "4":
            self.lentry()
        elif inp == "5":
            self.quit()
        else:
            raw_input("Invalid input. Press enter")
            self.mainMenu()

    def lookup(self):
        self.header("Entry lookup")

        self.name = raw_input("What name would you like to look up?")
        if db.get(name) == None:
            print (raw_input("Name does not exist, press enter to continue"))
            self.mainMenu()
        else:
            print self.db[name]
            raw_input("Press enter to continue.")
            self.mainMenu()

    def sentry(self):
        self.header("Set an Entry")

        self.name = raw_input("What name would you like to add?: ")
        if self.db.get(self.name) != None:
            raw_input("Name already exists, press enter to continue")
            self.mainMenu()
        else:
            self.number = raw_input("Please enter the number: ")
            self.db[self.name] = self.number
            raw_input("Name and number entered. Press enter to continue")
            self.mainMenu()

    def dentry(self):
        self.header("Delete an Entry")

        self.name = raw_input("What entry would you like to delete?: ")
        if self.db.get(self.name) == None:
            raw_input("Name does not exist! Press enter to continue")
            self.mainMenu()
        else:
            del self.db[self.name]
            raw_input(" Deleted. Press enter to continue ")
            self.mainMenu()

    def lentry(self):
        self.header("List all entries")
        for entry in self.db.items():
            print "%s's number is %s" % entry
        raw_input("Press enter to continue:  ")
        self.mainMenu()

    def quit(self):
        self.t = raw_input("Are you sure? (y/n)")
        if  self.t != "y":
            self.mainMenu()
        with open("pb.pickle", 'w') as f1:
            pickle.dump(self.db, f1)

    def header(self,input):
        os.system('clear')
        print "Electronic Phone Book"
        print input
    print "=" * 21

pb = phone_book()
pb.mainMenu()
