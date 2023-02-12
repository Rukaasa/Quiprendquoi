
from django.views import generic
from django.shortcuts import render, redirect

from recipes.forms.catalog import StudentsForm


class Registerview(generic.FormView):
    template_name = 'contact.html'
    form_class = StudentsForm

    def add_form(request):
        if request.method == 'POST':
            form = StudentsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/myapp')
        else:
            form = StudentsForm()
            return render(request, 'index.html', {'form': form})
