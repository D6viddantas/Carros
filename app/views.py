from django.shortcuts import render,redirect
from .models import Car
from .forms import CarModelForm
def cars_view(requests):
    search = requests.GET.get('search')
    cars = (Car.objects.filter(model__icontains=search) if search else Car.objects.all()).order_by('model')
    return render(request=requests,
                  template_name='pages/cars.html',
                  context={'cars':cars})
def newcar_view(requests):
    if requests.method == 'POST':
        new_car_form = CarModelForm(requests.POST,requests.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()

    return render(request=requests,
                  template_name='pages/newcar.html',
                  context={'new_car_form':new_car_form})