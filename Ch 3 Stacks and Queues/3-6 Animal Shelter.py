class Animal:
	def __init__(self, name):
		self.name = name
		self.__order = None

	def setOrder(self, order):
		self.__order = order

	def returnOrder(self):
		return self.__order


class Dog(Animal):
	def __init__(self, name):
		super().__init__(name)


class Cat(Animal):
	def __init__(self, name):
		super().__init__(name)


class AnimalQueue():
	def __init__(self):
		self.dogs = []
		self.cats = []
		self.__order = 0

	def enqueue(self, a):
		a.setOrder(self.__order)
		self.__order += 1

		print("Enqueued ", a.name)

		if isinstance(a, Dog):
			self.dogs.append(a)
		elif isinstance(a, Cat):
			self.cats.append(a)


	def dequeueAny(self):
		if not len(self.dogs) and not len(self.cats):
			return "All animals are sold out"

		elif not len(self.dogs):
			self.dequeueDog()
			
		elif not len(self.cats):
			self.dequeueCat()

		# compare orders/arrival
		dog = self.dogs[0]
		cat = self.cats[0]
		if dog.returnOrder() <= cat.returnOrder():
			return self.dogs.pop(0).name
		else:
			return self.cats.pop(0).name


	def dequeueDog(self):
		if not len(self.dogs):
			return "All Dogs are sold out"

		return self.dogs.pop(0).name


	def dequeueCat(self):
		if not len(self.cats):
			return "All Cats are sold out"

		return self.cats.pop(0).name


	def printDogsCats(self):
		print("Dogs: ", self.dogs)
		print("Cats: ", self.cats)


# creating animals
d1 = Dog("dDaniel")
d2 = Dog("dTommy")
c1 = Cat("cGarfield")
c2 = Cat("cKitty")
c3 = Cat("cNeo")
c4 = Cat("cKaddy")
print(d1.name)

# creating queue
q = AnimalQueue()
# q.printDogsCats()

# inserting animals in queue
q.enqueue(d1)
q.enqueue(c1)
q.enqueue(c2)
q.enqueue(c3)
q.enqueue(d2)
q.enqueue(c4)

# q.printDogsCats()

print("\nDequeued Any: ", q.dequeueAny())
print("Dequeued Cat: ", q.dequeueCat())
print("Dequeued Dog: ", q.dequeueDog())
print("Dequeued Dog: ", q.dequeueDog())
print("Dequeued Any: ", q.dequeueCat())
print("Dequeued Cat: ", q.dequeueCat())
print("Dequeued Cat: ", q.dequeueCat())
print("Dequeued Cat: ", q.dequeueCat())
print("Dequeued Any: ", q.dequeueAny())
