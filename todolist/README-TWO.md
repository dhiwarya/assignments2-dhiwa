# Weekly PBP Assignment
Dhiwa Arya Kusumah 
2106657115

## Assignment 6 - Javascript and AJAX
### Deployment Link
https://dhiwa-assignment2.herokuapp.com/todolist/

## Describe the difference between asynchronous programming with synchronous programming.
#### Asyncrhonus
Asynchronous programming is a technique that allows your software to begin a work that could take a while to complete while still being able to respond to other events without having to wait until that task is complete. When that task is finished, the outcome is displayed in your software.

#### Synchronus
A single thread is assigned by synchronous applications to process a request or finish a task. A lengthy process like a database query will block all other threads because synchronous activities take place one at a time.

## 2. When Implementing Javascript and AJAX, there is an application in the paradigms of Event-Driven Programming. Describe the reasoning for those paradigms and state some examples of its application.
In an event-driven programming paradigm, entities (such as objects, services, and so on) communicate with one another by passing messages through a proxy. Normally, the messages are held in a queue before being processed by the consumers.
Event-driven programming is the dominant paradigm used in GUIs and other applications (eg, JavaScript web applications) that is centered on performing certain actions in response to user input. For example in the implementation of this task, namely the "Create Task" button.

## 3. Describe the implementation of asynchronous programming in AJAX.
1. Use <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script> inside of base.html or header html.
2. Add <script> inside html file to implement javascript.
3. Write AJAX syntax using JQuert in your script.
4. AJAX will listen to every request and response.
5. Each response or data will be processed asynchronously.
6. Allowing the page to show data without having it to resfresh.

## 4. Explain how you would implement the checklist above.
1. Create a new function into the views that allows it to return the data in json.
'''ruby
def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task), content_type="application/json")
'''
2. Add a new path for show_json
'''ruby
 path('json/', show_json, name='show_json'),
'''
3. Make a function to get the task to todolist.html
'''ruby
function showJson(){
        $.get("/todolist/json/", function(data){
            for(i = 0; i < data.length; i++){
                addText(data[i].fields.title, data[i].fields.description, data[i].fields.is_finished, data[i].fields.date, data[i].fields.pk)
            }
        })
    }
'''
4. Create a new create-task function for AJAX
'''ruby
def create_task_ajax(request):
     if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        date = datetime.datetime.now()
        is_finished = False
        item = Task(title=title, description=description, user=user, date=date, is_finished=is_finished)
        item.save()
        return JsonResponse({"Message": "Task Success"},status=200)
'''
5. Add new path for create_task_ajax
'''ruby
 path('create/', create_task_ajax, name = 'create_task_ajax'),
'''
6. Write a function in javascript that connects the modal to the create path and then allows it to be processed asynchronously
'''ruby
function makeCards(){
        let text= "";
        $.ajax({
            url: "{% url 'todolist:show_todolist_json' %}",
            type: "GET",
            dataType: "json",
            success: function(data){
                for(let task of data){
                    text += `<div class="m-2 card p-2">
                        <p class="text font-weight-bold">Task : ${task.fields.title}</p>
                        <p>Description : ${task.fields.description}</p>
                        <p>Created : ${task.fields.date}</p>
                        <p>Status : 
                            <span class=" ${task.fields.is_finished ? 'text-danger unfinished':'text-success finished'}">
                                ${task.fields.is_finished ? 'Completed':'Unfinished'}
                            </span>
                        </p>
                        <button class="btn" ><a><i class="fa fa-trash"></i></a></button>
                        <input class='todolist-check' 
                                        type="checkbox" 
                                        id='${task.pk}' 
                                        value= '${task.pk}'
                                        name="finishbtn"
                                        ${task.fields.is_finished ?  'checked':''} 
                                        />             
                    </div>`             

                }
                $('#card-container').html(text);

            } ,
            error: function(data){
                console.log('Error Detected');
            }
        })}

    function submitForm(){
            $.ajax({
                type: "POST",
                url: "{% url 'todolist:create_task_ajax' %}",
                data: {
                    title: $("#inputTitle").val(),
                    description: $("#inputDescription").val(),
                    csrfmiddlewaretoken: "{{ csrf_token }}",
                  },
                dataType: "json",
                success: function(){
                    $("#modalForm").modal('hide')
                    makeCards()
                },
                error: function(error){
                    alert("error")
                }
            })
            return false;
        
    }
'''

