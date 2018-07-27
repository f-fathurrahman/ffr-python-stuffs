from __future__ import print_function

import numpy as np
import tensorflow as tf

sess = tf.Session()

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
z = x + y

print( "z = ", sess.run(z, feed_dict={x: 3, y:4.3}) )

print( "z = ", sess.run(z, feed_dict={x: [3,1.2], y:[4.3, 3.1]}) )

