def calc_cd(amount, rate, months):
  # Month 01
  balance = amount  + amount * rate / 12

  count = 1
  while count < months:
    balance = balance  + balance * rate / 12
    count += 1

  return int(balance * 100) / 100


def compound_interest(value, rate, months):
  rate = rate / 12 # Monthly Rate
  balance =  value + value * (1+rate) # The first month
  print("For {} month the amount is {}".format('1',balance))
  cmonth = 2
  while cmonth <= months:
    balance =  value + balance * (1+rate)
    print("For {} month the amount is {}".format(cmonth,balance)) 
    cmonth += 1
    
  return (int((balance -value )* 100) / 100) 

def sum_squared(N):
  sum = 0
  count = 1
  while count <= N:
    sum = sum + count ** 2
    count += 1
  return sum

def reverse_number(number):
  strnumber = ''
  while number > 0:
    strnumber = strnumber + str(number % 10)
    number = int(number / 10)
  return strnumber

# print(compound_interest(100,0.05,4))
# print(compound_interest(200,0.06,5))
# print(compound_interest(50,0.05,12))
# print(sum_squared(100))
# print(reverse_number(1335))

# Assume card_number is a String of numbers
def sum_odd_places(card_number):
  total = 0
  for i in range(len(card_number)-1, -1, -2):
    if i % 2 == 1:
        total += int(card_number[i])
    
  return total

# Assume card_number is a String of numbers
def sum_even_places(card_number):
  total = 0
  for i in range(len(card_number)-1, -1, -1):

    if i % 2 == 0:
      print(str(i) + ' - ' + card_number[i])
      double = int(card_number[i]) * 2
      if double > 9:    
        double -= 9
      total += double
  return total

# Building a Deck of cards
def buildDeck():
    deck = []
    for suite in ["Hearts", "Spades", "Clubs", "Diamonds"]:
        # as well as its cards
        for card_num in range(2, 11):
            name = [str(card_num), "of", suite]
            card = " ".join(name)
            deck.append(card) # Append adds the string to the deck

            if card_num == 2:
                print(card)

    for face in ["Jack", "Queen", "King", "Ace"]:
        name = [face, "of", suite]
        card = " ".join(name)
        deck.append(card)
    # return deck

# print(sum_odd_places('4012888888881881'))
# print(sum_even_places('4012888888881881'))
buildDeck()

def alarm_clock(day):
  if day == "Sun" or day == "Sat":
    return "9:00"
  else:
    return "7:00"

for i in range(5):
  day = i * 2 % 7
  days = ["Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat"]
  print(days[day], alarm_clock(days[day]))


def card_title(number, suite):
  suites = ["Hearts", "Clubs", "Spades", "Diamonds"]
  numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven",
             "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
  return numbers[number] + " of " + suites[suite]

if __name__ == '__main__':
  print(card_title(2, 3))
  print(card_title(8, 0))
  print(card_title(0, 2))
  print(card_title(10, 1))

def find_indices_of_character(ch, string):
  indices = []
  for i in range(len(string)):
    if string[i] == ch:
      indices.add(i)
  return indices


# print(find_indices_of_character('F', 'Foundation'))


def average_evens(numbers):
    # Implement your solution here
    total = 0
    count = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
            count += 1
    return total / count

# print(average_evens([2, 4, 5, 8]))

def count_vowels(words):
  # Enter your implementation here
    count = 0
    for word in words:
      for ch in word:
        if ch == 'a' or ch == 'A':
          count += 1
        elif ch == 'e' or ch == 'E':
          count += 1
        elif ch == 'i' or ch == 'I':
          count += 1
        elif ch == 'o' or ch == 'O':
          count += 1
        elif ch == 'u' or ch == 'U':
          count += 1
    return count

# print(count_vowels(['dog', 'cat', 'cow', 'rabbit']))

def eliminate_duplicates(collection):  
    clean = []  
    clean.append(collection[0])
    for i in range(len(collection)):
        if collection[i] not in clean:
            clean.append(collection[i])
    return clean

# print(eliminate_duplicates(['dog', 'cat', 'cow', 'rabbit']))

import random as r

def shuffle(items):
  for i in range(len(items)):
    # Generate a random number between 0 and 51, inclusive
    rand_idx = r.randint(0, len(items)-1)
    temp = items[i] # Store the original value in a temp variable
    items[i] = items[rand_idx] # Save the random "card" to it
    items[rand_idx] = temp # And move the original card there

  return items

# def main():
#   deck = []

