# Week 7 Assignment: Hands-On Lab — Shopping List Manager
list_warmup.py - Practises basic list operations by creating a fruits list, reading items by index, using .append() and .remove() and printing the count with len().
shopping_list.py - An interactive menu (add / remove / show / done) that manages a shopping list and safely handles removing items that aren't there.
list_report.py - Loops through a list to print it numbered, count names longer than 4 letters and find the longest name using a loop comparison.

Why is it safer to check 'in' before calling .remove()?
If you call .remove() on an item that isn't in the list, Python raises a ValueError and the program crashes. Checking with in first lets the program handle the missing item calmly for example by printing "That item is not on your list." and keep running. This matters in programs like the shopping list manager where users can type anything including items they never added.
