# uniform search

![image-20191121163628656](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191121163628656.png)

找到最有可能展开的node来进行展开

![image-20191121163918294](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191121163918294.png)

上面提到的fringe是s, s->e, s->e->h，每次选出一个后就要把它remove，然后通过successor function来展开。

![image-20191121164340569](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191121164340569.png)

以上这个图介绍dfs非常形象

![image-20191121164946316](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191121164946316.png)

这里是一些符号说明

![image-20191121165821155](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191121165821155.png)

这里的空间复杂度是O(bm)是指，算法每往下搜索时，都会保存当前的状态，每次保存b个状态

![image-20191121165841069](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191121165841069.png)

![image-20191121170110340](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191121170110340.png)

bfs不一定是最优的，当你每个action的权重是1时它是最优的（想一下最短路算法）

![image-20191121205433156](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191121205433156.png)

结合了两种算法，每次得从第一个node开始算起

# CSP 1（constraint satidfaction problem）

![image-20191206113752543](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206113752543.png)

searching有两种，第一种是用最少的代价找出路径，第二种是判断到goal state是否有路径，不需要考虑代价。在这里csp是identification problem

![image-20191206123018320](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206123018320.png)

上面是符号的一些说明，这个是涂色问题

![image-20191206123428689](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206123428689.png)

上面的限制公式是符合情况下

![image-20191206123724212](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206123724212.png)

把限制条件抽象为图

![image-20191206153624609](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206153624609.png)

![image-20191206154658357](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206154658357.png)

这是另一种求解的方法，每次先随机选一种颜色，然后邻居就损失一种颜色，如果这样展开是合法的话就这样展开，否者backtracking

# Minimax

![image-20191029165728877](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191029165728877.png)

倒数第二个是判断新的state是否合法，比如说越界或者是否撞墙了

![image-20191029170025854](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191029170025854.png)

Zero sum

win win

![image-20191029170427238](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191029170427238.png)

左边的数字是父母状态到儿子状态要走的步数

![image-20191029234151355](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191029234151355.png)

根节点最大化utility，其他节点最小化儿子节点

![image-20191029234732177](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191029234732177.png)

每一层是一个玩家

![image-20191029234903716](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191029234903716.png)

**![image-20191031092146019](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191031092146019.png)**

最左边搜索到的答案是3，那么看第二个一开始碰上是2，不可能比3要大，所以就直接剪掉，这样启发式地剪枝

# alpha beta

![image-20191031093214492](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191031093214492.png)

![image-20191031093232647](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191031093232647.png)

上面两张ppt的意思是，拿右边的作为例子，对于min来说，每次找到最少的那个v，如果是比之前计算的还要少，我们就不更新它，因为root是要算最少中的最大，所以要另一边求出来的v' < v我们就不展开v'

![image-20191031095519577](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191031095519577.png)

以上是其中一个例子，每个node搜索完之后都会接受children返回的信息来更新自己的最低或最高标准

![image-20191031101915550](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191031101915550.png)

## alpha-beta example

