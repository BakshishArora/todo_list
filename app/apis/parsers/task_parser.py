from flask_restx import reqparse
from app.models.enum import Category
from app.models.enum import Status 
from app.models.enum import Priorities

class TaskParser:

    @classmethod
    def payload_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='enter unique id')
        parser.add_argument('task', type=str, required=True, help='mention the task here')
        parser.add_argument('category', type=str, required= True, choices=[ct.value for ct in Category], 
                            help="mention category of work: {}".format(", ".join([ct.value for ct in Category])))
        parser.add_argument('priority', type=str, required=True, choices=[p.value for p in Priorities],
                            help="Choose Priority Level: {}".format(", ".join([p.value for p in Priorities])))
        parser.add_argument('status', type=str, required=True, choices=[t.value for t in Status], 
                            help="Choose Task Status: {}".format(", ".join([t.value for t in Status ]))) 
        
        return parser

    @classmethod
    def update_task_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='enter unique id')
        parser.add_argument('task name', type=str, help='mention new task name here', default= "unknown")
        parser.add_argument('category', type=str, choices=[ct.value for ct in Category], 
                            help="mention new category of work: {}".format(", ".join([ct.value for ct in Category])))
        parser.add_argument('priority', type=str, choices=[p.value for p in Priorities], default="unknown",
                            help="Choose Priority Level: {}".format(", ".join([p.value for p in Priorities])))
        parser.add_argument('status', type=str, choices=[t.value for t in Status],
                            help="Choose Task Status: {}".format(", ".join([t.value for t in Status ]))) 
        
        return parser
    

