class StackNode():
    # next can default to "None", meaning the end of a Stack 
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class Stack():
    def __init__(self):
        self.size = 0
        self.front = None # Nothing in stack to start
    
    # Add a new element to the "Stack"
    def push(self, data):
        node = StackNode(data)
        if self.size == 0:
            self.front = node
        else:
            current = self.front
            while current.next != None:
                current = current.next
            current.next = node
        self.size += 1
    
    #Remove the last element added to the Stack
    def pop(self):
        current = self.front
        if self.size == 0: # Empty Stack
            return None
        elif self.size == 1: 
            popped = current
            self.front = None
        else: 
            while current.next.next != None:
                current = current.next
            popped = current.next
            current.next = None
        
        self.size -= 1
        return popped.data
    
if __name__ == '__main__':
    s = Stack()
    # for i in range(1, 10):
    #     s.push(i)
    
    # while s.size > 0:
    #     print(s.pop())
    for i in range(1,5):
        s.push(i)

    while s.size > 0:
        element = s.pop()
        if element % 2 == 0:
            s.push(element + 1)
        print(element)


class TV():
  def __init__(self):
    self.channel = 1
    self.volume = 10
    self.on = False

  def turn_on(self):
    self.on = True

  def turn_off(self):
    self.on = False

  def increase_volume(self):
    self.volume += 1

  def decrease_volume(self):
    self.volume -= 1

  def channel_up(self):
    # Only 120 channels
    self.channel = (self.channel + 1) % 120

  def channel_down(self):
    # Only 120 channels
    self.channel = (self.channel - 1) % 120

  def set_channel(self, new_channel):
    if new_channel > 0 and new_channel <= 120:
      self.channel = new_channel
    else:
      print("Unknown Channel")

if __name__ == '__main__':
  tv = TV()
  for i in range(10):
    tv.increase_volume()

  tv.set_channel(300)

  print("Current Volume:", tv.volume)
  print("Current Channel:", tv.channel)


  class Card:
    def __init__(self, number, suite):
        self.number = number
        self.suite = suite

    def is_face(self):
        # Ace, Jack, Queen, King
        if self.number in [1, 11, 12, 13]:
            return True
        else:
            return False
  
    def is_ace(self):
        if self.number == 1:
            return True
        else:
            return False
  
    def __str__(self):
            printOut = ""
            if self.number == 1:
                printOut = "Ace of " + suite
            elif self.number == 2:
                printOut = "Two of " + suite
            elif self.number == 3:
                printOut = "Three of " + suite
            elif self.number == 4:
                printOut = "Four of " + suite
            elif self.number == 5:
                printOut = "Five of " + suite
            elif self.number == 6:
                printOut = "Six of " + suite
            elif self.number == 7:
                printOut = "Seven of " + suite
            elif self.number == 8:
                printOut = "Eight of " + suite
            elif self.number == 9:
                printOut = "Nine of " + suite
            elif self.number == 10:
                printOut = "Ten of " + suite
            elif self.number == 11:
                printOut = "Jack of " + suite
            elif self.number == 12:
                printOut = "Queen of " + suite
            else:
                printOut = "King of " + suite
            return printOut

if __name__ == '__main__':
  suites = ["Clubs", "Diamonds", "Spades", "Hearts"]
  for num in [3, 6, 9, 12]:
    suite = suites[num % 4]
    card = Card(num, suite)
    print(card)

from datetime import datetime

class Exercise():
  def __init__(self, exerlang, title, desc):
    self.exerlang = exerlang
    self.title = title
    self.desc = desc
    self.visible = False
    self.created = datetime.utcnow()

  def update_exerlang(self, exerlang):
    self.exerlang = exerlang

  def update_title(self, title):
    self.title = title

  def update_desc(self, desc):
    self.desc = desc

  def toggle_visibility(self):
    self.visible = not self.visibility # Flip the value

  def __str__(self):
    # Should return something like:
    # "<Exercise (Typing Exercise - Representing TYPOS Exercises)>"
    # "<Exercise (Document Code - Check Exercise)>"
    return '<Exercise {0} (1)>'.format(self.title, self.exertype)    
  

