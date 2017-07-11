import create_emotion_data_pkl
create_emotion_data_pkl.create_pkl_file()
import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
import network
net = network.Network([18, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)