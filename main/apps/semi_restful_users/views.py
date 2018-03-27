# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def users(req):
    context = {
        'users': User.objects.all()
    }
    return render(req, 'semi_restful_users/index.html', context)
#GET request - calls the index method to display all the users. This will need a template.

def new_user(req):
    return render(req, 'semi_restful_users/new.html')
#GET request - calls the new method to display a form allowing users to create a new user. This will need a template.

def show_user(req, user_id):
    context = {
        'user': User.objects.get(id = user_id)
    }
    return render(req, 'semi_restful_users/view.html', context)
#GET - calls the show method to display the info for a particular user with given id. This will need a template.

def edit_user(req, user_id):
    context = {
        'user': User.objects.get(id = user_id)
    }
    return render(req, 'semi_restful_users/edit.html', context)
#GET request - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template.

def create_user(req):
    errors = User.objects.basic_validator(req.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error, extra_tags=tag)
        return redirect('/users/new')
    User.objects.create(first_name=req.POST['first_name'], last_name=req.POST['last_name'], email=req.POST['email'])
    user_id = User.objects.last().id
    return redirect ('/users/{}'.format(user_id))
#POST - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.

def delete_user(req, user_id):
    User.objects.get(id = user_id).delete()
    return redirect('/users')
#GET - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.

def update_user(req, user_id):
    errors = User.objects.basic_validator(req.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error, extra_tags=tag)
        return redirect('/users/new')
    user = User.objects.get(id = user_id)
    user.first_name = req.POST['first_name']
    user.last_name = req.POST['last_name']
    user.email = req.POST['email']
    user.save()
    return redirect ('/users/{}'.format(user_id))
#POST - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.