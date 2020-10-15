import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

print(tf.version)
v_1 = tf.constant([1, 2, 3, 4])
v_2 = tf.constant([2, 4, 6, 8])
v_add = tf.add(v_1, v_2)
with tf.compat.v1.Session() as tess:
    print(tess.run(v_add))

