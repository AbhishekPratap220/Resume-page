def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name = 'shaktiman', power = 'lezar')
print_kwargs(name = 'shaktiman')
print_kwargs(name = 'shaktiman', power = 'lezar')

enemy = 'Dr. Jackaal'