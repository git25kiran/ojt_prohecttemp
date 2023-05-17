from django.shortcuts import render,HttpResponse

def home_view(request):

    return render(request,'temp_app\\homepage.html')




def task1_view(request):

    
    test_str = 'Om Sai Ram'
 
    #print("The original string is : " + str(test_str))
    
    temp = test_str.split()
    
    res = []
    for i in range(len(temp)):
        
        if i % 2 == 0:
            res.append(''.join(list(reversed(temp[i]))))
        else :
            res.append(temp[i])
            
    res = ' '.join(res)
    context ={
        'original_string' : test_str,
        'reverse_string' : res    

    }
    return render(request, 'temp_app\\task1.html',context)
    
def task2_view(request):
    num = 6378265
    reversed_num = 0

    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    context ={
        'original_number' : num,
        'reversed_number' : reversed_num    

    }
    return render(request, 'temp_app\\task2.html',context)



def task3_view(request):
    string = input("Enter any string:- ")
    string1 = string[ : : -1]

    if (string == string1):
        {string}

    else:
        {string}
    context ={
        'original_string' : string,
       
    }
    return render(request, 'temp_app\\task3.html',context)




        