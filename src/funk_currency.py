import re
from collections import Counter
from typing import Any, Dict, List


def search_transactions(transaction_1: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """Фильтрация списка словарей для проверки строки поиска"""

    return [transaction for transaction in transaction_1 if
            "description" in transaction and re.search(search_string, transaction["description"])
            ]


def categorize_transactions(transaction_2: List[Dict[str, Any]], categories_2: Dict[str, List[str]]) -> Dict[str, int]:
    """Подсчет операций в каждой категории, используя ключи."""

    category_count: Dict[str, int] = Counter()
    for transaction in transaction_2:
        if "description" in transaction:
            for category, keywords in categories_2.items():
                """Наличие хотя бы одного ключа в описании транзакции"""
                if (keyword.lower() in transaction["description"].lower() for keyword in keywords):
                    category_count[category] += 1
                    break
    return dict(category_count)
