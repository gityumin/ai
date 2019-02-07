import tensorflow as tf
import numpy as np
flags = tf.flags
FLAGS = flags.FLAGS
flags.DEFINE_string("data","hello","test")
a = tf.placeholder("float")
b = tf.placeholder("float")
y = tf.multiply(a,b)
sess = tf.Session()
print sess.run(y,feed_dict={a:4,b:5})
<<<<<<< HEAD
print FLAGS.data
=======
print "hello !!"
>>>>>>> c285babdeb662d4034a01ff5f5463d7f61876bfb
