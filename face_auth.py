import cv2
import os

REFERENCE_IMAGE = "assets/user_face.jpg"


def authenticate_user():
    # Check if reference image exists
    if not os.path.exists(REFERENCE_IMAGE):
        print("Reference image not found!")
        return False

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Load reference image
    reference = cv2.imread(REFERENCE_IMAGE)
    reference_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)

    reference_faces = face_cascade.detectMultiScale(
        reference_gray,
        scaleFactor=1.2,
        minNeighbors=5
    )

    if len(reference_faces) == 0:
        print("No face found in reference image.")
        return False

    ref_x, ref_y, ref_w, ref_h = reference_faces[0]
    reference_face = reference_gray[
        ref_y:ref_y + ref_h,
        ref_x:ref_x + ref_w
    ]

    camera = cv2.VideoCapture(0)

    print("Look at the camera...")

    authenticated = False

    while True:
        ret, frame = camera.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5
        )

        for (x, y, w, h) in faces:

            live_face = gray[y:y + h, x:x + w]

            try:
                live_face = cv2.resize(
                    live_face,
                    (reference_face.shape[1], reference_face.shape[0])
                )

                difference = cv2.absdiff(reference_face, live_face)

                score = difference.mean()

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Score: {score:.2f}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 0, 0),
                    2
                )

                # Lower score = more similar
                if score < 45:
                    authenticated = True

            except Exception:
                pass

        cv2.imshow("Face Authentication", frame)

        key = cv2.waitKey(1)

        if authenticated:
            break

        if key == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

    return authenticated