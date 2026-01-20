"""Logger module - Logging utilities"""

import logging
from typing import Optional
from pathlib import Path


class Logger:
    """Logger utility"""
    
    _loggers = {}
    
    @staticmethod
    def get_logger(name: str, log_file: Optional[str] = None) -> logging.Logger:
        """Get or create logger"""
        if name in Logger._loggers:
            return Logger._loggers[name]
        
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        if log_file:
            Path(log_file).parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            logger.addHandler(file_handler)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        
        logger.addHandler(console_handler)
        Logger._loggers[name] = logger
        
        return logger
    
    @staticmethod
    def disable_all() -> None:
        """Disable all loggers"""
        logging.disable(logging.CRITICAL)
    
    @staticmethod
    def enable_all() -> None:
        """Enable all loggers"""
        logging.disable(logging.NOTSET)