class CQueue:
  def __init__(self):
    self.numbers = []
    self.size = 0

  def enqueue(self, number):
    self.size += 1
    self.numbers.append(number)

  def is_empty(self):
    return self.size == 0

  def dequeue(self):
    # Enter your implementation here
      self.size -= 1
      return self.numbers.pop()

    
a_list = [1, 2, 4, 3, 5, 6]
q = CQueue()
for item in a_list:
  q.enqueue(item)

output = []
while q.is_empty() == False:
  output.append(q.dequeue())
print(output)

    
class Clock():
  def __init__(self, time):
    self.time = time

  def print_time(self):
    # self.time = "6:30"
    print(self.time)

  def set_time(self, time):
    self.time = time    

if __name__ == '__main__':
  carolinaClock = Clock("5:30")
  print(id(carolinaClock))
  parisClock = carolinaClock
  parisClock.set_time("10:30")
  print(id(parisClock))
  carolinaClock.print_time()


class Exercise():
  def __init__(self, exerlang, title, desc):
    self.exerlang = exerlang
    self.title = title
    self.desc = desc
    self.visible = False
    self.created = datetime.utcnow()

  # Uncommon, but for when you accidentally save in the wrong language
  def update_exerlang(self, exerlang):
    self.exerlang = exerlang

  def update_title(self, title):
    self.title = title

  def update_desc(self, desc):
    self.desc = desc

  def toggle_visibility(self):
    self.visible = not self.visible # Flip the value

  def __str__(self):
    # Should return something like:
    # "<Exercise (Typing Exercise - Representing TYPOS Exercises)>"
    # "<Exercise (Document Code - Check Exercise)>"
    return '<Exercise ({0} - {1})>'.format(self.title, self.desc)

class TypingExercise():
  def __init__(self, exerlang, title, desc, image_data, source_code):
    Exercise.__init__(self, exerlang, title, desc)
    # Can also use super().__init__(self, exerlang, title, desc)
    self.source_code = source_code
    self.image_data = image_data

  def update_image_data(self, image):
    self.image_data = image

  def get_image_data(self):
    return self.image_data  

# e = Exercise('Python','Test 1','Python Desc')  
te = TypingExercise('Python','Test 1','Python Desc','image','source code')
print(te)
print(te.get_image_data())


class Spell:
    def __init__(self, name, incantation):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + " - " + self.incantation + "\n" + self.get_description()
                     
    def get_description(self):
        return "No description"

    def perform(self):
        print(self.incantation)


class Aero(Spell):
  def __init__(self):
    Spell.__init__(self, "Aero", "Quetzacoatl Aerora")
    self.description = "An Elemental spell that places a vortex of air shooting victims upward"

  def get_description(self):
    return self.description

class Drain(Spell):
    def __init__(self):
      Spell.__init__(self, "Drain", "Diabolos Drainga")
      self.description = "Drains life from the victim and is absorbed into the caster"

    def get_description(self):
        return self.description
    
if __name__ == '__main__':
  print(Aero())
  # spell = Aero()
  # spell.perform()
  # print(spell)
  # print(Drain())    


  spells={
    'Charms': {
        'aberto' : 'a spell used to open doors',
        'accio' : 'a spell used to summon items'
    },
    'Healing': {
        'anapneo' : 'a spell used to clear an airway ',
        'episkey' : 'a spell used to fix broken noses'
    }
}
print("These are all the spells you can use: ")
for magic in spells.values():
  for name, description in magic.items():
    print(name)

houses={
    "Gryffindor" : {
        "student1" : "Harry Potter",
        "student2" : "Hermione Granger"
    },
    "Slytherin" : {
        "student1" : "Draco Malfoy",
        "student2" : "Tom Riddle"
    }
}

gryffindorStudent2 = houses['Gryffindor']['student2']
print('Gryffindor Student Number 2', gryffindorStudent2)    

