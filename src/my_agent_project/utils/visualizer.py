"""Visualizer module - Data visualization utilities"""

from typing import Dict, List, Any, Optional
import json


class Visualizer:
    """Data visualization utility"""
    
    @staticmethod
    def format_agent_state(agent_state: Dict[str, Any]) -> str:
        """Format agent state for visualization"""
        return json.dumps(agent_state, indent=2)
    
    @staticmethod
    def create_metrics_report(metrics: Dict[str, Any]) -> str:
        """Create formatted metrics report"""
        report = []
        report.append("=" * 50)
        report.append("METRICS REPORT")
        report.append("=" * 50)
        
        for metric_name, stats in metrics.items():
            report.append(f"\n{metric_name}:")
            for key, value in stats.items():
                report.append(f"  {key}: {value}")
        
        return "\n".join(report)
    
    @staticmethod
    def create_comparison_table(data: List[Dict[str, Any]]) -> str:
        """Create comparison table"""
        if not data:
            return "No data to display"
        
        keys = list(data[0].keys())
        table = []
        
        table.append(" | ".join(keys))
        table.append("-" * (10 * len(keys)))
        
        for row in data:
            values = [str(row.get(k, 'N/A')) for k in keys]
            table.append(" | ".join(values))
        
        return "\n".join(table)
