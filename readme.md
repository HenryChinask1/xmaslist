**SECRET SANTA PICKER**

Get my group's secret santas picked with the click of a button!

Create an emails.py file like the following example and add as many santas as needed.

Example `emails.py`

```python
sender_email: dict[str, str] = {'email': 'example@gmail.com', 'password': 'pass word phrase'}

secret_keeper: list[str] = ['abbey': 'abbey@email.com']

santas: dict[str, tuple[str, list[str]]] = {'beth': ('beth@email.com', ['jeff', 'beth']),
                                            'jeff': ('jeff@email.com', ['jeff', 'beth']),
                                            'joel': ('joel@email.com', ['joel', 'chelsea']),
                                            'chelsea': ('chelsea@email.com', ['joel', 'chelsea'])}
```

Install dependencies:
`uv sync`

Usage:
`uv run .\xmaslist\main.py`