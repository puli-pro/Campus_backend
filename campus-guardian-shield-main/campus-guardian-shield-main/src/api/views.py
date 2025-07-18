from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils.face_recognition import recognize_face  # Import your face recognition logic
import json

@csrf_exempt
def face_recognition_view(request):
    if request.method == "POST":
        if "image" not in request.FILES:
            return JsonResponse({"error": "No image file provided"}, status=400)

        image_file = request.FILES["image"]

        # Call the face recognition function
        try:
            result = recognize_face(image_file)  # Adjust this based on your face_recognition.py logic
            return JsonResponse({"result": result})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)