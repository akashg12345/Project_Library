import traceback

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import books
# def homepage(request):
#     query = request.GET.get("name")
#     return HttpResponse(f"heloo {query} how are u")

def homepage(request) :              # request variable is to collect HTTPRequest from browser 

    """Here request method could be POST OR GET"""
    
    ## Assigning values to variables by collecting from POST request METHOD 

    name = request.POST.get("bname")
    price = request.POST.get("bprice")
    quantity = request.POST.get("bqty")
    is_active = request.POST.get("is_active")

    if request.method == "POST":    ### if request method will be POST than only loop will execute
        if not request.POST.get("bid"):

            b_name = name
            b_price = price
            b_quantity = quantity
            b_is_active = is_active
            
            books.objects.create(name = b_name, price = b_price, quant = b_quantity,is_active = b_is_active)  
            return redirect("homepage")     # will return to homepage function and request method will be GET

        else:
            book_id = request.POST.get("bid")
            # Exception Handling if id provided is not valid one
            try:
                book_obj = books.objects.get(id=book_id)  ## Risky code should be in try block
            except books.DoesNotExist as msg:
                traceback.print_exc()   ## traceback.print_exec will print detailed error message
                return HttpResponse(f"Error:id does not exist \n{msg} ")
            else:  ## else will be execute only when there is no exceptions occurred for given code

                book_obj.name = name
                book_obj.price = price
                book_obj.quant = quantity
                book_obj.is_active = is_active
                book_obj.save()
            return redirect("show_all_table")

    elif request.method == "GET" :

        all_books = books.objects.all()  ## objects is default models Manager
        data = {"books": all_books}
        return render(request, "home3.html", context=data) ## context = mapping the collected data in dictionary

## Performing Various CURD(create,update,read,delete) operations 
 
## 1- For  Showing Fetched Data from Browser:- reading the data 

def show_all_table(request) :

    book = books.objects.all()
    data = {"books":book}
    return render(request,"show_all_table.html",context = data)

## 2- Updating  the existing  Data

def edit_data(request, bid) :

    try:
        book = books.objects.get(id=bid)
    except books.DoesNotExist as msg:
        return HttpResponse(f"Error : Id does not exist \nType{msg}")
    else:
        data = {"single_book" : book}  
        return render(request, template_name = "home3.html", context = data)
## 3 - Deleteing the data

def delete_data(request, id) :
    
    if request.method == "POST":
        try:
            book = books.objects.get(id=id)
        except books.DoesNotExist as msg:
            traceback.print_exc()  
            return HttpResponse(f"No entry  exist for ID:- {id}\n{msg}")
        else:
            book.delete()
        return redirect("show_all_table")
    else:
        return HttpResponse(f"Request method {request.method} is not valid..!")


def Soft_Delete(request,id) :

    data = books.objects.get(id = id)
    data.is_active = "N"    ## soft delete will not delete the object physically but will changed the status to "N"
    data.save()
    return redirect("show_all_table")


def Soft_Delete_All(request) : ## will set the is_active status to "N" for all books

    delete_data = books.objects.all()
    for data in delete_data:
        data.is_active = "N"
        data.save()
    return redirect("homepage")

def Show_All_Soft_Deleted(request) :
    print(request.method)

    soft_deleted = books.active.all() ## used customed model Manager to obtain desired set of data and override the default method
    data = {"books" : soft_deleted}

    ## return render : - Combines a given template with a given context dictionary and returns an HttpResponse object

    return render(request,template_name = "Restore_Deleted.html",context=data)

## RESTORE THE THE DATA ie : changing the status of books to active 

def Restore_Soft_Deleted(request,id):
    print(request.method)
    data = books.objects.get(id = id)
    data.is_active = "Y"
    data.save()
    BOOK = books.objects.filter(is_active = "N")
    return render(request,template_name = "Restore_Deleted.html",context={"books":BOOK})


def greet():
    print("hello")






