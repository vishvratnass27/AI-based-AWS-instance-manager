import cv2
from cvzone.HandTrackingModule import HandDetector
import boto3
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
ec2 = boto3.resource("ec2")

allOs = []

def myOSLaunch():
  instances = ec2.create_instances(
          ImageId="ami-0a2acf24c0d86e927",
          MinCount=1,
          MaxCount=1,
          InstanceType="t2.micro",
          SecurityGroupIds=["sg-0950cdf4fbeccaf56"]
      )
  myId = instances[0].id
  allOs.append(myId)
  print("Total Number of OS:", len(allOs))
  print(myId)

def osTerminate():
  osDelete = allOs.pop()
  ec2.instances.filter(InstanceIds=[osDelete]).terminate()
  print(osDelete)
  print("Total number of instances:", len(allOs))

def endAllInstances():
    print("Terminating All instances as the program is closed!!!")
    while True:
        if allOs == []:
            break
        osDelete = allOs.pop()
        print(osDelete)
        ec2.instances.filter(InstanceIds=[osDelete]).terminate()


detector = HandDetector(maxHands=1)
while True:
  status, photo = cap.read()
  hand = detector.findHands(photo, draw=False)
  cv2.imshow("photo", photo)
#   print(cv2.waitKey(100))
  if cv2.waitKey(1000) == 13:
    break
  if hand:
    lmlist = hand[0]
    noOfFingers = detector.fingersUp(lmlist)
    if noOfFingers == [0,1,0,0,0]:
      print("Index Finger")
      myOSLaunch()
    if noOfFingers == [1,0,0,0,0] and allOs != []:
      print("Thumb")
      osTerminate()
endAllInstances()
cv2.destroyAllWindows()
cap.release()
