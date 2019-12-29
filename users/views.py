from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
#from django.urls import reverse_lazy
from users.forms import *
from users.models import UploadImages, Profile
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#from django.views.generic.edit import CreateView, DeleteView, UpdateView
#from django.contrib.auth import get_user


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!, You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = AddImage(request.POST, request.FILES)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)  #instance is the current informations of the object before the changes
        u_form = UserUpdateForm(request.POST,
                                   instance=request.user)

        if form.is_valid():
            new_image = UploadImages(
                image_label=form.cleaned_data["description"],
                image=form.cleaned_data["image"],
                pub_date=timezone.now(),
                user=request.user
            )
            new_image.save()
            messages.success(request, f'New image added')

        if u_form.is_valid() and p_form.is_valid():
            # x = Profile.objects.get(user=request.user)
            # x.profile_image = p_form.cleaned_data['profile_image']
            # x.save()
            p_form.save()
            u_form.save()
            messages.success(request, f'Account updated succesfully')
            return redirect('profile')

    else:
        form = AddImage()
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)

    return render(request, 'profile.html', {'form': form, 'pform': p_form,
                                            'uform': u_form,
                                            'images': UploadImages.objects.filter(user=request.user)})


def delete(request, pk):
    if request.method == 'POST':
        old_img = UploadImages.objects.get(id=pk)
        old_img.delete()
        return redirect('profile')