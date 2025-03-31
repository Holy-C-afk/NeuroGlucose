from django.http import JsonResponse
from ai.prediction import predict_glucose_variation

def detect_variation(request):
    """
    Django view to handle blood sugar variation detection.
    """
    video_path = request.GET.get('video_path')  # Replace with actual video file handling logic
    if not video_path:
        return JsonResponse({'error': 'No video file provided'}, status=400)

    try:
        prediction = predict_glucose_variation(video_path)
        return JsonResponse({'status': 'success', 'prediction': prediction.tolist()})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)