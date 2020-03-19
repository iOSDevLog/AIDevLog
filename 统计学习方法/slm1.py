#!/usr/bin/env python
# -*- coding: utf-8 -*-

from manimlib.imports import *


class Title(Scene):
    def construct(self):
        title = TextMobject("《统计学习方法》").scale(2)
        author = TextMobject(
            "李航"
        )
        VGroup(title, author).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(author, DOWN),
        )
        self.wait()

        aidevlog = TextMobject(
            r"公众号：AIDevLog", r"网站：https://2020.iosdevlog.com")
        aidevlog.next_to(title, DOWN)
        self.play(Transform(author, aidevlog))
        self.play(ApplyMethod(author.to_corner, DR))
        self.wait()

        transform_title = TextMobject(r"第1章", r"统计学习方法概论").scale(1.5)
        transform_title.to_corner(UL)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, author)),
        )
        self.wait()


class SupervisedStep(Scene):
    def construct(self):
        transform_title = TextMobject(r"第1章", r"统计学习方法概论").scale(1.5)
        transform_title.to_corner(UL)
        self.add(transform_title)
        self.wait()

        step_title = TextMobject("监督学习的实现步骤").scale(1.2)
        step_title.to_corner(UL)
        self.add(step_title)
        self.play(
            Transform(transform_title, step_title),
        )
        self.wait()

        text1 = TextMobject("1. 得到一个有限的训练数据集合")
        text2 = TextMobject("2. 确定模型的假设空间，也就是 所有的备选模型")
        text3 = TextMobject("3. 确定模型选择的准则，即学习 的策略")
        text4 = TextMobject("4. 实现求解最优模型的算法 ")
        text5 = TextMobject("5. 通过学习方法选择最优模型")
        text6 = TextMobject("6. 利用学习的最优模型对新数据进行预测或分析")

        text1.shift(2).to_edge(LEFT)
        text2.next_to(text1, DOWN, aligned_edge=LEFT)
        text3.next_to(text2, DOWN, aligned_edge=LEFT)
        text4.next_to(text3, DOWN, aligned_edge=LEFT)
        text5.next_to(text4, DOWN, aligned_edge=LEFT)
        text6.next_to(text5, DOWN, aligned_edge=LEFT)

        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)


class Model(Scene):
    def construct(self):
        transform_title = TextMobject("监督学习问题")
        transform_title.to_corner(UL)
        self.play(Write(transform_title))
        self.wait()

        arrow1 = Arrow(LEFT, RIGHT).move_to(LEFT*3)
        self.play(GrowArrow(arrow1))
        self.wait()

        learn_system = TextMobject('学习系统')
        learn_system.set_color_by_gradient(GREEN, BLUE)
        learn_system.shift(2).next_to(arrow1)
        learn_system.border = SurroundingRectangle(
            learn_system, color=BLUE, opacity=0.5, fill_color=WHITE)
        self.play(Write(VGroup(learn_system, learn_system.border)))
        self.wait()

        trainData = TexMobject(
            r"\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right), \cdots,\left(x_{N}, y_{N}\right)")
        trainData.next_to(learn_system, UP, buff=0.2, aligned_edge=RIGHT)
        self.play(Write(trainData))
        self.wait()

        arrow2 = Arrow(LEFT, RIGHT)
        arrow2.next_to(learn_system)
        self.play(GrowArrow(arrow2))
        self.wait()

        model = TextMobject('模型')
        model.set_color_by_gradient(BLUE, RED)
        model.next_to(arrow2)
        model.border = SurroundingRectangle(
            model, buff=0.2, color=RED, opacity=0.5, fill_color=WHITE)
        self.play(Write(VGroup(model, model.border)))
        self.wait()

        hypothesis = TexMobject(
            r"\begin{array}{l}Y=\hat{f}(X) \\ \hat{P}(Y | X)\end{array}")
        hypothesis.next_to(model, UP)
        self.play(Write(hypothesis))
        self.wait()

        t3 = TextMobject('预测系统')
        t3.set_color_by_gradient(RED, GREEN)
        t3.next_to(learn_system, DOWN, buff=2)
        t3.border = SurroundingRectangle(
            t3, color=BLUE, opacity=0.5, fill_color=WHITE)
        self.play(Write(VGroup(t3, t3.border)))
        self.wait()

        arrow3 = Arrow(t3.get_top(), model.border.get_bottom())
        arrow4 = Arrow(model.border.get_bottom(), t3.get_top())
        self.play(GrowArrow(arrow3), GrowArrow(arrow4))
        self.wait()

        test_data = TexMobject(r"x_{N+1}")
        test_data.next_to(t3, LEFT, buff=2)
        self.play(Write(test_data))
        self.wait()

        arrow5 = Arrow(LEFT, RIGHT)
        arrow5.next_to(test_data)
        self.play(GrowArrow(arrow5))
        self.wait()

        arrow6 = Arrow(LEFT, RIGHT)
        arrow6.next_to(t3)
        self.play(GrowArrow(arrow6))
        self.wait()

        test_label = TexMobject(r"y_{N+1}")
        test_label.next_to(arrow6)
        self.play(Write(test_label))
        self.wait()


