import tensorflow as tf
import numpy as np

flags = tf.flags
FLAGS = flags.FLAGS
flags.DEFINE_string("data","hello","test")
flags.DEFINE_string("data2","world","test")
a = tf.placeholder("float")
b = tf.placeholder("float")
y = tf.multiply(a,b)
sess = tf.Session()
print sess.run(y,feed_dict={a:4,b:5})
print FLAGS.data
print FLAGS.data2
print "hello !!"
