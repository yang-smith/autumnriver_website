+++
title = "激活ChatGPT（prompt工程小白到进阶）"
+++

## 前言

就像好的搜索引擎使用技巧可以大幅度提升你的搜索效率，一些灵活的与ChatGPT沟通的技巧可以大幅度增强你使用AI的能力。

我将这些技巧的学习分为三个阶段：

1. 学习基本原则
2. 学习如何结构化编写prompt
3. 探索让GPT辅助你编写prompt

下面我将分别说明这三个阶段。

## 基本原则

基本原则有两条：1. 尽可能清晰  2. 尽可能让GPT多思考

### 清晰

gpt的本质是在做概率推断，获得的信息越多越准确。极限情况，你对chatgpt说“一”，gpt就麻了，它不知道你要表达什么，无从推断。

假设你想知道怎么做一道地道的川菜麻婆豆腐。以前如果你在Google上搜索“麻婆豆腐”，搜索引擎会根据关键词给你展示许多食谱网站。你只需点击第一页出现的几个结果就很容易找到做法。

但如果直接对聊天机器人说“麻婆豆腐”，它可能无法准确理解你的需求。聊天机器人可能会给出一些与实际做法无关的回答。相反，如果你详细描述：“`请提供一份做地道川菜麻婆豆腐的食谱，必须包括所需原料、步骤、小技巧等信息，并在每个步骤后给出解释，最后总结这道菜的口感特点`”，那么聊天机器人就能准确理解你的需求，并给出具体和有用的食谱。

这说明在使用聊天机器人时，需要清晰具体的描述,而不是简单的关键词，才能获取高质量的回答。这与搜索引擎的使用有很大不同。明确的表达可以帮助聊天机器人更好地理解需求，从而给出更好的响应。**在保证输出质量下限的同时，还可以提高输出质量的上限！**

这和以往使用 Google 等搜索引擎的经验是完全不同的。

### 让gpt多思考

让GPT多思考就是让GPT做推理，而不是直接回答。

