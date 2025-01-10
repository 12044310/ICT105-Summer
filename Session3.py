# Seeing the world #
#1.Think of at least five places in the world you’d like to visit.​#
places_visit = ['Finland','Norge','Danmark','Switzerland','Iceland']

#2.Print your list in its original order.#
print(places_visit)

#3.Use sorted() to print your list in alphabetical order without modifying the actual list.#
sorted_places = sorted(places_visit)
print(sorted_places)

#4.Show that your list is still in its original order by printing it.#
print(places_visit)

#5.Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.​#
places_visit.reverse()
print(places_visit)

#6.Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.#
places_visit.reverse()
print(places_visit)

#7.Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.​#
places_visit.sort()
print(places_visit)

#8.Use sort() to change your list so it’s stored in reverse-alphabetical order.​#
places_visit.sort(reverse=True)
print(places_visit)

#----------------------------------------------------------------------------------------#
#Lists - Dinner Party#
#1.Make a list that includes at least three people you’d like to invite to dinner.#
dinner_list = ['Jenny','Ellen','Chaos']

#2.inviting them to dinner.​#
for list in dinner_list:
    print(f"{list},I'd like to invite you for dinner tonight.")

#3.One of your guests can’t make the dinner.
#Modify your list, replacing the name of the guest who can’t make it with the  name of the new person you are inviting.​#
dinner_list[dinner_list.index("Chaos")] = "JC"

#4.Print a second set of invitation messages, one for each person who is still in your list.​#
for list in dinner_list:
    print(f"{list},I'd like to invite you for dinner tonight.")

#There is now a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.​#

#5.Use insert() to add one new guest to the beginning of your list.​#
dinner_list.insert(0,"Jungle")

#6.Use insert() to add one new guest to the middle of your list.​#
dinner_list.insert(2,"Ganma")

#7.Use append() to add one new guest to the end of your list.​#
dinner_list.append("Rong")

#8.Print a new set of invitation messages, one for each person in your list#
for list in dinner_list:
    print(f"{list},I'd like to invite you for dinner tonight.")

#New dinner table won’t arrive in time for the dinner, and now you have space for only two guests. #

#9.Add a new line that prints a message saying that you can invite only two people for dinner. ​#
print ("Unfortunately,I can invite only two people for dinner.")

#10.Use pop() to remove guests from your list one at a time until only two names remain in your list#
while len(dinner_list) > 2:
    remove_list = dinner_list.pop()
#11.print a message to that person letting them know you’re sorry you can’t invite them to dinner. ​#
    print(f"Sorry {remove_list}, I can't invite you to dinner tonight. ")

#12.Print a message to each of the two people still on your list, letting them know they’re still invited. ​.#
for list in dinner_list :
    print(f"Hi {list},you're still invited to dinner tonight")