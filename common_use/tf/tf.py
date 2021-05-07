import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

print(tf.version)
v_1 = tf.constant([1, 2, 3, 4])
v_2 = tf.constant([2, 4, 6, 8])
v_add = tf.add(v_1, v_2)
with tf.compat.v1.Session() as tess:
    print(tess.run(v_add))

r = tf.rank(10)
print(r.dtype)

tensor_object = tf.convert_to_tensor([1, 2, 3, 4])
print(tensor_object)

sess_1 = tf.compat.v1.InteractiveSession()
print(tf.add(tf.constant([2, 3, 4, 5]), tf.constant([1, 4, 6, 9])))
