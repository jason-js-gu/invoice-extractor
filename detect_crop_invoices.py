import os

import cv2


def detect_and_crop_invoices(image_path, output_dir="invoices"):
    os.makedirs(output_dir, exist_ok=True)

    # Load and preprocess image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 200)

    # Find contours
    contours, _ = cv2.findContours(
        edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    invoice_count = 0
    for contour in contours:
        # Approximate the contour to a polygon
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        # Filter by rectangular shape and reasonable size
        if len(approx) == 4 and cv2.contourArea(contour) > 10000:
            x, y, w, h = cv2.boundingRect(approx)
            cropped_invoice = image[y : y + h, x : x + w]
            output_path = os.path.join(output_dir, f"invoice_{invoice_count}.jpg")
            cv2.imwrite(output_path, cropped_invoice)
            invoice_count += 1

    print(f"{invoice_count} invoices detected and saved to {output_dir}/")


# Example usage:
detect_and_crop_invoices("your_photo.jpg")
