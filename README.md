
# Svaeva Library Documentation

## Svaeva Class

# Svaeva: A Multichannel HyperStack for LLMOPS

Svaeva is a robust and versatile HyperStack designed for LLMOPS (Low Latency, Massive Online Processing Systems). It is capable of handling multiple channels of data simultaneously, making it an ideal solution for complex data processing tasks.

The system can process a wide variety of data types, including but not limited to heart bit rates, skin galvanization levels, neuronal activity, and eye tracking data. This makes Svaeva highly adaptable and suitable for a range of applications, particularly in the fields of health, neuroscience, and user experience research.

Svaeva's API client is organized into several classes, each corresponding to a specific resource in the API. This structure allows for efficient data management and easy access to the various resources.

The `Svaeva` class serves as the main interface for the Svaeva library. It manages the connection to the Svaeva API and provides access to various resources, including present models, platforms, groups, users, and actions.

### Class Attributes

- `conn`: A `requests.Session` object used for making HTTP requests.
- `token`: The API key used for authentication.
- `present`: An instance of the `PresentModels` class.
- `platform`: An instance of the `Platforms` class.
- `group`: An instance of the `Groups` class.
- `users`: An instance of the `Users` class.
- `actions`: An instance of the `Actions` class.
- `end`: The API endpoint.

### Methods

- `__init__(self, api_key: str, end_point="http://127.0.0.1:8000")`: The constructor method. It initializes the `Svaeva` object, sets the API key, establishes a session, and checks the API connection.
- `end_point(self, end)`: Sets the API endpoint.
- `set_headers(self)`: Updates the session headers with the API key.
- `check(self) -> None`: Checks the API connection. If successful, it initializes the `present`, `platform`, `group`, `users`, and `actions` attributes. If the connection fails, it raises an `InvalidToken` exception.

### Usage

```python
# Initialize the Svaeva object
svaeva = Svaeva("your_api_key")
```

## PresentModels Class

The `PresentModels` class manages present models within the Svaeva API. It provides methods to get all present models, retrieve a specific present model, set a present model, update a present model, and delete a present model.

### Class Attributes

- `conn`: A `requests.Session` object used for making HTTP requests.
- `url`: The API endpoint for present models.

### Methods

- `__init__(self, conn: Session, end_point: str)`: The constructor method. Initializes the `PresentModels` object with a session and an endpoint.
- `__call__(self, *args: Any, **kwds: Any) -> Any`: Returns all present models. If a dictionary is provided as an argument, it retrieves the present models that match the criteria.
- `__getattr__(self, name)`: Retrieves a specific present model by name. Raises an `InvalidPresentModelID` exception if the model doesn't exist.
- `__setattr__(self, name, value)`: Sets a present model. Raises an `ErrorSettingPresentModel` exception if the model cannot be set.
- `update(self, **kwargs)`: Updates a present model. Requires passing the present model ID and the new values as keyword arguments.
- `loaded(self)`: Returns a list of all loaded present models.
- `__delattr__(self, name)`: Deletes a present model.

### Usage

```python
# Initialize the PresentModels object
presentModels = PresentModels(conn, end_point)

# Get all present models
print(presentModels())

# Get a specific present model
print(presentModels.model1)

# Set a present model
presentModels.model1 = {"description": "test model", "value": 100}

# Update a present model
presentModels.update(id="model1", description="new test model")

# Delete a present model
del presentModels.model1
```

## Platforms Class

The `Platforms` class handles platforms in the Svaeva API. It provides methods to get all platforms, retrieve a specific platform, set a platform, update a platform, and delete a platform.

### Class Attributes

- `conn`: A `requests.Session` object used for making HTTP requests.
- `url`: The API endpoint for platforms.

### Methods

- `__init__(self, conn: Session, end_point: str)`: The constructor method. Initializes the `Platforms` object with a session and an endpoint.
- `__call__(self, *args: Any, **kwds: Any) -> Any`: Returns all platforms. If a dictionary is provided as an argument, it retrieves the platforms that match the criteria.
- `__getattr__(self, name)`: Retrieves a specific platform by name. Raises an `InvalidPlatformID` exception if the platform doesn't exist.
- `__setattr__(self, name, value)`: Sets a platform. Raises an `ErrorSettingPlatform` exception if the platform cannot be set.
- `update(self, **kwargs)`: Updates a platform. Requires passing the platform ID and the new values as keyword arguments.
- `loaded(self)`: Returns a list of all loaded platforms.
- `__delattr__(self, name)`: Deletes a platform.

### Usage

```python
# Initialize the Platforms object
platforms = Platforms(conn, end_point)

# Get all platforms
print(platforms())

# Get a specific platform
print(platforms.platform1)

# Set a platform
platforms.platform1 = {"description": "test platform", "value": 100}

# Update a platform
platforms.update(id="platform1", description="new test platform")

# Delete a platform
del platforms.platform1
```

