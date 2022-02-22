import os 
import pandas as pd
import numpy as np 
import json
import pymongo

path = r"./data"
try:
    os.chdir(path)
except:
    pass
files = os.listdir()

def resources(files):
	print(files)
	final_list = []
	for file in files:
	    with open(file) as f:
	        try:
	            data = json.loads(f.read(), encoding='utf-8')
	        except Exception as e:
	            print("error in file:",file)
	            pass

	#         print(data)
	        for i in range (len(data["entry"])):
	            resource_dict = {}
	            temp_list = []
	            if data["entry"][i]["resource"]["resourceType"] == "Patient":
	                
	                resource_dict["resource_type"] = data["entry"][i]["resource"]["resourceType"]
	                resource_dict["id"] = data["entry"][i]["resource"]["id"]
	                try:
	                    resource_dict["identifier"] = data["entry"][i]["resource"]["identifier"]
	            #         print(identifier)
	                except:
	                    pass
	                try:
	                    resource_dict["active"] = data["entry"][i]["resource"]["active"]
	#                     print("active:",active)
	                except Exception as e:
	            #             print("error:",e)
	                    pass
	                try:
	                    resource_dict["telecom"] = data["entry"][i]["resource"]["telecom"]
	                except:
	                    pass
	                try:
	                    resource_dict["name"] = data["entry"][i]["resource"]["name"][0]["given"]
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
	                    resource_dict["deceasedDateTime"] = data["entry"][i]["resource"]["deceasedDateTime"]
	                except Exception as e:
	                    pass
	                try:
	                    resource_dict["address"] = data["entry"][i]["resource"]["address"][0]["line"] # + data["entry"][i]["resource"]["address"][0]["city"]
	                    address.append(data["entry"][i]["resource"]["address"][0]["city"])
	                    address.append(data["entry"][i]["resource"]["address"][0]["state"])
	                    address.append(data["entry"][i]["resource"]["address"][0]["country"])
	                    resource_dict["address"] = ",".join(address)
	#                     print(address)
	                except:
	            #         resource_dict["address"] = data["entry"][i]["resource"]["address"][0]["line"]
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


if __name__ == "__main__":
    try:

        final_list = resources(files)
        print(final_list)
        df = pd.DataFrame(final_list, columns =["resource_type","id","identifier","active",
"telecom","name","gender", "birthDate", "deceasedBoolean","deceasedDateTime" ,"address" , 
 "organization","period","maritalStatus","communication" ])
        df.to_excel("patients.xlsx")
                
    except Exception as exception:
        raise exception