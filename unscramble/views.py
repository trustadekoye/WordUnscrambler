from django.shortcuts import render
from .forms import WordForm
from .utils import unscramble

# Create your views here.
def unscramble_view(request):
    form = WordForm(request.POST)
    unscrambled_words = []

    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            scrambled_word = form.cleaned_data['scrambled_word']
            unscrambled_word = unscramble(scrambled_word)

    context = {
        'form': form,
        'unscrambled_words': unscrambled_word,
    }
    return render(request, 'unscramble/index.html', context)