"""Executor module - Action execution and management"""

from typing import Any, Dict, List, Callable, Optional
from enum import Enum


class ExecutionStatus(Enum):
    """Execution status enumeration"""
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Task:
    """Task representation"""
    
    def __init__(self, task_id: str, action: Callable, args: tuple = (), kwargs: Dict = None):
        self.task_id = task_id
        self.action = action
        self.args = args
        self.kwargs = kwargs or {}
        self.status = ExecutionStatus.PENDING
        self.result = None
        self.error = None
        
    def execute(self) -> Any:
        """Execute task"""
        try:
            self.status = ExecutionStatus.RUNNING
            self.result = self.action(*self.args, **self.kwargs)
            self.status = ExecutionStatus.SUCCESS
            return self.result
        except Exception as e:
            self.status = ExecutionStatus.FAILED
            self.error = str(e)
            raise


class Executor:
    """Action executor"""
    
    def __init__(self, max_concurrent_tasks: int = 5):
        self.max_concurrent_tasks = max_concurrent_tasks
        self.task_queue = []
        self.execution_history = []
        self.active_tasks = {}
        
    def submit_task(self, task_id: str, action: Callable, args: tuple = (), kwargs: Dict = None) -> Task:
        """Submit task for execution"""
        task = Task(task_id, action, args, kwargs)
        self.task_queue.append(task)
        return task
    
    def execute_tasks(self) -> List[Task]:
        """Execute queued tasks"""
        executed = []
        
        while self.task_queue and len(self.active_tasks) < self.max_concurrent_tasks:
            task = self.task_queue.pop(0)
            self.active_tasks[task.task_id] = task
            
            try:
                task.execute()
                executed.append(task)
            finally:
                del self.active_tasks[task.task_id]
                self.execution_history.append(task)
        
        return executed
    
    def get_execution_status(self) -> Dict[str, Any]:
        """Get execution status"""
        return {
            'queued_tasks': len(self.task_queue),
            'active_tasks': len(self.active_tasks),
            'completed_tasks': len(self.execution_history),
            'max_concurrent': self.max_concurrent_tasks
        }
    
    def get_task_result(self, task_id: str) -> Optional[Any]:
        """Get result of completed task"""
        for task in self.execution_history:
            if task.task_id == task_id:
                return task.result
        return None
