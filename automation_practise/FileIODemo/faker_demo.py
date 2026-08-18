from faker import Faker
# Localization: Specify a locale like Faker('it_IT') to generate Italian data. 
# Seeding: Use fake.seed_instance(12345) to ensure reproducible results. 
# Custom Providers: Create classes inheriting from BaseProvider to add specific data types. 
# Unique Values: Use .unique to ensure generated values (like emails) do not repeat. 
f=Faker('it_IT') 
print(f.name())
print(f.address())