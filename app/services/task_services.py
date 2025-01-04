class TaskServices:

    @classmethod
    def create_tasks(cls, payload):
        # insert the data into the database
        return {"payload": payload }
    
    @classmethod
    def get_all_tasks(cls):
        return {}
    
    @classmethod
    def update_task(cls, payload):
        # set value function
        return {"message": f"Task successfully updated for {payload['id']}"}, 200
    
    @classmethod
    def delete_task(cls, id):
        # use .find() to check if the id id present in db or not 
        if not id:
            return {"message": "Task already deleted"}, 200
        # if found delete it from the database
        return {"message": "Task deleted successfully"}, 200


         