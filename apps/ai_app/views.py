from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
from django.conf import settings
import json

# Configure Gemini avec votre clé API
genai.configure(api_key=settings.GOOGLE_API_KEY)

# Initialise le modèle Gemini que vous souhaitez utiliser
# Vous pouvez choisir 'gemini-pro' pour du texte, ou 'gemini-1.5-flash' pour plus de vitesse.
# Consultez la documentation de Google AI pour les modèles disponibles.
model = genai.GenerativeModel('gemini-pro')

@csrf_exempt # Pour les requêtes POST sans jeton CSRF, à utiliser avec prudence en production
def gemini_chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message")

            if not user_message:
                return JsonResponse({"error": "Message is required."}, status=400)

            # Envoyer le message à Gemini et obtenir une réponse
            response = model.generate_content(user_message)

            return JsonResponse({"reply": response.text})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return render(request, "mon_app_ia/chat.html") # Ou un template pour un formulaire de base