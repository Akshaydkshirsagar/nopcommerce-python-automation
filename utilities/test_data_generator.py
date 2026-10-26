import uuid


# unique email _generate helper function
def generate_unique_email(base_email="user@example.com"):
    unique_id=uuid.uuid4().hex[:8]
    return base_email.replace('@',f"_{unique_id}@")

