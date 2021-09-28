# Removing Black Pixels from Matrix

This is a Google challenge based exercise with a simple objective of removing all the black pixels (represented by the number 1) of a matrix, which are connected to the border.

This connection can be directly or indirectly, like horizontally or vertically as seen in the exemple below.

<br />

```python
stateMatrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]

result = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1],
]
```

<br />

### FYI

This project is not finished yet. As it is still in development, you can be free for clonning this repo and trying it by yourself.

You can find in code.py the functions made and how is it going.

It is not needed to install anything. And if you just want to check the results, just clone it into your device, then:

1. Open the terminal on the folder path.
2. Run the command below:

```shell
python code.py
```

It will automatically run the result.

<br />
<br />

> Follow me: [Instagram](https://instagram.com/eugaoliver), [LinkedIn](https://linkedin.com/in/gabrielocramos), [Twitter](https://twitter.com/eugaoliver)
