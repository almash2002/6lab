'''Тізімдердегі, кортеждердегі, жиындардағы және
 сөздіктердегі әдістерді қарастырып,барлығына ортақ
 5 әдісті және ерекшеленетін бірнеше (2-3) әдістерді қолдананатын бағдарлама жаз. '''

list = ["Yerzhanova", "Almash", "Yerzhanovna"]

print("\n", "Лист:"+"\n", list)

list.append("20 y.o")
print("\n", list)

x = "28.02.2002"
list.insert(3, x)
print("\n", list)

list.pop(4)
print("\n", list)

#-----------------------------------------------------------------------------

tuple = ("Kazakhstan", "Oral")
print("\n", "Кортеж:"+"\n", tuple)

tuple2 = ("Kazakhstan", "Almaty")
tuple3 = tuple + tuple2
print("\n", tuple3)

print("\n", tuple3.count("Kazakhstan"))

print("\n", tuple3.index("Almaty"))

#-----------------------------------------------------------------------------

set = {"Satbayev University", "Course 4", "Computer Science"}

print("\n", "Коллекция:"+"\n", set)

set.add("GPA: 3.2")
print("\n", set)

set.remove("Course 4")
print("\n", set)

print("\n", len(set))

set2= {"Satbayev University", "Programming Engenering", "Shablony Proektirovanie"}
print("\n", set2)
print("\n", set.difference(set2))

#-----------------------------------------------------------------------------

dict = {"IIN": "020728651302", "Phone number": "87072801433"}

print("\n", "Словарь:"+"\n", dict)

dict["Home number"] = "280-14-33"
print("\n", dict)

dict.pop("IIN")
print("\n", dict)

v = dict.get("Phone number")
print("\n", v)

k = dict.keys()
print("\n", k)

