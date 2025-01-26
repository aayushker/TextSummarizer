from django.shortcuts import render
from rest_framework.views import APIView, Response
from .process import preProcessing, sentenceScoring, extractTopSentences

# Create your views here.

class SummarizerView(APIView):
    def post(self, request):
        data = request.data
        text = data['text']
        sentences, words = preProcessing.preProcess_text(text)
        sentenceScores = sentenceScoring.score_sentences(sentences, words)
        topSentences = extractTopSentences.summarize_text(sentenceScores)
        return Response(topSentences)