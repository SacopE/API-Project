import requests

url = 'https://www.movebank.org/movebank/service/public/json?&study_id=2911040&individual_local_identifiers=4262-84830876&sensor_type=gps&event_reduction_profile=EURING_03'

response = requests.get(url)

data = response.json()

num = 0

possibilities = {}

print('This application is view information about a study for the Waved Albatross & it\'s migration patterns.')

for i in data['individuals'][0]:
    num += 1
    print(f"{num}: {i}")
    possibilities[num] = i
print('8: Quit')
while True:
    choice = int(input('Enter the number of the data type you want to access.\n'))
    if choice - 1 in range(8):
        if choice == 8:
            print('Goodbye!')
            break
        elif choice == 7:
            location = int(input('Enter the number of the location you want to access (0 to 478): '))
            if location - 1 in range(478):
                print(data['individuals'][0][possibilities[choice]][location])
            else:
                print('Please choose a valid number')
        else:
            print(data['individuals'][0][possibilities[choice]])
    else:
        print('Please choose a valid number')
# location = int(input('Enter the number of the location you want to access (0 to 478)'))

# print(data['individuals'][0]['locations'][location])




# https://www.movebank.org/movebank/service/public/json?study_id=2911040&individual_local_identifiers=4262-84830876&sensor_type=gps