"""
Template for bar projcet
"""

from datetime import datetime
import threading
import time
print "========================================================"
orderQueue = []
oID = 0;
inventory = {}
drinkMenu = []
exitFlag = 0

## CLASSES ##
class BartenderThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
		global orderQueue
		startUp()
		printMenu()
		printInventory()
		timer = 2
		while timer >0:
			print "OrderQueue is size :" + str(len(orderQueue))
			if len(orderQueue) >= 1:
				print "Order found!"
				handleOrder()
			else:
				print "Waiting for orders..."
			time.sleep(8)
			timer -=1

class ButlerThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
		global orderQueue
		time.sleep(5)
		guest = "Alex"
		placeOrder(guest,0)

class Ingredient:
	def __init__(self, name, ingredientType, amountLeft, lastRestocked):
		self.name = name
		self.ingredientType = ingredientType # ingredient Types: spirit (True), mixer (False)
		self.amountLeft = amountLeft
		self.lastRestocked = lastRestocked

	def getIngredientName(self):
		return self.name

	def getAmount(self):
		return self.amountLeft

	def restock (self, amount):
		self.amountLeft = amount
		self.lastRestocked = datetime.today()

	def getLastRestocked(self):
		return self.lastRestocked

	def consume(self, amount):
		if self.amountLeft > amount:
			self.amountLeft = self.amountLeft-amount
			return True
		else:
			return False

class Order:
	def __init__(self, oID, guest, recipieNr):
		self.oID = oID
		self.guest = guest
		self.recipieNr = recipieNr

	def getOID(self):
		return self.oID
	def getOrderGuestName(self):
		return self.guest
	def getOrderRecipieNr(self):
		return self.recipieNr

class Recipie:
	def __init__(self, name, description, cost, ingredients):
		self.name = name
		self.description = description
		self.cost = cost
		self. ingredients = ingredients
	def getRecipieName(self):
		return self.name
	def getIngredients(self):
		return self.ingredients

## Functions

def startUp():
	global inventory, drinkMenu
	ingredientX = Ingredient("Bombay Sapphire Gin", 1, 75, datetime.today())
	ingredientY = Ingredient("Schweppes Tonic Water", 0, 33, datetime.today())
	ingredientZ = Ingredient("Orange Juice", 0, 100, datetime.today())
	ingredientA = Ingredient("Sierra Tequila", 1, 50, datetime.today())
	ingredientB = Ingredient("Bacardi Rum", 1, 75, datetime.today())
	inventory[ingredientX.getIngredientName()] = ingredientX
	inventory[ingredientY.getIngredientName()] = ingredientY
	inventory[ingredientA.getIngredientName()] = ingredientA
	inventory[ingredientB.getIngredientName()] = ingredientB
	inventory[ingredientZ.getIngredientName()] = ingredientZ

	drinkMenu.append(Recipie("Gin and Tonic", "A classy drink for a classy gentleman.", 50, {'Bombay Sapphire Gin': 4, 'Schweppes Tonic Water': 20}))
	drinkMenu.append(Recipie("Cuba Libre", "Gharr, that be good!", 50, {'Bacardi Rum': 4, 'Coca Cola': 20}))
	drinkMenu.append(Recipie("Tequila Sunrise", "Ayayayay! What a way to wake up!", 50, {'Sierra Tequila': 4, 'Orange Juice': 20}))

def printMenu():
	print "+---- Drinks Menu: ----+"
	for drink in drinkMenu:
		print "| >> " + drink.getRecipieName()
	print "+----------------------+"

def printInventory():
	print "Inventory:"
	for key, value in inventory.items():
		print str(key) + " - " + str(value.getAmount()) + "cl. remaining."

def placeOrder(guestName, recipieNr):
	contactGuest(guestName, "PLACING ORDER")
	global oID, drinkMenu
	oID += 1
	orderQueue.append(Order(oID, guestName, recipieNr))
	contactGuest(guestName, "ORDER "+str(oID)+": "+drinkMenu[recipieNr].getRecipieName()+" is PLACED")

def handleOrder():
	global orderQueue
	order = orderQueue.pop(0)
	guestName = order.getOrderGuestName()
	contactGuest(guestName, "START")
	drinkMade = makeDrink(guestName, order.getOrderRecipieNr())
	if drinkMade:
		contactGuest(guestName, "FINISH")
	else: 
		contactGuest(guestName, "FAILED")

def contactGuest(guest, contactType):
	print "Guest " + guest + " has been contacted regarding: " + contactType

def contactAdmin(problem, string):
	print problem + string

def makeDrink(guestName, recipieNr):
	global drinkMenu, inventory		
	#make drink
	print "makeDrink def has recipieNr: " + str(recipieNr)
	recipieName = drinkMenu[recipieNr].getRecipieName()
	contactGuest(guestName, "CHECKING INV "+recipieName)
	contactGuest(guestName, "MAKING "+recipieName)
	recipie = drinkMenu[recipieNr].getIngredients()
	if checkDrink(recipie):
		for ingredient, amount in recipie.items():
			#servostuff for each ingredient.
			print ingredient, amount
			print inventory[ingredient].getAmount()
			inventory[ingredient].consume(amount)
			if inventory[ingredient].getAmount() < 12:
				contactAdmin("WARNING: Ingredient low! Restock soon!", ingredient)
		print"drink made"
	else:
		print "Unsuccessful: not enough inventory."
		return False
	return True

def checkDrink(recipie):
	global inventory
	for ingredient, amount in recipie.items():
		if inventory[ingredient].getAmount() < amount:
			print "not enough "+ ingredient
			return False
	return True
		
def restock(ingredient, iType, amount):
	global inventory
	if ingredient in inventory.keys():
		inventory[ingredient].restock(amount)
	else:
		ingredientX = Ingredient(ingredient, iType, amount, datetime.today())
		inventory[ingredientX.getIngredientName()] = ingredientX

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

# Create new threads
Bartender = BartenderThread(1, "iBartender", 1)
Butler = ButlerThread(2, "iButler", 2)
Butler.setDaemon(1)



#############
## RUNTIME ##
#############

# Start new Threads
Bartender.start()
Butler.start()

#resupply
#print "restocking Gin"
#restock("Bombay Sapphire Gin", 1, 5000)
#printInventory()
Bartender.join()
printInventory()
print "Exiting Main Thread"