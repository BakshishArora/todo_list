from app.services.task_services import TaskServices

class TaskController:

    @classmethod
    def create_task(cls, payload):
        # returns tasks for the day
        if not payload:
            return {"message": "Payload cannot be empty"}, 400
        else:
            return TaskServices.create_tasks(payload)
        
    @classmethod
    def tasks(cls):
        data = TaskServices.get_all_tasks()
        if not data:
            return {"message": "All caught up. No tasks present as of now"}, 200
        else:
            return data

    @classmethod
    def task_by_id(cls,id):
        # the function returns the top 10 tasks added by the ascending order by the date 
        return {"Task": "tasks are returned here"}


    @classmethod
    def update_task(cls, payload):
        if not payload:
            return {'message': "Payload cannot be empty"}, 404
        
        for key, value in list(payload.items()):
            if value == 'unknown':
                del payload[key]

        if not payload:
            return {'message': 'Everything is up to date'}, 200
        
        return TaskServices.update_task(payload)
         
    @classmethod
    def delete_task(cls, id):
        
        if TaskServices.delete_task(id):
            return {'message': "Task removed successfully"} , 200
        
        return TaskServices.delete_task(id)
        

        