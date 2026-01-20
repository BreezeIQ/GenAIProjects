"""Metrics module - Performance metrics collection"""

from typing import Any, Dict, List
from collections import defaultdict
import time


class Metrics:
    """Metrics collection and tracking"""
    
    def __init__(self):
        self._metrics = defaultdict(list)
        self.counters = defaultdict(int)
        self.timers = {}
        
    def record(self, metric_name: str, value: Any) -> None:
        """Record metric value"""
        self._metrics[metric_name].append({
            'value': value,
            'timestamp': time.time()
        })
    
    def increment_counter(self, counter_name: str, amount: int = 1) -> None:
        """Increment counter"""
        self.counters[counter_name] += amount
    
    def start_timer(self, timer_name: str) -> None:
        """Start timer"""
        self.timers[timer_name] = time.time()
    
    def stop_timer(self, timer_name: str) -> float:
        """Stop timer and return elapsed time"""
        if timer_name in self.timers:
            elapsed = time.time() - self.timers[timer_name]
            self.record(f"{timer_name}_duration", elapsed)
            del self.timers[timer_name]
            return elapsed
        return 0.0
    
    def get_metric_stats(self, metric_name: str) -> Dict[str, Any]:
        """Get statistics for metric"""
        if metric_name not in self._metrics or not self._metrics[metric_name]:
            return {}
        
        values = [m['value'] for m in self._metrics[metric_name]]
        
        return {
            'count': len(values),
            'min': min(values),
            'max': max(values),
            'avg': sum(values) / len(values),
            'latest': values[-1]
        }
    
    def get_all_metrics(self) -> Dict[str, Any]:
        """Get all metrics summary"""
        return {
            'metrics': {k: self.get_metric_stats(k) for k in self._metrics},
            'counters': dict(self.counters),
            'active_timers': list(self.timers.keys())
        }
