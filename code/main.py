import os 
import pandas as pd
import numpy as np 
import json
import pymongo

path = "\\data\\"   #r"./code/data"
# os.chdir(path)
current_dir = os.getcwd()
print("current_dir",current_dir)
files = os.listdir(current_dir+path)
# address = []
# print(files)

def resources(files):
	# print(files)
	final_list = []
	for file in files:
		with open(current_dir +path+file) as f:
			try:
				data = json.loads(f.read(), encoding='utf-8')
			except Exception as e:
				# print("error in file:",file)
				pass
			address = []
			identifier_dict = {
				"Medical Record Number": "",
				"Social Security Number":"",
				"Driver's License":"",
				"Passport Number":""
				}
			identifier = []

	#         print(data)
			for i in range (len(data["entry"])):
				resource_dict = {}
				temp_list = []



				if data["entry"][i]["resource"]["resourceType"] == "Patient":
					
					resource_dict["resource_type"] = data["entry"][i]["resource"]["resourceType"]
					resource_dict["id"] = data["entry"][i]["resource"]["id"]
					try:
						# resource_dict["identifier"] = data["entry"][i]["resource"]["identifier"]
						identifier_dict["Medical Record Number"] = data["entry"][i]["resource"]["identifier"][1]["value"]
						identifier_dict["Social Security Number"] = data["entry"][i]["resource"]["identifier"][2]["value"]
						identifier_dict["Driver's License"] = data["entry"][i]["resource"]["identifier"][3]["value"]
						identifier_dict["Passport Number"] = data["entry"][i]["resource"]["identifier"][4]["value"]
						identifier.append(identifier_dict)
						resource_dict["identifier"] = identifier 
				#         print(identifier)
					except:
						pass
					try:
						if data["entry"][i]["resource"]["deceasedDateTime"] != []:
							resource_dict["active"] = "yes"

	#                     print("active:",active)
					except Exception as e:
						
						resource_dict["active"] = "No"
				#             print("error:",e)
						
					try:
						resource_dict["telecom"] = data["entry"][i]["resource"]["telecom"][0]["value"]
					except:
						pass
					try:

						name = data["entry"][i]["resource"]["name"][0]["given"][0]
						family = data["entry"][i]["resource"]["name"][0]["family"]

						resource_dict["name"] = name + " "+family
					except:
						pass
					try:
						resource_dict["gender"] = data["entry"][i]["resource"]["gender"]
					except:
						pass
					try:
						resource_dict["birthDate"] = data["entry"][i]["resource"]["birthDate"]
					except:
						pass
					try:
						resource_dict["deceasedBoolean"] = data["entry"][i]["resource"]["deceasedBoolean"]
					except Exception as e:
						pass
					try:
						resource_dict["multipleBirthBoolean"] = data["entry"][i]["resource"]["multipleBirthBoolean"]
					except:
						pass
					try:
						resource_dict["deceasedDateTime"] = data["entry"][i]["resource"]["deceasedDateTime"]
					except Exception as e:
						pass
					try:
						address = data["entry"][i]["resource"]["address"][0]["line"] # + data["entry"][i]["resource"]["address"][0]["city"]
						address.append(data["entry"][i]["resource"]["address"][0]["city"])
						address.append(data["entry"][i]["resource"]["address"][0]["state"])
						address.append(data["entry"][i]["resource"]["address"][0]["country"])
						address = ','.join(map(str, address))
						resource_dict["address"] = address
	#                     print(address)
					except Exception as e:
				#         resource_dict["address"] = data["entry"][i]["resource"]["address"][0]["line"]
						pass

					try:
						resource_dict["maritalStatus"] = data["entry"][i]["resource"]["maritalStatus"]["coding"][0]["display"]
					except:
						pass
					try:    
						resource_dict["organization"] = data["entry"][i]["resource"]["organization"]
					except:
						pass
					try:    
						resource_dict["period"] = data["entry"][i]["resource"]["period"]
	#                     print(period)
					except:
						pass
					try:    
						resource_dict["communication"] = data["entry"][i]["resource"]["communication"][0]["language"]["coding"][0]["display"]
	#                     print(communication)
					except:
						pass
					try:    
						resource_dict["language"] = data["entry"][i]["resource"]["communication"][0]["language"]["coding"][0]["display"]
	#                     print(language)
					except:
						pass   
					try:    
						resource_dict["preferred"] = data["entry"][i]["resource"]["communication"][0]["language"]["coding"][0]["display"]
	#                     print(preferred)
					except:
						pass 

					final_list.append(resource_dict)
	#                 print(final_list)
					i+=1

	return final_list

def mondo_db_save(df):
	path = os.getcwd()
	print("path",path)
	# path = "./"   #r"./code/data"
	

	out = df.to_dict()
	file = "/sample.json"
	with open(current_dir+file, "w") as outfile:
		json.dump(out, outfile)
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	emis_db = myclient["emis_database"]
	mycol = emis_db["resources"]
	file = "sample.json"
	with open(file) as f:
		data = json.loads(f.read())
		# print("mongodb", data)
		mycol.insert_many(data)

def db_search():
	for y in mycol.find():
		print(y) 


if __name__ == "__main__":
    try:

        final_list = resources(files)
        print(final_list)
        df = pd.DataFrame(final_list, columns =["resource_type","id","identifier","active",
"telecom","name","gender", "birthDate", "deceasedBoolean","multipleBirthBoolean","deceasedDateTime" ,"address" , 
 "organization","period","maritalStatus","communication" ])
        df.to_excel("patients.xlsx")
        try:
            mondo_db_save(df)
        except Exception as e:
            pass 
				
    except Exception as exception:
	    raise exception