#Sort lis `list5` in ascending order based on the degrees value of its elements
.

list5 = [("Geoffrey Hinton", "Toronto", "Machine Learning"), ("Yoshua Bengio", "Montreal", "Deep Learning"), ("Andrew Ng", "Stanford", "Artificial Intelligence")]

list5.sort(key=lambda x: x[2])