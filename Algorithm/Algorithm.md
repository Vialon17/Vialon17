
# Algorithm and Data Structure

## Before

### 三羊三狼过河问题：
* 首先定义河两边的状态
* 进行状态循环， 用于确认状态；
    * 确认两边状态，确认船位置 
    * 判断两边状态是否完全调换完毕
        * 是：结束循环/递归返回
        * 否：(这里是 _循环嵌套_)
            * 进行运输循环，五种运输方式：
                > 一狼一羊;两狼;两羊;一狼;一羊
                * 判断两边是否符合规则（羊数>=狼数）：
                * 是，进行运输并改变两边状态并跳出运输循环
                * 否，继续循环寻找其他运势方式
------

[The Euclidean Algorithm](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)

__The Euclidean Algorithm for finding GCD(A,B) is as follows:__

* __If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.__ 
* __If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.__
* __Write A in quotient remainder form (A = B⋅Q + R).__
* __Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R).__
* __do circle.__
-----

### D&C思路

1. 确定问题的 __基线条件__。
2. 确定如何进行问题分析以逐步缩小问题规模，使其符合基线条件。
   
旬如递归、循环等问题的解决使用非常方便。

### 归纳证明

对于快速排序，可使用类似的推理。在基线条件中，我证明这种算法对空数组或包含一个元素的数组管用。在归纳条件中，我证明如果快速排序对包含一个元素的数组管用，对包含两个元素的数组也将管用；如果它对包含两个元素的数组管用，对包含三个元素的数组也将管用，以此类推。因此，我可以说，快速排序对任何长度的数组都管用。这里不再深入讨论归纳证明，但它很有趣，并与[D&C](#the-euclidean-algorithm)协同发挥作用。

-----


   Here is the nodetext of python,
   and i well use chinese to write it.

   python数据结构与算法
   #python算法部分

---------
## 3.基本数据结构

### **3.4 队列**

   **模拟打印任务**

   考虑计算机科学实验室里的这样一个场景：在任何给定的一小时内，实验室里都有约 10 个学生。他们在这一小时内最多打印2次，并且打印的页数从 1 到 20 不等。实验室的打印机比较老旧，每分钟只能以低质量打印 10 页。可以将打印质量调高，但是这样做会导致打印机每分钟只能打印 5 页。降低打印速度可能导致学生等待过长时间。那么，应该如何设置打印速度呢？

   首先构建打印队列queue用以对任务进行排序处理；
   初始化打印机状态和队列；

   构建整体循环
   
    初始化循环环境变量；
   	判断每秒是否存在新元素进入队列：
   	存在新元素：
   		把该元素压入队列，并根据任务包大小进行计算打印操作所需时间（此处单独建立函数用以计算每个任务包预估时间），同时记录进入时间戳；
   	检测打印机状态：
   	空闲：
   		判断打印队列：
   		打印队列为空：
   			sleep若干秒；结束打印循环。
   		打印队列不为空：
   			pop最前面的任务进入打印机，记录当前时间戳；
   			计算上一任务从进入时间戳到下一任务进入打印机的时间戳差值，并记录至其他数据结构（列表、字典）；
   	不为空闲：
   		根据打印机任务最初时间戳计算正在操作任务剩余操作时间；
   	根据正在打印任务剩余时间分别对队列中剩余元素打印时间进行计算；

### **3.5 双端队列**

   相当于堆栈、队列的结合，排序原则不固定，
   前后均可进出；

### **3.6 列表**

   并非所有语言都有列表？（md智障）

   （直接有三方库多元化数据结构）
   分为有序、无序列表，区别为有序列表中元素的相对位置取决于其基本特征，通常可以进行有意义比较并进行排序处理后的列表；

   有趣的是，list删除元素的方法是赋值指针跳过操作；
   "在分析链表操作的时间复杂度时，考虑其是否需要遍历列表。以有n个节点的链表为例，isEmpty 方法的时间复杂度是(1)O，这是因为它只需要执行一步操作，即检查 head 引用是否为None。length方法则总是需要执行 n 步操作，这是因为只有完全遍历整个列表才能知道究竟有多少个元素。"

      think：
          把list做成三元素形式：序列号 + 字符串 + 指针，这样length方法大o复杂度仅仅为O(1)，但相应会增加空间成本，当储存数据少量或者优先考虑时间成本时，可适当采用；当数据量庞大或者算力较优秀的情况下，适合使用O(n)的正常list形式；

   习题：

   	2，**+AB+CD+EF;
   	   +A*+BC+DE
   	   ++***ABCDEF
   	9，当链表节点数为1时，考虑使用length方法判断大小后直接赋值为空链表；
------

##  4。递归

      递归算法原则：
      	递归必须有最基本的情况；
      	递归必须改变其状态并向基本情况靠近；
      	递归必须不断调用函数本身；
      相比于高等生命体的模糊算法，递归本身属于基本生命体的基础算法，递归最大的困难在于资源占用率，虽然节省代码量，但其时间占用量会显得十分突兀；实际操作时应尽量减少使用递归除非当问题逻辑比较混乱复杂且递归算法计算量不大的时候考虑递归最佳；

      递归核心问题：
      	递归基本模型的寻找。
      		当然这个基本模型可以选用ifelse进行复杂化处理，引入其他函数方法进行补充更佳；
      	递归条件的改变寻找(其实不是主要问题)；
      简单说明例(仅说明思路)：
      歇尔平斯基三角：
      def function(len):
      	if len >= 3:
      		function_draw(len)
      		function(len/2)*3
      		##三次递归调用
      分支递归结构和分叉树结构类似，在递归中多次调用递归函数，形成分支，但整体复杂程度较简单，不如分叉树。

   **汉诺塔问题：**

      最基本问题：
      	判断塔中下面的盘是否比上面的大：
      	yes：循环
      	no：
      		借助第三根柱子调换顺序
      over。
      ps:
      	python中调用两个变量甚至不需要借助三方变量：
      	python:
      		a = 12; b = 13
      		a, b = b, a
      	C++:
      		int a = 12, b = 13, c;
      		c = a, a = b, b = c;

_迷宫问题：crazy？_

   	 从起始位置开始，首先向北移动一格，然后在新的位置再递归地重复本过程。
   	 如果第一步往北行不通，就尝试向南移动一格，然后递归地重复本过程。
   	 如果向南也行不通，就尝试向西移动一格，然后递归地重复本过程。
   	 如果向北、向南和向西都不行，就尝试向东移动一格，然后递归地重复本过程。
   	如果4个方向都不行，就意味着没有出路。
   	#？重复向右问题。
    ps:此处为copy。

**算法目的**：了解不同的问题解决策略，在结局优化问题时进行有选择规划；

      贪婪算法：最优解？？
      	使用尽可能多的硬币，然后尽可能多地使用面值第 2 大的硬币。这种方法叫作贪婪算法——试图最大程度地解决问题。(copy)
      递归解决最优解：
      	基本思路：
      		判断剩余零钱面额与额定面值是否相等：
      		相等：
      			返回该硬币面值(找到最后一枚)；
      		不相等：
      			选择最少硬币数：
      				按照1枚1分的硬币进行递加至面额(递归)；
      				1枚5分硬币 + 剩余面额(递归)；
      				1枚10分硬币+ 剩余面额(递归)；
      				1枚25分硬币+ 剩余面额(递归)；
      但递归嵌套层数贼tm大，占用内存量更不用说，比穷举好点吧。

事实上，针对找零金额是 63 分的情况，它需要进行 67 716 925 次递归调用才能找到最优解。

考虑逆向递归，可能一些情况下会有优势。

当然，动态规划的核心是进行逆向递归局域最优解处理，用于节省数据计算量。

      递归阶乘
      def function(num):
      	if type(num) != int:
      		raise TypeError('Need int type!')
      	if num >= 1:
      		return num * function(num - 1)
      	else: return 1


      递归过河：
      要求：
           三狮子三羊，船仅装两个，两边狮子数不大于羊。
      #a[0] -> lion, a[1] -> sheep;
      state_a = [3, 3, 1]
      state_b = [0, 0, 0]
      func = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
      def function():
      	for i in func:

   本质为选择性堆栈问题。
   ##https://blog.csdn.net/ggjkd/article/details/119086844

   帕斯卡三角：

      temp = []
      def function(n):
      	if n == 1:
      		return 1
      	else:
      		for i in n:
      			temp[i] = function(n-1)
   ....

------

## **顺序搜索和二分搜索(快速搜索)：**

* __顺序搜索__
    > 顺序搜索时间复杂度BigO(n)，直接遍历搜索整个列表即可；
* __二分搜索__
    > 二分搜索较为常用，其核心思想为：
    > 
    >> 在有序数组Array中，依次中值检索。
    > 
    > 通过不断缩放数组大小(每次进行二分裂排除)，二分排序可以快速找到相应值。<br>
    >其时间复杂度BigO(log<sub>n</sub>)  
    > **但注意二分搜索的前提为：有序数列**

## __散列(HASH)：__

极尽化的简要搜索模式，将搜索时间复杂度降低为BigO(1)的一种操作（理论上），十分类似于 Python中的Dict类型。  
散列表的本质为一组固定长度的地址索引队列，队列内容为Value，存在特定function算法用于将Key与该散列表的Value绑定（一种映射关系）。

散列表的特点：
  * 存在唯一的映射Function使输入的数据转变为特定的整数；
  * 该映射Function针对不同的数据映射值唯一（理想情况）；
  * 散列表的值不存在可重复性（dict/set 特性之一）；

也就是说，将Value储存在某特定队列中，通过Function与相应的Key值建立映射关系，这样使得队列查询的时间复杂度**BigO(n) -> BigO(1)**,  

当然，过程中存在很多情况使得 得到的散列表中存在`映射冲突现象`，即
```
Different Keys have the same Value through the specific mapping function.
``` 
So there we need to solve this problem, here we have three functions to do it:
* It's easy to create more difficult Function or longer Hash Table to avoid the conflict between two keys.
* We can store a momery address pointing to a linked list in the Hash Table, so when there appears the conflict keys, they can be stored in a special short list included in the Hash Table.
```
Just like this:
    ### Here we create a price table mapping the names.
    Hash Table = ['0x0002c', '0x000y3', '0x00056', '0x025a3', '0x0045k']
    list1 = ['5.05$', '2.31$'] # momery address:0x0002c
    list2 = ['21.00$', '5.23$', '45.50$'] # momery address:0x000y3

    when you find the 'apple' price, the Hash Function will return the '0x0002c' address, then you'll traverse the list1 by order and finally find the apple's price:2.31$.

    # Attention:
        1. the lists shouldn't be too long that may make effects on the algorithm's execution rate;
        2. though this way can solve the conflict temporarily, it'll speed down the time complexity function: BigO = O(1)*O(n), which there the 'n' means the list's length.
        3. there shouldn't have many vacancies in the hash table, which means u'r wasting momery space.
```
* When there comes the conflict in Hash table, we can store the value in the neighboring vacancy(the next 'None' default vacancy) to improve the table's utilization.<br> It's better to use another Hash function to locate those conflict keys.  
  For example:
    > The Hash Table:
        >>{0 : '77', 1: None, 2: None, 3: None, 4: '26', 5:'93', 6: '17', 7: None, 8: None, 9: '31', 10: '54'}<br>
        >>Instruction:<br>
            >>>the hash function's rule:
               >>>> Use the key divide by the length of the hash table,leave the remainder as the index to store the key.
               >>>>
            >>>so there we can store the 77 in index zero, 26 in index 4th and so on.
            >>>       
    >>But when we store 44 into this hash table, there should have a function to solve the conflict between 77 and 44, the strategy is that: use the Next None vacancy(1+ n^2), so we store the 44 in the index of 2rd, we have to value 'n' 2(f(n) = 5) if the 2rd has its value so that the 44 is stored in 5th vacancy.<br>
    >Just like this...

**`Load Factor`**:the utilization of the hash table, and is always expressed as the divider of the numbers of the elements and the length of the table[^2].
$$
    λ = \frac N L
$$

Let's get clarity on thoughts about the Hash table:
> There first we have three element in this strategy:
> * The key: We wanna get the "Apple" price;
> * The index: The storage site of the Apple's price;
> * The value: The data of the Apple's price that we wanna store;
> Here we use a Hash function to change the key into a index in the hash table which store the value, and if there comes the conflict, we had three methods to make it.
>

The Application:
* The hash table is usually used in retrieving data;
* It can also be used in storing some website's local cache in order to accelerate the web's loading speed and reduce the server's computation;
* Just like the dict data structure in Python, the Hash Table can avoid repetition;
* And so on...

**Notice**: here just a essay followwing my step is, so I used some own vocabularise, it's more comforatable to read the book "[Problem Solving with Algorithms and Data Structures Using Python](https://www.ituring.com.cn/book/2482)"

*PostScript*: I privately think "[Grokking Algorithms](https://www.ituring.com.cn/book/1864)" is easier to underastand than the upper.

[^2]: N: numbers of the elements; L: length of the Hash table.

------
## 排序Sort:

### 快速排序：Stack:qui_sork function

> 主要利用[D&C](#D&C思路)逐步将问题简化，使其接近问题的基线条件，然后进行比较，其时间复杂度BigO(nlog<sub>2</sub>n)；<br>其核心思想为：
>
>> * 基线条件：当元素个数小于等于2个时，可以直接进行比较并进行排序；
>> * 缩减步骤：元素个数较多时，采取二分法将整个数组Array断裂为三个部分：前、中(仅为一个元素/基准值)、后；然后前后两个数组内的元素分别于基准值进行比较并置换数组，使整个前数组整体小于基准值，后数组大于基准值；
>> * 进行递归操作；
>
>时间复杂度分析为：二分搜索BigO(log<sub>n</sub>)和简单排序（每次排序的时间复杂度为BigO(n)之积）

> __Add Info__  
> There the Quick Sort is based on the Merge Sort.  
> Due to we have mastered the Quick Sort, I'll introduce the Merge Sort simply here.
> divide the list into single element using dichotomy method and recursion and then recombinate the ones with comparing.  ~~it's too complex i thought.~~  
> __Merge Sort will use more storage space that Quick Sort.__

### **冒泡排序：Bubble Sort (Stack:qui_sork_fack function)**

~~It's funny that I had confused the Bubble Sort with the Quick Sort and regarded Bubble as Quick at first.~~

The Bubble Sort's `core thought`: 

* find the maximum value in the list and put it in the first.
* `recursion` or `cycle`.

It's easy to understand and use in practical works.  
we just need compare the fist value with the other values, if there has another value is greater than the first, regard it as the first and continue.  
We get the maximum of the list after comparison for `n cycles`.   
Then we throw away it temporarily and start the comparison bwtween the second with the left ones to get `the second maximum`(n-1 cycles), just do cycle and we can sort the list finally.

The Time Complexity for Bubble Sort: BigO(n<sup>2</sup>)
> In fact, the number of the comparison is:$\frac 12*n^2+ \frac 12*n = n+(n-1)+(n-2)+...+1$  

Bubbble Sort is usually regarded as the loser when considering the efficient because of its most useless comparisons, so there we have the `Select Sort`.

> **Select Sort (Stack:ins\_sort function)** 
> Just like the Bubble Sort, Seclect Sort also needs BigO(n<sub>2</sub>), but through change the index of list, we can reduce the numbers of the warping sites.  
> Compared with the Bubble Sort, the flashing star of the Select Sort is that it just needs one exchange step in every cycle.

> __Insert Sort__  
> Insert Sort is very likely with the select Sort, which the time complaxity function is BigO(n<sup>2</sup>) and needs nested cycles to complete its work. The flashing attraction of Insert Sort is that, it'll create an ordered child list inside target list, so the work left is moving other element into the ordered list.  
> But it will be more efficient than the Select Sort beacuse __the moving step which just needs one assignment step is faster than the exchanging step in the Select Sort or Bubble Sort for three steps .__   
> The textbook said that "The Insert Sort shows its good conduct in the benchmarks compared with other sorting algorithms".

### Hill Sort

Hill Sort seems like the combination of several simple Insert Sort. In fact, it does the previous sort to divide the list into several smaller lists, and that will improve the efficiency of the Insert Sort latter.  
Here  it's the steps:
* Sort the list `properly`;<br>
  
    >What means property? Well, that's a good question, we could do the limit for sorting so that we get n lists for which list whose length is n or the list itself.  
    >The purpose of the previous sort is to reduce the unnecessary steps in the following sort, so it's a good thought dividing the list into several parts and keeping the balance between the sorting steps.

* Do the previous sort for the several parts of the list(Using Insert Sort);

    >There have the listA = [26, 87, 19], listB = [16, 53, 24], listC = [44, 95, 31], so we do the following:  
    > ```
    > list = [26, 87, 19, 16, 53, 24, 44, 95, 31];
    > listA = [26, 87, 19], listB = [16, 53, 24], listC = [44, 95, 31];
    > compare A1, B1 with C1; A2, B2 with C; A3, B3 with C3;
    > get new listA, listB and listC;
    > ```

* Do the Insert Sort for the target list.

We calculated the time complexity function BigO() and the result shows that the BigO function is between BigO(n) and BigO(n<sup>2</sup>) which proves how powerful the preprocessing is. _I privately think there should have some relations between the BigO function and the `proper` preprocessing._

### Sort Summary

According to the complexity of the time complexity function BigO(), we get the sort methods by order:
* BigO(nlog<sub>2</sub>n) => **Quick Sort** and Merge Sort
* BigO(n<sup>2/3</sup>) => **Hill Sort**(n -> n<sup>2</sup>)
* BigO(n<sup>2</sup>) => **Insert Sort**, Select Sort, Bubble Sort
  
    > Attention: The time complexity function usually is calculated by the worst situation

------

## Graph and Binary Tree

### Graph

Graph is used for describing the relational network between different objects almostly.

We can find many examples in our daily life: The family tree, The network of interpersonal relationship, The network of animal's predation and so on. It's a basic data structure that we could have learned in primary school everly.

The Graph's Composition:
* `Vertex`: the point representing one object ifself;
* `Edge`: the connection of two vertexes to show there has relation between them;

    >The Graph is divided into two kinds: `digraph` and `undigraph` according to if there the edge has its direction,

* `Weight`: the abstract concept the parter of the Edge to measure the relation in two vertexes;