这个[视频](https://www.youtube.com/watch?v=jvpWtwVSvjA)讲得很清楚

![image-20191031102412924](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191031102412924.png)

这节课还有[笔记](https://inst.eecs.berkeley.edu/~cs188/fa18/assets/notes/n3.pdf)，后期如果视频的内容忘记了，可以去看

## 课后作业

[link](https://inst.eecs.berkeley.edu/~cs188/fa18/assets/hw/CS_188_Fall_2018_Written_HW3.pdf)

# uncertainty

## expectimax search

![image-20191031214407074](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191031214407074.png)

在算最小化的时候，右边的node的值是54.5，做了一个average。为什么呢？因为这时候opponent是做了一个random action

![image-20191031214548624](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191031214548624.png)

以上算法就是minimax的改良版，在min的时候做一个期望的估计

![image-20191031215051852](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191031215051852.png)

上面是这个算法的一个例子

![image-20191031221506562](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191031221506562.png)

Q: 有以上这么一个问题，当你的opponent是80%的几率做minimax search还有20%的几率做random action，那么你model你的tree search的时候，你要怎么生成你的树

A: 你还是需要使用Expectimax，因为你在的father node 的计算公式将会是这样：

```python
v = max(v, 0.8*minimax(child) + 0.2*random(child))
```

![image-20191031224753901](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191031224753901.png)

以上这个是多agent时如何选择，绿色选绿色的值，蓝色选蓝色的值

![image-20191031225229975](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191031225229975.png)

为什么我们大多数时候选择average，而不是minimax，因为根据吃豆人游戏来看，minimax容易让我们的agent胆小怕事

![image-20191101100928514](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191101100928514.png)

以上是expected utility的缺点，通过平方后，minimax的路径不会改变，但是expectimax会收到影响

![image-20191101101754056](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191101101754056.png)

以上才进入这节课的正题

![image-20191101112543721](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191101112543721.png)

上面定义了lotteries是什么，看起来就是一个期望值的意思

![image-20191101102458139](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191101102458139.png)

这个例子是说：如果agent违背这个定理，他会进入一个循环，浪费它所有的钱

![image-20191101102939893](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191101102939893.png)

上面说了，加权平均是理性的表现，理性就是最大化期望值

![image-20191101113306261](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191101113306261.png)

# Markov Decision Processes

![image-20191105163313325](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191105163313325.png)

上面是给出一些定义

transaction T(s, a, s')方程是说，如果在state s下采取action a那么这个状态转移到s'的概率有多大

![image-20191105163738455](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191105163738455.png)

mdp的意思是他只跟前一个state和前一个action有关系，它不再跟其他状态有关了

![image-20191105164400551](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191105164400551.png)

policy是指对于每个state都给出对应的这个state的action，就像右边那个小地图一样，最后我们的policy就是一系列的action组成

![image-20191105204906384](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191105204906384.png)

最大化总的价值，让agent最快找到reward。解决以上问题的方法是使用decay

![image-20191105205324271](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191105205324271.png)

可以使用以下这个方法来进行衰减，在实际中多使用exponential来进行衰减

![image-20191105211057803](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191105211057803.png)

三个状态的定义

![image-20191105211414862](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191105211414862.png)

这个是V*(s)

![image-20191105211441634](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191105211441634.png)

这个是Q-value

![image-20191105212041325](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191105212041325.png)

上面三条公式经常看到

![image-20191105212334466](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191105212334466.png)

搜索时会遇到的几个问题，出现重复的状态，出现无限搜索状态，需要剪枝

![image-20191105213215364](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191105213215364.png)

![image-20191107221538082](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191107221538082.png)

Vk下面的k是指向前走的深度k。也就是要搜索的时间k

细细品味上一个图，其中Q(a, s)是指绿色和下面大三角形的值。V(s)是在所有的绿色中选出最优的一个

![image-20191107200939189](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191107200939189.png)

policy是state到action的映射

utility是每一个transaction后得到的action的求和（可带有discount）

V(s)是这个state到最终状态的最优值

Q-value是走一步之后这个action得到的reward和未来的V组成的最优值

![image-20191107220803787](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191107220803787.png)

![image-20191107223915831](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191107223915831.png)

这一页的ppt讲了为什么Vk是收敛的，因为看到红色小圈圈，左边一项指数减少，最后Vk的递增项不断减少

![image-20191107225150176](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191107225150176.png)

这里跟上面的V*相比是不需要算所有的action，就只指定特定的action就可以了

# RL

![image-20191111221135919](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191111221135919.png)

以上就是rl跟mdp的区别，现在我不知道T和R

![image-20191112162024111](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191112162024111.png)

以上是model-based learning，后面会讲model-free learning

![image-20191112162600253](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191112162600253.png)

首先你探索，有了data之后，你learn model然后生成数据，然后迭代模型

![image-20191112165131498](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191112165131498.png)

上面是解释了这两种model的区别

![image-20191119221633131](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191119221633131.png)

我们可以使用上面这个公式，先做出action，然后根据这个new state来算average，选一个最大的action走。但是这样做会有不好的地方，就是你在真实的世界中你不能先走一步然后再reset，因为这个世界是dynamic的，你不能做预判

![image-20191119222409337](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191119222409337.png)

这就是我们所说的贝叶斯平滑方法，适合使用在iA

![image-20191120100103821](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191120100103821.png)

传统的强化学习没有R和T，需要动态地更新我们的模型

![image-20191120102650023](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191120102650023.png)

这是著名的q-learning公式，与其计算得出V value，不如计算Q-value，但是这个想法不能用到negotiation里面，因为你不能不断地尝试然后重来

# RL2

![image-20191203163638647](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191203163638647.png)

以上就是我们q learning算法，相比于计算第一个公式，我们不能够直接计算出T的数值，而是用移动平均的方法

![image-20191203164122561](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191203164122561.png)

alpha要慢慢地减少

![image-20191203164439758](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191203164439758.png)

![image-20191203164505331](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191203164505331.png)

epslion greedy algo，epsion的数值要比较小



![image-20191203165212281](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191203165212281.png)

n是代表你去过那里的次数，这是求出一个权重，表示越经常去的地方就越不可能再去哪儿了

![image-20191203165529130](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191203165529130.png)

所以我们的q learning可以改写成以下这个式子，越经常采取的action就很少再计算了

![image-20191203211833490](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191203211833490.png)

引入了机器学习的思想，来求解出不同的feature  



![image-20191203220256719](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191203220256719.png)

太强了，过拟合就是会出现这种现象，就是说出现奇怪现象的概率大大增加

# probability

![image-20191206111916693](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206111916693.png)

之前都是searching和planing，这节课开始model uncertainty

![image-20191206112201430](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206112201430.png)

基本上是讲数学知识

![image-20191206162239573](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206162239573.png)

联合概率分布式是一条数据

![image-20191206162318158](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206162318158.png)

边缘概率分布式一个子表格 

![image-20191206162812088](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206162812088.png)

上面是带条件的分布

![image-20191206163414116](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206163414116.png)

条件概率就是一个normalization的过程

![image-20191206164939990](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206164939990.png)

![image-20191206165200547](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206165200547.png)

# Bayes' Nets

![image-20191206202320610](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206202320610.png)

![image-20191206205331492](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206205331492.png)

变量之间的独立很难做到，但是条件变量的独立可以做到。注意，上面这个式子非常拗口。X变量跟Y变量相互独立是在给定z的条件下的情况下发生的。

你可以这么直观地理解，如果你把z去掉，那么式子就变成P(x, y) = P(x ) P(y )。x和y变量是相互独立的。加上z条件后就变成条件相互独立。 

第二个式子也是条件独立的定义，P(x| z, y)是给定z and y条件的x概率，它等于P(x | z)，这是因为有了z变量之后，y变量的出现不会对x的观察有非常大的影响。

![image-20191206210435940](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206210435940.png)

可以用这个例子辅助理解，如果房子一开始有烟了，有没有火对alarm是否要响相关性不大

![image-20191206211614479](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206211614479.png)

 ![image-20191206220108780](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206220108780.png)

这又是一个强假设



# Bayes independence

![image-20191206222358257](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206222358257.png)

上面试概率论的知识回顾

![image-20191206222821892](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206222821892.png)

bayes可以解决的问题

![image-20191206223305652](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191206223305652.png)

最后一个式子是为了简化计算的一种计算方式

![image-20191207110855487](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191207110855487.png)

bayes网络给出一个唯一的假设，我觉得也是非常强的，就是说一个变量的值变成只跟它的父母变量有关，而不是跟所有的变量有关

![image-20191207112334790](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191207112334790.png)

这张图很有必要不断地复习。

首先看第一行的公式，P(x, y, z, w) = P(x) * P(y|x) * P(z| x, y) * P(w| x, y, z), 这个是一定成立的chain rule

由于我们把图建模成上面的因果关系，根据bayes net的假设：每个节点只跟其parent节点有关。我们的公式可以化简成下面这种形式：P(z) * P(y|x) * P(z | y) * P(w | z)

我们可以得到这些conditional independence w 独立于 给定了z的x和y

同时上面的式子也可以写成w独立于给定y的X变量

![image-20191207114425213](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191207114425213.png)

在这里，我们不能够说x和z是一定相互独立的，因为x可能影响z通过y

![image-20191207114731248](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191207114731248.png)

上面这个例子说给出这么一个bayes net我们能够说x和z是相互独立的吗？不能

![image-20191207115121733](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191207115121733.png)

在这里是证明了，如果使用这种bayes net并且使用conditional independence。那么z和x是不是相互独立的，经过数学的推导是Yes

![image-20191207115534372](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191207115534372.png)

这是另外一种分支结构

![image-20191207115922117](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191207115922117.png)

![image-20191208114956787](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191208114956787.png)

这是用来判断变量之间是否条件独立的标准，左边是当这些情况发生了，条件独立就不存在，因为信息发生了流通。

inactive means block the info, so it shows independence

![image-20191208115145983](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191208115145983.png)

在这种情况下，第一个是独立的，其他不独立。对照上面的三元组来看

![image-20191208120256348](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191208120256348.png)

第二个例子，第三个不成立

![image-20191208120547651](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191208120547651.png)

![image-20191208133000751](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191208133000751.png)

如果三个变量是相互独立的，你需要给出左边这么多的assumption

# Bayes inference 

so hard

# Bayes sampling

sampling

rejection sampling

likelihood weight sampling

glide sampling

# Decision Network

![image-20191209101801140](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191209101801140.png)

combine two part, one is plan and the other is model the uncertainty

![image-20191209102258508](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191209102258508.png)

基本的符号说明

![image-20191209103113087](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191209103113087.png)

计算过程，这个过程好像mdp

![image-20191209103757594](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191209103757594.png)

上面是这个流程图的计算方法，左下角是找到最大expected utility的action

![image-20191209110356410](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191209110356410.png)

# HMM

![image-20191209120618309](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191209120618309.png)

![image-20191209121820186](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191209121820186.png)

总是能够收敛到一个相同的数值

# Partial filtering

# Dynamic Bayes Net

![image-20191209205018630](/Users/huojunyi/Library/Application Support/typora-user-images/image-20191209205018630.png)

