from deepface import DeepFace
import os
cwd=os.getcwd()
cwd=cwd.removesuffix('pragram.py')
# Path to the image containing known faces (reference image)
reference_image_path = rf"{cwd}\accenture\Dataset\Screenshot 2023-08-06 194422.png"

# Path to the image you want to recognize (target image)
target_image_path = rf"{cwd}\accenture\Dataset\IMG_20230608_160345.jpg"

# Perform face recognition
result = DeepFace.verify(reference_image_path, target_image_path)

# Print the result
if result["verified"]:
    print("The target image contains the same person as the reference image.")
    print("Facial distance:", result["distance"])
else:
    print("The target image does not contain the same person as the reference image.")
    print("Facial distance:", result["distance"])
recognition = DeepFace.find(img_path = reference_image_path, db_path = rf"{cwd}/accenture/dataset/mokith")