def class_average(roster):
  # Enter your implementation here
  total = 0
  for key, value in roster.items():
    total += int(value)
  return total / len(roster)

# print(class_average({"Harry": 90, "Ron": 80, "Malfoy": 92, "Hermione": 100}))   
 
# print(class_average({"Leo": 95, "Don": 100, "Ralph": 75, "Mike": 75})) 

# print(class_average({"Kwame":93, "Wheeler":76, "Linka":76, "Gi":80, "Ma-Ti":91})) 


def caesar_cipher(sentence, cipher):
  # Enter your implementation here
  words = sentence.split(' ')
  encryptSentenceList = []
  for word in words:
      encryptWord = ''
      for ch in word:
        if ch in cipher:
          encryptWord += cipher[ch]
        else:
          encryptWord += ch 
      encryptSentenceList.append(encryptWord)
  
  return ' '.join(encryptSentenceList) 
               
        

cipher = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m',
'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

print(caesar_cipher("Programming is fun!", cipher))
print(caesar_cipher("cat", cipher))

mydict = {"cat":12, "dog":6, 
          "elephant":23, "bear":20}

keylist = list(mydict.keys())

keylist.sort()
print(keylist)
print(keylist[3])

answer = mydict.get("cat") // mydict.get("dog")
print(answer)

print("dog" in mydict)
print(23 in mydict)

total = 0

for akey in mydict:
  if len(akey) > 3:
    total = total + mydict[akey]
print(total)    

print(mydict["dog"])

mydict["mouse"] = mydict.get("cat") + mydict.get("dog")

print(mydict.get("mouse"))

# mydict["mouse"] = mydict.get("cat") + mydict.get("magpie")

# print(mydict.get("mouse"))

weather = {
  "coord": {
    "lon": -78.64,
    "lat": 35.78
  },
  "weather": [{
    "id": 802,
    "main": "Clouds",
    "description": "scattered clouds",
    "icon": "03d"
  }],
  "base": "stations",
  "main": {
    "temp": 66.16,
    "feels_like": 59.65,
    "temp_min": 64,
    "temp_max": 68,
    "pressure": 1012,
    "humidity": 45
  },
  "visibility": 16093,
  "wind": {
    "speed": 9.17,
    "deg": 310,
    "gust": 26.4
  },
  "clouds": {
    "all": 40
  },
  "dt": 1587235069,
  "sys": {
    "type": 1,
    "id": 5645,
    "country": "US",
    "sunrise": 1587206216,
    "sunset": 1587253811
  },
  "timezone": -14400,
  "id": 4487042,
  "name": "Raleigh",
  "cod": 200
}

print(weather.get("main").get("temp"))


def letter_count(character):
  filename = "djangobasic1/persons_app/wordlist.txt"
  # Complete the rest of the solution here
  file_object = open(filename,"r")
  file_lines = file_object.readlines()
  
  count = 0
  for line in file_lines:
    if line[0] == character:
      count += 1
  return count  

print(letter_count('a'))


import math
def squared(number):
  try:
    if number >= 0:
      return number ** 2
    else:
      raise Exception("Number cannot be less than zero")
  except Exception as e:
    return e

for n in [5, 10, -5]:
  print("Number: {}".format(n))
  calc = squared(n)
  print("Squared: {}".format(calc))

import csv

filename = "djangobasic1/persons_app/iris.csv"
fi = open(filename, 'r')
reader = csv.DictReader(fi)

for field in reader.fieldnames:
  print(field)

fi.close()

import csv
fi = open('data.csv','w')
cols = ['id','exam1','exam2','category']

writer = csv.DictWriter(fi, fieldnames=cols)
writer.writeheader()

writer.writerow({'id':253, 'exam1':98, 'exam2':80,'category':'Freshman'})
writer.writerow({'id':254, 'exam1':75, 'exam2':76,'category':'Sophmore'})
fi.close()

import datetime
from django.utils import timezone

print(datetime.datetime.now())
print(timezone.now())