## Groups Class

The `Groups` class manages groups in the Svaeva API. It provides methods to get all groups, retrieve a specific group, set a group, update a group, and delete a group.

### Class Attributes

- `conn`: A `requests.Session` object used for making HTTP requests.
- `url`: The API endpoint for groups.

### Methods

- `__init__(self, conn: Session, end_point: str)`: The constructor method. Initializes the `Groups` object with a session and an endpoint.
- `__call__(self, *args: Any, **kwds: Any) -> Any`: Returns all groups. If a dictionary is provided as an argument, it retrieves the groups that match the criteria.
- `__getattr__(self, name)`: Retrieves a specific group by name. Raises an `InvalidGroupID` exception if the group doesn't exist.
- `__setattr__(self, name, value)`: Sets a group. Raises an `ErrorSettingGroup` exception if the group cannot be set.
- `update(self, **kwargs)`: Updates a group. Requires passing the group ID and the new values as keyword arguments.
- `loaded(self)`: Returns a list of all loaded groups.
- `__delattr__(self, name)`: Deletes a group.

### Usage

```python
# Initialize the Groups object
groups = Groups(conn, end_point)

# Get all groups
print(groups())

# Get a specific group
print(groups.group1)

# Set a group
groups.group1 = {"description": "test group", "value": 100}

# Update a group
groups.update(id="group1", description="new test group")

# Delete a group
del groups.group1
```

## Users Class

The `Users` class handles users in the Svaeva API. It provides methods to get all users, retrieve a specific user, set a user, update a user, and

## Users Class

The `Users` class handles users in the Svaeva API. It provides methods to get all users, retrieve a specific user, set a user, update a user, and delete a user.

### Class Attributes

- `conn`: A `requests.Session` object used for making HTTP requests.
- `url`: The API endpoint for users.

### Methods

- `__init__(self, conn: Session, end_point: str)`: The constructor method. Initializes the `Users` object with a session and an endpoint.
- `__call__(self, *args: Any, **kwds: Any) -> Any`: Returns all users. If a dictionary is provided as an argument, it retrieves the users that match the criteria.
- `__getattr__(self, name)`: Retrieves a specific user by name. Raises an `InvalidUserID` exception if the user doesn't exist.
- `__setattr__(self, name, value)`: Sets a user. Raises an `ErrorSettingUser` exception if the user cannot be set.
- `update(self, **kwargs)`: Updates a user. Requires passing the user ID and the new values as keyword arguments.
- `loaded(self)`: Returns a list of all loaded users.
- `__delattr__(self, name)`: Deletes a user.

### Usage

```python
# Initialize the Users object
users = Users(conn, end_point)

# Get all users
print(users())

# Get a specific user
print(users.john)

# Set a user
users.john = {"group_id": "test", "platform": "whatsapp", "phone_number": "+351919771555"}

# Update a user
users.update(id="john", group_id="new_test")

# Delete a user
del users.john
```

## Actions Class

The `Actions` class manages actions in the Svaeva API. It provides methods to get all actions, retrieve a specific action, set an action, update an action, and delete an action.

### Class Attributes

- `conn`: A `requests.Session` object used for making HTTP requests.
- `url`: The API endpoint for actions.

### Methods

- `__init__(self, conn: Session, end_point: str)`: The constructor method. Initializes the `Actions` object with a session and an endpoint.
- `__call__(self, *args: Any, **kwds: Any) -> Any`: Returns all actions. If a dictionary is provided as an argument, it retrieves the actions that match the criteria.
- `__getattr__(self, name)`: Retrieves a specific action by name. Raises an `InvalidActionID` exception if the action doesn't exist.
- `__setattr__(self, name, value)`: Sets an action. Raises an `ErrorSettingAction` exception if the action cannot be set.
- `update(self, **kwargs)`: Updates an action. Requires passing the action ID and the new values as keyword arguments.
- `loaded(self)`: Returns a list of all loaded actions.
- `__delattr__(self, name)`: Deletes an action.

### Usage

```python
# Initialize the Actions object
actions = Actions(conn, end_point)

# Get all actions
print(actions())

# Get a specific action
print(actions.action1)

# Set an action
actions.action1 = {"description": "test action", "value": 100}

# Update an action
actions.update(id="action1", description="new test action")

# Delete an action
del actions.action1

## Conclusion

In conclusion, Svaeva is a powerful tool for managing and processing large amounts of multichannel data in real-time. Its versatility and adaptability make it suitable for a wide range of applications. Its well-structured API client ensures efficient data management and ease of use. Whether you're conducting health research, studying neuronal activity, or analyzing user behavior through eye tracking, Svaeva provides a reliable and efficient solution.
