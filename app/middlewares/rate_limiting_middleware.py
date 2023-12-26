from datetime import datetime, timedelta
from django.http import JsonResponse

class RateLimitingMiddleware:
    RATE_LIMIT_DURATION = timedelta(minutes=1)
    RATE_LIMIT_REQUESTS = 60

    def __init__(self, get_response):
        self.get_response = get_response
        self.request_counts = {}

    def __call__(self, request):
        user_ip = request.META['REMOTE_ADDR']

        # Unpacking request_count and last_request
        # At first, request_count is set to 0 and last_request is set to datetime.min
        request_count, last_request = self.request_counts.get(user_ip, (0, datetime.min))

        elapsed_time = datetime.now() - last_request

        if elapsed_time > self.RATE_LIMIT_DURATION:
            request_count = 1
        else:
            if request_count >= self.RATE_LIMIT_REQUESTS:
                return JsonResponse({'error': 'Too many requests'}, status=429)
            
            request_count += 1

        # After each request, request_counts is changed.
        self.request_counts[user_ip] = (request_count, datetime.now())

        response = self.get_response(request)

        return response
        