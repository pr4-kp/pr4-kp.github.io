---
title: Modular forms — what do I make of them?
date: 2024-05-30
tags:
  - modular forms
  - algebra
  - group theory
  - group actions
  - analysis
  - complex analysis
math: true
draft: true
description: "blahhhh TODO"
---

This past semester, I joined a research project that was tackling the problem of finding the index of subgroups of the group $\mathrm{SL}_2(\Z)$ and $\mathrm{SL}_3(\Z)$ (recall that $\mathrm{SL}_n(R)$ is the group of $n\times n$ matrices with entries in a ring $R$ and determinant $1$).

Our main concern was finding out if a machine learning algorithm could learn some strategy to figure out the index of a group, giving us an answer to the previous question. However, I think there is also some value in talking about why we would care about such a question. I kept hearing that the group $\mathrm{SL}_2(\Z)$ and its subgroups were related to something called a _modular form_, but (admittedly because it was not related to our research and requires some complex analysis) we did not cover what they were.

## Motivation: an exercise in an algebra textbook

My first interaction with modular forms was through Beachy and Blair's algebra textbook, which was the textbook for my first proof-based mathematics class. The very last problem of section 7 reads
{{< thmbox class="Problem">}}
Let $F$ be a field and let $G$ be the set of all rational functions over $F$ of the form $f(x)=\frac{ax+b}{cx+d}$, where $a,b,c,d\in F$ and $ad-bc=1$. Prove that $G$ is a group under composition of functions and that $G$ is isomorphic to $\mathrm{PSL}_2(F)$.
{{</ thmbox>}}