在 Prompt 中添加逐步推理的要求，能让语言模型投入更多时间逻辑思维，输出结果也将更可靠准确。举一个**[OpenAI 官方的例子](https://platform.openai.com/docs/guides/gpt-best-practices/tactic-instruct-the-model-to-work-out-its-own-solution-before-rushing-to-a-conclusion)**，如果你需要 GPT 回答某一个学生的答案是否正确，Prompt 是 `判断学生的解决方案是否正确`的话，面对复杂的计算问题和答案，GPT 有很大的概率会给出错误的答案，因为 GPT 并不会像人一样先进行推理答案再进行回答，而是会立即给出判断。在短暂的判断中，就无法给出正确的答案（就好比人类无法在短时间计算复杂数学一样）。换成这样的Prompt：`首先自己解决问题，然后再将自己的解决方案与学生的解决方案进行比较，并评估学生的解决方案是否正确。在自己完成问题之前，不要确定学生的解决方案是否正确`。在 Prompt 中给出明确的引导和条件，就能够让 GPT 模型花费更多的时间推导答案，从而得到更加准确的结果。

另一种有效的方法是引导GPT模型将一个复杂的任务分解成多个简单的子任务，并逐个完成它们。

这种任务拆分的方法涉及到首先将一个大型、复杂的任务划分为若干个更小、更易管理的子任务。接下来，我们分别指导GPT模型专注于每个子任务的推理过程。完成所有子任务后，将各部分的结果综合起来，形成一个全面的最终结果。采用这种方法的优势在于，它能够让GPT模型在处理每一个子任务时更加集中注意力，从而有效提高输出的准确性和质量。

### 一些即用的，增强性能的prompt

#### 下面这些语句可以加入到任意的对话结尾，可以一定程度的让GPT回答的更好。

- PS (Plan and Solve): Let’s first understand the problem and devise a plan to solve the problem. Then, let’s carry out the plan and solve the problem step by step.（让我们先理解问题，然后制定计划来解决问题。之后，让我们按照计划一步一步解决问题。）

- PS+ (Plan and Solve): Let’s first understand the problem, extract relevant variables and their corresponding numerals, and make a plan. Then, let’s carry out the plan, calculate intermediate variables (pay attention to correct numerical calculation and commonsense), solve the problem step by step, and show the answer. （让我们先理解问题，提取相关的变量及对应的数字，并制定计划。然后，让我们执行计划，计算中间变量(注意正确的数字计算和常识)，一步一步解决问题，并给出答案。）

- APE (Automatic Prompt Engineer): Let’s work this out in a step by step way to be sure we have the right answer. （让我们一步步地解决问题以确保有正确答案）

- OPRO (Optimization by PROmpting): Take a deep breath and work on this problem step-by-step.（深吸一口气，并逐步解决问题）

- A little bit of arithmetic and a logical approach will help us quickly arrive at the solution to this problem. （稍微进行一些算术运算和逻辑思考，可以帮助我们快速得出这个问题的解决方案。）

- Let's combine our numerical command and clear thinking to quickly and accurately decipher the answer.（让我们结合数字命令和清晰的思维，快速准确地解密答案。）

## 结构化prompt

当你想让chatGPT实现更加复杂一些的任务时，你就需要更加复杂的prompt。那么如何编写复杂的prompt。你可以使用下面的结构化prompt技巧。

什么是结构化？拿日常读书写作举例。在我们所读的书籍中，它们运用了各种标题、子标题、段落和句子等语法元素，在我们自己写作过程中，我们也会将内容分章节分段落的表达想法。简而言之，结构化Prompt的概念类似于写作的过程：它通过结构帮助我们清晰、有条理地表达我们的想法。

正如我们在日常生活中使用各种写作模板以便于阅读和表达，例如古代的八股文、现代的简历模板、学生实验报告模板和论文模板等，这些结构模板帮助我们以组织有序的方式呈现内容。同理，编写结构化的Prompt也可以借助各种优质模板，这不仅使写作过程更加轻松，还能提高内容的效果和效率。因此，选择或创造适合自己的模板，就像使用PPT模板一样，可以极大地提升结构化Prompt的质量。

我的一个模板是：

``` md
####**背景**

描述任务背景

####**目标任务**

告诉GPT它的最终目标是什么

####**实现策略**

告诉GPT，如何一步步实现上面的目标

####**输出示例**
给出输出示例

####**限制点和重要事项**
告诉GPT有哪些限制点或者重要的事项
```

在实现策略部分，可以使用AOT结构：
``` md
AoT（AOT  algorithm of thoughts） 在模仿算法思维。通过下面的几个workflow实现任务。

1. 定义问题：AoT 首先明确说明问题。
2. 收集信息：AoT 会提示LLM获取必要信息。
3. 分析信息：LLM会分析收集的信息。
4. 提出假设：提出一个初始解决方案。
5. 测试假设：LLM反驳假设，设想潜在结果。
6. 得出结论：LLM提供完善的解决方案。
```

根据上面的原理，看看下面书单筛选的例子：
```md       
    ####**背景**
    
    我正在寻找一些书籍的详细信息，以便决定是否选读。
    
    ####**目标任务**
    
    请为以下的书籍提供简介。这将帮助我了解每本书的内容和特点，并帮助我做出决策。
    
    ####**实现策略**
    
    take a deep breath and think step by step：
    
    1. 针对提供的书单，先确定书籍的完整标题和作者。
    2. 搜索和收集每本书的详细简介。
    3. 对收集到的简介进行简化，确保简介清晰且信息完整。
    4. 根据简介提供的信息，对书籍进行初步评估，包括可能的受众、风格、主题等。
    5. 将所有的信息整合后，按照书单的顺序提供给用户。
    - **示例**
        
        书名：《XXXX》，作者：“AAAA”：
        
        - 简介：此书描述了......
        - 评估：适合喜欢历史小说的读者，风格偏向于描述性，主题集中在......
    
    ####**限制点和重要事项**
    
    1. 所提供的信息必须基于事实。
    2. 如果某本书的具体内容未知，需直接说明不知道。
    3. 尽量提供完整且简洁的简介。
    
    ####书单如下
```

结构化prompt还有很多的内容可以探索，感兴趣的朋友可以关注即刻 李继刚 或者参考[LangGPT](https://github.com/yzfly/LangGPT)

## 让GPT帮你完成prompt

真正的改变在于，你可以教会GPT如何写Prompt，进而让它帮你完成这一任务。

你可以将上述所有技巧喂给GPT，让它成为一位Prompt撰写专家。在这种模式下，你只需提供一个Prompt的初稿，GPT便能够自动对其进行优化。这意味着，通过简单的初步输入，GPT能够运用其学习到的技巧，帮助你精炼和提升Prompt的质量。

具体而言，这种方法带来的优势包括：

1. **提升Prompt质量**：经过精心训练的GPT能够根据最佳实践撰写Prompt，确保其结构完整，充分发挥GPT模型的潜力。
2. **节省精力与时间**：这种方法使得原本繁琐的Prompt编写过程自动化，用户无需从头开始构思Prompt的框架，极大地节约了时间和精力。
3. **便于迭代和优化**：在GPT的协助下，用户可以快速迭代和优化Prompt版本，评估效果，并选择最佳模板，从而轻松实现优化。
4. **广泛的适应性**：GPT能够学习并掌握针对不同领域和任务的Prompt编写技巧，轻松适应新的需求。

## 总结

从上述内容中，我们可以看出与ChatGPT高效沟通的三个层次：

1. **理解基本原则**：这是使用ChatGPT的基础，强调的是清晰性和促使GPT深入思考。通过生动、形象的类比，我们可以更好地理解并应用这些原则。
2. **掌握结构化Prompt的技巧**：在这一层次中，我们学习如何利用背景、目标、策略和限制条件等框架来引导GPT有效解决复杂问题。
3. **利用GPT辅助Prompt的编写**：这代表了与ChatGPT交互的高层次，实现了自动化生成高质量Prompt的目标，减少了重复性劳动。

通过逐步深入这三个层次，我们可以建立与ChatGPT更加高效和丰富的协作关系，充分发挥其巨大的潜力，创造更多的价值。

## 参考

[gpt-embeddings](https://guangzhengli.com/blog/zh/gpt-embeddings/)

[prompt-engineering-for-developers](https://github.com/datawhalechina/prompt-engineering-for-developers)

[algorithm of thoughts](https://mp.weixin.qq.com/s/HH2JthU7pmiSjbHsJKpy7w)     

[思维树](https://twitter.com/bindureddy/status/1700715030046802148)   