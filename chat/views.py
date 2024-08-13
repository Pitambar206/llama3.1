from django.http import JsonResponse
from .llama_model import Llama3

bot = Llama3("meta-llama/Meta-Llama-3.1-8B-Instruct")

def chatbot_view(request):
    if request.method == "POST":
        user_input = request.POST.get("input", "")
        response_stream, _ = bot.get_response_stream(user_input)

        response_text = ""
        for token in response_stream:
            response_text += token
            print("Response from model:", response_text)

        return JsonResponse({"response": response_text})

    return JsonResponse({"error": "Invalid request method"}, status=400)
