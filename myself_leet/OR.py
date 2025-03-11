#!/usr/bin/env python
# coding=utf-8

# @Author     : whiteding
# @FileName   : ordinal_regression_demo.py
# @Reference  : https://github.com/EthanRosenthal/spacecutter


import torch
import torch.nn as nn
import torch.optim as optim


class OrdinalRegressionModel(nn.Module):
    def __init__(self, input_dim, num_classes, scale=5.0):
        super(OrdinalRegressionModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)  # 不管多少类, 输出1个scalar, 类似线性回归

        self.num_classes = num_classes
        num_cutpoints = self.num_classes - 1
        # 初始化num_cutpoints个分割点
        self.cutpoints = torch.arange(num_cutpoints).float() * scale / (num_classes - 2) - scale / 2
        self.cutpoints = nn.Parameter(self.cutpoints)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        # [batch_size, num_classes-1]
        y_pred = self.cutpoints - x
        return y_pred


# 损失函数
def cumulative_logit_loss(y_true, y_pred):
    num_classes = y_pred.size(1) + 1
    y_true = y_true.long()

    # 注意, 不是softmax, 是sigmoid
    cumulative_probs = torch.sigmoid(y_pred)

    # [batch_size, num_classes]
    cumulative_probs = torch.cat([torch.zeros_like(cumulative_probs[:, :1]),
                                  cumulative_probs,
                                  torch.ones_like(cumulative_probs[:, :1])], dim=1)

    probs = cumulative_probs[:, 1:] - cumulative_probs[:, :-1]

    y_true_one_hot = torch.eye(num_classes)[y_true].to(y_pred.device)
    log_probs = torch.log(probs + 1e-10)

    loss = -torch.sum(y_true_one_hot * log_probs, dim=1)
    return loss.mean()


# 创建模型
input_dim = 10  # 假设输入特征维度为10
num_classes = 4  # 五个评分等级[0,1,2,3,4]
model = OrdinalRegressionModel(input_dim, num_classes)

# 训练模型
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = cumulative_logit_loss

# 生成训练数据
X_train = torch.rand(100, input_dim)
y_train = torch.randint(0, num_classes, (100,))

# 训练循环
for epoch in range(10):
    model.train()
    optimizer.zero_grad()

    outputs = model(X_train)
    loss = criterion(y_train, outputs)

    loss.backward()
    optimizer.step()

    print(f"model.cutpoints:{model.cutpoints}")
    print(f'Epoch [{epoch + 1}/10], Loss: {loss.item():.4f}')