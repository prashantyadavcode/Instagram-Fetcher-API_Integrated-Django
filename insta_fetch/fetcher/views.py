from django.http import JsonResponse
from .services import fetch_instagram_post

def latest_post(request):

    data = fetch_instagram_post()

    if data:
        return JsonResponse({"success": True, "data": data})
    return JsonResponse({"success": False, "error": "Could not fetch post"})