#   # A Nested loop to traverse each suite
#   for suite in ["Hearts", "Spades", "Clubs", "Diamonds"]:
#     # as well as its cards
#     for card_num in range(2, 11):
#       name = [str(card_num), "of", suite]
#       card = " ".join(name)
#       deck.append(card) # Append adds the string to the deck

#     for face in ["Jack", "Queen", "King", "Ace"]:
#       name = [face, "of", suite]
#       card = " ".join(name)
#       deck.append(card)

#   print("Ordered")
#   print(deck)
#   # Lists are complex, so if we update the list in a function
#   # it will update in the original list too!
#   shuffle(deck)
#   print("Shuffled")
#   print(deck)

# if __name__ == '__main__':
#   main()
      

def add_matrices(list1, list2):
    add_list = []
    for i in range(len(list1)):
        alist1 = list1[i]
        alist2 = list2[i]
        alist = []
        for j in range(len(alist1)):
          alist.append(alist1[j] + alist2[j])
        add_list.append(alist)
    return add_list

# print(add_matrices([[1,2],[1,2],[1,2]],[[1,2],[1,2],[1,2]]))

import math
def distance(p0, p1):
  x1 = p0[0]
  y1 = p0[1]
  x2 = p1[0]
  y2 = p1[1]

  return math.sqrt((x2-x1)**2+(y2-y1)**2)

def triangle_area(points):
   a = distance(points[0], points[1])
   b = distance(points[1], points[2])
   c = distance(points[2], points[0])
   print("A - {}, B - {}, C - {} ".format(a,b,c))
   s = ( a + b + c) / 2
   return math.sqrt(s*(s-a)*(s-b)*(s-c))

# print(triangle_area([[1.5, -3.4], [4.6, 5.0], [9.5, -3.4]]))
# print(triangle_area([[2.5, 2.0], [5.0, -1.0], [4.0, 2.0]]))
# print(triangle_area([[2.0, 2.0], [4.0, 4.0], [6.0, 6.0]]))

def grayscale(pixels):
    gsList = []
    for pixel in pixels:
        alist = []
        for values in pixel:            
            total = 0    
            for value in values:
                total += value
            alist.append(int(total / len(values)))
        gsList.append(alist)
    return gsList              

pixels = [[[222, 152, 158], [248, 189, 194], [247, 149, 156]],
          [[171, 169, 171], [244, 244, 244], [226, 217, 219]],
          [[154, 154, 154], [212, 212, 212], [110, 110, 110]]]

# print(grayscale(pixels))

words = [['dog', 'cat', 'cow', 'rabbit'], 
         ['sesame', 'chia', 'flax', 'sunflower'],
         ['Toyota','Chevy','Porsche','Dodge'],
         ['Monday','Tuesday','Wednesday','Thurday']]

# print(len(words[3][2]))
# print(words[0][len(words[0][0])])
# print(words[1][2])
# print(words[2][2])

for i in range(len(words)):
  for j in range(len(words)):
    print(words[i][j])

def function(nested_list):
  total = 0
  for i in range(len(nested_list) - 1, -1, -1):
    for j in range(len(nested_list[i]) - 1, -1, -1):
      if nested_list[i][j] % 3 == 0:
        total += nested_list[i][j]
  return total

alist = [[3, 4, 5], [7, 9, 5], [6, 7, 9]]
# print(function(alist))

def nearest_point(coordinates, points):
  closest = points[0]
  closest_dist = distance(coordinates, closest)
  for i in range(points):
    point = points[i]
    dist = distance(coordinates, point)
    if dist > closest_dist:
      closest = points[i]
      closest_dist = dist
  return closest
      

def summation(numbers, depth):
  if len(numbers) == 1:
    print("Non-recursive Call", depth)
    return numbers[0]
  else:
    print("Recursive Call", depth)
    subset = numbers[1:]
    return numbers[0] + summation(subset, depth + 1)

# summation([6,5,4,3,2,1], 1)  

def reverse(string):
    if len(string) == 1:
      return string
    else:
       return reverse(string[1:])+string[0]
    
# print(reverse("Hello"))

def linear_search(alist, key, idx):
  if alist[idx] == key and idx > -1:
    return idx
  else:
    return linear_search(alist, key, idx+1)
  
# print(linear_search([1,2,3,4,5,6,7,8,9,0], 5, -1))  

def int_to_bin(number):
    if number <= 1:
        return str(number)
    else:
        remainder = number % 2
        return int_to_bin(int(number/2))+str(remainder)
    
print(int_to_bin(8))    
      


          