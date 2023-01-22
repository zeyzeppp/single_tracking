import cv2
import numpy as np

trackingAlgorithms = ["BOOSTING", "MIL", "KCF", "CSRT", "TLD", "MEDIANFLOW", "MOSSE"]

i = 3
t_algorithm = trackingAlgorithms[i]

if t_algorithm == "BOOSTING":
    tracker = cv2.legacy.TrackerBoosting_create()
    print(tracker)

elif t_algorithm == "MIL":
    tracker = cv2.legacy.TrackerMIL_create()
    print(tracker)

elif t_algorithm == "KCF":
    tracker = cv2.legacy.TrackerKCF_create()
    print(tracker)

elif t_algorithm == "CSRT":
    tracker = cv2.legacy.TrackerCSRT_create()
    print(tracker)

elif t_algorithm == "TLD":
    tracker = cv2.legacy.TrackerTLD_create()
    print(tracker)

elif t_algorithm == "MEDIANFLOW":
    tracker = cv2.legacy.TrackerMedianFlow_create()
    print(tracker)

elif t_algorithm == "MOSSE":
    tracker = cv2.legacy.TrackerMOSSE_create()
    print(tracker)

else:
    print("[ERROR].. number out of the index !")


cap = cv2.VideoCapture("resources_görev/deneme_bt.mp4")

ret, frame = cap.read()
frame = cv2.resize(frame, (540, 960))
#frame = cv2.flip(frame, 1)


# checking
if ret == False:
    print("[ERROR].. something went wrong when loading !")

elif ret == None:
    print("[ERROR].. wrong path !")

else:
    pass

boxCoordinates = cv2.selectROI(frame)
print("BOX COORDINATES:", boxCoordinates)

ret = tracker.init(frame, boxCoordinates)
print("[INFO]... RETURN:", ret)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (540, 960))
    # frame = cv2.flip(frame, 1)

    if ret == False:
        print("[ERROR].. something went wrong when loading !")

    elif ret == None:
        print("[ERROR].. wrong path !")

    else:
        pass

    ret, boxCoordinates = tracker.update(frame)

    if ret == True:
        (x,y, w, h) = [int(k) for k in boxCoordinates]
        #loc = (x, y, w, h)
        x_c = ((2*x) + w)/2
        y_c = ((2*y) + h)/2
        center = (x_c, y_c)
        print("[INFO].. center is calculated", center)
        cv2.rectangle(frame, (x,y), ((x+w), (y+h)), (0, 0, 255), 2)
        cv2.putText(frame, str(tracker), (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 4)

    else:
        cv2.putText(frame, "No Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 4)

    cv2.imshow("SINGLE TRACKING", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()






