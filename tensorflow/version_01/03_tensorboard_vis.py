import tensorflow as tf

a = tf.constant(3.0, dtype=tf.float32)
b = tf.constant(4.0) # tf.float32 by default
total = a + b
print(a)
print(b)
print(total)

writer = tf.summary.SummaryWriter()
writer.add_graph( tf.get_default_graph() )
writer.close()

