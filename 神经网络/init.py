import sklearn.datasets
import sklearn.linear_model
import matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
from 神经网络.nn import plot_decision_boundary
from 神经网络.nn import NeuralNetwork

np.random.seed(1)

font = fm.FontProperties(fname='D:\\anaconda\\Lib\\site-packages\\matplotlib\\mpl-data\\fonts\\ttf\\STHeiti-Light.ttc')
matplotlib.rcParams['figure.figsize'] = (10.0, 8.0)


if __name__ == "__main__":

    plt.figure(figsize=(16, 40))

    xy, colors = sklearn.datasets.make_moons(60, noise=1.0)


    expect_outputed = []
    for c in colors:
        if c == 1:
            expect_outputed.append([0,1])
        else:
            expect_outputed.append([1,0])

    expect_outputed = np.array(expect_outputed).T

    # 设计3层网络，改变隐藏层神经元的个数，观察神经网络分类红蓝点的效果
    hidden_layer_neuron_num_list = [10]

    for i, hidden_layer_neuron_num in enumerate(hidden_layer_neuron_num_list):
        plt.subplot(5, 2, i + 1)
        plt.title(u'隐藏层神经元数量: %d' % hidden_layer_neuron_num, fontproperties = font)

        nn = NeuralNetwork([2, hidden_layer_neuron_num, 2], True)

        # 输出和输入层都是2个节点，所以输入和输出的数据集合都要是 nx2的矩阵
        nn.set_xy(xy.T, expect_outputed)
        nn.set_num_iterations(1500)
        nn.set_learning_rate(0.1)
        w, b = nn.training_modle()
        plot_decision_boundary(xy, colors, nn.predict_by_modle)

    plt.show()