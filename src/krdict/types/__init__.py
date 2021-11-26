"""
Contains types defined by the krdict module.
"""

from .meaning_category import MeaningCategoryProxy as MeaningCategory
from .subject_category import SubjectCategoryProxy as SubjectCategory
from .exceptions import KRDictException

__all__ = [
    'KRDictException',
    'MeaningCategory',
    'SubjectCategory'
]
