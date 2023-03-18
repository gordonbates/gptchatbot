import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

chatbot = ChatBot('MyChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_input = json.loads(request.body)['message']
        response = chatbot.get_response(user_input)
        return JsonResponse({'response': str(response)})
    else:
        return render(request, 'index.html')
