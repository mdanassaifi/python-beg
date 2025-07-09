def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, city="New York")
print_kwargs(first_name="John", last_name="Doe", occupation="Engineer")
print_kwargs(country="USA", state="California", zip_code="90001")