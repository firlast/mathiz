# 0.1.0

Creating `Mathiz` class and adding essential methods.

## Major commits

- [711deb7](https://github.com/firlast/mathiz/commit/711deb7): Adding `Server` class;
- [8cdbf2f](https://github.com/firlast/mathiz/commit/8cdbf2f): Adding method to register routes;
- [25976f5](https://github.com/firlast/mathiz/commit/25976f5): Adding method to run server;
- [ca6050a](https://github.com/firlast/mathiz/commit/ca6050a): Adding method to process request with threads;
- [9a4936a](https://github.com/firlast/mathiz/commit/9a4936a): Logging request in `_process` method;
- [e18a8aa](https://github.com/firlast/mathiz/commit/e18a8aa): Print run server message;

# 0.2.0

Update [WSBLib](https://github.com/firlast/wsblib) version and using globals variable to provide request object.

## Major commits

- [cfdfabe](https://github.com/firlast/mathiz/commit/cfdfabe): Updating project requirements;
- [13962c4](https://github.com/firlast/mathiz/commit/13962c4): Handling `KeyboardException` and closing socket;
- [93631da](https://github.com/firlast/mathiz/commit/93631da): Using globals to provide request object;
- [3a51ac3](https://github.com/firlast/mathiz/commit/3a51ac3): Creating `RequestData` instance in `__init__.py`;
- [fd0bf8e](https://github.com/firlast/mathiz/commit/fd0bf8e): Handling `OSError` exception if the address is already in use;

# 0.2.1

Fix [WSBLib](https://github.com/firlast/wsblib) version in setup script.

## Major commits

- [3b8d65f](https://github.com/firlast/mathiz/commit/3b8d65f): Fix `wsblib` version in setup script.

# 0.2.2

Update [WSBLib](https://github.com/firlast/wsblib) version.

## Major commits

- [4fba261](https://github.com/firlast/mathiz/commit/4fba261): Update `wsblib` version in setup script;
- [6bfb7b9](https://github.com/firlast/mathiz/commit/6bfb7b9): Update project requirements.

# 0.3.0

Adding `Mathiz.register_route` method, encrypt cookies data and update [WSBLib](https://github.com/firlast/wsblib) version.

## Major commits

- [73294bd](https://github.com/firlast/mathiz/commit/73294bd): Update project requirements;
- [ba30772](https://github.com/firlast/mathiz/commit/ba30772): Adding `EncryptCookies` class;
- [905d079](https://github.com/firlast/mathiz/commit/905d079): Create function to encrypt cookies;
- [4bb03c2](https://github.com/firlast/mathiz/commit/4bb03c2): Create function to decrypt cookies;
- [23481b3](https://github.com/firlast/mathiz/commit/23481b3): Encrypt cookies in `Mathiz._process` method;
- [09ddd51](https://github.com/firlast/mathiz/commit/09ddd51): Updating requirements.txt;
- [27a613f](https://github.com/firlast/mathiz/commit/27a613f): Removing empty dict from `RequestData` instance;
- [377f4a3](https://github.com/firlast/mathiz/commit/377f4a3): Update wsblib version in setup script;
- [0263f8c](https://github.com/firlast/mathiz/commit/0263f8c): Encrypt just cookie value;
- [b7aa6b6](https://github.com/firlast/mathiz/commit/b7aa6b6): Decrypt received cookies;
- [24555b6](https://github.com/firlast/mathiz/commit/24555b6): Creating `register_route` method to register routes.