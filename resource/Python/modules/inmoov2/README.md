# InMoov2 Python Library

The InMoov2 Python library provides a simple way to start and and control an InMoov2 service.

## Installation
Already installed when InMoov2 service is installed

## Usage

To use the InMoov2 Python library, you'll first need to connect to a InMoov2 service. You can do this using the `connect` function:

```python
import myrobotlab
import inmoov2

myrobotlab.connect()

# default will be an InMoov2 robot named i01
robot = inmoov2.start()

# creating a differently named robot may not work well ... yet
robot = inmoov2.start('i02')
```

## Contributing
Contributions to the InMoov2 Python library are always welcome. To contribute, simply fork the repository, make your changes, and submit a pull request.

## License
The InMoov2 Python library is licensed under the MIT License.

## Dependencies
MyRobotLab Python Library (>= 0.9)
