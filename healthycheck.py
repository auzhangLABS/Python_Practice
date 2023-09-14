#Code Challenge Parse Staus JSON
import json


#since this is a json file used JSON package
new_data= """
{ 
  "Status": "Healthy",
  "Checks": [
    {
      "Name": "Connections",
      "Status": "Healthy"
    },
    {
      "Name": "ConnectionRead",
      "Status": "unHealthy"
    },
    {
      "Name": "redis",
      "Status": "Healthy"
    },
    {
      "Name": "ProcessCheck",
      "Status": "Healthy"
    },
    {
      "Name": "UserProfile",
      "Status": "unHealthy"
    },
    {
      "Name": "features",
      "Status": "unHealthy",
      "Description": "sample sample sample"
    },
    {
      "Name": "shutdown",
      "Status": "Healthy"
    },
    {
      "Name": "lifespan",
      "Status": "unHealthy"
    }
  ]
}

"""



new_datav2 = json.loads(new_data)
# print(new_datav2)
# 2 dict in data. One is Status and the other is Checks. Checks dict has values 
# of list
#getting values for key Checks
# print(new_datav2.get("Checks"))
# data = new_datav2.get("Checks")
# print(data)

#make a function that will output the number of healthy and unhealthy checks
def nums(di):
  data = di.get("Checks")
  #print(data) this is here to validate information is passing correctly
  h_count = 0
  u_count = 0
  invalid = 0
  for x in data:
    eq = x.get('Status').lower()
    #print(eq) this is here to validate information is passing correctly
    if eq =="healthy":
      h_count = h_count + 1
    elif eq == "unhealthy":
      u_count = u_count + 1
    else:
      invalid = invalid + 1
  #return(h_count,u_count,invalid)
  return(f'Numbers of healthy checks: {h_count} \nNumbers of unhealthy checks: {u_count} \nNumbers of Invalid checks: {invalid}')

#make a function that will create and output the list of unhealthy names
def nameh(di):
  data = new_datav2.get("Checks")
  # print(data)
  h_items = []
  u_items = []
  invalid = []
  for x in data:
    eq = x.get("Status").lower()
    if eq == "healthy":
      name = x.get("Name")
      h_items.append(name)
    elif eq == 'unhealthy':
      name1 = x.get("Name")
      u_items.append(name1)
    else:
      name2 = x.get("Name")
      invalid.append(name2)
  # return(h_items,u_items,invalid)
  return(f'List of healthy checks items: {h_items} \nList of unhealthy checks items: {u_items} \nList of invalid checks items: {invalid}')


def main():
  print(nums(new_datav2))
  print(nameh(new_datav2))

main()