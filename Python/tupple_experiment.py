def add_policy(v1, v2, v3, v4, v5, v6):
    print(v1, v2, v3, v6)


policies = (
    ("superman", "persons", "*", "*", "read", "allow"),
    ("superman", "persons", "*", "*", "write", "allow"),
    ("superman", "persons", "*", "*", "update", "allow")
)
for policy in policies:
    add_policy(*policy)
