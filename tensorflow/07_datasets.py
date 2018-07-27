from __future__ import print_function

import tensorflow as tf

my_data = [
    [0, 1,],
    [2, 3,],
    [4, 5,],
    [6, 7,],
]

slices = tf.data.Dataset.from_tensor_slices(my_data)
next_item = slices.make_one_shot_iterator().get_next()

print(slices)

sess = tf.Session()

while True:
    try:
        print(sess.run(next_item))
    except tf.errors.OutOfRangeError:
        break




