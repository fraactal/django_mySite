from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de Tarea", max_length=100, widget=forms.TextInput(attrs={'class':'input'}))
    #descripcion = forms.Textarea(label="Descripcion de Tarea", required=False)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class':'input'}), label="Descripcion de Tarea", required=False)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Titulo del Proyecto", widget=forms.TextInput(attrs={'class':'input'}), max_length=100)
