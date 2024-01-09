# pylint: disable=no-member
# pylint: disable=unsubscriptable-object
import base64
import cv2
from flask import current_app as app
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import numpy as np

def process_image(request_data):
    
    # ANSWER_KEY = request_data.get("ANSWER_KEY", {})  
    ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 2, 4: 1} 
    # Decode Base64 image data
    image_data = request_data.get("image", "")
    # image_data = image_data.split(",")[1]  # Get the actual Base64-encoded data
    image_bytes = base64.b64decode(image_data)
    image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    
    # Read the image using OpenCV
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 75, 200)

    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    docCnt = None

    if len(cnts) > 0:
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:
                docCnt = approx
                break

    paper = four_point_transform(image, docCnt.reshape(4, 2))
    warped = four_point_transform(gray, docCnt.reshape(4, 2))
    thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    questionCnts = []

    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)
        if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
            questionCnts.append(c)

    # Check if questionCnts is not empty before sorting
    if questionCnts:
        questionCnts = contours.sort_contours(questionCnts, method="top-to-bottom")[0]
        correct = 0

        for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
            cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
            bubbled = None

            for (j, c) in enumerate(cnts):
                mask = np.zeros(thresh.shape, dtype="uint8")
                cv2.drawContours(mask, [c], -1, 255, -1)
                mask = cv2.bitwise_and(thresh, thresh, mask=mask)
                total = cv2.countNonZero(mask)

                if bubbled is None or total > bubbled[0]:
                    bubbled = (total, j)

            color = (255, 0, 0)
            k = ANSWER_KEY[q]

            if k == bubbled[1]:
                color = (0, 255, 0)
                correct += 1

            cv2.drawContours(paper, [cnts[k]], -1, color, 3)

        score = (correct / 5.0) * 100
        porcentaje = max(0.0, min(100.0, score))
        nota = round((porcentaje / 100) * 7.0, 1)        

        cv2.putText(paper, "{:.1f}".format(nota), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        # resultado_escritura = cv2.imwrite(os.path.join("./reviewed/", f"{name}.jpg"), paper)
        _, paper_encoded = cv2.imencode('.png', paper)
        paper_base64 = base64.b64encode(paper_encoded.tobytes()).decode('utf-8')
        paper_base64_with_prefix = f'data:image/png;base64,{paper_base64}'
        return {'image': paper_base64_with_prefix, 'nota': nota}
    else:
        # Handle the case when questionCnts is empty
        return {'error': 'No contours found in the image'}