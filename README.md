# Django project setup

In this assignment, we will learn how to set up a Django project layout using good practices and conventions.

We've already made some steps for you. As you can see, the Django project is already initialized. To do that, we used the Django `startproject` command.

From this point on, we will guide you step by step to fulfill the requirements for this assignment.

When you push your code changes and create the pull request, all tests in this project are going to be run to see if everything is correct. Make sure to each of the following points are implemented in order to have all tests passing.

## Requirements for this assignment:

### Project settings

Search for the `demo_project/settings/base.py` file. This will be the main repository of configurations for the whole project. As a very first step in this assignment, we will define a new custom setting. Name it `NEW_SETTING`, and set the value `"This is my first Django project"`.

### Creating a django application

As you can see so far, this is an empty Django project. We want to create a new Django application called `accounts`. You will probably need to take a look at the Django `startapp` command. Make sure the `accounts` application is created inside `wdd-django-project-setup/demo_project` directory.

Once the application is created, you will need to add it into the list of `INSTALLED_APPS` in `settings/base.py`. Just add the string `"accounts"` into that list.

### Writing your first View

Now that we have our new `accounts` application set up, we want to add a new View and URL rule so we are able to start making requests to our application.

Create a new `urls.py` file in the `demo_project/accounts` folder. You can take a look at the already created `demo_project/demo_project/urls.py` as a reference.

In the `accounts/views.py` file, add a new `hello_world` View. It's just supposed to return a `Response` object containing the string `"Hello World!"`.

Finally, set a new rule in `accounts/urls.py`, to match the `hello_world` View with the `/accounts/hello-world` URL.


## Running tests locally

If you want to run the tests while developing instead of waiting to push your changes and create the pull request, you can follow these steps.

```bash
$ cd wdd-django-project-setup/
$ export PYTHONPATH=demo_project/
$ export DJANGO_SETTINGS_MODULE=demo_project.settings.base
$ django-admin test demo_project
```
