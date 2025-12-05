basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

data = {

}
data.update(basic_data)
data.update(advanced_data)
print(data)