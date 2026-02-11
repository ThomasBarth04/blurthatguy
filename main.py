import cv2
print("a")

cap = cv2.VideoCapture('data/debatten.mp4')
frames = []

count = 0
if not cap.isOpened():
    print("Error: Could not open video file.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
        count += 1
        if (count == 10):
            break

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

for frame in frames:
    print(frame)
