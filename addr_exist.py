import requests

def check_addresses_exist(address_list, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    results = {}
    for address in address_list:
        params = {'address': address, 'key': api_key}
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'OK':
                results[address] = 'Exists'
            else:
                results[address] = 'Does not exist'
        else:
            results[address] = 'Error checking address'
    return results

# Example usage
api_key = 'AIzaSyBCAuzvQ5vMh96dVoSjY288YFnZ2JMTssQ'  # Replace with your actual Google API key
addresses = [
    "aoesrntoaiesrnt",
    # "517 29 1/4 Rd, Grand Junction, CO 81504",
    # "381 Surrey Ridge, Eaton, CO 80615",
    # "1887 Tartan Rd, Turlock, CA 95382",
    # "19980 Soaring Wing Dr, Colorado Springs, CO 80908",
    # "181765 Arrowwood Dr, Monument, CO 80132",
    # "5353 N. Hwy 1, Ft. Collins, CO 80524",
    # "858 Timber Lakes Grove, Monument, CO 80132",
    # "10209 Cherokee Dr, Salida, CO 81201",
    # "7024 Maplewood Pl, Centennial, CO 80111",
    # "838 S. 199th Ln, Buckeye, AZ 85326",
    # "9266 E. 35th Ave, Denver, CO 80238",
    # "13992 E. Marina Dr. #105, Aurora, CO 80014",
    # "12995 Co Rd. 140, Salida, CO 81201",
    # "7526 Loch Fyne Ln, Colorado Springs, CO 80908",
    # "10188 W. Co. Rd. 190, Salida, CO 81201",
    # "P.O. Box 173, Elfrida, AZ 85610",
    # "24429 Beals Chapel Rd, Lenoir City, TN 37772",
    # "3509 Co. Rd. 250, Salida, CO 81201",
    # "18290 Canterbury Dr, Monument, CO 80132",
    # "822 Foxglove St, Erie, CO 80516",
    # "PO Box 482, Palmer Lake 80133",
    # "2017 Snyder Avenue, Colorado Springs, CO 80909",
    # "203 Wright St. Apt. 4-106 Lakewood, CO 80228",
    # "10251 W 44th Ave Unit 7-201 Wheat Ridge, CO 80033",
    # "1427 Bellaire Drive, Colorado Springs, CO 80909",
    # "6155 Shoup Road, Colorado Springs, CO, 80908",
    # "3771 Scott Lane, Colorado Springs, CO, 80907",
    # "28614 N 68th Drive, Peoria, AZ 85383",
    # "2200 Waterview Parkway, Apt. 31212, Richardson, TX 75080",
    # "8066 East Dartmouth Street, Mesa, AZ 85207",
    # "690 Vikings Parkway D-121 Eagan, MN 55121",
    # "478 W. Calle Franja Verde, Sahurita, AZ 85629",
    # "4716 West Saguaro Park Lane, Glendale AZ, 85310",
    # "2140 West Thunderbird Road,Building 26, Apt.  2621 Pheonix, AZ 85023",
    # "9414 West Fillmore Street, Tolleson, AZ 85353",
    # "4716 West Saguaro Park Lane, Glendale AZ, 85310",
    # "9620 Trotter Circle, Colorado Springs, CO 80908",
    # "2705 Heathrow Drive, Colorado Springs, CO 80920",
    # "2705 Heathrow Drive, Colorado Springs, CO 80920",
    # "6075 Moorfield Avenue, Colorado Springs, CO 80919",
    # "6953 Palace Drive, Colorado Springs, CO 80918",
    # "40 N. 4th Street, Apt.1G, Brooklyn NY 11249",
    # "3367 Lewis University, 1 University parkway, Romeoville, IL 60446",
    # "10211 Ura Lane, Apt. 8-307, Thorton CO 80260",
    # "615 North Cascade Avenue, Apt 2, Colorado Springs, CO 80903",
    # "940 N Murray Blvd. Apt 13, Colorado Springs, CO 80915",
    # "6426 Wicklow Circle West, Colorado Springs, CO 80918",
    # "14750 Millhaven Place, Colorado Springs, CO 80908",
    # "3268 Divine Heights Apt. 203, Colorado Springs, CO 80922",
    # "6171 Anders Ridge Lane, Colorado Springs, CO 80927",
    # "6339 Monarch Circle, Colorado Springs, CO 80919",
    # "1235 Farragut Avenue, Colorado Springs, CO 80908",
    # "916 Summer Games Drive, Colorado Springs, CO 80905",
    # "61 S McCullock Blvd West, Pueblo West, CO 81007",
]

results = check_addresses_exist(addresses, api_key)
for address, status in results.items():
    print(f"{address}: {status}")
