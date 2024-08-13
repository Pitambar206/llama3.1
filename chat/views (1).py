from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from .llama_model import Llama3

bot = Llama3("meta-llama/Meta-Llama-3.1-8B-Instruct")

@csrf_exempt 
def chatbot_view(request):
    if request.method == "POST":
        user_input = request.POST.get("input", "")
        response = StreamingHttpResponse(
            bot._chatbot(user_input),
            content_type='text/plain',
        )
        
        return response
