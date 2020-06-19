# Quickstart
*[< Index](index.md)*

To get started, you need to ensure you installed gbapi from pip. If you haven't
done so yet, do it with:
```
pip install gbapi
```
Then you need to import the package into your code:
```py
import gbapi
```
The module exposes a `Client` class, which you need to construct:
```py
gb = Client()
```
It requires no arguments, and is going to be your portal to the wonderful world
of GameBanana. All you need to do now, is (in an asynchronous function) call the
corresponding getter coroutines. For example:
```py
await gb.get_map(123)
```
will fetch the map with the ID `123` and return a `Map` object for you to get
your information from. All submission types have their own classes. All of these
classes inherit from a special base class called `BaseSubmission`. This class
implements some basic properties, that every submission has. Examples of these
properties are: `.game`, `.author`, `.name`, `.id`, `.views`, `.likes`. Some of
them can have their own special properties. For example, `WiP` objects have a
`.finished_work` property and `Request` objects have a `.deadline` property.

Technically this is everything you'd need to know to start using the wrapper.
If you want to go deeper, view the [API Reference](reference.md).