fare_stages=[0,3,5,7,8]
dist={
    (0,1):10,
    (1,2):15,
    (2,3):5,
    (3,4):20,
    (4,5):15,
    (5,6):13,
    (6,7):15,
    (7,8):10,
}

def get_fare_stage(src,dest):
    for src_stage in reversed(fare_stages):
        if src >= src_stage:
            break
    for dest_stage in fare_stages:
        if dest <= dest_stage:
            break
    return src_stage,dest_stage
    
def calculate_distance(src, dest):
    distance=0
    next_stop = src + 1
    while(next_stop <= dest):
        distance += dist[(next_stop - 1, next_stop)]
        next_stop += 1
    return distance

def get_fare(dist,np):
    dist=dist-2
    charge=20+dist*5
    if np>=2:
        charge*=np
    return charge



numOfPassengers=int(input("Enter number of passengers: "))
source=int(input("Enter source: "))
destination=int(input("Enter destination: "))

src,dest=get_fare_stage(source,destination)
distance=calculate_distance(src,dest)
fare=get_fare(distance,numOfPassengers)

print(f"Fare for {numOfPassengers} persons : Rs{fare}")