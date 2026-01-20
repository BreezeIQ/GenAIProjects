"""Validator module - Input validation"""

from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod


class Validator(ABC):
    """Abstract validator"""
    
    @abstractmethod
    def validate(self, value: Any) -> bool:
        """Validate value"""
        pass


class TypeValidator(Validator):
    """Type validator"""
    
    def __init__(self, expected_type):
        self.expected_type = expected_type
    
    def validate(self, value: Any) -> bool:
        """Validate type"""
        return isinstance(value, self.expected_type)


class RangeValidator(Validator):
    """Range validator"""
    
    def __init__(self, min_val: Optional[float] = None, max_val: Optional[float] = None):
        self.min_val = min_val
        self.max_val = max_val
    
    def validate(self, value: Any) -> bool:
        """Validate range"""
        try:
            val = float(value)
            if self.min_val is not None and val < self.min_val:
                return False
            if self.max_val is not None and val > self.max_val:
                return False
            return True
        except (TypeError, ValueError):
            return False


class CompositeValidator:
    """Composite validator - combines multiple validators"""
    
    def __init__(self, validators: List[Validator]):
        self.validators = validators
    
    def validate(self, value: Any) -> bool:
        """Validate using all validators"""
        return all(validator.validate(value) for validator in self.validators)
    
    def validate_dict(self, data: Dict[str, Any], validation_rules: Dict[str, Validator]) -> bool:
        """Validate dictionary against rules"""
        for key, validator in validation_rules.items():
            if key not in data:
                return False
            if not validator.validate(data[key]):
                return False
        return True
