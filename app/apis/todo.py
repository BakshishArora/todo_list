from flask import Flask, request
import requests
from flask_restx import Resource, Api, Namespace
from app.controller.task_controller import TaskController
from app.apis.parsers.task_parser import TaskParser

api = Namespace(name='tasks', description='The Task Handler')

@api.route('/newtask', methods=['POST'])
class CreateTask(Resource):
    @api.expect(TaskParser.payload_parser())
    def post(self):
        payload = dict()
        parser = TaskParser.payload_parser().parse_args()
        payload['id']= parser['id']
        payload['category'] = parser['category']
        payload['priority'] = parser['priority']
        payload['task'] = parser['task']
        payload['status'] = parser['status']
        return TaskController.create_task(payload)


@api.route('/gettask', methods=['GET'])
class Tasks(Resource):
    def get(self):
        return TaskController.tasks()
    

@api.route('/<int:id>', methods=['GET', 'DELETE'])
class TaskID(Resource):
    def get(self, id):
        return TaskController.task_by_id(id)
    
    def delete(self , id):
        return TaskController.delete_task(id)
    
@api.route('/update', methods=['PUT'])
class UpdateTask(Resource):
    @api.expect(TaskParser.update_task_parser())
    def put(self):
        payload = dict()
        parser = TaskParser.update_task_parser().parse_args()
        if not parser['id']:
            return {"Error": "Task ID is mandatory"}, 404
        payload['id']=parser['id']
        payload['category']=parser['category']
        payload['priority']=parser['priority']
        payload['status']= parser['status']
        return TaskController.update_task(payload)
    
