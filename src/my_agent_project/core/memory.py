"""Memory module - Agent memory management"""

from typing import Any, Dict, List, Optional
from collections import deque


class Memory:
    """Agent memory management system"""
    
    def __init__(self, capacity: int = 1000, memory_type: str = 'fifo'):
        self.capacity = capacity
        self.memory_type = memory_type
        self.storage = deque(maxlen=capacity)
        self.metadata = {}
        
    def store(self, data: Any, metadata: Optional[Dict] = None) -> None:
        """Store data in memory"""
        entry = {
            'data': data,
            'metadata': metadata or {},
            'timestamp': len(self.storage)
        }
        self.storage.append(entry)
        
    def retrieve(self, index: int = -1) -> Any:
        """Retrieve data from memory"""
        if self.storage:
            return self.storage[index]['data']
        return None
    
    def retrieve_by_type(self, data_type: str) -> List[Any]:
        """Retrieve all data of specific type"""
        results = []
        for entry in self.storage:
            if entry['metadata'].get('type') == data_type:
                results.append(entry['data'])
        return results
    
    def clear(self) -> None:
        """Clear all memory"""
        self.storage.clear()
        
    def get_capacity_usage(self) -> float:
        """Get memory usage percentage"""
        return (len(self.storage) / self.capacity) * 100
    
    def get_size(self) -> int:
        """Get current memory size"""
        return len(self.storage)
