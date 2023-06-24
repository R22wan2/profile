from django.shortcuts import render,redirect
from django.http  import HttpResponse
# Create your views here.
def flames(request):
    if request.method=='POST':
        name1=request.POST['name1']
        name2=request.POST['name2']
        def flames(boy_name, girl_name):

            boy_name = boy_name.lower().replace(" ", "")
            girl_name = girl_name.lower().replace(" ", "")


            characters = list(set(boy_name + girl_name))

            length = len(characters)

            disition = ['F', 'L', 'A', 'M', 'E', 'S']

            while len(disition) > 1:
                count = length % len(disition)
                if count == 0:
                    count = len(disition)
                disition.pop(count - 1)

            return disition[0]
    

        result = flames(str(name1),str(name2))
        if result == 'F':
            return render(request,'FRIEND.html')
       
        elif result == 'L':
               return render(request,'love.html')
        elif result == 'A':
               return render(request,'affectionate.html')
        elif result == 'M':
               return render(request,'marage.html')
        elif result == 'E':
               return render(request,'enimy.html')
        elif result == 'S':
               return render(request,'siblings.html')
        else:pass
      
        

        return redirect('back')
    return render(request,'intro.html')