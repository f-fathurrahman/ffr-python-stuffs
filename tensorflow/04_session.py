from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

a = tf.constant(3.1, dtype=tf.float32)
b = tf.constant(4.3) # tf.float32 by default
total = a + b
print(a)
print(b)
print(total)

writer = tf.summary.FileWriter(".")
writer.add_graph( tf.get_default_graph() )

sess = tf.Session()
print("total = ", sess.run(total))


