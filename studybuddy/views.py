from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import AudioFileForm, NoteRenameForm, NoteEditForm, UserRegisterForm
from .models import AudioFile, Note

from .tasks import generate_notes_from_audio

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if request.method == "POST":
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = form.save(commit=False)
            audio_file.user = request.user
            audio_file.save()
            # Redirect to success page or stay on same page
            return redirect("index")

    else:
        form = AudioFileForm()

    # Retrieve audio files uploaded by current user
    user_audio_files = AudioFile.objects.filter(user=request.user)
    context = {
        "form": form,
        "audio_files": user_audio_files
    }

    return render(request, "studybuddy/user.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "studybuddy/login.html", {
                "message": "Invalid Credentials!"
            })

    return render(request, "studybuddy/login.html")


def logout_view(request):
    logout(request)
    return render(request, "studybuddy/login.html", {
        "message": "Logged out"
    })


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Account created for {username}! You can now log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'studybuddy/register.html', {
        "form": form
    })


def delete_audio(request, audio_id):
    if request.user.is_authenticated:
        audio_file = AudioFile.objects.filter(
            pk=audio_id, user=request.user).first()

        if audio_file:
            audio_file.delete()
    return HttpResponseRedirect(reverse("index"))


def delete_note(request, note_id):
    if request.user.is_authenticated:
        note = get_object_or_404(Note, pk=note_id, user=request.user)

        if request.method == "POST":
            note.delete()
            return HttpResponseRedirect(reverse("index"))


def rename_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == "POST":
        form = NoteRenameForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = NoteRenameForm(instance=note)
    return render(request, 'studybuddy/rename_note.html', {
        "form": form,
    })


def generate_notes(request, audio_id):
    audio_file = get_object_or_404(AudioFile, pk=audio_id, user=request.user)
    messages.success(
        request, f"Notes are being generated! This will take a few minutes.")
    # Triggers celery task
    generate_notes_from_audio.delay(audio_file.id)
    return redirect('index')


def view_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    return render(request, 'studybuddy/view_note.html', {'note': note})


def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    if request.method == "POST":
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return render(request, 'studybuddy/view_note.html', {'note': note})
    else:
        form = NoteEditForm(instance=note)
    return render(request, "studybuddy/edit_note.html", {
        "form": form,
    })