class SupervisedLearning(Scene):
    CONFIG = {
        "train_title": "训练集",
        "train_set": r"$T=\left\{\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right), \cdots,\left(x_{N}, y_{N}\right)\right\}$",
        "vector_title": "特征向量",
        "vector": r"$x=\left(x^{(1)}, x^{(2)}, \cdots, x^{(n)}\right)^{T}$",
        "vector_i": r"$x_{i}=\left(x_{i}^{(1)}, x_{i}^{(2)}, \cdots, x_{i}^{(n)}\right)^{\mathrm{T}}$",
        "model": "模型",
        "decision": "1. 决策函数",
        "decision_function": r"$Y=f(X)$",
        "predict": "  预测形式",
        "decision_predict": r"$y=f(x)$",
        "condition": "2. 条件概率分布",
        "condition_function": r"$P(Y | X)$",
        "condition_predict": r"$\arg \max \limits_{y} x(y | x)$",
    }

    def construct(self):
        transform_title = TextMobject("监督学习")
        transform_title.to_corner(UL)
        self.play(Write(transform_title))
        self.wait()

        texts = TextMobject(
            self.train_title,
            self.train_set,
            self.vector_title,
            self.vector,
            self.vector_i,
        )

        texts[0].next_to(LEFT*4, UP*6)

        for i in range(1, len(texts)):
            texts[i].next_to(texts[i-1], DOWN, aligned_edge=LEFT)

        self.play(Write(texts))
        self.wait(2)
        self.remove(texts)

        models = TextMobject(
            self.model,
            self.decision,
            self.decision_function,
            self.predict,
            self.decision_predict,
            self.condition,
            self.condition_function,
            self.predict,
            self.condition_predict,
        )

        models[0].next_to(LEFT*4, UP*6)
        models[1].next_to(models[0], DOWN, aligned_edge=LEFT)
        models[2].next_to(models[1], RIGHT, buff=3)
        models[3].next_to(models[1], DOWN, aligned_edge=LEFT)
        models[4].next_to(models[2], DOWN, aligned_edge=LEFT)
        models[5].next_to(models[3], DOWN, aligned_edge=LEFT)
        models[6].next_to(models[4], DOWN, aligned_edge=LEFT)
        models[7].next_to(models[5], DOWN, aligned_edge=LEFT)
        models[8].next_to(models[6], DOWN, aligned_edge=LEFT)

        self.play(Write(models))
        self.wait()


class Statisc(Scene):
    def construct(self):
        transform_title = TextMobject("统计学习三要素")
        transform_title.to_corner(UL)
        self.add(transform_title)
        self.wait()

        model = TextMobject(
            "模型")
        strategy = TextMobject(
            "策略")
        algorithm = TextMobject(
            "算法")

        primary = VGroup(model, strategy, algorithm).arrange(DOWN)
        self.play(Write(primary))
        self.wait()

        self.play(FadeOut(strategy), FadeOut(algorithm))
        self.play(ReplacementTransform(
           model , transform_title
        ))
        self.wait()


class End(Scene):
    def construct(self):
        transform_title = TextMobject("谢谢观看").scale(2)

        account = TextMobject(
            r"公众号：AI开发日志（AIDevLog）")
        website = TextMobject(
            r"网站：https://2020.iosdevlog.com")
        github = TextMobject(
            "视频源码：https://github.com/iOSDevLog/AIDevLog")

        self.play(
            Write(transform_title),
            FadeInFrom(
                VGroup(account, website, github).arrange(DOWN).to_edge(DOWN), DOWN),
        )
        self.wait()
