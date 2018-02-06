import tensorflow as tf

a = tf.Variable([[1, 1], [2, 2]])
sess = tf.Session()
onehot_labels = tf.sparse_to_dense(a, [5, 5], 1.0, 0.0,)
sess.run(tf.initialize_all_variables())
print(sess.run(onehot_labels))