# Flask Auth Demo

This is a quick demonstration of how to implement authentication and authorization using the Flask framework.

*Requirements*
- Flask
- Flask SQLalchemy
- Werkzeug utils


## Authentication

Authentication means checking that a user is who they say they are. In practice, we use this to log a user in by:

- Checking their credentials (username, password)
- Check the user is valid


## Authorization

Authorization means giving the user permission to visit areas of your site. In practice, once a user is logged in we want to show them different areas of the site. This means:

- Updating the login status (show a logout option)
- Allowing the user to view their profile.


## About Werkzeug

Werkzeug is a crucial part of the Flask framework and it provides lots of extremely useful utilities for building web applications. One of those utilities is password hashing and checking.

It comes installed with Flask so there's no need to install separately. Here's how to use the utils.

```python
from werkzeug.security import generate_password_hash, check_password_hash

def create_password(self, password):
    """Takes a string and hashes a password."""
    self.password = generate_password_hash(password)

def is_valid_password(self, password):
    """Checks a password hash against a string."""
    return check_password_hash(self.password, password)
```
