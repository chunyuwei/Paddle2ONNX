# Copyright (c) 2021  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import paddle
from onnxbase import APIOnnx
from onnxbase import randtool


class Net(paddle.nn.Layer):
    """
    simple Net
    """

    def __init__(self, p=2):
        super(Net, self).__init__()
        self.p = p

    def forward(self, inputs, _inputs):
        """
        forward
        """
        x = paddle.dist(inputs, _inputs, p=self.p)
        x = x + 1
        return x


def test_dist_9():
    """
    api: paddle.dist
    op version: 9
    """
    op = Net()
    op.eval()
    # net, name, ver_list, delta=1e-6, rtol=1e-5
    obj = APIOnnx(op, 'dist', [9])
    obj.set_input_data(
        "input_data",
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')),
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')))
    obj.run()


def test_dist_10():
    """
    api: paddle.dist
    op version: 10
    """
    op = Net()
    op.eval()
    # net, name, ver_list, delta=1e-6, rtol=1e-5
    obj = APIOnnx(op, 'dist', [10])
    obj.set_input_data(
        "input_data",
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')),
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')))
    obj.run()


def test_dist_11():
    """
    api: paddle.dist
    op version: 11
    """
    op = Net()
    op.eval()
    # net, name, ver_list, delta=1e-6, rtol=1e-5
    obj = APIOnnx(op, 'dist', [11])
    obj.set_input_data(
        "input_data",
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')),
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')))
    obj.run()


def test_dist_12():
    """
    api: paddle.dist
    op version: 12
    """
    op = Net()
    op.eval()
    # net, name, ver_list, delta=1e-6, rtol=1e-5
    obj = APIOnnx(op, 'dist', [12])
    obj.set_input_data(
        "input_data",
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')),
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')))
    obj.run()


def test_dist_0():
    """
    api: paddle.dist
    op version: 12
    """
    op = Net(p=0)
    op.eval()
    # net, name, ver_list, delta=1e-6, rtol=1e-5
    obj = APIOnnx(op, 'dist', [12])
    obj.set_input_data(
        "input_data",
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')),
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')))
    obj.run()


def test_dist_inf():
    """
    api: paddle.dist
    op version: 12
    """
    op = Net(p=float('inf'))
    op.eval()
    # net, name, ver_list, delta=1e-6, rtol=1e-5
    obj = APIOnnx(op, 'dist', [12])
    obj.set_input_data(
        "input_data",
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')),
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')))
    obj.run()


def test_dist___inf():
    """
    api: paddle.dist
    op version: 12
    """
    op = Net(p=float('-inf'))
    op.eval()
    # net, name, ver_list, delta=1e-6, rtol=1e-5
    obj = APIOnnx(op, 'dist', [12])
    obj.set_input_data(
        "input_data",
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')),
        paddle.to_tensor(
            randtool("float", -1, 1, [3, 3, 3]).astype('float32')))
    obj.run()
