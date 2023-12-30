---
title: Group structures
date: 2022-11-09
tags:
  - abstract algebra
  - subgroups
  - sylow
  - group actions
math: true
draft: false
description: "Introductory methods I've gathered for studying the structure of finite groups."
---

I've been working on Beachy and Blair's [Abstract Algebra Book](https://www.johnabeachy.com/),
specifically their chapter on Group structure (7), and I wanted to summarize what I've learned about group structures.

## Finite groups and structure

The problems and results derived from this chapter almost all concern with finite groups. We know _a lot_ about finite groups. For example, we have this result:

{{< thmbox class="Theorem" name="Burnside, 1904">}}
Every group of order $p^a q^b$, where $p$ and $q$ are (not necessarily distinct) primes is solvable.
{{</ thmbox >}}

Which was later killed by:

{{< thmbox class="Theorem" name="Feit–Thompson theorem, 1963">}}
Every odd group is solvable.
{{</ thmbox>}}

I'll explain what solvability is later, but this theorem was so fundamental that mathematicians decided it was time to classify every possible finite group (with a special condition) after this discovery was found. And they [succeeded](https://en.wikipedia.org/wiki/Classification_of_finite_simple_groups)!

What is the condition? The groups had to be **simple**.

### Simple groups

{{< thmbox class="Definition" name="Simple group">}}
A group is called **simple** if it has no _normal_ subgroups except the trivial group and itself.
{{</ thmbox>}}

Recall that normal subgroups are very useful. If $N$ is a normal subgroup of $G$, then we can define $G/N$, the quotient group of $G$ with $N$. It turns out the only type of subgroup that allows this structure to form is a normal subgroup.

Therefore these "simple" groups have a unique property: we can't take any quotient and get anything meaningful, we either get the whole group, or the trivial group. However, this is a good thing, this means we can't reduce the group down.

To show why this is important, consider how primes are used in number theory. A prime only has itself and $1$ as divisors. Analogously, simple groups are the prime numbers of group theory. While we can't just multiply (in group theory, we call this an **external direct product**) simple groups together to form a larger group, we can use a generalization of products, [extensions](https://en.wikipedia.org/wiki/Group_extension) to get different kinds of groups. However, there is still more work to be done to classify all finite groups. The [extension problem](https://en.wikipedia.org/wiki/Group_extension#Extension_problem) asks us whether we can reach all finite groups via extensions.

The easiest simple groups to describe with an undergraduate knowledge of group theory are

1. The cyclic groups of prime order, $\mathbb{Z}/p\mathbb{Z}$.
2. The alternating groups of $n$ letters, $A_n$.
3. The **projective special linear groups** $\mathrm{PSL}_n(F)$ for any finite field $F$ (with a few exceptions).

I'd recommend looking into these yourself if interested.

### Solvable groups

{{< thmbox class="Definition" name="Solvable group">}}
A finite group $G$ is **solvable** if there is a finite chain of subgroups $G = N_0\supseteq N_1\supseteq\cdots \supseteq N_n$ such that

1. $N_i$ is a normal subgroup of $N_{i-1}$,
2. $N_{i-1}/N_i$ is a prime cyclic group ($\mathbb{Z}/p\mathbb{Z}$),
3. $N_n = \\{ 1 \\}$.
   {{</ thmbox>}}

Speaking very vaguely, we can mod out a normal subgroup of $G$ such that its quotient with $G$ is a prime order cyclic group, and then continue this process until we end up with the trivial group. This helps us because if $G$ is solvable, then either:

1. It has a nontrivial subgroup, or
2. It only has the trivial subgroup, and $G/\\{1\\}$ is a cyclic group of prime order.

There are many more series like the previous chain, which I hope to cover in a different post. A very important one is

{{< thmbox class="Definition" name="Composition series">}}
A chain of subgroups for a group $G$ such that $G = N_0\supseteq N_1\supseteq\cdots \supseteq N_n$ and

1. $N_i$ is a normal subgroup of $N_{i-1}$,
2. $N_{i-1}/N_i$ is a _simple_ group,
3. $N_n = \\{ 1 \\}$,

is called a **composition series** of $G$.
{{</ thmbox>}}

The power of this series is realized with:

{{< thmbox class="Theorem" name="Jordan-Holder" >}}
All composition series for the same group have the same lengths, and the groups $N_{i-1}/N_i$, called the **composition factors** are just permutations of the composition factors of any other composition series.
{{</ thmbox>}}

What this theorem is saying is that every composition series _looks_ similar. The composition series lets us know what simple groups are needed to extend the trivial group to any desired group. Theorem (6) tell us that if we found a different path of extensions by simple groups, the simple groups we chose would be the same. While not every group has a composition series, the ones that do give us hints to their structure.

**Exercise.** Show that $\mathbb{Z}$ does not have a composition series.

Theres an issue with these series: how do we find normal subgroups?
For finite groups we have an aid.

### The Sylow theorems

I won't state the [Sylow Theorems](https://en.wikipedia.org/wiki/Sylow_theorems) here, but they allow us to guarantee the existence of subgroups of order $p^k$, where $p$ is a prime, and $k$ is the largest possible number such that $p^k$ divides the order of the group. What's more, if we can show that there is only one of these groups, then we can conclude it is normal.

There were many problems littered in the book about proving that any group of order $148$, $48$, $96$, using varying techniques, but they tend to start with finding the Sylow $p$-subgroups of a group with the given order.

The proof of the Sylow Theorems relied on something with even more use, and I would argue, bridges the gap between real life and group theory.

### Group actions are powerful

Group actions were the hardest thing for me to understand when I was learning group theory, so I hope to give a broad introduction to them.

{{< thmbox class="Definition" name="Group action">}}
A group $G$ acts on a set $S$ by "moving" elements of $S$ in some predefined way. I write $G\curvearrowright S$. There are 2 traits that a group action must satisfy. For $s\in S$, and $g,h\in G$,

1. $1\curvearrowright s = s$.
2. $a\curvearrowright (b \curvearrowright s) = (ab) \curvearrowright s$.

We call "$\curvearrowright$" a **group action**.
{{</ thmbox>}}

We can define a group action however we want. Here's the simplest example:

**Example.** $(G,\cdot)$ can act on itself. Let's define, for $a,g \in G$, $a\curvearrowright g = a\cdot g$. If we let $a$ act on all elements of $G$, it will end up permuting them in some way.

The way we define the action is slightly limited, but it allows us to take full advantage of group properties. The action in Example (1) is boring, since it just uses element multiplication. For a more interesting example, we could let the $n$'th Dihedral group $D_n$ act on an $n$-gon by letting it rotate and reflect the polygon. This tells us a lot about how rotations and reflections interact on the polygon (such as $1$ rotation and $1$ reflection is the same as $n-1$ rotations), since we can abstract it to the group structure.

I think group actions explain why groups are so synonymous with symmetry. You can apply a group to any object with symmetry, and then use the group structure to determine useful properties about it.

**Problem.** Let $G$ be a group of order $2m$, there $m$ is odd. Show that $G$ is not simple.

{{< thmbox class="Proof">}}
Consider the homomorphism $\phi_1:G\to S_{2m}$, which exists
due to Cayley's theorem. Let $\phi_1(g) = f_g$, where
$f_g:G\to G$ is the permutation by $g\curvearrowright G$.

Now let $\phi_2 : S_{2m} \rightarrow \\{\pm1\\}$ be the
even-odd permutation homomorphism.

**Claim.** $\phi_2\circ \phi_1:G\rightarrow \\{\pm1\\}$ is surjective.

$\phi_2\circ\phi_1(1)=1$, since the identity is $(1)$, an
even permutation.

If $\|G\|=2m$, then $\exists a\in G$ such that $o(a)=2$.
Then consider $f_a\in S_{2m}$.
For $x\in G$, we know that $f_a(x)=y$,
for some $y\neq x\in G$, and $f_a(f_a(x)) = x$.
Therefore the transposition $(x,y)$ is in the permutation $f_a$.
As we continue for all elements in $G$, we find that there
are $2m/2 = m$ transpositions in $f_a$. Since $m$ is
odd, $f_a$ is an odd permutation, and $\phi_2\circ\phi_1(a)=-1$. Therefore $\phi_2\circ\phi_1$ is surjective.

Using this, we know that $\ker(\phi_2\circ \phi_1)$ is a
subgroup of $G$, and
$$ [G:\ker(\phi_2\circ \phi_1)] = 2, $$
so $\ker(\phi_2\circ \phi_1)\trianglelefteq G$, and $G$ is not simple.
{{</ thmbox>}}

## Useful tools for examining group structure

### Characteristic subgroups

**Characteristic subgroups** are subgroups $H$ of a group $G$ that are invariant under automorphisms of $G$. In symbols, if $H\leq G$, and $\varphi(H) = H \ \forall \varphi \in \mathrm{Aut}(G)$, then $H$ is a characteristic subgroup of $G$.

You don't need to actually understand all these words, I'll just note the important takeaways:

{{< thmbox class="Proposition">}}
Characteristic subgroups

1. Are normal subgroups,
2. Make normal subgroups transitive.
   {{</ thmbox>}}

(1) tells us that characteristic subgroups are some stronger definition of normal subgroups. (2) works in a specific way. You likely found out that $K \trianglelefteq H \trianglelefteq G$, does not immediately imply that $K \trianglelefteq G$. However, characteristic subgroups are a _stronger_ form of normal subgroups. If $K \trianglelefteq H \trianglelefteq G$ and $K$ is a _characteristic_ subgroup of $H$, then we can stretch to our conclusion $K \trianglelefteq G$.

For specific chains for solvable groups, we can show that these normal subgroups can be characteristic subgroups as well, and that allows us to reach as far as we want when claiming some group in the chain is normal to any other group in the chain.

**Problem.** Prove that if $G$ is finite, then any normal Sylow $p$-subgroup of $G$ is a characteristic subgroup.

{{< thmbox class="Proof">}}
$\mathrm{Syl}_p(G)$ has all elements of order $p^n$ for all
$n\in \mathbb{N}$. Since order is preserved in automorphisms,
for any $a\in \mathrm{Syl}_p(G)$, we have $o(\phi(a)) = p^k$ for some
$k\in\mathbb{N}$, and therefore $\phi(a)\in\mathrm{Syl}_p(G)$, so
$\phi(\mathrm{Syl}_p(G))\subseteq\mathrm{Syl}_p(G)$. Since the order of the image of an automorphism is preserved, or $\|\phi(\mathrm{Syl}_p(G))\| = \|\mathrm{Syl}_p(G)\|$, we have $\phi(\mathrm{Syl}_p(G))=\mathrm{Syl}_p(G)$.
{{</ thmbox>}}

### Group actions on subgroups (and more)

Since group actions move all elements of a set, we can do something clever. Every group element corresponds to a group action, and every group action corresponds to some permutation of the set $A$. Therefore, if the set is finite, we can create a homomorphism $\varphi: G\to S_{\|A\|}$ between
$G$ and the symmetric group on $\|A\|$ letters. Since the kernel of
a homomorphism is a normal subgroup of $G$, if we can show that $\ker\varphi$ is non-trivial, we can find a normal subgroup.

If we let that set be the set of left cosets of some subgroup $H$ of $G$,
and let the action be just multiplying the element to the left side of the coset (you can verify this is an action)
then we can create the map $\varphi: G\to S_{[G:H]}$.

There's another action we can define, if we gather all the [conjugate subgroups](https://groupprops.subwiki.org/wiki/Conjugate_subgroups) of $H$ and let $G$ act on them by conjugation, we create a map $\varphi: G\to S_{k}$, where $k$ is the number of conjugate subgroups to $H$.

A more advanced application of group actions is by letting the action define a linear transformation on a vector space. This is the grounding idea of [representation theory](https://en.wikipedia.org/wiki/Representation_theory). Since matrices (linear transformations) have a stricter definition, and linear algebra in general is highly studied, we can reach a lot more conclusions from this connection.

### "Guaranteed" normal subgroups

There are two types of subgroups that we can form for any group that are always normal in said group.

{{< thmbox class="Definition">}}
The **center** of a group $G$ is the set of all elements that commute with all elements of $G$. It is denoted $Z(G)$
{{</ thmbox>}}
{{< thmbox class="Definition">}}
The **commutator subgroup** of $G$ is the set of all $xyx^{-1}y^{-1}$ for $x,y\in G$. It is denoted $G'$.
{{</ thmbox>}}

If these are trivial or the whole group, they can provide useful information too. If the center is the entire group, then the group is abelian.

The commutator subgroups are useful since we can take the commutator of the commutator, $(G')'$, and so on. If this eventually terminates at the trivial group $\\{1\\}$ (we call this series the **derived series**), we can show that the group $G$ is solvable.

### The isomorphism theorems

See [this link](https://en.wikipedia.org/wiki/Isomorphism_theorems) for their statements.

**Problem.** Assume we know that $A_n$ is simple for $n\geq 5$. Find all normal subgroups of $S_n$ for $n\geq 5$.

{{< thmbox class="Proof">}}
Let $H\trianglelefteq S_n$ be any group other than $A_n$ normal to $S_n$.
By the first isomorphism theorem, $H\cap A_n \trianglelefteq H$, so $H\cap A_n = H \implies H \subseteq A_n$ or $H\cap A_n=\\{1\\}$, since $H$ is normal.

If $H \subseteq A_n$, then by the second isomorphism theorem, $A_n/H \trianglelefteq S_n/A_n\cong \mathbb{Z}_2$.
So either $A_n/H$ is trivial, in which case $H=A_n$,
or $H$ has index $2$ in $A_n$, which is not possible, since that
would mean $A_n$ is not simple.

Otherwise, if $H\cap A_n=\\{1\\}$, $H$ has an odd permutation.
Then $A_nH = S_n$. With these two facts, we conclude
$S_n\cong A_n\times H$ and $H\cong \mathbb{Z}_2$. However,
$S_n$ is not isomorphic to $A_n\times\mathbb{Z}_2$, since it has
a non-trivial center, and all $S_n$ for $n\geq 5$ have a trivial center.
{{</ thmbox>}}

## What about infinite groups?

I came to realize while I finished this chapter that results were primarily applied to finite groups. This is because, in my opinion, the study of infinite groups has more on the horizon that of finite groups. This is not to discredit the work on finite groups, classifying all finite simple groups is probably one of the most monumental discoveries made in this field. However, if we want to keep pushing the boundaries of groups, infinite groups are just more interesting.

I think that's why geometric group theory has proven to be such a useful framework: it's nearly useless for finite groups, but allows us to see a general structure (such as knowing about groups of finite index) for these infinite groups in which we can't just find the Sylow $2$-subgroups.
