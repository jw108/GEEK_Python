text = "She sells sea shells on the sea shore " \
       "The shells that she sells are sea shells I'm sure." \
       "So if she sells sea shells on the sea shore " \
       "I'm sure that the shells are sea shore shells"

print('Получено выражение: '"\t", text)

text = set(text.lower().split())
print(f'В представленном тексте содержится {len(text)} уникальных слов')